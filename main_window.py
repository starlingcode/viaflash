import os
import requests
import pathlib
import shutil
import json

from PySide6.QtWidgets import QMainWindow, QMessageBox, QProgressDialog, QPushButton, QComboBox
from PySide6.QtCore import Slot, QFileInfo, QFile, QIODevice, QSize, QRect
from PySide6.QtGui import QPixmap
from PySide6.QtUiTools import QUiLoader

from ui_mainwindow import Ui_MainWindow
from dfu_util import DfuUtil
from via_module import ViaModule
from sync3_scale_editor import Sync3ScaleEditor
from gateseq_pattern_editor import GateseqPatternEditor

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.app_path = os.path.dirname(os.path.abspath(__file__))
        self.sync3_dir = self.app_path + '/sync3/'
        self.gateseq_dir = self.app_path + '/gateseq/'
        self.statusBar.setStyleSheet("background-color:rgb(0, 0, 0); color:rgb(255, 255, 255);");
        self.setFixedSize(QSize(585, 640))


        self.stored_module_data = {}
        self.repo_url = 'https://raw.githubusercontent.com/starlingcode/viafirmware/master'
        self.firmwareSelect.insertItem(0, 'Flash local firmware:')
        self.firmwareSelect.setCurrentIndex(-1)
        self.firmware_manifest = []
        self.remote_firmware_selection = {}

        self.dfu = DfuUtil(str(pathlib.Path(__file__).parent.absolute()))
        self.via = None

        self.get_remote()        

        self.reset_for_new_via()
 
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
    def on_firmwareSelect_activated(self):
        try:
            self.remote_firmware_selection = self.firmware_manifest[self.firmwareSelect.currentIndex()]
        except IndexError:
            self.remote_firmware_selection = {}
        self.update_firmware_selection()


