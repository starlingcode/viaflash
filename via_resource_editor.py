from PySide6.QtWidgets import QDialog, QInputDialog, QMessageBox, QFileDialog
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
        name = self.get_resource_set_name(self.set_slug)
        if name = '':
            return
        self.set.save_set(name)
        self.update_resource_sets()
        self.selectResourceSet.setCurrentIndex(self.selectResourceSet.findText(name))
        self.update_resource_ui()

    @Slot()
    def on_selectResourceSet_activated(self):
        #TODO check for unsaved changes
        slug = self.selectResourceSet.currentText()
        if slug in self.resource_set_slugs:
            self.set_slug = slug
            self.set.load_set(slug)
            self.switch_slot(self.active_idx)

    @Slot() 
    def on_saveForRack_clicked(self):
        bin_write_dir = QFileDialog.getExistingDirectory(self, "Select save directory")
        self.set.pack_binary(bin_write_dir + '/')


# Load/save resource 

    def handle_select_resource(self):
        #TODO check for unsaved changes
        resource_slug = self.selectResource.currentText()
        if resource_slug in self.resource_slugs:
            self.resource_slug = resource_slug
            self.set.replace_resource(resource_slug, self.active_idx)
            self.switch_slot(self.active_idx)

    def handle_save_resource(self):
        name = self.get_resource_name(self.resource_slug)
        if name = '':
            return
        self.set.save_resource(name, self.active_idx)
        self.update_resources()
        self.update_resource_selection(name)
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
        self.resource_slug = self.set.data[slot_num]
        self.update_resource_selection(self.resource_slug)
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
