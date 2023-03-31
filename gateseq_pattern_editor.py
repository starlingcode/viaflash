from PySide6.QtWidgets import QInputDialog, QMessageBox, QPushButton
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QUndoCommand, QUndoStack, QKeySequence

from ui_resources.ui_gateseq_pattern_editor import Ui_gateseqPatternEditor
from viatools.gateseq_patterns import GateseqPatternSet
from via_resource_editor import ViaResourceEditor

from gateseq_sequence_edit import GateseqSequenceEdit


class AddRecipeCommand(QUndoCommand):
    
    def __init__(self, pattern, recipe, ui_callback):
        super().__init__()
        self.setText('Add %d/%d' % (recipe[0], recipe[1]))
        self.pattern = pattern
        self.recipe = recipe
        self.ui_callback = ui_callback
        self.old_fill = None

    def redo(self):
        self.idx = self.pattern.add_data(self.recipe)
        self.ui_callback()

    def undo(self):
        self.pattern.remove_data(self.idx)
        self.ui_callback()


class RemoveRecipeCommand(QUndoCommand):

    def __init__(self, pattern, idx, ui_callback):
        super().__init__()
        self.setText('Remove index %d' % (idx + 1))
        self.pattern = pattern
        self.idx = idx
        self.ui_callback = ui_callback


    def redo(self):
        self.ratio = self.pattern.remove_data(self.idx)
        self.ui_callback()


    def undo(self):
        self.pattern.add_data(self.ratio, self.idx)
        self.ui_callback()



class ClearRecipesCommand(QUndoCommand):

    def __init__(self, pattern, ui_callback):
        super().__init__()
        self.setText('Clear sequences')
        self.pattern = pattern
        self.ui_callback = ui_callback


    def redo(self):
        self.old_order = self.pattern.clear_data()
        self.ui_callback()


    def undo(self):
        self.pattern.reload_data(self.old_order)
        self.ui_callback()


class UpdateStepCommand(QUndoCommand):

    def __init__(self, pattern, seq_idx, step_idx, state, ui_callback):
        super().__init__()
        self.setText('Update sequence %d step %d' % (seq_idx + 1, step_idx + 1))
        self.pattern = pattern
        self.seq_idx = seq_idx
        self.step_idx = step_idx
        self.state = state
        self.ui_callback = ui_callback


    def redo(self):
        self.backup = self.pattern.get_data()
        self.new_idx = self.pattern.update_step(self.seq_idx, self.step_idx, self.state)
        self.ui_callback()


    def undo(self):
        self.pattern.reload_data(self.backup)
        self.ui_callback()


class UpdateLengthCommand(QUndoCommand):

    def __init__(self, pattern, idx, length, ui_callback):
        super().__init__()
        self.setText('Update sequence %d to length' % (idx + 1, length))
        self.pattern = pattern
        self.idx = idx
        self.length = length
        self.ui_callback = ui_callback


    def redo(self):
        self.backup = self.pattern.get_recipe(self.idx)
        self.new_idx = self.pattern.update_length(self.idx, self.length)
        self.ui_callback()


    def undo(self):
        self.pattern.reload_recipe(self.new_idx, self.backup)
        self.ui_callback()


class ReorderPatternCommand(QUndoCommand):
    
    def __init__(self, pattern, idx_to_move, destination, ui_callback):
        super().__init__()
        self.setText('Move sequence %d to %d' % (idx_to_move + 1, destination + 1))
        self.pattern = pattern
        self.idx_to_move = idx_to_move
        self.destination = destination
        self.ui_callback = ui_callback


    def redo(self):
        self.pattern.reorder_data(self.idx_to_move, self.destination)
        self.redo_destination = self.idx_to_move
        self.redo_idx_to_move = self.destination
        self.ui_callback()


    def undo(self):
        self.pattern.reorder_data(self.redo_idx_to_move, self.redo_destination)
        self.ui_callback()


class UpdateSortedCommand(QUndoCommand):
    
    def __init__(self, pattern, is_sorted, ui_callback):
        super().__init__()
        self.setText('Set sorted to %s' % (str(is_sorted)))
        self.pattern = pattern
        self.is_sorted = is_sorted
        self.ui_callback = ui_callback


    def redo(self):
        if self.is_sorted:
            self.old_order = self.pattern.update_sorted(True)
            self.ui_callback()
        else:
            self.old_order = self.pattern.update_sorted(False)
            if self.old_order:
                self.pattern.reload_data(self.old_order)
            self.ui_callback()


    def undo(self):
        if not self.is_sorted:
            self.old_order = self.pattern.update_sorted(True)
            self.ui_callback()
        else:
            self.pattern.update_sorted(False)
            self.pattern.reload_data(self.old_order)
            self.ui_callback()


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

        self.switch_slot(0)

        self.unsorted_data = None

        self.setFocusPolicy(Qt.ClickFocus)

