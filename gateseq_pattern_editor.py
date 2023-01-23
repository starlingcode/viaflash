from PySide6.QtWidgets import QInputDialog, QMessageBox, QPushButton
from PySide6.QtCore import Slot

from ui_gateseq_pattern_editor import Ui_gateseqPatternEditor
from viatools.gateseq_patterns import GateseqPatternSet
from via_resource_editor import ViaResourceEditor

from gateseq_sequence_edit import GateseqSequenceEdit

class GateseqPatternEditor(ViaResourceEditor, Ui_gateseqPatternEditor):
    def __init__(self, resource_dir='./', remote_resources = {}, slug='original', style_text=""):
        super().__init__() 
        self.setupUi(self)
        self.setStyleSheet(style_text)

        self.remote_resources = remote_resources
        # TODO check if new remote resource or set collides with existing local slug

        self.set = GateseqPatternSet(resource_dir, slug)
        self.set_slug = slug

        self.update_resource_sets()
        self.update_resources()

        self.create_pattern_grid()

        for slot_num in range(0, 8):
            eval('self.slot%d' % (slot_num+1)).clicked.connect(lambda state=True, x=slot_num: self.switch_slot(x))
        self.selectResource.activated.connect(self.handle_select_resource)
        self.saveResource.clicked.connect(lambda state=True: self.handle_save_resource())

        self.slot1.setChecked(True)
        self.switch_slot(0)

# Edit pattern recipe

    @Slot()
    def on_length_valueChanged(self):
        self.steps.setMaximum(self.length.value())

    @Slot()
    def on_addEuclidean_clicked(self):
        if (len(self.set.resources[self.active_idx].data['data']) < 16):
            self.set.resources[self.active_idx].add_data([self.steps.value(), self.length.value()])
            self.update_resource_ui()
            self.unsaved_changes = True
        else:
            QMessageBox(title='Pattern full', text='Click a sequence to remove it.')

    @Slot()
    def on_clearSequences_clicked(self):
        if QMessageBox.question(self, 'Clear Sequences', 'Clear all sequences?') == QMessageBox.Yes: 
            self.set.resources[self.active_idx].data['data'] = []
            self.update_resource_ui()

# Pattern recipe dispaly helpers

    def create_pattern_grid(self):
        self.sequence_editors = []
        for i in range(0, 16):
            seq_edit = GateseqSequenceEdit()
            seq_edit.remove.clicked.connect(lambda state=True, x=i: self.remove_button_pushed(x))
            for j in range(0, 64):
                seq_edit.step_buttons[j].clicked.connect(lambda state=True, x=i, y=j : self.step_button_pushed(x, y))
            # seq_edit.length_entry.valueChanged.connect(lambda state=True, x=i : self.update_sequence_length(x))
            self.sequence_editors.append(seq_edit)
            self.sequenceEditLayout.addWidget(seq_edit)

        self.sequenceEditLayout.setContentsMargins(0,0,0,0)            
        self.update_resource_ui()

    def remove_button_pushed(self, idx):
        self.set.resources[self.active_idx].remove_data(idx)
        self.update_resource_ui()

    def step_button_pushed(self, seq_idx, step_idx):
        if self.sequence_editors[seq_idx].step_buttons[step_idx].isChecked():
            self.set.resources[self.active_idx].update_step(seq_idx, step_idx, True)
        else:
            self.set.resources[self.active_idx].update_step(seq_idx, step_idx, False)
        self.update_resource_ui()

    def update_sequence_length(self, seq_idx):
        length = self.sequence_editors[seq_idx].length_entry.value()
        self.set.resources[self.active_idx].update_length(seq_idx, length)
        self.update_resource_ui()

    def update_resource_ui(self):
        self.resourceDescription.setText(self.set.resources[self.active_idx].data['description'])
        sequences = self.set.resources[self.active_idx].data['data']
        idx = -1
        for idx, sequence in enumerate(sequences):
            for button in self.sequence_editors[idx].step_buttons:
                button.setChecked(False)
            self.sequence_editors[idx].show()
            self.sequence_editors[idx].label.setText('%s/%s' % (sequence[0], sequence[1]))
            baked = self.set.resources[self.active_idx].expand_sequence(sequence)
            for i in range(0,64):
                if baked[i % len(baked)] == 1:
                    self.sequence_editors[idx].step_buttons[i].setChecked(True)
                self.sequence_editors[idx].step_buttons[i].setEnabled(True)
            for i in range(len(baked), 64):
                self.sequence_editors[idx].step_buttons[i].setEnabled(False)
            self.sequence_editors[idx].length_entry.setValue(len(baked))
        for i in range(idx+1, 16):
            self.sequence_editors[i].hide()

