from PySide6.QtWidgets import QDialog, QButtonGroup
from PySide6.QtCore import Slot

from ui_wavetable_set_editor import Ui_wavetableSetEditor
from ui_wavetable_browser import Ui_wavetableBrowser
from viatools.wavetables import Wavetable, WavetableSet
from via_resource_editor import ViaResourceEditor

from resourcesetbuttons import (Slot1Button, Slot2Button, Slot3Button, Slot4Button,
    Slot5Button, Slot6Button, Slot7Button, Slot8Button)

import json

class WavetableBrowser(QDialog, Ui_wavetableBrowser):
    def __init__(self, table_file, slope_file, slug, max_table_size):
        super().__init__()
        self.setupUi(self)
        self.init_table_dict(table_file, slope_file)
        self.table_file = table_file
        self.slope_file = slope_file
        self.max_table_size = max_table_size
        if self.table_dict[slug]['type'] == 'slope_pair':
            self.slopePair.setChecked(True)
            self.type = 'slope_pair'
        else:
            self.cycle.setChecked(True)
            self.type = 'cycle'
        self.update_type()
        self.table_size = self.table_dict[slug]['size']
        self.update_size()
        self.tableSize.setCurrentIndex(self.tableSize.findText(str(self.table_size)))
        self.selectTable.setCurrentIndex(self.selectTable.findText(slug))
        self.tableSizeWarning.setText('(the first %d will be used)' % max_table_size) 
        self.init_viz(Wavetable(self.table_file, slug, self.slope_file, max_table_size)
)

    @Slot() 
    def on_slopePair_clicked(self):
        self.type = 'slope_pair'
        self.update_type()

    @Slot() 
    def on_cycle_clicked(self):
        self.type = 'cycle'
        self.update_type()

    @Slot() 
    def on_tableSize_activated(self):
        try: 
            self.table_size = int(self.tableSize.currentText())
            self.update_size()
        except:
            pass

    @Slot()
    def on_selectTable_activated(self):
        self.table = Wavetable(self.table_file, self.selectTable.currentText(), self.slope_file, self.max_table_size)
        self.switch_table()

    def update_resource_ui(self):
        self.viz1.update_resource_ui('wireframe', self.table)
        self.viz2.update_resource_ui('contour', self.table)
        self.viz3.update_resource_ui('waveform', self.table)
        self.viz4.update_resource_ui('fft', self.table)

    def init_viz(self, table):
        self.viz1.init_viz('wireframe', table)
        self.viz2.init_viz('contour', table)
        self.viz3.init_viz('waveform', table)
        self.viz4.init_viz('fft', table)

    def init_table_dict(self, table_file, slope_file):
        self.table_dict = {}
        with open(slope_file) as infile:
            raw_slopes = json.load(infile)
        with open(table_file) as infile:
            raw_tables = json.load(infile)
            for table in raw_tables:
                self.table_dict[table] = {}
                attack_samples = raw_slopes[raw_tables[table]['slopes'][0]]['samples']
                self.table_dict[table]['size'] = len(attack_samples)
                if attack_samples[0][0] == 0 and attack_samples[0][-1] == 32767:
                    self.table_dict[table]['type'] = 'slope_pair'
                else:
                    self.table_dict[table]['type'] = 'cycle'
                
    def update_type(self):
        self.selectTable.clear()
        self.tableSize.clear()
        valid_sizes = set()
        valid_tables = []
        for table, properties in self.table_dict.items():
            if properties['type'] == self.type:
                valid_sizes.add(properties['size'])
                valid_tables.append(table)
        valid_size_list = sorted(valid_sizes)
        for size in valid_size_list:
            self.tableSize.insertItem(-1, str(size))
            self.table_size = size
        for table in valid_tables:
            self.selectTable.insertItem(-1, table)
            
    def update_size(self):
        self.selectTable.clear()
        valid_tables = []
        for table, properties in self.table_dict.items():
            if properties['type'] == self.type and properties['size'] == self.table_size:
                valid_tables.append(table)
        for table in valid_tables:
            self.selectTable.insertItem(-1, table)


class WavetableEditor(ViaResourceEditor):
    def __init__(self, resource_dir='./', remote_resources = {}, slug='original', style_text="", table_file='./tables.json', slope_file='./slopes.json'):
        super().__init__() 
        self.setupUi(self)
        self.setStyleSheet(style_text)
        self.style_text = style_text

        self.remote_resources = remote_resources
        # TODO check if new remote resource or set collides with existing local slug
        self.size_limit_data = {'table_size': 9}
        self.set = WavetableSet(resource_dir, slug, table_file, slope_file)
        self.set_slug = slug
        self.slope_file = slope_file
        self.table_file = table_file

        self.update_resource_sets()
        self.init_viz(self.set.resources[0])
        self.update_resources()

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


# Edit wavetable recipe

    @Slot()
    def on_openBrowser_clicked(self):
        self.launch_browser()

    @Slot()
    def on_tableMode_activated(self):
        self.update_slot_buttons()
        

# Override set editor base class methods

    def update_resource_ui(self):
        self.viz1.update_resource_ui('wireframe', self.table)
        self.viz2.update_resource_ui('contour', self.table)
        self.viz3.update_resource_ui('waveform', self.table)
        self.viz4.update_resource_ui('fft', self.table)

    def init_viz(self, table):
        self.viz1.init_viz('wireframe', table)
        self.viz2.init_viz('contour', table)
        self.viz3.init_viz('waveform', table)
        self.viz4.init_viz('fft', table)

    def update_slot_buttons(self):
        mode = self.tableMode.currentText()
        for slot in self.slot_list:
            if slot in self.slot_lists_per_mode[mode]:
                slot.show()
            else:
                slot.hide()
        active_slot = self.slot_lists_per_mode[mode][0]
        active_slot.setChecked(True)
        self.switch_slot(self.slot_list.index(active_slot))


    def launch_browser(self):
        self.browser = WavetableBrowser(self.table_file, self.slope_file, self.set.resources[self.active_idx].slug, self.size_limit_data['table_size'])
        self.browser.swapTable.clicked.connect(self.swap_table)
        self.browser.close.clicked.connect(self.close_browser)
        self.browser.setStyleSheet(self.style_text)
        self.browser.exec()

    # TODO figure this out with like title and slug logic
    def swap_table(self):
        slug = self.browser.selectTable.currentText()
        self.set.replace_resource(slug, self.active_idx)
        self.switch_slot(self.active_idx)
        self.browser.accept()
    
    def close_browser(self):
        self.browser.accept()

 
    def update_resource_selection(self, slug):
        self.tableName.setText(slug)
        self.table = Wavetable(self.table_file, slug, self.slope_file, self.size_limit_data['table_size']) 
        self.update_resource_ui()
        
    def update_resources(self):
        self.resource_slugs, self.resource_titles = self.set.get_available_resources()


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
        self.table_modes = ['Audio', 'Envelope', 'Sequence', 'Drum Envelope']
        self.table_mode_sizes = {
            'Audio': 8, 
            'Envelope': 8, 
            'Sequence': 8, 
            'Drum Envelope': 1
        }
        self.size_limit_data = {'table_size': 9, 'memory_footprint': 160000}
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
        self.size_limit_data = {'table_size': 9, 'memory_footprint': 116000}
        super().__init__(resource_dir, remote_resources, slug, style_text, table_file, slope_file) 


