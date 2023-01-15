from PySide6.QtWidgets import QDialog, QInputDialog, QMessageBox, QFileDialog
from PySide6.QtCore import Slot, Qt

class ViaResourceEditor(QDialog):
    def __init__(self):
        super().__init__()        
        self.unsaved_changes = False
        self.active_idx = 0

        self.resource_slugs = {}
        self.resource_set_slugs = {}
        self.resource_titles = {}
        self.resource_set_titles = {}
        
        # Base class must initialize self.set as ViaResourceSet derived class

    @Slot()
    def on_saveResourceSet_clicked(self):
        name = self.get_resource_set_name(self.set.data['title'])
        if name == '':
            return
        description = self.get_description(self.set.data['description'])
        self.set.save_set(name, description)
        self.update_resource_sets()
        self.selectResourceSet.setCurrentIndex(self.selectResourceSet.findText(self.resource_set_titles[name]))
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

    def update_set_slug(self, set_slug):
        self.set_slug = set_slug
        self.update_resource_sets()

    def handle_select_resource(self):
        #TODO check for unsaved changes
        resource_title = self.selectResource.currentText()
        if resource_title in self.resource_titles:
            self.resource_slug = self.resource_titles[resource_title]
            self.set.replace_resource(self.resource_slug, self.active_idx)
            self.switch_slot(self.active_idx)

    def handle_save_resource(self):
        name = self.get_resource_name(self.resource_slugs[self.resource_slug])
        if name == '':
            return
        default_description = ''
        if 'description' in self.set.resources[self.active_idx].data:
            default_description = self.set.resources[self.active_idx].data['description']
        description = self.get_description(default_description)
        self.set.save_resource(name, self.active_idx, description)
        self.update_resources()
        self.update_resource_selection(name)
        self.update_resource_ui()

# Save/load helpers

    def update_resource_selection(self, name):
        self.selectResource.setCurrentIndex(self.selectResource.findText(name))
        
    def update_resource_sets(self):
        self.selectResourceSet.clear()
        self.resource_set_slugs, self.resource_set_titles = self.set.get_available_resource_sets()
        resource_titles = []
        for resource in self.resource_set_slugs:
             resource_titles.append(self.resource_set_slugs[resource])
        resource_titles = sorted(resource_titles, reverse=True)
        for resource_title in resource_titles:
             self.selectResourceSet.insertItem(-1, resource_title)
        self.selectResourceSet.setCurrentIndex(self.selectResourceSet.findText(self.resource_set_slugs[self.set_slug]))

    
    def update_resources(self):
        self.selectResource.clear()
        self.resource_slugs, self.resource_titles = self.set.get_available_resources()
        resource_titles = []
        for resource in self.resource_slugs:
             resource_titles.append(self.resource_slugs[resource])
        resource_titles = sorted(resource_titles, reverse=True)
        for resource_title in resource_titles:
             self.selectResource.insertItem(-1, resource_title)

    def switch_slot(self, slot_num):
#        if self.unsaved_changes:
#            if self.prompt_to_discard():
#                self.unsaved_changes = False
#            else:
#                switch_slot(self.active_idx)
#                return 
        self.active_idx = slot_num
        self.resource_slug = self.set.data['slug_list'][slot_num]
        self.update_resource_selection(self.resource_slugs[self.resource_slug])
        self.update_resource_ui()

    def prompt_to_discard(self):
        if QMessageBox.question(self, "", 'Unsaved changes will be lost, continue?') == QMessageBox.Yes:
            return True
        else:
            return False
        # Ask user if they wish to save any unsaved changes

    # Make sure this does not collide with existing resource in a case insensitive fashion
    def get_resource_name(self, default=''):
        title = QInputDialog.getText(self, 'Save Resource', 'Enter resource name:', text=default)[0]
        remote_titles = []
        remote_slugs = []
        for slug in self.remote_resources['resources']:
            remote_titles.append(self.resource_slugs[slug].lower())
            remote_slugs.append(slug.lower())
        while title.lower() in remote_titles or title.lower() in remote_slugs:
            filename = QInputDialog.getText(self, 'Save Resource', 'Reserved name, enter new name:', text=default)[0]
        if title in self.resource_slugs:
            if QMessageBox.question(self, 'Overwrite?', 'Name in use, overwrite?') == QMessageBox.No:
                return
        return title

    # Make sure this does not collide with existing resource set in a case insensitive fashion
    def get_resource_set_name(self, default=''):
        title = QInputDialog.getText(self, 'Save Resource Set', 'Enter resource set name:', text=default)[0]
        remote_titles = []
        remote_slugs = []
        for slug in self.remote_resources['resources']:
            remote_titles.append(self.resource_slugs[slug].lower())
            remote_slugs.append(slug.lower())
        while title.lower() in remote_titles or title.lower() in remote_slugs:
            title = QInputDialog.getText(self, 'Save Resource Set', 'Reserved name, enter new name:', text=default)[0]
        if title in self.resource_set_slugs:
            if QMessageBox.question(self, 'Overwrite?', 'Name in use, overwrite?') == QMessageBox.No:
                return
        return title

    def get_description(self, default=''):
        return QInputDialog.getText(self, 'Enter Description', 'Enter a description if you want to :)', text=default)[0]

    def keyPressEvent(self, evt):
        if evt.key() == Qt.Key_Enter or evt.key() == Qt.Key_Return:
            return
        super().keyPressEvent(evt)
