from PySide6.QtWidgets import QInputDialog, QMessageBox 
from PySide6.QtCore import Slot

from ui_gateseq_pattern_editor import Ui_gateseqPatternEditor
from viatools.gateseq_patterns import GateseqPatternSet
from via_resource_editor import ViaResourceEditor

class GateseqPatternEditor(ViaResourceEditor, Ui_gateseqPatternEditor):
    def __init__(self, resource_dir='./', remote_resources = {}, slug='original'):
        super().__init__() 
        self.setupUi(self)

        self.remote_resources = remote_resources
        # TODO check if new remote resource or set collides with existing local slug

        self.set = GateseqPatternSet(resource_dir, slug)

        self.update_resource_sets()
        self.update_resources()

        self.create_pattern_grid()

        self.slot1.setChecked(True)
        self.switch_slot(0)

# Edit pattern recipe

    @Slot()
    def on_length_valueChanged(self):
        self.steps.setMaximum(self.length.value())

    @Slot()
    def on_addEuclidean_clicked(self):
        if (len(self.set.resources[self.active_idx].data) < 16):
            self.set.resources[self.active_idx].add_data([self.steps.value(), self.length.value()])
            self.update_resource_ui()
            self.unsaved_changes = True
        else:
            QMessageBox('Pattern full', 'Click a sequence to remove it.')

    @Slot()
    def on_addX0x_clicked(self):
        #TODO launch checkbox widget
        return

    @Slot()
    def on_addText_clicked(self):
        #TODO check if valid sequence 
        if len(self.set.resources[self.active_idx].data) < 16:
            text = QInputDialog.getText(title='Enter Sequence As Text', label='Use ^ for on and _ for off')
            for character in text:
                if character not in ['^','_']:
                    QMessageBox('Entry problem', 'Please only use ^ and _ in your entry')
                    return
            self.set.resources[self.active_idx].add_data(text)
            self.update_resource_ui()
            self.unsaved_changes = True
        else:
            QMessageBox('Pattern full', 'Click a sequence to remove it.')

    @Slot()
    def on_clearSequences_clicked(self):
        if QMessageBox.question(self, 'Clear Ratios', 'Clear all ratios?') == QMessageBox.Yes: 
            self.set.resources[self.active_idx].data = []
            self.update_resource_ui()

# Pattern recipe dispaly helpers

    def create_pattern_grid(self):

        self.sequence_buttons = [ \
            self.sequence1, self.sequence2, self.sequence3, self.sequence4,\
            self.sequence5, self.sequence6, self.sequence7, self.sequence8,\
            self.sequence9, self.sequence10, self.sequence11, self.sequence12,\
            self.sequence13, self.sequence14, self.sequence15, self.sequence16,\
        ]
        for idx, button in enumerate(self.sequence_buttons):
            button.clicked.connect(lambda state=True, x=idx: self.seed_button_pushed(x))
        self.update_resource_ui()

    def seed_button_pushed(self, idx):
        self.set.resources[self.active_idx].remove_data(idx)
        self.update_resource_ui()

    def update_resource_ui(self):
        sequences = self.set.resources[self.active_idx].data
        idx = -1
        for idx, sequence in enumerate(sequences):
            self.sequence_buttons[idx].show()
            #TODO display non euclidean recipes
            self.sequence_buttons[idx].setText('%s/%s' % (sequence[0], sequence[1]))
        for i in range(idx+1, 16):
            self.sequence_buttons[i].hide()

