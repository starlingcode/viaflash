import sys
import json
import os
import numpy as np
import matplotlib

from PySide6.QtWidgets import QDialog, QPushButton, QSpacerItem, QSizePolicy, QMessageBox, QLabel
from PySide6.QtCore import QFile, Slot, QRect, Qt
from ui_sync3_scale_editor import Ui_sync3ScaleEditor
from ui_sync3_ratio import Ui_sync3Ratio
from viatools.sync3_scales import Sync3Scales

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

class Sync3RatioXY(FigureCanvasQTAgg):
    def __init__(self, numerator, denominator):
        fig = Figure(figsize=(1,1), facecolor='black')
        self.axes = fig.add_subplot(111)
        self.axes.axis('off')
        domain = np.linspace(0, 2 * np.pi * denominator, 256)
        self.axes.plot(np.sin(domain), np.cos(domain * (numerator/denominator)), color='white')
        super(Sync3RatioXY, self).__init__(fig)
    
    def update_plot(self, numerator, denominator):
        self.axes.cla()
        self.axes.set_facecolor('black')
        domain = np.linspace(0, 2 * np.pi * denominator, 256)
        self.axes.plot(np.sin(domain), np.cos(domain * (numerator/denominator)), color='white')
        self.draw()
        print('updating_plot')

class Sync3Ratio(QDialog):
    def __init__(self, numerator, denominator):
        super(Sync3Ratio, self).__init__()
        self.ui = Ui_sync3Ratio()
        self.ui.setupUi(self)
        self.ui.decimalData.setText('%.4f' % (numerator/denominator))
        self.ui.semitonesData.setText('%.4f' % (np.log2(numerator/denominator) * 12))
        self.ui.xyLayout.addWidget(Sync3RatioXY(numerator,denominator))

class Sync3ScaleEditor(QDialog):
    def __init__(self, scale_path='./', binary_path='./', scale_set='original'):
        super(Sync3ScaleEditor, self).__init__()
        
        self.ui = Ui_sync3ScaleEditor()
        self.ui.setupUi(self)
        
        self.engine = Sync3Scales()
        self.scale_dir = scale_path
        self.engine.scale_dir = scale_path
        self.engine.output_dir = binary_path
        
        self.scale_set_edit = []
        self.scale_edit = {}
        self.unsaved_scale_changes = False
        self.local_scale_sets = {}
        self.remote_scale_sets = {}
        self.scales = []
        self.remote_scales = []
        self.seed_ratio_buttons = []
        self.seed_ratio_spacers = []
        
        self.preview_idx = 0
        self.init_preview_display()

        self.create_seed_grid()
        self.get_scale_sets()
        self.get_scales()
        self.load_scale_set(scale_set)

        self.active_slot = 0
        self.ative_scale_id = ''
        self.active_ratio_idx = 0

# Save/load helpers

    def get_scale_sets(self):
        with open(self.scale_dir + 'local_manifest.json') as local_manifest:
            self.local_scale_sets = json.load(local_manifest)
        with open(self.scale_dir + 'remote_manifest.json') as remote_manifest:
            self.remote_scale_sets = json.load(remote_manifest)
        self.ui.selectScaleSet.clear()
        for scale_set in [*self.local_scale_sets] + [*self.remote_scale_sets]:
            self.ui.selectScaleSet.addItem(scale_set) 
        for scale_set in self.remote_scale_sets:
            for scale in scale_set:
                self.remote_scales.append(scale)

    def get_scales(self):
        for root, dirs, files in os.walk(self.scale_dir + 'scales'):
            for file in files:
                slug = file.split('.json')[0]
                self.scales.append(slug)
        for scale in self.scales:
            self.ui.selectScale.addItem(scale) 
    
    def load_scale_set(self, scale_set):
        self.engine.load_scale_set(scale_set)
        self.ui.slot1.setChecked(True)
        self.switch_slot(0)

    def switch_slot(self, slot_num):
        if self.unsaved_scale_changes:
            if self.prompt_to_discard():
                switch_slot(self.active_slot)
                self.unsaved_scale_changes = False
            else:
                return 
        self.active_slot = slot_num
        self.active_scale_id = self.engine.scale_set[slot_num]
        self.load_scale(self.active_scale_id)

    def prompt_to_discard(self):
        if QMessageBox.question(self, "", 'Unsaved changes will be lost, continue?') == QMessageBox.Yes:
            return True
        else:
            return False
        # Ask user if they wish to save any unsaved changes

    def load_scale(self, scale_id):
        if self.unsaved_scale_changes:
            if self.prompt_to_discard():
                self.unsaved_scale_changes = False
            else:
                cb_index = self.ui.selectScale.findText(self.active_scale_id)
                self.ui.selectScale.setCurrentIndex(cb_index) 
                return 
        cb_index = self.ui.selectScale.findText(scale_id)
        self.ui.selectScale.setCurrentIndex(cb_index)
        self.active_scale_id = scale_id
        self.update_grid()        
        self.update_fill_method(self.engine.scales[scale_id]['fill_method'])

    def save_scale(self):
        filename = QInputDialog.getText(self, 'Save Scale', 'Enter scale name:')
        if filename in [*self.local_scale_sets]:
            if QMessageBox.question(self, 'Overwrite?', 'Name in use, overwrite?') == QMessageBox.No:
                return
        while filename in [*self.remote_scale_sets]:
            filename = QInputDialog.getText(self, 'Save Scale', 'Reserved name, enter new name:') 
            if filename in [*self.local_scale_sets]:
                if QMessageBox.question(self, 'Overwrite?', 'Name in use, overwrite?') == QMessageBox.No:
                    return
        self.unsaved_scale_changes = False
        self.engine.save_scale(filename)
        # Save edit buffer to file

    def save_scale_set(self):
        filename = QInputDialog.getText(self, 'Save Scale Set', 'Enter scale set name:')
        if filename in [*self.local_scale_sets]:
            if QMessageBox.question(self, 'Overwrite?', 'Name in use, overwrite?') == QMessageBox.No:
                return
        while filename in [*self.remote_scale_sets]:
            filename = QInputDialog.getText(self, 'Save Scale Set', 'Reserved name, enter new name:') 
            if filename in [*self.local_scale_sets]:
                if QMessageBox.question(self, 'Overwrite?', 'Name in use, overwrite?') == QMessageBox.No:
                    return
        self.unsaved_scale_changes = False
        self.engine.save_scale_set(filename)
        # Save edit buffer to file

