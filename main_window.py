import os
import requests
import pathlib
import shutil

from PySide6.QtWidgets import QMainWindow, QMessageBox, QProgressDialog
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
        self.faceplate_image = QPixmap(self.app_path + '/img/blank.png')
        self.faceplate.setPixmap(self.faceplate_image)
        self.comboBox.setDisabled(True)
        self.flashButton.setDisabled(True)
        self.firmwareInfoButton.setDisabled(True)
        self.loadDefaultButton.setCheckable(False)
        self.detectButton.setDisabled(True)        

        self.stored_module_data = {}
        self.repo_url = 'https://raw.githubusercontent.com/starlingcode/viafirmware/master'
        self.comboBox.insertItem(0, 'Flash local firmware:')
        self.comboBox.setCurrentIndex(-1)
        self.firmware_manifest = []
        self.remote_firmware_selection = {}

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
        infoBox = QMessageBox();
        infoBox.setText(self.remote_firmware_selection['description']);
        infoBox.exec();
    
    @Slot()    
    def on_flashButton_clicked(self):
        self.initiate_flash()
    
    @Slot()    
    def on_comboBox_activated(self):
        try:
            self.remote_firmware_selection = self.firmware_manifest[self.comboBox.currentIndex()]
        except IndexError:
            self.remote_firmware_selection = {}
        self.update_firmware_selection()

# Application functions
 
    def get_remote(self):
        r = requests.get(self.repo_url + '/manifest.json')
        if r.status_code == 200:
            self.statusBar.showMessage('Remote firmware loaded')
            self.firmware_manifest = r.json()
            for idx, firmware in enumerate(self.firmware_manifest):
                self.comboBox.insertItem(idx, firmware['name'])
        else: 
            self.statusBar.showMessage('Cannot connect to network, local mode only')
        self.detectButton.setEnabled(True)

    def detect_module(self):
        module_found, serial = self.dfu.detect_module()
        if module_found:
            self.detectButton.setDisabled(True)
            self.statusBar.showMessage('Via found with serial %s, looking for firmware..' % serial)
            self.via = ViaModule(serial, self.firmware_manifest)
            self.read_option_bytes()
        else:
            self.statusBar.showMessage('No hardware detected -- Pushed DFU button?  Removed expander cable?')

    def read_option_bytes(self):
        read_successful, ob_path = self.dfu.read_option_bytes()
        if read_successful:
            with open(ob_path, 'rb') as ob_file:
                self.via.parse_option_bytes(ob_file.read())
                #TODO: Mimic save as calibration logic
                if self.via.firmware == 'calibration':
                    if self.via.version == 255:
                        self.dfu.store_eeprom_data(self.via.firmware_key, self.via.version, self.via.serial)
                        self.statusBar.showMessage('Via found with serial %s, calibration data updated' % self.via.serial)
                    else:
                        self.statusBar.showMessage('Via found with serial %s, calibration process not completed' % self.via.serial)
                elif self.via.firmware == 'unknown':
                    self.statusBar.showMessage('Via found in unknown state')
                else:
                    self.dfu.store_eeprom_data(self.via.firmware_key, self.via.version, self.via.serial)
                    self.statusBar.showMessage('Via found with serial %s, %s, version %d, data saved' 
                                                % (self.via.serial, self.via.firmware.upper(), self.via.version))
        else:
            self.via.read_protected = True
        self.get_stored_module_data()
        self.flashButton.setEnabled(True)
    
    def get_stored_module_data(self):
        for root, dirs, files in os.walk(self.app_path + '/module_data'):
            for file in files:
                info = file.split('-')
                serial = info[2]
                datecode = int(info[3].split('.')[0])
                version = int(info[1])
                firmware_slug = int(info[0])
                if serial not in self.stored_module_data:
                    self.stored_module_data[serial] = {}
                if firmware_slug not in self.stored_module_data:
                    self.stored_module_data[serial][firmware_slug] = {}
                self.stored_module_data[serial][firmware_slug][datecode] = {'version': version, 'path': file}
        self.comboBox.setEnabled(True)    

    def update_firmware_selection(self): 
        try:
            faceplate_path = '/img/' + self.remote_firmware_selection['token'] + '.png'
            r = requests.get(self.repo_url + faceplate_path)
            path = self.app_path + faceplate_path
            if r.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(r.content)
            self.firmwareInfoButton.setEnabled(True)
            self.loadDefaultButton.setEnabled(True)
            preset = self.get_latest_module_data(self.remote_firmware_selection['optionByte'])
            if 'path' in preset:
                print(preset['path'])
                if preset['path'].split('-')[0] == '254':
                    self.statusBar.showMessage('No saved data found, loading factory deaults')
                else:
                    self.statusBar.showMessage('Loading lastest saved data')
            else:
                self.statusBar.showMessage('No calibration info, please select and run CALIBRATION')
        except KeyError: # local firmware selected
            path = self.app_path + '/img/blank.png'
            self.firmwareInfoButton.setDisabled(True)
            self.loadDefaultButton.setDisabled(True)
        self.faceplate_image = QPixmap(path)
        self.faceplate.setPixmap(self.faceplate_image)

    def get_latest_module_data(self, firmware_key):
        if self.via.serial not in self.stored_module_data:
            return {}
        elif firmware_key in self.stored_module_data[self.via.serial]:
            maxkey = max(self.stored_module_data[self.via.serial][firmware_key], key=int)
            return self.stored_module_data[self.via.serial][firmware_key][maxkey]
        elif 254 in self.stored_module_data[self.via.serial]:
            maxkey = max(self.stored_module_data[self.via.serial][254], key=int)
            return self.stored_module_data[self.via.serial][254][maxkey]   

    def initiate_flash(self):
        if 'token' in self.remote_firmware_selection:
            bin_path = '/binaries/' + self.remote_firmware_selection['token'] + '.bin'
            r = requests.get(self.repo_url + bin_path)
            path = self.app_path + bin_path
            firmware_key = self.remote_firmware_selection['optionByte']
            firmware_version = self.remote_firmware_selection['latestVersion']
            if r.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(r.content)
                preset_file = self.get_latest_module_data(firmware_key)
                success = self.dfu.flash_eeprom(self.app_path + '/module_data/' + preset_file['path'])
                #TODO Handle errors
                if success:
                    print(path)
                    success = self.dfu.flash_firmware(path, firmware_key, firmware_version, False)
                    if success:
                        self.reset_for_new_via()
            else:
                self.statusBar.showMessage('Firmware file not downloaded, check network')
        else:
            return
            # Flash local
            
    def reset_for_new_via(self):
        self.detectButton.setEnabled(True)
        self.comboBox.setDisabled(True)        
        self.comboBox.setCurrentIndex(-1)
        self.firmwareInfoButton.setDisabled(True)
        self.flashButton.setDisabled(True)
        
