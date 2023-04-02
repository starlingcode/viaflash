from PySide6.QtWidgets import QInputDialog, QMessageBox, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QSizePolicy
from PySide6.QtCore import Slot, Qt, QMimeData
from PySide6.QtGui import QUndoCommand, QUndoStack, QKeySequence, QDrag

from ui_resources.ui_osc3_quantization_editor import Ui_osc3QuantizationEditor
from viatools.osc3_quantizations import Osc3QuantizationSet
from via_resource_editor import ViaResourceEditor

from dragremovebuttons import DragButton, RemoveButton

class ChordButton(QWidget):

    def __init__(self, parent_window):
        super().__init__()
        self.drag = DragButton(parent_window)
        self.remove = RemoveButton()
        self.degrees = QLabel()
        self.degrees.setAlignment(Qt.AlignHCenter)
        self.notes = QLabel()
        self.notes.setAlignment(Qt.AlignHCenter)
        self.layout = QHBoxLayout(self)
        policy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.degrees.setSizePolicy(policy)
        self.notes.setSizePolicy(policy)
        self.layout.addWidget(self.drag)
        self.layout.addWidget(self.degrees)
        self.layout.addWidget(self.notes)
        self.layout.addWidget(self.remove)
        self.idx = 0
        self.parent_window = parent_window
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setSizePolicy(policy)

    def update_ratio(self, pitch1, pitch2, note_list):
        self.degrees.setText('%d, %d' % (int(pitch1), int(pitch2)))
        scale_size = len(note_list)
        self.notes.setText('%s, C, %s' % (note_list[int(pitch1) % scale_size], note_list[int(pitch2) % scale_size]))

    def set_idx(self, idx):
        self.idx = idx
        self.drag.set_idx(idx)

# Data controller functions

class AddNoteCommand(QUndoCommand):
    
    def __init__(self, chord_set, note, ui_callback):
        super().__init__()
        self.setText('Add note to scale')
        self.chord_set = chord_set
        self.note = note
        self.ui_callback = ui_callback

    def redo(self):
        self.idx = self.chord_set.add_note(self.note)
        self.ui_callback()

    def undo(self):
        self.chord_set.remove_note(self.note)
        self.ui_callback()


class RemoveNoteCommand(QUndoCommand):
    
    def __init__(self, chord_set, note, ui_callback):
        super().__init__()
        self.setText('Remove note from scale')
        self.chord_set = chord_set
        self.note = note
        self.ui_callback = ui_callback

    def redo(self):
        self.idx = self.chord_set.remove_note(self.note)
        self.ui_callback()

    def undo(self):
        self.chord_set.add_note(self.note)
        self.ui_callback()


class AddChordCommand(QUndoCommand):
    
    def __init__(self, chord_set, chord, ui_callback):
        super().__init__()
        self.setText('Add chord %d/%d' % (chord[0], chord[1]))
        self.chord_set = chord_set
        self.chord = chord
        self.ui_callback = ui_callback

    def redo(self):
        self.idx = self.chord_set.add_chord(self.chord)
        self.ui_callback()


    def undo(self):
        self.chord_set.remove_chord(self.idx)
        self.ui_callback()


class RemoveChordCommand(QUndoCommand):

    def __init__(self, chord_set, idx, ui_callback):
        super().__init__()
        self.setText('Remove chord at index %d' % (idx))
        self.chord_set = chord_set
        self.idx = idx
        self.ui_callback = ui_callback


    def redo(self):
        self.chord = self.chord_set.remove_chord(self.idx)
        self.ui_callback()


    def undo(self):
        self.chord_set.add_chord(self.chord, self.idx)
        self.ui_callback()


class ClearChordsCommand(QUndoCommand):

    def __init__(self, chord_set, ui_callback):
        super().__init__()
        self.setText('Clear chords')
        self.chord_set = chord_set
        self.ui_callback = ui_callback


    def redo(self):
        self.old_order = self.chord_set.clear_chords()
        self.ui_callback()


    def undo(self):
        self.chord_set.reload_data(self.old_order)
        self.ui_callback()


class ReorderChordsCommand(QUndoCommand):
    
    def __init__(self, chord_set, idx_to_move, destination, ui_callback):
        super().__init__()
        self.setText('Move chord from index %d to %d' % (idx_to_move + 1, destination + 1))
        self.chord_set = chord_set
        self.idx_to_move = idx_to_move
        self.destination = destination
        self.ui_callback = ui_callback


    def redo(self):
        self.chord_set.reorder_chords(self.idx_to_move, self.destination)
        self.redo_destination = self.idx_to_move
        self.redo_idx_to_move = self.destination
        self.ui_callback()


    def undo(self):
        self.chord_set.reorder_chords(self.redo_idx_to_move, self.redo_destination)
        self.ui_callback()