# Seed ratio dispaly helpers

    def seed_button_pushed(self, idx):
        scale_id = self.active_scale_id
        ratio = self.engine.scales[scale_id]['seed_ratios'][idx]
        self.ratio_dialog = Sync3Ratio(ratio[0], ratio[1])
        self.ratio_dialog.setGeometry(QRect(200, 200, 180, 271))
        self.ratio_dialog.ui.removeRatio.clicked.connect(self.remove_ratio)
        self.ratio_dialog.ui.close.clicked.connect(self.close_ratio_dialog)
        self.ratio_dialog.setWindowTitle('%d/%d' % (ratio[0], ratio[1]))
        self.active_ratio_idx = idx
        self.ratio_dialog.exec()

    def close_ratio_dialog(self):
        self.ratio_dialog.accept()

    def remove_ratio(self):
        scale_id = self.active_scale_id
        self.engine.scales[scale_id]['seed_ratios'].pop(self.active_ratio_idx)
        self.ratio_dialog.accept()
        self.update_grid()
        self.unsaved_scale_changes = True

    def create_seed_grid(self):
        self.num_columns = 4
        self.num_rows = 8
        for row in range(0, self.num_rows):
            for column in range(0, self.num_columns):
                idx = row * self.num_columns + column
                new_button = QPushButton()
                new_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                sp = new_button.sizePolicy()
                sp.setRetainSizeWhenHidden(True)
                new_button.setSizePolicy(sp)
                new_button.clicked.connect(lambda state=True, x=idx: self.seed_button_pushed(x))
                self.seed_ratio_buttons.append(new_button)
                self.ui.seedRatioGrid.addWidget(new_button, row, column)

    def update_grid(self):
        seed_ratios = self.engine.scales[self.active_scale_id]['seed_ratios']
        idx = -1
        for idx, ratio in enumerate(seed_ratios):
            self.seed_ratio_buttons[idx].show()
            self.seed_ratio_buttons[idx].setText('%s/%s' % (ratio[0], ratio[1]))
        for i in range(idx+1, 31):
            self.seed_ratio_buttons[i].hide()
        self.engine.render()
        self.update_preview()

# Fill method helpers

    def update_fill_method(self, fill_method):
        if self.engine.scales[self.active_scale_id]['fill_method'] != fill_method:
            self.unsaved_scale_changes = True
        if fill_method == 'octave':
            self.ui.fillOctave.setChecked(True)
            self.engine.scales[self.active_scale_id]['fill_method'] = fill_method
        elif fill_method == 'tritave': 
            self.ui.fillTritave.setChecked(True)
            self.engine.scales[self.active_scale_id]['fill_method'] = fill_method
        elif fill_method == 'expand':       
            self.ui.fillExpand.setChecked(True)
            self.engine.scales[self.active_scale_id]['fill_method'] = fill_method
        self.engine.render()
        self.update_preview()

