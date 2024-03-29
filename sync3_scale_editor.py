from PySide6.QtWidgets import QDialog, QSizePolicy, QMessageBox, QLabel, QFileDialog, QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QUndoCommand

from ui_resources.ui_sync3_scale_editor import Ui_sync3ScaleEditor
from ui_resources.ui_sync3_ratio_add import Ui_sync3RatioAdd
from viatools.sync3_scales import Sync3ScaleSet
from via_resource_editor import ViaResourceEditor
from dragremovebuttons import DragButton, RemoveButton

import numpy as np


class Sync3RatioAdd(QDialog, Ui_sync3RatioAdd):

    def __init__(self, parent_window):
        super().__init__()
        self.setupUi(self)
        self.parent_window = parent_window
        numerator = int(self.numerator.value())
        denominator = int(self.denominator.value())
        self.ratioDisplay.update(numerator, denominator)

        
    @Slot()
    def on_numerator_valueChanged(self):
        self.ratioDisplay.update(self.numerator.value(), self.denominator.value())


    @Slot()
    def on_denominator_valueChanged(self):
        self.ratioDisplay.update(self.numerator.value(), self.denominator.value())


    @Slot()
    def on_addRatio_clicked(self):
        self.parent_window.add_seed_ratio([self.numerator.value(), self.denominator.value()])    

class RatioRow(QWidget):

    def __init__(self, parent_window):
        super().__init__()
        self.drag = DragButton(parent_window)
        self.ratio = QLabel()
        self.ratio.setAlignment(Qt.AlignHCenter)
        self.decimal = QLabel()
        self.decimal.setAlignment(Qt.AlignHCenter)
        self.semitones = QLabel()
        self.semitones.setAlignment(Qt.AlignHCenter)
        self.remove = RemoveButton()
        self.layout = QHBoxLayout(self)
        policy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.ratio.setSizePolicy(policy)
        self.decimal.setSizePolicy(policy)
        self.semitones.setSizePolicy(policy)
        self.layout.addWidget(self.drag)
        self.layout.addWidget(self.ratio)
        self.layout.addWidget(self.decimal)
        self.layout.addWidget(self.semitones)
        self.layout.addWidget(self.remove)
        self.idx = 0
        self.parent_window = parent_window
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setSizePolicy(policy)

    def set_idx(self, idx):
        self.idx = idx
        self.drag.set_idx(idx)

    def update_ratio(self, numerator, denominator):
        self.ratio.setText('%s/%s' % (numerator, denominator))
        self.decimal.setText('%.4f' % (numerator/denominator))
        self.semitones.setText('%.4f' % (np.log2(numerator/denominator) * 12))


# Data controller functions

class AddRatioCommand(QUndoCommand):
    
    def __init__(self, scale, numerator, denominator, ui_callback):
        super().__init__()
        self.setText('Add %d/%d' % (numerator, denominator))
        self.scale = scale
        self.numerator = numerator
        self.denominator = denominator
        self.ui_callback = ui_callback
        self.old_fill = None


    def redo(self):
        self.idx = self.scale.add_data([self.numerator, self.denominator])
        can_fill = self.scale.check_fill_ok()
        if not can_fill and self.scale.get_fill() != "expand":
            self.old_fill = self.scale.set_fill('expand')
        self.ui_callback()


    def undo(self):
        self.scale.remove_data(self.idx)
        if self.old_fill:
            self.set_fill(self.old_fill)
        self.ui_callback()


class RemoveRatioCommand(QUndoCommand):

    def __init__(self, scale, idx, ui_callback):
        super().__init__()
        self.setText('Remove index %d' % (idx))
        self.scale = scale
        self.idx = idx
        self.ui_callback = ui_callback


    def redo(self):
        self.ratio = self.scale.remove_data(self.idx)
        self.ui_callback()


    def undo(self):
        self.scale.add_data(self.ratio, self.idx)
        self.ui_callback()


class ClearRatiosCommand(QUndoCommand):

    def __init__(self, scale, ui_callback):
        super().__init__()
        self.setText('Clear ratios from scale')
        self.scale = scale
        self.ui_callback = ui_callback


    def redo(self):
        self.old_order = self.scale.clear_data()
        self.ui_callback()


    def undo(self):
        self.scale.reload_data(self.old_order)
        self.ui_callback()


