import os
import requests
import pathlib

from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot, QFileInfo, QFile, QIODevice, QSize
from PySide6.QtGui import QPixmap
from PySide6.QtUiTools import QUiLoader

from ui_mainwindow import Ui_MainWindow
from dfu_util import DfuUtil
from via_module import ViaModule
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

        self.dfu = DfuUtil(str(pathlib.Path(__file__).parent.absolute()))
        self.via = None

        self.get_remote()        
        
    def __del__(self):
        return

# User input slots

    @Slot()    
    def on_detectButton_clicked(self):
        self.detect_module()    
        
    @Slot()    
    def on_firmwareInfoButton_clicked(self):
        return
    
    @Slot()    
    def on_flashButton_clicked(self):
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
        dfu_process = self.dfu.run_process_blocking(['-l'])
        result = dfu_process.stdout.decode('utf-8')
        if 'Found DFU: [0483:df11]' in result:
            self.detectButton.setDisabled(True)
            serial = result[-14:-2]
            self.statusBar.showMessage('Via found with serial %s, looking for firmware..' % serial)
            self.via = ViaModule(serial, self.firmware_manifest)
            self.read_option_bytes()
        else:
            self.statusBar.showMessage('No hardware detected -- Pushed DFU button?  Removed expander cable?')

    def read_option_bytes(self):
        if os.path.exists(self.dfu.ob_path):
            os.remove(self.dfu.ob_path)
        arguments = '--device 0483:df11 -a 1 -s 0x1FFFF804:4 -U %s' % self.dfu.ob_path
        dfu_process = self.dfu.run_process_blocking(arguments.split())
        result = dfu_process.stdout.decode('utf-8')        
        if '100%' in result:
            with open(self.dfu.ob_path, 'rb') as ob_file:
                self.via.parse_option_bytes(ob_file.read())
                if self.via.firmware == 'calibration':
                    if self.via.version == 0:
                        # self.dfu.backup_eeprom(self.via.firmware)
                        self.statusBar.showMessage('Via found with serial %s, calibration data found' % self.via.serial)
                        # Store calibration
                    else:
                        self.statusBar.showMessage('Via found with serial %s, calibration process not completed' % self.via.serial)
                elif self.via.firmware == 'unknown':
                    self.statusBar.showMessage('Via found in unknown state')
                else:
                    self.dfu.backup_eeprom(self.via.firmware)
                    self.statusBar.showMessage('Via found with serial %s, %s, version %d, data saved' 
                                                % (self.via.serial, self.via.firmware.upper(), self.via.version))
        else:
            self.via.read_protected = True
    
     