# Preview helpers

    def init_preview_display(self):
        self.decimalPreview = QLabel()
        self.decimalPreview.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.decimalPreview.setText('Value')
        self.semitonePreview = QLabel()
        self.semitonePreview.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.semitonePreview.setText('Value')
        self.ratioPreview = QLabel()
        self.ratioPreview.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.ratioPreview.setText('Value')
        self.xyPreview = Sync3RatioXY(1, 1)
        self.ui.previewContainer.addWidget(self.ratioPreview)
        self.ui.previewContainer.addWidget(self.decimalPreview)
        self.ui.previewContainer.addWidget(self.semitonePreview)
        self.ui.previewContainer.addWidget(self.xyPreview) 
        self.decimalPreview.hide()
        self.semitonePreview.hide()
        self.xyPreview.hide()
        self.ui.previewSelect.addItem('Ratio')
        self.ui.previewSelect.addItem('Decimal')
        self.ui.previewSelect.addItem('Semitone')
        self.ui.previewSelect.addItem('XY')
        self.ui.previewSelect.setCurrentIndex(0)

    def change_preview_display(self, display_type):
        if display_type == 'Decimal':
            self.ratioPreview.hide()
            self.decimalPreview.show() 
            self.semitonePreview.hide() 
            self.xyPreview.hide()      
        if display_type == 'Semitone':
            self.ratioPreview.hide()
            self.decimalPreview.hide() 
            self.semitonePreview.show() 
            self.xyPreview.hide()      
        if display_type == 'XY':
            self.ratioPreview.hide()
            self.decimalPreview.hide() 
            self.semitonePreview.hide() 
            self.xyPreview.show()      
        if display_type == 'Ratio':
            self.ratioPreview.show()
            self.decimalPreview.hide() 
            self.semitonePreview.hide() 
            self.xyPreview.hide()      

    def update_preview(self):
        numerator = self.engine.scales[self.active_scale_id]['numerators'][self.preview_idx]
        denominator = self.engine.scales[self.active_scale_id]['denominators'][self.preview_idx]
        self.decimalPreview.setText('%.4f' % (numerator/denominator))
        self.semitonePreview.setText('%.4f' % (np.log2(numerator/denominator) * 12))
        self.ratioPreview.setText('%d/%d' % (numerator, denominator)) 
        self.xyPreview.update_plot(numerator, denominator)       

# Load/save scale set

    @Slot()
    def on_saveScaleSet_clicked(self):
        self.save_scale_set()
        # Prompt user for name or overwrite
        # Load slot1    

    @Slot()
    def on_selectScaleSet_activated(self):
        self.load_scale_set(self.selectScaleSet.getText())
        # Load new scale set/prompt user to save changes
        # Import the scale set to the editor state storage data structure    

# Select slot

    @Slot()
    def on_slot1_clicked(self):
        self.switch_slot(0)
    
    @Slot()
    def on_slot2_clicked(self):
        self.switch_slot(1)
    
    @Slot()
    def on_slot3_clicked(self):
        self.switch_slot(2)
    
    @Slot()
    def on_slot4_clicked(self):
        self.switch_slot(3)

    @Slot()
    def on_slot5_clicked(self):
        self.switch_slot(4)

    @Slot()
    def on_slot6_clicked(self):
        self.switch_slot(5)

    @Slot()
    def on_slot7_clicked(self):
        self.switch_slot(6)

    @Slot()
    def on_slot8_clicked(self):
        self.switch_slot(7)

# Load/save scale

    @Slot()
    def on_selectScale_activated(self):
        self.load_scale(self.getText())
        return

    @Slot()
    def on_saveScale_clicked(self):
        self.save_scale()
        return

# Edit seed ratios

    @Slot()
    def on_addSeedRatio_clicked(self):
        if self.engine.add_seed_ratio(self.active_scale_id, self.ui.numerator.value(), self.ui.denominator.value()):
            self.update_grid()
            self.unsaved_scale_changes = True
            print('Added')
        else:
            print('Dupe')

    @Slot()
    def on_addFromScala_clicked(self):
        return
        # Prompt to select scala file, render once new ratios added

    @Slot()
    def on_clearSeedRatios_clicked(self):
        if QMessageBox.question(self, 'Clear Ratios', 'Clear all ratios?') == QMessageBox.Yes: 
            self.engine.scales[self.active_scale_id]['seed_ratios'] = []
            self.update_grid()

# Tiling method selection

    @Slot()
    def on_fillExpand_clicked(self):
        self.update_fill_method('expand')

    @Slot()
    def on_fillOctave_clicked(self):
        self.update_fill_method('octave')

    @Slot()
    def on_fillTritave_clicked(self):
        self.update_fill_method('tritave')

# Preview section slots

    @Slot()
    def on_cvSlider_valueChanged(self):
        self.preview_idx = self.ui.cvSlider.value() + self.ui.knob.value()    
        self.update_preview()

    @Slot()
    def on_knob_valueChanged(self):
        self.preview_idx = self.ui.cvSlider.value() + self.ui.knob.value()
        self.update_preview()

    @Slot()
    def on_previewSelect_activated(self):
        self.change_preview_display(self.ui.previewSelect.currentText())
        self.update_preview()