class ReorderScaleCommand(QUndoCommand):
    
    def __init__(self, scale, idx_to_move, destination, ui_callback):
        super().__init__()
        self.setText('Move ratio from index %d to %d' % (idx_to_move + 1, destination + 1))
        self.scale = scale
        self.idx_to_move = idx_to_move
        self.destination = destination
        self.ui_callback = ui_callback


    def redo(self):
        self.scale.reorder_data(self.idx_to_move, self.destination)
        self.redo_destination = self.idx_to_move
        self.redo_idx_to_move = self.destination
        self.ui_callback()


    def undo(self):
        self.scale.reorder_data(self.redo_idx_to_move, self.redo_destination)
        self.ui_callback()


class UpdateSortedCommand(QUndoCommand):
    
    def __init__(self, scale, is_sorted, ui_callback):
        super().__init__()
        self.setText('Set sorted to %s' % (str(is_sorted)))
        self.scale = scale
        self.is_sorted = is_sorted
        self.ui_callback = ui_callback


    def redo(self):
        if self.is_sorted:
            self.scale.update_sorted(True)
            self.ui_callback()
        else:
            self.scale.update_sorted(False)
            self.ui_callback()


    def undo(self):
        if not self.is_sorted:
            self.scale.update_sorted(True)
            self.ui_callback()
        else:
            self.scale.update_sorted(False)
            self.ui_callback()


class UpdateFillCommand(QUndoCommand):
    
    def __init__(self, scale, fill_method, ui_callback):
        super().__init__()
        self.setText('Set fill method to %s' % (str(fill_method)))
        self.scale = scale
        self.fill_method = fill_method
        self.ui_callback = ui_callback


    def redo(self):
        self.old_fill_method = self.scale.set_fill(self.fill_method)
        self.ui_callback()


    def undo(self):
        self.scale.set_fill(self.old_fill_method)
        self.ui_callback()


class Sync3ScaleEditor(ViaResourceEditor, Ui_sync3ScaleEditor):
    
    def __init__(self, resource_dir='./', remote_resources = {}, slug='original', style_text=''):
        super().__init__() 
        self.setupUi(self)
        self.setStyleSheet(style_text)
        self.style_text = style_text

        self.fill_help = {}
        self.fill_help["expand"] = "The seed ratios (in the list to the left) will be spread evenly across the full knob/CV range."
        self.fill_help["octave"] = "The seed ratios (in the list to the left) will be spread across the control range by transposing by the total range in octaves"
        self.fill_help["tritave"] = "The seed ratios (in the list to the left) will be spread across the control range by transposing by the total range in tritaves. Works great with ratios using odd numbers."
        
        self.sorted_help = "The list of seed ratios above will be automatically sorted and loaded in ascending order"
        self.unsorted_help = "The list of seed ratios above can be freely reordered using the on the button on the far left of each row"

        self.remote_resources = remote_resources

        self.set = Sync3ScaleSet(resource_dir, slug)
        self.set_slug = slug

        self.update_resource_sets()
        self.update_resources()

        self.active_ratio_idx = 0
        self.create_seed_ratio_grid()

        self.update_preview_idx()
        self.update_preview()

        for slot_num in range(0, 8):
            eval('self.slot%d' % (slot_num+1)).clicked.connect(lambda state=True, x=slot_num: self.switch_slot(x))
            eval('self.slot%d' % (slot_num+1)).setToolTip("Edit scale " + str(slot_num + 1))
        self.selectResource.activated.connect(self.handle_select_resource)
        self.saveResource.clicked.connect(lambda state=True: self.handle_save_resource())

        self.unsorted_data = None

        self.switch_slot(0)

        self.update_resource_ui()
        
        self.setFocusPolicy(Qt.ClickFocus)

        self.initToolTips()
            

