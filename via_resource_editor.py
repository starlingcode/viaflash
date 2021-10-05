from PySide6.QtWidgets import QDialog, QInputDialog, QMessageBox
from PySide6.QtCore import Slot

class ViaResourceEditor(QDialog):
    def __init__(self):
        super().__init__()        
        self.unsaved_changes = False
        self.active_idx = 0
        
        # Base class must initialize self.set as ViaResourceSet derived class

    @Slot()
    def on_saveResourceSet_clicked(self):
        name = self.get_resource_set_name()
        self.set.save(name)
        self.update_resource_sets()

    @Slot()
    def on_selectResourceSet_currentTextChanged(self):
        #TODO check for unsaved changes
        self.set.load(self.selectPatternSet.currentText())

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

    @Slot()
    def on_slot9_clicked(self):
        self.switch_slot(8)
    
    @Slot()
    def on_slot10_clicked(self):
        self.switch_slot(9)
    
    @Slot()
    def on_slot11_clicked(self):
        self.switch_slot(10)

    @Slot()
    def on_slot12_clicked(self):
        self.switch_slot(11)

    @Slot()
    def on_slot13_clicked(self):
        self.switch_slot(12)

    @Slot()
    def on_slot14_clicked(self):
        self.switch_slot(13)

    @Slot()
    def on_slot15_clicked(self):
        self.switch_slot(14)

    @Slot()
    def on_slot16_clicked(self):
        self.switch_slot(15)

    @Slot()
    def on_slot17_clicked(self):
        self.switch_slot(16)
    
    @Slot()
    def on_slot18_clicked(self):
        self.switch_slot(17)
    
    @Slot()
    def on_slot19_clicked(self):
        self.switch_slot(18)
    
    @Slot()
    def on_slot20_clicked(self):
        self.switch_slot(19)

    @Slot()
    def on_slot21_clicked(self):
        self.switch_slot(20)

    @Slot()
    def on_slot22_clicked(self):
        self.switch_slot(21)

    @Slot()
    def on_slot23_clicked(self):
        self.switch_slot(22) 

    @Slot()
    def on_slot24_clicked(self):
        self.switch_slot(23)

# Load/save pattern

    @Slot()
    def on_selectResource_currentTextChanged(self):
        #TODO check for unsaved changes
        self.set.replace_resource(self.selectResource.currentText(), self.active_idx)

    @Slot()
    def on_saveResource_clicked(self):
        name = self.get_resource_name()
        self.set[self.active_idx].save(name)
        self.update_resources()

# Save/load helpers

    def update_resource_sets(self):
        self.selectResourceSet.clear()
        self.resource_set_slugs = self.set.get_available_resource_sets()
        for resource_set in self.resource_set_slugs:
             self.selectResource.insertItem(-1, resource_set)
    
    def update_resources(self):
        self.selectResource.clear()
        self.resource_slugs = self.set.get_available_resources()
        for resource in self.resource_slugs:
             self.selectResource.insertItem(-1, resource)

    def switch_slot(self, slot_num):
        if self.unsaved_changes:
            if self.prompt_to_discard():
                switch_slot(self.active_slot)
                self.unsaved_pattern_changes = False
            else:
                return 
        self.active_idx = slot_num
        self.update_resource_ui()

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

    def get_resource_name(self, default=''):
        filename = QInputDialog.getText(self, 'Save Resource', 'Enter resource name:', text=default)
        while filename in self.remote_resources['resources']:
            filename = QInputDialog.getText(self, 'Save Resource', 'Reserved name, enter new name:', text=default) 
        if filename in self.resource_slugs:
            if QMessageBox.question(self, 'Overwrite?', 'Name in use, overwrite?') == QMessageBox.No:
                return
        return filename

    def get_resource_set_name(self, default=''):
        filename = QInputDialog.getText(self, 'Save Resource Set', 'Enter resource set name:', text=default)
        while filename in self.remote_resources['sets']:
            filename = QInputDialog.getText(self, 'Save Resource Set', 'Reserved name, enter new name:', text=default) 
            if filename in self.resource_set_slugs:
                if QMessageBox.question(self, 'Overwrite?', 'Name in use, overwrite?') == QMessageBox.No:
                    return
        return filename
