from PySide6.QtWidgets import QInputDialog, QMessageBox 
from PySide6.QtCore import Slot

from ui_scanner_wavetable_editor import Ui_scannerWavetableEditor
from viatools.wavetables import WavetableSet
from via_resource_editor import ViaResourceEditor

class ScannerWavetableEditor(ViaResourceEditor, Ui_scannerWavetableEditor):
    def __init__(self, resource_dir='./', remote_resources = {}, slug='original', style_text="", table_file='./tables.json', slope_file='./slopes.json'):
        super().__init__() 
        self.setupUi(self)
        self.setStyleSheet(style_text)

        self.remote_resources = remote_resources
        # TODO check if new remote resource or set collides with existing local slug

        self.set = WavetableSet(resource_dir, slug, table_file, slope_file)

        self.update_resource_sets()
        self.update_resources()

        self.slot1.setChecked(True)
        self.switch_slot(0)

# Edit wavetable recipe

    @Slot()
    def on_openBrowser_clicked(self):
        return

    @Slot()
    def on_openPreview_clicked(self):
        return

# Override set editor base class methods
 
    def update_resource_selection(self, name):
        self.tableName.setText(name)
        
    def update_resources(self):
        return

    def update_resource_ui(self):
        return
