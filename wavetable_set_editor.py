from PySide6.QtWidgets import QDialog, QButtonGroup, QAbstractItemView
from PySide6.QtCore import Slot, Qt

from superqt import QLabeledRangeSlider

from ui_resources.ui_wavetable_set_editor import Ui_wavetableSetEditor
from ui_resources.ui_wavetable_browser import Ui_wavetableBrowser
from viatools.wavetables import Wavetable, WavetableSet
from via_resource_editor import ViaResourceEditor

from resourcesetbuttons import (Slot1Button, Slot2Button, Slot3Button, Slot4Button,
    Slot5Button, Slot6Button, Slot7Button, Slot8Button)

import json

class WavetableBrowser(QDialog, Ui_wavetableBrowser):
    def __init__(self, table_file, slope_file, slug, max_table_size, mem_footprint):
        super().__init__()
        self.setupUi(self)
        self.init_table_dict(table_file, slope_file)
        self.table_file = table_file
        self.slope_file = slope_file
        # TODO do we need these random extra long tables?
        if mem_footprint < max_table_size:
            self.table_slider_max = mem_footprint
        else:
            self.table_slider_max = 9
        self.max_table_size = max_table_size
        self.selected_tags = []
        self.init_size_select()
        self.init_tag_list()
        self.update_filter()
        self.table = Wavetable(self.table_file, slug, self.slope_file, max_table_size)
        self.tableIdx.setMaximum(len(self.table.expand()) - 1)
        self.init_viz(self.table)
        self.tableIdxLabel.setText("1")
        self.tableList.setCurrentItem(self.tableList.findItems(slug, Qt.MatchExactly)[0])

    @Slot() 
    def updateTableSize(self, value_tuple):
        self.min_size = int(self.tableSize.sliderPosition()[0])
        self.max_size = int(self.tableSize.sliderPosition()[1])
        self.update_filter()

    @Slot()
    def on_tableList_itemSelectionChanged(self):
        #TODO title to slug
        self.table = Wavetable(self.table_file, self.tableList.currentItem().text(), self.slope_file, self.max_table_size)
        self.table_idx = self.tableIdx.value()
        self.tableIdx.setMaximum(len(self.table.expand()) - 1)
        self.update_resource_ui()

    @Slot()
    def on_tableIdx_valueChanged(self):
        self.table_idx = self.tableIdx.value()
        self.tableIdxLabel.setText(str(self.table_idx + 1))
        self.viz3.update_plot(self.table, self.table_idx)
        self.viz4.update_plot(self.table, self.table_idx)

    @Slot()
    def on_tagList_itemSelectionChanged(self):
        self.selected_tags = []
        for item in self.tagList.selectedItems():
            self.selected_tags.append(item.text())
        self.update_filter()

    @Slot()
    def on_clearTags_clicked(self):
        self.tagList.clearSelection()
        self.select_mode = 'or'
        self.orButton.setChecked(True)
        for tag in self.tag_set:
            self.selected_tags.append(tag)
        self.update_filter()

    @Slot()
    def on_orButton_clicked(self):
        self.select_mode = 'or'
        self.update_filter()

    @Slot()
    def on_andButton_clicked(self):
        self.select_mode = 'and'
        self.update_filter()

    def update_resource_ui(self):
        self.viz1.update_plot(self.table)
        self.viz2.update_plot(self.table)
        self.viz3.update_plot(self.table, self.table_idx)
        self.viz4.update_plot(self.table, self.table_idx)
        self.tableDescription.setText(self.table.data['description'])

    def init_viz(self, table):
        self.viz1.init_viz('wireframe', table)
        self.viz2.init_viz('3dfft', table)
        self.viz3.init_viz('waveform', table)
        self.viz4.init_viz('fft', table)

    def init_table_dict(self, table_file, slope_file):
        self.table_dict = {}
        self.tag_set = set()
        with open(slope_file) as infile:
            raw_slopes = json.load(infile)
        with open(table_file) as infile:
            raw_tables = json.load(infile)
            for table in raw_tables:
                self.table_dict[table] = {}
                attack_samples = raw_slopes[raw_tables[table]['slopes'][0]]['samples']
                self.table_dict[table]['size'] = len(attack_samples)
                self.table_dict[table]['tags'] = []
                for tag in raw_tables[table]['tags']:
                    self.tag_set.add(tag)
                    self.table_dict[table]['tags'].append(tag)

    def init_size_select(self):
        self.tableSize.setRange(1, self.table_slider_max)
        self.tableSize.setValue([1, self.table_slider_max])
        self.min_size = int(1)
        self.max_size = int(self.table_slider_max)
        self.tableSize.valueChanged.connect(self.updateTableSize)
        self.tableSizeWarning.setText('(the first %d will be used)' % self.max_table_size)

    def init_tag_list(self):
        for tag in self.tag_set:
            self.tagList.addItem(tag)
            self.selected_tags.append(tag)
        self.tagList.setSelectionMode(QAbstractItemView.MultiSelection)
        self.select_mode = 'or'
        self.orButton.setChecked(True)

                
    def update_filter(self):
        self.tableList.clear()
        valid_tables = set()
        for table, properties in self.table_dict.items():
            if properties['size'] >= self.min_size and properties['size'] <= self.max_size:
                if self.select_mode == 'or':
                    for tag in self.selected_tags:
                        if tag in properties['tags']:
                            valid_tables.add(table)
                elif self.select_mode == 'and':
                    is_ok = True
                    for tag in self.selected_tags:
                        if tag not in properties['tags']:
                            is_ok = False
                    if is_ok:
                        valid_tables.add(table)
        for table in valid_tables:
            self.tableList.addItem(table)