# Remote firmware flashing flow
 
    def get_remote(self):
        r = requests.get(self.repo_url + '/manifest.json')
        if r.status_code == 200:
            self.statusBar.showMessage('Remote firmware loaded')
            self.firmware_manifest = r.json()
            for idx, firmware in enumerate(self.firmware_manifest):
                self.firmwareSelect.insertItem(idx, firmware['name'])
        else: 
            self.statusBar.showMessage('Cannot connect to network, local mode only')

    def detect_module(self):
        module_found, serial = self.dfu.detect_module()
        if module_found:
            self.detectButton.hide()
            self.statusBar.showMessage('Via found with serial %s, looking for firmware..' % serial)
            self.via = ViaModule(serial, self.firmware_manifest)
            self.read_option_bytes()
        else:
            self.statusBar.showMessage('No hardware detected -- Pushed DFU button?  Removed expander cable?')

    def read_option_bytes(self):
        self.get_stored_module_data()
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
                    #ugly hack to store as calibration
                    if self.via.serial not in self.stored_module_data: 
                        print(self.stored_module_data)
                        self.dfu.store_eeprom_data(254, self.via.version, self.via.serial)

        else:
            self.dfu.read_unprotect()
            self.statusBar.showMessage('Device under read protection, restoring...')
        self.get_stored_module_data()
    
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
        self.firmwareSelectLabel.show()
        self.firmwareSelect.show()    
        #TODO: implement default preset load for relevant firmwares

    def update_firmware_selection(self): 
        try:
            faceplate_path = '/img/' + self.remote_firmware_selection['token'] + '.png'
            r = requests.get(self.repo_url + faceplate_path)
            path = self.app_path + faceplate_path
            if r.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(r.content)
            self.firmwareInfoButton.show()
            self.loadDefaultButton.show()
            preset = self.get_latest_module_data(self.remote_firmware_selection['optionByte'])
            if 'path' in preset:
                if preset['path'].split('-')[0] == '254':
                    self.statusBar.showMessage('No saved data found, loading factory deaults')
                else:
                    self.statusBar.showMessage('Loading lastest saved data')
            else:
                # TODO move and formalize
                self.statusBar.showMessage('No calibration info, please select and run CALIBRATION')
            self.init_editor()

        except KeyError: # local firmware selected
            path = self.app_path + '/img/blank.png'
            self.firmwareInfoButton.setDisabled(True)
            self.loadDefaultButton.setDisabled(True)
        self.faceplate_image = QPixmap(path)
        self.faceplate.setPixmap(self.faceplate_image)
        self.firmwareInfoButton.show()
        self.loadDefaultButton.show()
        self.flashButton.show()

    def get_latest_module_data(self, firmware_key):
        last_firmware = {}
        last_calibration = {}
        last_firmware_time = 0
        last_calibration_time = 0
        if self.via.serial not in self.stored_module_data:
            return last_firmware
        if firmware_key in self.stored_module_data[self.via.serial]:
            maxkey = max(self.stored_module_data[self.via.serial][firmware_key], key=int)
            last_firmware = self.stored_module_data[self.via.serial][firmware_key][maxkey]
            last_firmware_time = maxkey
        if 254 in self.stored_module_data[self.via.serial]:
            maxkey = max(self.stored_module_data[self.via.serial][254], key=int)
            last_calibration = self.stored_module_data[self.via.serial][254][maxkey]
            last_calibration_time = maxkey
        if last_calibration_time > last_firmware_time:
            return last_calibration
        else:
            return last_firmware

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
                #TODO: fix for calibration
                try:
                    success = self.dfu.flash_eeprom(self.app_path + '/module_data/' + preset_file['path'])
                except:
                    success = False
                #TODO Handle errors
                if success:
                    success = self.dfu.start_firmware_flash(path)
                if success:
                    self.flash_resources()
                if success:
                    ob_key = firmware_key
                    self.dfu.construct_optionbytes(ob_key, firmware_version)
                    success = self.dfu.flash_optionbytes()
                if success:
                    self.reset_for_new_via()
            else:
                self.statusBar.showMessage('Firmware file not downloaded, check network')
        else:
            return
            # Flash local
            
    def reset_for_new_via(self):
        self.faceplate_image = QPixmap(self.app_path + '/img/blank.png')
        self.faceplate.setPixmap(self.faceplate_image)

        self.detectButton.show()
        self.detectButton.setEnabled(True)

        self.firmwareSelectLabel.hide()
        self.firmwareSelect.hide()
        self.flashButton.hide()
        self.firmwareInfoButton.hide()
        self.loadDefaultButton.hide()
        self.edit1Label.hide() 
        self.edit1Select.hide() 
        self.openEdit1.hide()
        self.edit2Label.hide() 
        self.edit2Select.hide() 
        self.openEdit2.hide()        
 
# Viatools Editor Launch
 
    def init_editor(self):
        if self.remote_firmware_selection['token'] == 'sync3':
            self.init_sync3()
        elif self.remote_firmware_selection['token'] == 'gateseq':
            self.init_gateseq()
        else:
            self.edit1Label.hide()
            self.edit1Select.hide()
            self.openEdit1.hide()              
            self.edit2Label.hide()
            self.edit2Select.hide()
            self.openEdit2.hide()              
    
# Viatools compatible binary packing

    def flash_resources(self):
        if self.remote_firmware_selection['token'] == 'sync3':
            self.prepare_sync3_binary()
            return self.dfu.start_resource_flash('0x8020000', self.app_path + '/binaries/sync3scales.bin') 
        else:
            return True

