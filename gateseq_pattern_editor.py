import sys
import json
import os
import numpy as np
import matplotlib

from PySide6.QtWidgets import QDialog, QPushButton, QSpacerItem, QSizePolicy, QMessageBox, QLabel
from PySide6.QtCore import QFile, Slot, QRect, Qt
from ui_gateseq_pattern_editor import Ui_gateseqPatternEditor
from viatools.gateseq_patterns import GateseqPatterns

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

class GateseqPatternEditor(QDialog):
    def __init__(self, pattern_path='./', binary_path='./', pattern_set='original'):
        super(GateseqPatternEditor, self).__init__()
        
        self.ui = Ui_gateseqPatternEditor()
        self.ui.setupUi(self)
        
        self.engine = GateseqPatterns()
        self.pattern_dir = pattern_path
        self.engine.pattern_dir = pattern_path
        self.engine.output_dir = binary_path
        
        self.pattern_set_edit = []
        self.pattern_edit = {}
        self.unsaved_pattern_changes = False
        self.local_pattern_sets = {}
        self.remote_pattern_sets = {}
        self.patterns = []
        self.remote_patterns = []

        self.create_pattern_grid()

        self.get_pattern_sets()
        self.get_patterns()
        self.load_pattern_set(pattern_set)

        self.active_slot = 0
        self.ative_pattern_id = ''
        self.active_sequence_idx = 0


# Load/save pattern set

    @Slot()
    def on_savePatternSet_clicked(self):
        self.save_pattern_set()
        # Prompt user for name or overwrite
        # Load slot1    

    @Slot()
    def on_selectPatternSet_activated(self):
        self.load_pattern_set(self.selectPatternSet.getText())
        # Load new pattern set/prompt user to save changes
        # Import the pattern set to the editor state storage data structure    

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

# Load/save pattern

    @Slot()
    def on_selectPattern_activated(self):
        self.load_pattern(self.getText())
        return

    @Slot()
    def on_savePattern_clicked(self):
        self.save_pattern()
        return

# Edit seed ratios

    @Slot()
    def on_addEuclidean_clicked(self):
        #TODO check if valid sequence 
        if self.engine.add_sequence(self.active_pattern_id, [self.ui.steps.value(), self.ui.length.value()]):
            self.update_grid()
            self.unsaved_pattern_changes = True
            print('Added')
        else:
            print('Sequence bank full')

    @Slot()
    def on_addX0x_clicked(self):
        #TODO launch checkbox widget
        return

    @Slot()
    def on_addText_clicked(self):
        #TODO check if valid sequence 
        text = QInputDialog.getText(title='Enter Sequence As Text', label='Use ^ for on and _ for off')
        if self.engine.add_sequence(self.active_pattern_id, text):
            self.update_grid()
            self.unsaved_pattern_changes = True
            print('Added')
        else:
            print('Sequence bank full')

    @Slot()
    def on_clearSequences_clicked(self):
        if QMessageBox.question(self, 'Clear Ratios', 'Clear all ratios?') == QMessageBox.Yes: 
            self.engine.patterns[self.active_pattern_id]['sequences'] = []
            self.update_grid()

# Pattern recipe dispaly helpers

    def create_pattern_grid(self):

        self.sequence_buttons = [ \
            self.ui.sequence1, self.ui.sequence2, self.ui.sequence3, self.ui.sequence4,\
            self.ui.sequence5, self.ui.sequence6, self.ui.sequence7, self.ui.sequence8,\
            self.ui.sequence9, self.ui.sequence10, self.ui.sequence11, self.ui.sequence12,\
            self.ui.sequence13, self.ui.sequence14, self.ui.sequence15, self.ui.sequence16,\
        ]
        for idx, button in enumerate(self.sequence_buttons):
            button.clicked.connect(lambda state=True, x=idx: self.seed_button_pushed(x))

    def seed_button_pushed(self, idx):
        self.engine.remove_sequence(self.active_pattern_id, idx)
        self.update_grid()

    def update_grid(self):
        sequences = self.engine.patterns[self.active_pattern_id]['sequences']
        idx = -1
        print(sequences)
        for idx, sequence in enumerate(sequences):
            self.sequence_buttons[idx].show()
            #TODO display non euclidean recipes
            self.sequence_buttons[idx].setText('%s/%s' % (sequence['recipe'][0], sequence['recipe'][1]))
        for i in range(idx+1, 16):
            self.sequence_buttons[i].hide()


