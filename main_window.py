import os
import requests
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

        with open(self.app_path + '/viatools.qss') as stylesheet:
            self.style_text = stylesheet.read()
            self.setStyleSheet(self.style_text)
        self.statusBar.setStyleSheet("background-color:rgb(0, 0, 0); color:rgb(255, 255, 255);");
        self.setFixedSize(QSize(585, 640))

        self.stored_module_data = {}
        self.repo_url = 'https://raw.githubusercontent.com/starlingcode/viafirmware/master'
        self.firmwareSelect.insertItem(0, 'Flash local firmware:')
        self.firmwareSelect.setCurrentIndex(-1)
        self.firmware_manifest = []
        self.remote_firmware_selection = {}

        self.dfu = DfuUtil(self.app_path)
        self.via = None

        self.get_remote()        

        self.reset_for_new_via()
 
        self.init_set_editor_data()

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
        infoBox.setStyleSheet(self.style_text)
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
        data_path = self.app_path + '/module_data'
        if os.path.exists(data_path) is False:
            os.mkdir(data_path)
        for root, dirs, files in os.walk(data_path):
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
        if 'token' in self.remote_firmware_selection:
            token = self.remote_firmware_selection['token']
            faceplate_path = '/img/' + token + '.png'
            r = requests.get(self.repo_url + faceplate_path)
            path = self.app_path + faceplate_path
            if r.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(r.content)
            # self.loadDefaultButton.show()
            preset = self.get_latest_module_data(self.remote_firmware_selection['optionByte'])
            if 'path' in preset:
                if preset['path'].split('-')[0] == '254':
                    self.statusBar.showMessage('No saved data found, loading factory deaults')
                else:
                    self.statusBar.showMessage('Loading lastest saved data')
            else:
                # TODO move and formalize
                self.statusBar.showMessage('No calibration info, please select and run CALIBRATION')
            self.faceplate_image = QPixmap(path)
            self.faceplate.setPixmap(self.faceplate_image)
            self.firmwareInfoButton.show()
            self.flashButton.show()
            self.init_set_editor(token)
        else:
            path = self.app_path + '/img/blank.png'
            self.firmwareInfoButton.hide(True)
            self.loadDefaultButton.hide(True)
            self.reset_editor()

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
        data_path = self.app_path + '/binaries'
        if os.path.exists(data_path) is False:
            os.mkdir(data_path)
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

        self.reset_editor()

# Viatools compatible binary packing

    def flash_resources(self):
        token = self.remote_firmware_selection['token']
        if token in self.editor_data:
            self.editor1.set.load_set(self.edit1Select.currentText())
            self.editor1.set.pack_binary()
            return self.dfu.start_resource_flash(self.editor_data[token]['resource1_address'], self.app_path + '/%s/binaries/%s.bin' % (token, self.editor1.set.slug)) 
        else:
            return True

# Resource editor setup

    def init_set_editor_data(self):
        self.editor_data = {}
        self.editor_data['gateseq'] = {
            'object1_name': 'pattern',
            'editor1_object': GateseqPatternEditor,
            'resource1_address': '0x8020000'
        }        
        self.editor_data['sync3'] = {
            'object1_name': 'scale',
            'editor1_object': Sync3ScaleEditor,
            'resource1_address': '0x8020000'
        }       


    def reset_editor(self):
        self.edit1Label.hide()
        self.edit1Select.clear()
        self.edit1Select.hide()
        self.openEdit1.hide()              
        self.edit2Label.hide()
        self.edit2Select.hide()
        self.edit2Select.clear()
        self.openEdit2.hide()              

    def init_set_editor(self, token):
        data_path = self.app_path + '/' + token
        if os.path.exists(data_path) is False:
            os.mkdir(data_path)
        print('Initializing set editor')
        self.reset_editor()
        if token in self.editor_data:
            self.edit1Select.show()
            self.edit1Label.show()
            object_name = self.editor_data[token]['object1_name']
            object_name_plural = object_name + 's'
            self.edit1Label.setText("Select %s set:" % object_name)
            self.openEdit1.clicked.connect(self.launch_editor1)
            self.openEdit1.show()
            self.openEdit1.setText('Edit ' + object_name.title() + ' Set') 
            firmware_dir = self.app_path + '/%s/' % token
            print(firmware_dir)
            r = requests.get(self.repo_url + '/%s/manifest.json' % token)
            if r.status_code == 200:
                self.statusBar.showMessage('Remote %s sets loaded' % object_name)
                self.remote_resources = {}
                self.remote_resources['sets'] = r.json()
                self.remote_resources['resources'] = []
                for idx, set_slug in enumerate(self.remote_resources['sets']): 
                    set_url = self.repo_url + '/%s/%s.json' % (token, set_slug)
                    r_set = requests.get(set_url)
                    if r_set.status_code == 200:
                        with open(firmware_dir + '%s.json' % set_slug, 'wb') as set_file:
                            set_file.write(r_set.content)
                        for resource in r_set.json():
                            resource_url = (self.repo_url + '/%s/%s/%s.json' % (token, object_name_plural, resource)) # hacky pluralization of resource name
                            r_resource = requests.get(resource_url)
                            if r_resource.status_code == 200:
                                self.remote_resources['resources'].append(resource)
                                data_path = firmware_dir + '/' + object_name_plural
                                if os.path.exists(data_path) is False:
                                    os.mkdir(data_path)
                                with open(firmware_dir + '%s/%s.json' % (object_name_plural, resource), 'wb') as resource_file:
                                    resource_file.write(r_resource.content)
                            else:
                                print('Resource dl error on ' + resource_url)
                    else:
                        #TODO error handling
                        print('Set dl error on ' + set_url)
                        print(r_set)
                        return
            else:
                #TODO error handling
                print('Manifest dl error')
                return
            self.populate_edit1Select(firmware_dir)
            self.editor1 = self.editor_data[token]['editor1_object'](firmware_dir, self.remote_resources, self.edit1Select.currentText(), self.style_text)
            self.editor1.finished.connect(self.get_slug_from_editor1)

    def populate_edit1Select(self, firmware_dir, selected_slug='original'):
        self.edit1Select.clear()
        for root, dirs, files in os.walk(firmware_dir):
            for file in files:
                self.edit1Select.insertItem(-1, file.replace('.json', ''))
            break
        self.edit1Select.setCurrentIndex(self.edit1Select.findText(selected_slug))        

    @Slot()
    def launch_editor1(self):
        # set editor size?
        self.editor1.show()

    @Slot()
    def get_slug_from_editor1(self):
        selected_slug = self.editor1.set.slug
        self.populate_edit1Select(self.remote_firmware_selection['token'], selected_slug)

###

    def handle_network_error(self, error):
        self.pop_up_message('Network error', 'Unable to load remote resource, please check internet connectivity and try again.')

    def handle_flashing_error(self, error):
        self.pop_up_message('Flashing error', 'Unable to flash resource, please reconnect module and try again')

    def handle_detect_error(self, error):
        self.pop_up_message('Module detect error', 'Unable to flash resource, please reconnect module and try again')