# Sync3 editor setup

    def init_sync3(self):
        self.edit1Select.clear()
        self.edit1Select.show()
        self.edit1Select.activated.connect(self.sync3_scale_set_select)
        self.edit1Label.show()
        self.edit1Label.setText("Select scale set:")
        self.openEdit1.clicked.connect(self.launch_sync3_scale_editor)
        self.openEdit1.show()
        self.openEdit1.setText('Edit Scale Set') 
        r = requests.get(self.repo_url + '/sync3/manifest.json')
        if r.status_code == 200:
            self.statusBar.showMessage('Remote scale sets loaded')
            self.sync3_remote_scale_sets = r.json()
            with open(self.sync3_dir + 'remote_manifest.json', 'wb') as manifest_file:
                 manifest_file.write(r.content)
            for idx, scale_set in enumerate(self.sync3_remote_scale_sets):
                self.edit1Select.insertItem(idx, scale_set)
                for scale in self.sync3_remote_scale_sets[scale_set]:
                    scale_url = (self.repo_url + '/sync3/%s.json' % scale)
                    r_scale = requests.get(scale_url)
                    if r_scale.status_code == 200:
                        with open(self.sync3_dir + 'scales/%s.json' % scale, 'wb') as scale_file:
                            scale_file.write(r_scale.content)
                    else:
                        #TODO error handling
                        print('filedl error')
                        return
        else:
            #TODO error handling
            return
        with open(self.sync3_dir + 'local_manifest.json', 'r') as manifest_file:
            self.sync3_local_scale_sets = json.load(manifest_file)
        self.sync3_scale_set_select()
        self.sync3_editor = Sync3ScaleEditor(self.sync3_dir, self.app_path + '/binaries/', self.sync3_scale_set)

    def prepare_sync3_binary(self):
        self.sync3_editor.engine.load_scale_set(self.sync3_scale_set)
        self.sync3_editor.engine.render()
        self.sync3_editor.engine.pack_binary()

    @Slot()
    def launch_sync3_scale_editor(self):
        self.sync3_editor.setGeometry(QRect(200, 200, 400, 606))
        self.sync3_editor.show()
    
    @Slot()
    def sync3_scale_set_select(self):
        self.sync3_scale_set = self.edit1Select.currentText()

# Gateseq editor setup

    def init_gateseq(self):
        self.edit1Select.clear()
        self.edit1Select.show()
        self.edit1Select.activated.connect(self.gateseq_pattern_set_select)
        self.edit1Label.show()
        self.edit1Label.setText("Select pattern set:")
        self.openEdit1.clicked.connect(self.launch_gateseq_pattern_editor)
        self.openEdit1.show()
        self.openEdit1.setText('Edit Pattern Set') 
        r = requests.get(self.repo_url + '/gateseq/manifest.json')
        if r.status_code == 200:
            self.statusBar.showMessage('Remote pattern sets loaded')
            self.gateseq_remote_pattern_sets = r.json()
            with open(self.gateseq_dir + 'remote_manifest.json', 'wb') as manifest_file:
                 manifest_file.write(r.content)
            for idx, pattern_set in enumerate(self.gateseq_remote_pattern_sets):
                self.edit1Select.insertItem(idx, pattern_set)
                for pattern in self.gateseq_remote_pattern_sets[pattern_set]:
                    pattern_url = (self.repo_url + '/gateseq/patterns/%s.json' % pattern)
                    r_pattern = requests.get(pattern_url) 
                    if r_pattern.status_code == 200:
                        with open(self.gateseq_dir + 'patterns/%s.json' % pattern, 'wb') as pattern_file:
                            pattern_file.write(r_pattern.content)
                    else:
                        #TODO error handling
                        print('filedl error on ')
                        return
        else:
            #TODO error handling
            print('manifest error')
            return
        with open(self.gateseq_dir + 'local_manifest.json', 'r') as manifest_file:
            self.gateseq_local_pattern_sets = json.load(manifest_file)
        self.gateseq_pattern_set_select()
        self.gateseq_editor = GateseqPatternEditor(self.gateseq_dir, self.app_path + '/binaries/', self.gateseq_pattern_set)

    def prepare_gateseq_binary(self):
        self.gateseq_editor.engine.load_scale_set(self.gateseq_pattern_set)
        self.gateseq_editor.engine.render()
        self.gateseq_editor.engine.pack_binary()

    @Slot()
    def launch_gateseq_pattern_editor(self):
        self.gateseq_editor.setGeometry(QRect(200, 200, 400, 590))
        self.gateseq_editor.show()
    
    @Slot()
    def gateseq_pattern_set_select(self):
        self.gateseq_pattern_set = self.edit1Select.currentText()