# Edit scale recipe

    @Slot()
    def on_sorted_clicked(self):
        self.unsorted_data = self.set.resources[self.active_idx].get_data()
        sorted_command = UpdateSortedCommand(self.set.resources[self.active_idx], True, self.update_resource_ui)
        self.resource_undo_stack.push(sorted_command)
        self.sorted_flag = True


    @Slot()
    def on_unsorted_clicked(self):
        if self.unsorted_data:
            self.set.resources[self.active_idx].reload_data(self.unsorted_data)
        sorted_command = UpdateSortedCommand(self.set.resources[self.active_idx], False, self.update_resource_ui)
        self.resource_undo_stack.push(sorted_command)
        self.sorted_flag = False


    @Slot()
    def on_addSeedRatio_clicked(self):
        self.ratio_add_dialog = Sync3RatioAdd(self)
        self.ratio_add_dialog.setWindowTitle("Add ratio")
        self.ratio_add_dialog.setStyleSheet(self.style_text)
        self.ratio_add_dialog.close.clicked.connect(self.ratio_add_dialog.accept)
        self.ratio_add_dialog.exec()


    @Slot()
    def on_addFromScala_clicked(self):
        scala_path = QFileDialog.getOpenFileName(self, 'Import Scala File', filter="Scala Files (*.scl)")[0]
        with open(scala_path) as scala_file:
            scala_ratios = []
            for line in scala_file.readlines():
                fixed_line = line.replace('\n', '')
                fixed_line = fixed_line.replace(' ', '')
                parse_try = fixed_line.split('/')
                if len(parse_try) == 2:
                    if parse_try[0].isnumeric() and parse_try[1].isnumeric():
                        scala_ratios.append([int(parse_try[0]), int(parse_try[1])])
        for ratio in scala_ratios:
            self.add_seed_ratio(ratio)
                

    @Slot()
    def on_clearSeedRatios_clicked(self):
        clear_command = ClearRatiosCommand(self.set.resources[self.active_idx], self.update_resource_ui)
        self.resource_undo_stack.push(clear_command)
        

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


    def update_fill_method(self, fill_method):
        change_fill = UpdateFillCommand(self.set.resources[self.active_idx], fill_method, self.update_resource_ui)
        self.resource_undo_stack.push(change_fill)


# Preview section slots


    def update_preview_idx(self):
        self.preview_idx = min(31, (int((self.cvSlider.value() + 50) * .15) + self.knob.value() + 1))


    @Slot()
    def on_cvSlider_valueChanged(self):
        self.update_preview_idx()
        voltage = self.cvSlider.value() / 10
        self.cvLabel.setText("CV: %1.1f V" % voltage)
        self.update_preview()


    @Slot()
    def on_knob_valueChanged(self):
        self.update_preview_idx()
        self.update_preview()


# Seed ratio dispaly helpers

    def add_seed_ratio(self, ratio):
        if not self.check_data(ratio):
            reduced = self.reduce_ratio(ratio)
            warning_string = 'Ratio %d/%d exists in set as %d/%d, add duplicate?' % (ratio[0], ratio[1], reduced[0], reduced[1])
            if QMessageBox.question(self, 'Add duplicate?', warning_string) == QMessageBox.No:
                self.ratio_add_dialog.accept()
                return
        add_ratio = AddRatioCommand(self.set.resources[self.active_idx], ratio[0], ratio[1], self.update_resource_ui)
        self.resource_undo_stack.push(add_ratio)
        self.ratio_add_dialog.accept()


    def handle_drop(self, destination_idx):
        reorder = ReorderScaleCommand(self.set.resources[self.active_idx], self.dragged_idx, destination_idx, self.update_resource_ui)
        self.resource_undo_stack.push(reorder)


    def remove_button_pushed(self, idx):
        self.active_ratio_idx = idx
        self.remove_ratio()


    def remove_ratio(self):
        remove_ratio = RemoveRatioCommand(self.set.resources[self.active_idx], self.active_ratio_idx, self.update_resource_ui)
        self.resource_undo_stack.push(remove_ratio)