class WavetableEditor(ViaResourceEditor):
    def __init__(self, resource_dir='./', remote_resources = {}, slug='original', style_text="", table_file='./tables.json', slope_file='./slopes.json'):
        super().__init__() 
        self.setupUi(self)
        self.setStyleSheet(style_text)
        self.style_text = style_text

        self.remote_resources = remote_resources
        # TODO check if new remote resource or set collides with existing local slug
        self.set = WavetableSet(resource_dir, slug, table_file, slope_file)
        self.set_slug = slug
        self.slope_file = slope_file
        self.table_file = table_file

        self.update_resource_sets()
        self.init_viz(self.set.resources[0])
        self.update_resources()
        self.tableIdxLabel.setText("1")

        self.slot_lists_per_mode = {}
        self.slot_list = []
        self.buttonGroup = QButtonGroup(self)
        slot_count = 0

        for mode in self.table_modes:
            self.tableMode.addItem(mode)
            self.slot_lists_per_mode[mode] = []
            for i in range(0, self.table_mode_sizes[mode]):
                this_slot_button_name = 'slot%d' % (slot_count+1)
                # Shame shame shame shame
                setattr(self, this_slot_button_name, eval('Slot%dButton(self.layoutWidget)' % (i+1)))
                this_slot = eval('self.'+this_slot_button_name)
                self.buttonGroup.addButton(this_slot)
                self.slotGroup1.addWidget(this_slot)
                this_slot.configure_size()
                this_slot.setEnabled(True)
                this_slot.setCheckable(True)
                this_slot.setCheckable(True)
                this_slot.hide()
                self.slot_lists_per_mode[mode].append(this_slot)
                self.slot_list.append(this_slot)
                this_slot.clicked.connect(lambda state=True, x=slot_count: self.switch_slot(x))
                slot_count += 1

        self.tableMode.setCurrentIndex(0)
        
        self.update_slot_buttons()

        self.initToolTips()


# Edit wavetable recipe

    @Slot()
    def on_openBrowser_clicked(self):
        self.launch_browser()

    @Slot()
    def on_tableMode_activated(self):
        self.update_slot_buttons()
        
    @Slot()
    def on_tableIdx_valueChanged(self):
        self.table_idx = self.tableIdx.value()
        self.tableIdxLabel.setText(str(self.table_idx + 1))
        self.viz3.update_plot(self.table, self.table_idx)
        self.viz4.update_plot(self.table, self.table_idx)

