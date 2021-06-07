import os
import requests

from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot, QFileInfo, QFile, QIODevice, QSize
from PySide6.QtGui import QPixmap
from PySide6.QtUiTools import QUiLoader
from ui_mainwindow import Ui_MainWindow
# from repo.py import Repo
# from dfu_util.py import DFUUtil
# from update_dialog.py import UpdateDialog


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.app_path = os.path.dirname(os.path.abspath(__file__))
        self.statusBar.setStyleSheet("background-color:rgb(0, 0, 0); color:rgb(255, 255, 255);");
        self.setFixedSize(QSize(585, 640))
        self.flashButton.setDisabled(True)
        # not working
        # self.faceplate.setPixmap(QPixmap('img/blank.png'))
        self.comboBox.setDisabled(True)
        self.flashButton.setDisabled(True)
        self.firmwareInfoButton.setDisabled(True)
        self.loadDefaultButton.setCheckable(False)
        self.detectButton.setDisabled(True)        

        self.comboBox.insertItem(0, 'Select local firmware:')
        self.firmware_manifest = {}
        self.local_only = True

        self.get_remote()        
        
    def __del__(self):
        return

# User input slots

    @Slot()    
    def on_flashButton_clicked(self):
        return
    
    @Slot()    
    def on_firmwareInfoButton_clicked(self):
        return
    
    @Slot()    
    def on_detectButton_clicked(self):
        return
    
    @Slot()    
    def on_comboBox_activated(self, index):
        return

# Application functions
 
    def get_remote(self):
        r = requests.get('https://raw.githubusercontent.com/starlingcode/viafirmware/master/manifest.json')
        if r.status_code == 200:
            self.statusBar.showMessage('Remote firmware loaded')
            self.firmware_manifest = r.json()
            self.local_only = False
            for idx, firmware in enumerate(self.firmware_manifest):
                self.comboBox.insertItem(idx, firmware['name'])
        else: 
            self.statusBar.showMessage('Cannot connect to network, local mode only')
        self.detectButton.setEnabled(True)

    def detect_module(self):
        return
    def read_unprotect(self):
        return
    def prompt_for_calibration(self):
        return
    def flash_remote_firmware(self, slug):
        return
    def flash_local_firmware(self):
        return



    def firmware_id_to_string(self, id):
        return

    def download_image(self, token=''):
        return

    def check_repository(self):
        return

    def start_flash(self):
        return

    def download_binary(self, token=''):
        return

    def download_preset(self, token=''):
        return

    def select_local_firmware(self):
        return

    def check_dfu(self, dfu_util_binary=None):
        return

    # 'Public' slots

    @Slot()
    def update_status_bar(message):
        return
    
    @Slot()
    def progress_updater(percent):
        return
    
    @Slot()
    def via_firmware_id_to_name(serial):
        return
    
    @Slot()
    def prompt_for_calibration():
        return
    
    @Slot()    
    def option_bytes_completed(int):
        return
    
    # 'Private' slots

    @Slot()    
    def load_image():
        return
    
    @Slot()    
    def init_repository():
        return
    
    @Slot()    
    def detected_via():
        return
    
    @Slot()    
    def update_dfu_flashing():
        return
    
    @Slot()    
    def flashing_firmware_completed(int):
        return
    
    @Slot()    
    def flashing_presets_completed(int):
        return
    
    @Slot()    
    def download_error(self):
        return
    
    @Slot()    
    def binary_download_error(self):
        return
    
   
    @Slot()    
    def binary_download_completed(self):
        return

    # 'Private' signals

    def message(self, text=''):
        return
        
    def via_found_with_firmware(self, text=''):
        return
    