# Save/load helpers

    # Set menu
    def get_pattern_sets(self):
        with open(self.pattern_dir + 'local_manifest.json') as local_manifest:
            self.local_pattern_sets = json.load(local_manifest)
        with open(self.pattern_dir + 'remote_manifest.json') as remote_manifest:
            self.remote_pattern_sets = json.load(remote_manifest)
        self.ui.selectPatternSet.clear()
        for pattern_set in [*self.local_pattern_sets] + [*self.remote_pattern_sets]:
            self.ui.selectPatternSet.addItem(pattern_set) 
        for pattern_set in self.remote_pattern_sets:
            for pattern in pattern_set:
                self.remote_patterns.append(pattern)

    def get_patterns(self):
        for root, dirs, files in os.walk(self.pattern_dir + 'patterns'):
            for file in files:
                slug = file.split('.json')[0]
                self.patterns.append(slug)
        for pattern in self.patterns:
            self.ui.selectPattern.addItem(pattern) 
    
    def load_pattern_set(self, pattern_set):
        self.engine.load_pattern_set(pattern_set)
        self.ui.slot1.setChecked(True)
        self.switch_slot(0)

    def switch_slot(self, slot_num):
        if self.unsaved_pattern_changes:
            if self.prompt_to_discard():
                switch_slot(self.active_slot)
                self.unsaved_pattern_changes = False
            else:
                return 
        self.active_slot = slot_num
        self.active_pattern_id = self.engine.pattern_set[slot_num]
        self.load_pattern(self.active_pattern_id)

    def prompt_to_discard(self):
        if QMessageBox.question(self, "", 'Unsaved changes will be lost, continue?') == QMessageBox.Yes:
            return True
        else:
            return False
        # Ask user if they wish to save any unsaved changes

    def load_pattern(self, pattern_id):
        if self.unsaved_pattern_changes:
            if self.prompt_to_discard():
                self.unsaved_pattern_changes = False
            else:
                cb_index = self.ui.selectPattern.findText(self.active_pattern_id)
                self.ui.selectPattern.setCurrentIndex(cb_index) 
                return 
        cb_index = self.ui.selectPattern.findText(pattern_id)
        self.ui.selectPattern.setCurrentIndex(cb_index)
        self.active_pattern_id = pattern_id
        self.update_grid()        

    def save_pattern(self):
        filename = QInputDialog.getText(self, 'Save Pattern', 'Enter pattern name:')
        if filename in [*self.local_pattern_sets]:
            if QMessageBox.question(self, 'Overwrite?', 'Name in use, overwrite?') == QMessageBox.No:
                return
        while filename in [*self.remote_pattern_sets]:
            filename = QInputDialog.getText(self, 'Save Pattern', 'Reserved name, enter new name:') 
            if filename in [*self.local_pattern_sets]:
                if QMessageBox.question(self, 'Overwrite?', 'Name in use, overwrite?') == QMessageBox.No:
                    return
        self.unsaved_pattern_changes = False
        self.engine.save_pattern(filename)
        # Save edit buffer to file

    def save_pattern_set(self):
        filename = QInputDialog.getText(self, 'Save Pattern Set', 'Enter pattern set name:')
        if filename in [*self.local_pattern_sets]:
            if QMessageBox.question(self, 'Overwrite?', 'Name in use, overwrite?') == QMessageBox.No:
                return
        while filename in [*self.remote_pattern_sets]:
            filename = QInputDialog.getText(self, 'Save Pattern Set', 'Reserved name, enter new name:') 
            if filename in [*self.local_pattern_sets]:
                if QMessageBox.question(self, 'Overwrite?', 'Name in use, overwrite?') == QMessageBox.No:
                    return
        self.unsaved_pattern_changes = False
        self.engine.save_pattern_set(filename)
        # Save edit buffer to file
