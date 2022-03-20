from PySide6.QtWidgets import QDialog, QInputDialog, QMessageBox
from PySide6.QtCore import Slot, Qt

class ViaResourceEditor(QDialog):
    def __init__(self):
        super().__init__()        
        self.unsaved_changes = False
        self.active_idx = 0

        self.resource_slugs = []
        self.resource_set_slugs = []
        
        # Base class must initialize self.set as ViaResourceSet derived class

    @Slot()
    def on_saveResourceSet_clicked(self):
        name = self.get_resource_set_name()
        self.set.save_set(name)
        self.update_resource_sets()
        self.selectResourceSet.setCurrentIndex(self.selectResourceSet.findText(name))
        self.update_resource_ui()

    @Slot()
    def on_selectResourceSet_activated(self):
        #TODO check for unsaved changes
        slug = self.selectResourceSet.currentText()
        if slug in self.resource_set_slugs:
            self.set.load_set(slug)
            self.switch_slot(self.active_idx)

    @Slot() 
    def on_saveForRack_clicked(self):
        self.set.pack_binary()

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

    @Slot()
    def on_slot25_clicked(self):
        self.switch_slot(24)

# Load/save pattern

    @Slot()
    def on_selectResource_activated(self):
        #TODO check for unsaved changes
        if self.selectResource.currentText() in self.resource_slugs:
            self.set.replace_resource(self.selectResource.currentText(), self.active_idx)
            self.switch_slot(self.active_idx)

    @Slot()
    def on_saveResource_clicked(self):
        name = self.get_resource_name()
        self.set.save_resource(name, self.active_idx)
        self.update_resource_selection(name)
        self.update_resources()
        self.update_resource_ui()

# Save/load helpers

    def update_resource_selection(self, name):
        self.selectResource.setCurrentIndex(self.selectResource.findText(name))
        
    def update_resource_sets(self):
        self.selectResourceSet.clear()
        self.resource_set_slugs = self.set.get_available_resource_sets()
        for resource_set in self.resource_set_slugs:
             self.selectResourceSet.insertItem(-1, resource_set)
    
    def update_resources(self):
        self.selectResource.clear()
        self.resource_slugs = self.set.get_available_resources()
        for resource in self.resource_slugs:
             self.selectResource.insertItem(-1, resource)

    def switch_slot(self, slot_num):
#        if self.unsaved_changes:
#            if self.prompt_to_discard():
#                self.unsaved_changes = False
#            else:
#                switch_slot(self.active_idx)
#                return 
        self.active_idx = slot_num
        resource_slug = self.set.data[slot_num]
        self.update_resource_selection(resource_slug)
        self.update_resource_ui()

    def prompt_to_discard(self):
        if QMessageBox.question(self, "", 'Unsaved changes will be lost, continue?') == QMessageBox.Yes:
            return True
        else:
            return False
        # Ask user if they wish to save any unsaved changes

    def get_resource_name(self, default=''):
        filename = QInputDialog.getText(self, 'Save Resource', 'Enter resource name:', text=default)[0]
        print(filename)
        while filename in self.remote_resources['resources']:
            filename = QInputDialog.getText(self, 'Save Resource', 'Reserved name, enter new name:', text=default)[0]
        if filename in self.resource_slugs:
            if QMessageBox.question(self, 'Overwrite?', 'Name in use, overwrite?') == QMessageBox.No:
                return
        return filename

    def get_resource_set_name(self, default=''):
        filename = QInputDialog.getText(self, 'Save Resource Set', 'Enter resource set name:', text=default)[0]
        while filename in self.remote_resources['sets']:
            filename = QInputDialog.getText(self, 'Save Resource Set', 'Reserved name, enter new name:', text=default)[0]
            if filename in self.resource_set_slugs:
                if QMessageBox.question(self, 'Overwrite?', 'Name in use, overwrite?') == QMessageBox.No:
                    return
        return filename

    def keyPressEvent(self, evt):
        if evt.key() == Qt.Key_Enter or evt.key() == Qt.Key_Return:
            return
        super().keyPressEvent(evt)