# Edit pattern recipe

    @Slot()
    def on_length_valueChanged(self):
        self.steps.setMaximum(self.length.value())

    @Slot()
    def on_addEuclidean_clicked(self):
        add_recipe = AddRecipeCommand(self.set.resources[self.active_idx], [self.steps.value(), self.length.value()], self.update_resource_ui)
        self.resource_undo_stack.push(add_recipe)

    @Slot()
    def on_clearSequences_clicked(self):
        clear_recipes = ClearRecipesCommand(self.set.resources[self.active_idx], self.update_resource_ui)
        self.resource_undo_stack.push(clear_recipes)

    @Slot()
    def on_rulerSize_valueChanged(self):
        for editor in self.sequence_editors: 
            editor.reset_ruler(self.rulerSize.value())

    @Slot()
    def on_sorted_clicked(self):
        self.unsorted_data = self.set.resources[self.active_idx].get_data()
        sorted_command = UpdateSortedCommand(self.set.resources[self.active_idx], True, self.update_resource_ui)
        self.resource_undo_stack.push(sorted_command)
        #self.sortedHelp.setText(self.sorted_help)
        self.sorted_flag = True


    @Slot()
    def on_unsorted_clicked(self):
        if self.unsorted_data:
            self.set.resources[self.active_idx].reload_data(self.unsorted_data)
        sorted_command = UpdateSortedCommand(self.set.resources[self.active_idx], False, self.update_resource_ui)
        self.resource_undo_stack.push(sorted_command)
        #self.sortedHelp.setText(self.unsorted_help)
        self.sorted_flag = False

# Pattern recipe dispaly helpers

    def create_pattern_grid(self):
        self.sequence_editors = []
        for i in range(0, 16):
            seq_edit = GateseqSequenceEdit(self)
            seq_edit.remove.clicked.connect(lambda state=True, x=i: self.remove_button_pushed(x))
            for j in range(0, 64):
                seq_edit.step_buttons[j].clicked.connect(lambda state=True, x=i, y=j : self.step_button_pushed(x, y))
            seq_edit.length_entry.valueChanged.connect(lambda state=True, x=i : self.update_sequence_length(x))
            self.sequence_editors.append(seq_edit)
            self.sequenceEditLayout.addWidget(seq_edit)

        self.sequenceEditLayout.setContentsMargins(0,0,0,0)            
        self.update_resource_ui()

    def remove_button_pushed(self, idx):
        remove_recipe = RemoveRecipeCommand(self.set.resources[self.active_idx], idx, self.update_resource_ui)
        self.resource_undo_stack.push(remove_recipe)

    def step_button_pushed(self, seq_idx, step_idx):
        if self.sequence_editors[seq_idx].step_buttons[step_idx].isChecked():
            update_step = UpdateStepCommand(self.set.resources[self.active_idx], seq_idx, step_idx, True, self.update_resource_ui)
            self.resource_undo_stack.push(update_step)
        else:
            update_step = UpdateStepCommand(self.set.resources[self.active_idx], seq_idx, step_idx, False, self.update_resource_ui)
            self.resource_undo_stack.push(update_step)

    def update_sequence_length(self, seq_idx):
        # Stopping an infinte loop ... ewwwwiiieeee!
        old_length = self.set.resources[self.active_idx].get_length(seq_idx)
        length = self.sequence_editors[seq_idx].length_entry.value()
        if old_length != length:
            update_length = UpdateLengthCommand(self.set.resources[self.active_idx], seq_idx, length, self.update_resource_ui)
            self.resource_undo_stack.push(update_length)

    def handle_drop(self, destination_idx):
        reorder = ReorderPatternCommand(self.set.resources[self.active_idx], self.dragged_idx, destination_idx, self.update_resource_ui)
        self.resource_undo_stack.push(reorder)

    def update_resource_ui(self):
        self.resourceDescription.setText(self.set.resources[self.active_idx].data['description'])

        self.sorted.setChecked(True)
        if 'sorted' in self.set.resources[self.active_idx].data:
            if self.set.resources[self.active_idx].data['sorted'] is False:
                self.unsorted.setChecked(True)
                #self.sortedHelp.setText(self.unsorted_help)
                self.sorted_flag = False
            else:
                #self.sortedHelp.setText(self.sorted_help)
                self.sorted_flag = True
        else:
            #self.sortedHelp.setText(self.sorted_help)
            self.sorted_flag = True

        sequences = self.set.resources[self.active_idx].data['sorted_patterns']
        idx = -1
        for idx, sequence in enumerate(sequences):
            for button in self.sequence_editors[idx].step_buttons:
                button.setChecked(False)
            self.sequence_editors[idx].show()
            seq_text_tag = self.set.resources[self.active_idx].get_name(idx)
            self.sequence_editors[idx].label.setText(seq_text_tag)
            baked = self.set.resources[self.active_idx].expand_sequence(sequence)
            for i in range(0,64):
                if baked[i % len(baked)] == 1:
                    self.sequence_editors[idx].step_buttons[i].setChecked(True)
                self.sequence_editors[idx].step_buttons[i].setEnabled(True)
            for i in range(len(baked), 64):
                self.sequence_editors[idx].step_buttons[i].setEnabled(False)
            self.sequence_editors[idx].length_entry.setValue(len(baked))
            self.sequence_editors[idx].set_idx(idx)
        for i in range(idx+1, 16):
            self.sequence_editors[i].hide()
        if len(sequences) < 16:
            self.addEuclidean.setEnabled(True)
        else:
            self.addEuclidean.setEnabled(False)

        if self.set.is_clean():
            self.saveResourceSet.setEnabled(False)
        else:
            self.saveResourceSet.setEnabled(True)

    def showEvent(self, event):
        super().showEvent(event)
        self.undo_stack_init()

    def clear_menu(self):
        self.undo_action.setVisible(False)
        self.redo_action.setVisible(False)