# Override set editor base class methods

    def update_resource_ui(self):
        self.resourceDescription.setText(self.set.resources[self.active_idx].data['description'])
        self.viz1.update_plot(self.table)
        self.viz2.update_plot(self.table)
        self.viz3.update_plot(self.table, self.table_idx)
        self.viz4.update_plot(self.table, self.table_idx)
        if self.set.is_clean():
            self.saveResourceSet.setEnabled(False)
        else:
            self.saveResourceSet.setEnabled(True)

    def init_viz(self, table):
        self.viz1.init_viz('wireframe', table)
        self.viz2.init_viz('3dfft', table)
        self.viz3.init_viz('waveform', table)
        self.viz4.init_viz('fft', table)

    def update_slot_buttons(self):
        mode = self.tableMode.currentText()
        for slot in self.slot_list:
            if slot in self.slot_lists_per_mode[mode]:
                slot.show()
                slot.setToolTip("Select the table for " + mode + " mode " + str(self.slot_lists_per_mode[mode].index(slot) + 1))
            else:
                slot.hide()
        active_slot = self.slot_lists_per_mode[mode][0]
        active_slot.setChecked(True)
        self.switch_slot(self.slot_list.index(active_slot))


    def launch_browser(self):
        ok_table_length = self.get_allowable_table_size()
        self.browser = WavetableBrowser(self.table_file, self.slope_file, self.set.resources[self.active_idx].slug, self.size_limit_data['table_size'], ok_table_length)
        self.browser.swapTable.clicked.connect(self.swap_table)
        self.browser.close.clicked.connect(self.close_browser)
        self.browser.setStyleSheet(self.style_text)
        self.browser.exec()

    # TODO figure this out with like title and slug logic
    def swap_table(self):
        slug = self.browser.tableList.currentItem().text()
        self.set.replace_resource(slug, self.active_idx)
        self.switch_slot(self.active_idx)
        self.browser.accept()
    
    def close_browser(self):
        self.browser.accept()
 
    def update_resource_selection(self, slug):
        self.tableName.setText(slug)
        self.table = Wavetable(self.table_file, slug, self.slope_file, self.size_limit_data['table_size'])
        self.table_idx = self.tableIdx.value()
        self.tableIdx.setMaximum(len(self.table.expand()) - 1)
        self.update_resource_ui()
        
    def update_resources(self):
        self.resource_slugs, self.resource_titles = self.set.get_available_resources()

    def get_allowable_table_size(self):
        size_left = self.size_limit_data['memory_footprint'] - self.set.get_memory_footprint() + self.set.resources[self.active_idx].get_memory_footprint()
        ok_table_length = size_left/(514*2) # 514 samples per waveform in table, 2 bytes per sample
        if ok_table_length > self.size_limit_data['table_size']:
            ok_table_length = self.size_limit_data['table_size']
        return ok_table_length
    
    def initToolTips(self):
        super().initToolTips()
        self.openBrowser.setToolTip("Open a browser to choose a new table for this slot")
        self.tableIdx.setToolTip("Select a particular waveform from the table to display")
        self.tableMode.setToolTip("Select a group of tables to edit")



class ScannerWavetableEditor(WavetableEditor, Ui_wavetableSetEditor):
    def __init__(self, resource_dir='./', remote_resources = {}, slug='original', style_text="", table_file='./tables.json', slope_file='./slopes.json'):
        self.table_modes = ['X', 'Y']
        self.table_mode_sizes = {
            'X': 8, 
            'Y': 8
        }
        self.size_limit_data = {'table_size': 5, 'memory_footprint': 160000}
        super().__init__(resource_dir, remote_resources, slug, style_text, table_file, slope_file) 

class MetaWavetableEditor(WavetableEditor, Ui_wavetableSetEditor):
    def __init__(self, resource_dir='./', remote_resources = {}, slug='original', style_text="", table_file='./tables.json', slope_file='./slopes.json'):
        self.table_modes = ['Audio', 'Envelope', 'Sequence']
        self.table_mode_sizes = {
            'Audio': 8, 
            'Envelope': 8, 
            'Sequence': 8 
        }
        self.size_limit_data = {'table_size': 9, 'memory_footprint': 170048}
        super().__init__(resource_dir, remote_resources, slug, style_text, table_file, slope_file) 


class SyncWavetableEditor(WavetableEditor, Ui_wavetableSetEditor):
    def __init__(self, resource_dir='./', remote_resources = {}, slug='original', style_text="", table_file='./tables.json', slope_file='./slopes.json'):
        self.table_modes = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Global']
        self.table_mode_sizes = {
            'Group 1': 4, 
            'Group 2': 4, 
            'Group 3': 4, 
            'Group 4': 4, 
            'Global': 4
        }
        self.size_limit_data = {'table_size': 9, 'memory_footprint': 125048}
        super().__init__(resource_dir, remote_resources, slug, style_text, table_file, slope_file) 




