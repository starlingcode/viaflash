from PySide6.QtWidgets import QInputDialog, QMessageBox 
from PySide6.QtCore import Slot

from ui_osc3_quantization_editor import Ui_osc3QuantizationEditor
from viatools.osc3_quantizations import Osc3QuantizationSet
from via_resource_editor import ViaResourceEditor

class Osc3QuantizationEditor(ViaResourceEditor, Ui_osc3QuantizationEditor):
    def __init__(self, resource_dir='./', remote_resources = {}, slug='original', style_text=""):
        super().__init__() 
        self.setupUi(self)
        self.setStyleSheet(style_text)

        self.remote_resources = remote_resources
        # TODO check if new remote resource or set collides with existing local slug

        self.set = Osc3QuantizationSet(resource_dir, slug)
        self.set_slug = slug

        self.update_resource_sets()
        self.update_resources()

        self.create_note_grid()
        self.create_chord_grid()
        self.update_resource_ui()

        for slot_num in range(0, 3):
            eval('self.slot%d' % (slot_num+1)).clicked.connect(lambda state=True, x=slot_num: self.switch_slot(x))
        self.selectResource.activated.connect(self.handle_select_resource)
        self.saveResource.clicked.connect(lambda state=True: self.handle_save_resource())

        self.slot1.setChecked(True)
        self.switch_slot(0)

# Edit scale recipe

    @Slot()
    def on_addChord_clicked(self):
        if (len(self.set.resources[self.active_idx].data['chords']) < 16):
            self.set.resources[self.active_idx].add_chord([self.osc2Pitch.value(), self.osc3Pitch.value()])
            self.update_resource_ui()
            self.unsaved_changes = True
        else:
            QMessageBox(title='Chord set full', text='Click a chord to remove it.')

    @Slot()
    def on_padToFill_clicked(self):
        self.set.resources[self.active_idx].pad_to_length()
        self.update_resource_ui()

    @Slot()
    def on_clearSequences_clicked(self):
        if QMessageBox.question(self, 'Clear Chords', 'Clear all chords?') == QMessageBox.Yes: 
            self.set.resources[self.active_idx].data['chords'] = []
            self.update_resource_ui()

# Chord dispaly helpers

    def create_note_grid(self):

        self.note_buttons = [ \
            self.note1, self.note2, self.note3, self.note4,\
            self.note5, self.note6, self.note7, self.note8,\
            self.note9, self.note10, self.note11, self.note12
        ]
        for idx, button in enumerate(self.note_buttons):
            button.clicked.connect(lambda state=True, x=idx: self.note_button_pushed(x))
            button.setAutoExclusive(False)

    def note_button_pushed(self, idx):
        if self.note_buttons[idx].isChecked():
            self.set.resources[self.active_idx].add_note(idx)
        else:
            self.set.resources[self.active_idx].remove_note(idx)

    def create_chord_grid(self):

        self.chord_buttons = [ \
            self.chord1, self.chord2, self.chord3, self.chord4,\
            self.chord5, self.chord6, self.chord7, self.chord8,\
            self.chord9, self.chord10, self.chord11, self.chord12,\
            self.chord13, self.chord14, self.chord15, self.chord16,\
        ]
        for idx, button in enumerate(self.chord_buttons):
            button.clicked.connect(lambda state=True, x=idx: self.chord_button_pushed(x))

    def chord_button_pushed(self, idx):
        self.set.resources[self.active_idx].remove_chord(idx)
        self.update_resource_ui()

    def update_resource_ui(self):
        self.resourceDescription.setText(self.set.resources[self.active_idx].data['description'])
        scale = self.set.resources[self.active_idx].data['notes']
        for pitch in range(0, 12):
            if pitch in scale:
                self.note_buttons[pitch].setChecked(True)
            else:
                self.note_buttons[pitch].setChecked(False)
        scale_size = len(scale)
        self.osc2Pitch.setMinimum(-scale_size + 1)
        self.osc2Pitch.setMaximum(scale_size - 1)
        self.osc3Pitch.setMinimum(-scale_size + 1)
        self.osc3Pitch.setMaximum(scale_size - 1)
        chords = self.set.resources[self.active_idx].data['chords']
        idx = -1
        for idx, chord in enumerate(chords):
            self.chord_buttons[idx].show()
            #TODO display non euclidean recipes
            self.chord_buttons[idx].setText('%s/%s' % (chord[0], chord[1]))
        for i in range(idx+1, 16):
            self.chord_buttons[i].hide()