class Osc3QuantizationEditor(ViaResourceEditor, Ui_osc3QuantizationEditor):
    def __init__(self, resource_dir='./', remote_resources = {}, slug='original', style_text=""):
        super().__init__() 
        self.setupUi(self)
        self.setStyleSheet(style_text)

        self.remote_resources = remote_resources

        self.set = Osc3QuantizationSet(resource_dir, slug)
        self.set_slug = slug

        self.update_resource_sets()
        self.update_resources()

        self.create_note_grid()
        self.create_chord_grid()
        self.update_resource_ui()

        for slot_num in range(0, 3):
            eval('self.slot%d' % (slot_num+1)).clicked.connect(lambda state=True, x=slot_num: self.switch_slot(x))
            eval('self.slot%d' % (slot_num+1)).setToolTip("Edit quanitzation mode " + str(slot_num + 2))
        self.selectResource.activated.connect(self.handle_select_resource)
        self.saveResource.clicked.connect(lambda state=True: self.handle_save_resource())

        self.switch_slot(0)

        self.setFocusPolicy(Qt.ClickFocus)

        self.initToolTips()

# Edit scale recipe

    @Slot()
    def on_addChord_clicked(self):
        add_chord = AddChordCommand(self.set.resources[self.active_idx], [self.osc2Pitch.value(), self.osc3Pitch.value()], self.update_resource_ui)
        self.resource_undo_stack.push(add_chord)

    @Slot()
    def on_clearAll_clicked(self):
        clear_chords = ClearChordsCommand(self.set.resources[self.active_idx], self.update_resource_ui)
        self.resource_undo_stack.push(clear_chords)

    @Slot()
    def on_osc2Pitch_valueChanged(self):
        scale_names = self.get_note_names()
        scale_size = len(scale_names)
        self.osc2Note.setText(scale_names[self.osc2Pitch.value() % scale_size])

    @Slot()
    def on_osc3Pitch_valueChanged(self):
        scale_names = self.get_note_names()
        scale_size = len(scale_names)
        self.osc3Note.setText(scale_names[self.osc3Pitch.value() % scale_size])

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
            button.setToolTip("Add this note to the quantization (assuming a root of C)")

    def note_button_pushed(self, idx):
        if self.note_buttons[idx].isChecked():
            add_note = AddNoteCommand(self.set.resources[self.active_idx], idx, self.update_resource_ui)
            self.resource_undo_stack.push(add_note)
        else:
            remove_note = RemoveNoteCommand(self.set.resources[self.active_idx], idx, self.update_resource_ui)
            self.resource_undo_stack.push(remove_note)

    def create_chord_grid(self):

        self.chord_buttons = []
        self.chordHolder = QWidget()
        self.chordGrid = QVBoxLayout()

        num_tables = 16
        for row in range(0, num_tables):
            idx = row
            new_button = ChordButton(self)
            new_button.remove.clicked.connect(lambda state=True, x=idx: self.chord_button_pushed(x))
            new_button.set_idx(idx)
            self.chord_buttons.append(new_button)
            self.chordGrid.addWidget(new_button, row)

        self.chordGrid.insertStretch(-1)

        self.chordGrid.setSpacing(0)
        # self.seedRatioGrid.setContentsMargins(0,0,0,0)

        self.chordHolder.setLayout(self.chordGrid)
        self.chordScrollArea.setWidget(self.chordHolder)

    def chord_button_pushed(self, idx):
        remove_chord = RemoveChordCommand(self.set.resources[self.active_idx], idx, self.update_resource_ui)
        self.resource_undo_stack.push(remove_chord)

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
            self.chord_buttons[idx].update_ratio(chord[0], chord[1], self.get_note_names())
        for i in range(idx+1, 16):
            self.chord_buttons[i].hide()
        if len(self.set.resources[self.active_idx].data['chords']) < 16:
            self.addChord.setEnabled(True)
        else:
            self.addChord.setEnabled(False)
        
        scale_names = self.get_note_names()
        scale_size = len(scale_names)
        self.osc2Note.setText(scale_names[self.osc2Pitch.value() % scale_size])
        self.osc3Note.setText(scale_names[self.osc3Pitch.value() % scale_size])

        if self.set.is_clean():
            self.saveResourceSet.setEnabled(False)
        else:
            self.saveResourceSet.setEnabled(True)

    def get_note_names(self):
        notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        note_set = []
        for note in self.set.resources[self.active_idx].data['notes']:
            note_set.append(notes[note])
        return note_set

    def handle_drop(self, destination_idx):
        reorder = ReorderChordsCommand(self.set.resources[self.active_idx], self.dragged_idx, destination_idx, self.update_resource_ui)
        self.resource_undo_stack.push(reorder)

    def showEvent(self, event):
        super().showEvent(event)
        self.undo_stack_init()

    def clear_menu(self):
        self.menu.clear()

    def initToolTips(self):
        super().initToolTips()
        self.selectResource.setToolTip("Select an available quantization for this mode and open it in the editor")
        self.saveResource.setToolTip("Save the edited quantization")
        self.addChord.setToolTip("Add the chord specified by the Oscillator 2 and 3 Pitch selectors")
        self.osc2Pitch.setToolTip("Set the pitch offset in scale degrees from the root for oscillator 2 for this chord")
        self.osc3Pitch.setToolTip("Set the pitch offset in scale degrees from the root for oscillator 3 for this chord")
        self.clearAll.setToolTip("Clear all chords except for a default of (0, 0)")




