from PySide6.QtWidgets import QInputDialog, QMessageBox, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QSizePolicy
from PySide6.QtCore import Slot, Qt, QMimeData
from PySide6.QtGui import QUndoCommand, QUndoStack, QKeySequence

from ui_osc3_quantization_editor import Ui_osc3QuantizationEditor
from viatools.osc3_quantizations import Osc3QuantizationSet
from via_resource_editor import ViaResourceEditor

class ChordButton(QWidget):

    def __init__(self, parent_window):
        super().__init__()
        self.setAcceptDrops(True)
        self.button = QPushButton()
        self.degrees = QLabel()
        self.degrees.setAlignment(Qt.AlignHCenter)
        self.notes = QLabel()
        self.notes.setAlignment(Qt.AlignHCenter)
        self.layout = QHBoxLayout(self)
        policy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.button.setSizePolicy(policy)
        self.degrees.setSizePolicy(policy)
        self.notes.setSizePolicy(policy)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.degrees)
        self.layout.addWidget(self.notes)
        self.idx = 0
        self.parent_window = parent_window
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setSizePolicy(policy)


    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.RightButton:
            return

        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        self.parent_window.dragged_idx = self.idx

        dropAction = drag.exec()


    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            QPushButton.mousePressEvent(self, e)


    def dragEnterEvent(self, e):
        e.accept()


    def dropEvent(self, e):
        if not self.parent_window.sorted_flag:
            self.parent_window.handle_drop(self.idx)

    def update_ratio(self, pitch1, pitch2, note_list):
        self.button.setText('Remove')
        self.degrees.setText('%d, %d' % (int(pitch1), int(pitch2)))
        scale_size = len(note_list)
        self.notes.setText('%s, C, %s' % (note_list[int(pitch1) % scale_size], note_list[int(pitch2) % scale_size]))

# Data controller functions

class AddNoteCommand(QUndoCommand):
    
    def __init__(self, chord_set, pitch1, pitch2, ui_callback):
        super().__init__()
        #self.setText('Add %d/%d' % (numerator, denominator))
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
        #self.setText('Add %d/%d' % (numerator, denominator))
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
        #self.setText('Add %d/%d' % (numerator, denominator))
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
        #self.setText('Remove index %d' % (idx))
        self.chord_set = chord_set
        self.idx = idx
        self.ui_callback = ui_callback


    def redo(self):
        self.chord = self.chord_set.remove_chord(self.idx)
        self.ui_callback()


    def undo(self):
        self.idx = self.chord_set.add_chord(self.chord)
        self.ui_callback()


class ClearChordsCommand(QUndoCommand):

    def __init__(self, chord_set, ui_callback):
        super().__init__()
        # self.setText('Remove index %d' % (idx))
        self.chord_set = scale
        self.ui_callback = ui_callback


    def redo(self):
        self.old_order = self.chord_set.clear_data()
        self.ui_callback()


    def undo(self):
        self.chord_set.reload_data(self.old_order)
        self.ui_callback()


class ReorderChordsCommand(QUndoCommand):
    
    def __init__(self, chord_set, idx_to_move, destination, ui_callback):
        super().__init__()
        # self.setText('Remove index %d' % (idx))
        self.chord_set = scale
        self.idx_to_move = idx_to_move
        self.destination = destination
        self.ui_callback = ui_callback


    def redo(self):
        self.chord_set.reorder_data(self.idx_to_move, self.destination)
        self.redo_destination = self.idx_to_move
        self.redo_idx_to_move = self.destination
        self.ui_callback()


    def undo(self):
        self.chord_set.reorder_data(self.redo_idx_to_move, self.redo_destination)
        self.ui_callback()


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

        self.create_undo_stack()

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
            new_button.button.clicked.connect(lambda state=True, x=idx: self.chord_button_pushed(x))
            new_button.idx = idx
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

    def get_note_names(self):
        notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        note_set = []
        for note in self.set.resources[self.active_idx].data['notes']:
            note_set.append(notes[note])
        return note_set

    def handle_drop(self, destination_idx):
        reorder = ReorderScaleCommand(self.set.resources[self.active_idx], self.dragged_idx, destination_idx, self.update_resource_ui)
        self.resource_undo_stack.push(reorder)

    def create_undo_stack(self):
        self.resource_undo_stack = QUndoStack()
        self.undo_action = self.resource_undo_stack.createUndoAction(self, "Undo")
        self.undo_action.setShortcuts(QKeySequence.Undo)
        self.redo_action = self.resource_undo_stack.createRedoAction(self, "Redo")
        self.redo_action.setShortcuts(QKeySequence.Redo)
        self.addAction(self.undo_action)
        self.addAction(self.redo_action)

    def handle_drop(self, destination_idx):
        reorder = ReorderChordsCommand(self.set.resources[self.active_idx], self.dragged_idx, destination_idx, self.update_resource_ui)
        self.resource_undo_stack.push(reorder)