# Kinda like the data view

    def update_resource_ui(self):

        self.resourceDescription.setText(self.set.resources[self.active_idx].data['description'])

        self.sorted.setChecked(True)
        if 'sorted' in self.set.resources[self.active_idx].data:
            if self.set.resources[self.active_idx].data['sorted'] is False:
                self.unsorted.setChecked(True)
                self.sorted_flag = False
            else:
                self.sorted_flag = True
        else:
            self.sorted_flag = True

        seed_ratios = self.set.resources[self.active_idx].data['sorted_ratios']
        idx = -1
        for idx, ratio in enumerate(seed_ratios):
            self.seed_ratio_buttons[idx].show()
            self.seed_ratio_buttons[idx].update_ratio(ratio[0], ratio[1])
        for i in range(idx+1, 32):
            self.seed_ratio_buttons[i].hide()

        if not self.set.resources[self.active_idx].check_fill_ok():
            self.fillOctave.setEnabled(False)
            self.fillTritave.setEnabled(False)
        else:
            self.fillOctave.setEnabled(True)
            self.fillTritave.setEnabled(True)
        fill_mode = self.set.resources[self.active_idx].get_fill()
        if fill_mode == "expand":
            self.fillExpand.setChecked(True)
        elif fill_mode == "octave":
            self.fillOctave.setChecked(True)
        else:
            self.fillTritave.setChecked(True)

        self.update_preview()

        if self.set.is_clean():
            self.saveResourceSet.setEnabled(False)
        else:
            self.saveResourceSet.setEnabled(True)

    def update_preview(self):
        self.set.bake()
        numerator = self.set.resources[self.active_idx].baked['numerators'][self.preview_idx]
        denominator = self.set.resources[self.active_idx].baked['denominators'][self.preview_idx]
        self.previewLabel.setText("%d/%d" % (numerator, denominator))
        self.ratioPreview.update(numerator, denominator)

# General helper functions

    def check_data(self, ratio):
        if 'sorted' in self.set.resources[self.active_idx].data:
            if self.set.resources[self.active_idx].data['sorted'] is False:
                return True
        reduced_ratio = self.reduce_ratio(ratio)
        if reduced_ratio in self.set.resources[self.active_idx].data['seed_ratios']:
            return False
        else:
            return True

    def reduce_ratio(self, ratio):
        gcd = np.gcd(ratio[0], ratio[1])
        reduced_ratio = [1, 1]
        reduced_ratio[0] = int(ratio[0]/gcd)
        reduced_ratio[1] = int(ratio[1]/gcd)
        return reduced_ratio

    def create_seed_ratio_grid(self):
        self.seed_ratio_buttons = []
        self.seedRatioHolder = QWidget()
        self.seedRatioGrid = QVBoxLayout()

        num_tables = 32
        for row in range(0, num_tables):
            idx = row
            new_row = RatioRow(self)
            new_row.remove.clicked.connect(lambda state=True, x=idx: self.remove_button_pushed(x))
            new_row.set_idx(idx)
            self.seed_ratio_buttons.append(new_row)
            self.seedRatioGrid.addWidget(new_row, row)

        self.seedRatioGrid.insertStretch(-1)

        self.seedRatioGrid.setSpacing(0)
        # self.seedRatioGrid.setContentsMargins(0,0,0,0)

        self.seedRatioHolder.setLayout(self.seedRatioGrid)
        self.seedScrollArea.setWidget(self.seedRatioHolder)

    def showEvent(self, event):
        super().showEvent(event)
        self.undo_stack_init()

    def clear_menu(self):
        self.menu.clear()

    def initToolTips(self):
        super().initToolTips()
        self.selectResource.setToolTip("Select an available scale for this mode and open it in the editor")
        self.saveResource.setToolTip("Save the edited scale")
        self.addSeedRatio.setToolTip("Add new ratio to scale set")
        self.addFromScala.setToolTip("Import ratios from .scl file created in Scala")
        self.clearSeedRatios.setToolTip("Clear all ratios from the list except for a default of 1/1")
        self.sorted.setToolTip(self.sorted_help)
        self.unsorted.setToolTip(self.unsorted_help)
        self.fillExpand.setToolTip(self.fill_help['expand'])
        self.fillOctave.setToolTip(self.fill_help['octave'])
        self.fillTritave.setToolTip(self.fill_help['tritave'])
        self.knob.setToolTip("Preview the selected ratio for a given knob position and CV value")
        self.cvSlider.setToolTip("Preview the selected ratio for a given knob position and CV value")





