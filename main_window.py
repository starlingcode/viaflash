import os
import requests
import shutil
import json
import time

from PySide6.QtWidgets import QMainWindow, QMessageBox, QProgressDialog, QStyleFactory
from PySide6.QtCore import Slot, Signal, QSize, QRect, QRunnable, QThreadPool, QObject
from PySide6.QtGui import QPixmap

from ui_mainwindow import Ui_MainWindow
from dfu_util import DfuUtil
from via_module import ViaModule
from sync3_scale_editor import Sync3ScaleEditor
from gateseq_pattern_editor import GateseqPatternEditor
from osc3_quantization_editor import Osc3QuantizationEditor
from wavetable_set_editor import ScannerWavetableEditor
from wavetable_set_editor import MetaWavetableEditor
from wavetable_set_editor import SyncWavetableEditor

class WorkerSignals(QObject):
    finished = Signal()

class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.args = args
        self.kwargs = kwargs
        self.fn = fn
        self.signals = WorkerSignals()


    @Slot()  
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        self.fn(*self.args, **self.kwargs)
        self.signals.finished.emit()


class FileDownloaderSignals(QObject):
    showpb = Signal()
    progress = Signal(object)
    setrange = Signal(object, object)
    setcaption = Signal(object)
    hidepb = Signal()
    error = Signal(object)
    finished = Signal()


class FileDownloader(QRunnable):
    
    def __init__(self, url, path, main_window):
        super(FileDownloader, self).__init__()
        self.url = url
        self.path = path
        self.main_window = main_window
        self.pb = main_window.progressBar
        self.pblabel = main_window.progressBarLabel
        self.signals = FileDownloaderSignals()
        self.signals.showpb.connect(self.main_window.show_pb)
        self.signals.progress.connect(self.main_window.progressBar.setValue)
        self.signals.setrange.connect(self.main_window.progressBar.setRange)
        self.signals.setcaption.connect(self.main_window.progressBarLabel.setText)
        self.signals.hidepb.connect(self.main_window.hide_pb)

    @Slot()
    def run(self):
        r = requests.get(self.url, stream=True, timeout=20)
        if r.status_code == 200:
            file_size = int(r.headers.get('content-length', 0))
            block_size = 1024
            self.signals.showpb.emit()
            self.signals.setcaption.emit('Downloading : ' + self.url.split('/')[-1])
            self.signals.setrange.emit(0, file_size)
            size_downloaded = 0
            with open(self.path, 'wb') as write_file:
                for data in r.iter_content(block_size):
                    size_downloaded += block_size
                    self.signals.progress.emit(size_downloaded)
                    write_file.write(data) 
            self.signals.hidepb.emit()
            self.signals.finished.emit()
        else:
            self.signals.error.emit()
        

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        # Initialize the window with the structure defined in the qt designer file
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.app_path = os.path.dirname(os.path.abspath(__file__))

        # This is necessary to make the thing look somewhat like the qt designer template
        self.setStyle(QStyleFactory.create("Fusion"))
        # Read in the stylesheet, set it to things, store it to set to other windows we spawn
        with open(self.app_path + '/viatools.qss') as stylesheet:
            self.style_text = stylesheet.read()
            self.setStyleSheet(self.style_text)
        self.statusBar.setStyleSheet(self.style_text)

        # This will be used to run stuff in parallel with the main gui and event looop
        self.threadpool = QThreadPool()

        self.repo_url = 'https://raw.githubusercontent.com/starlingcode/viafirmware/master'

        # Initialize for flashing local firmware TODO this doesnt actually work
        self.firmwareSelect.insertItem(0, 'Flash local firmware:')
        self.firmwareSelect.setCurrentIndex(-1)

        # This gets filled when we read the remote manifest
        self.firmware_manifest = []

        # This gets filled with data from of the above manifest if we select a remote firmware
        self.remote_firmware_selection = {}

        # The hardware flashing helper
        self.dfu = DfuUtil(self.app_path)
        # This will be used to store data from the connected hardware module
        self.stored_module_data = {}
        self.via = None
 
        # Boolean to determine if a Via is connected       
        self.editSoftware = False

        # Look for remote data, this is where we find out if we have internet
        self.get_remote()        

        # This basically like resets the UI?
        self.reset_for_new_via()
 
        # This like sets up what we know about the different flavors of editors
        self.init_set_editor_data()

    def __del__(self):
        return

    # User input slots (make em quick so they dont block the UI)

    @Slot()    
    def on_detectButton_clicked(self):
        detect_worker = Worker(self.detect_module)
        self.threadpool.start(detect_worker)    

    @Slot()    
    def on_editResources_clicked(self):
        self.activate_editor()    
    
    @Slot()    
    def on_flashButton_clicked(self):
        self.initiate_flash()
    
    # WCM TODO the root of all evil

    def launch_firmware_update(self):
        update_worker = Worker(self.update_firmware_selection)
        update_worker.signals.finished.connect(self.create_set_editor_object)
        self.threadpool.start(update_worker)

    @Slot()    
    def on_firmwareSelect_activated(self):
        try:
            self.remote_firmware_selection = self.firmware_manifest[self.firmwareSelect.currentIndex()]
        except IndexError:
            self.remote_firmware_selection = {}
        self.firmwareSelect.setEnabled(False) 
        self.launch_firmware_update()



    @Slot()    
    def on_edit1Select_activated(self):
        self.resourceInfo.setText(self.titles_to_descriptions[self.edit1Select.currentText()])

    @Slot()
    def on_openEdit1_clicked(self):
        self.editor1.show()


    # General purpose functions

    @Slot()
    def create_set_editor_object(self):
        if self.token in self.editor_data:
            if self.editor_data[self.token]['object1_name'] != 'wavetable':
                self.editor1 = self.editor_data[self.token]['editor1_object'](self.firmware_dir, self.remote_resources, self.set_slug, self.style_text)
            else: 
                self.editor1 = self.editor_data[self.token]['editor1_object'](self.firmware_dir, self.remote_resources, self.set_slug, self.style_text, self.app_path + '/wavetables/tables.json', self.app_path + '/wavetables/slopes.json')
            self.editor1.finished.connect(self.get_slug_from_editor1)
        self.update_ui_new_editor()

    @Slot()
    def get_slug_from_editor1(self):
        selected_title = self.slugs_to_titles[self.editor1.set.slug]
        self.populate_edit1Select(self.remote_firmware_selection['token'], selected_title)

    # Stuff that basically just updates the main window widgets:

    def update_status_bar(self, message):
        self.statusBar.showMessage(message)

    def reset_for_new_via(self):
        self.faceplate_image = QPixmap(self.app_path + '/img/blank.png')
        self.faceplate.setPixmap(self.faceplate_image)

        self.detectButton.show()
        self.detectButton.setEnabled(True)
        self.editResources.show()
        self.editResources.setEnabled(True)

        self.firmwareSelectLabel.hide()
        self.firmwareSelect.hide()
        self.flashButton.hide()
        self.firmwareInfo.hide()
        self.loadDefaultButton.hide()
        self.reset_editor()

    def reset_editor(self):
        self.edit1Label.hide()
        self.edit1Select.clear()
        self.edit1Select.hide()
        self.openEdit1.hide()
        self.resourceInfo.hide()
        self.resourceSeparator.hide()
        self.progressBar.hide()
        self.progressBarLabel.hide() 

    def activate_editor(self):
        self.firmwareSelectLabel.show()        
        self.firmwareSelect.show()        
        self.editResources.hide()        
        self.editSoftware = True

    def update_ui_remote_firmware(self):
        self.update_status_bar('Remote firmware loaded')
        for idx, firmware in enumerate(self.firmware_manifest):
            self.firmwareSelect.insertItem(idx, firmware['name'])

    def update_ui_module_detected(self):
        self.detectButton.hide()
        self.editResources.hide()        

    def update_ui_module_loaded(self):
        self.firmwareSelectLabel.show()
        self.firmwareSelect.show()    
        self.flashButton.show()

    def update_ui_firmware_selected(self):
        self.faceplate.setPixmap(self.faceplate_image)
        self.firmwareInfo.show()
        self.firmwareInfo.setText(self.remote_firmware_selection['description'])
        if not self.editSoftware:
            self.flashButton.show()

    def update_ui_new_editor(self):
        object_name = self.editor_data[self.token]['object1_name']
        self.edit1Select.show()
        self.edit1Label.show()
        self.resourceInfo.show()
        self.resourceInfo.setText(self.titles_to_descriptions[self.edit1Select.currentText()])
        self.resourceSeparator.show()
        self.openEdit1.show()
        self.openEdit1.setText('Edit ' + object_name.title() + ' Set') 
        self.edit1Label.setText("Select %s set:" % object_name)
        self.firmwareSelect.setEnabled(True)

    def update_ui_no_editor(self):
        self.edit1Select.hide()
        self.edit1Label.hide()
        self.resourceInfo.hide()
        self.resourceSeparator.hide()
        self.openEdit1.hide()
        self.firmwareSelect.setEnabled(True) 
        self.update_status_bar("No editable resources")
        self.firmwareSelect.setEnabled(True)

    def update_ui_local_firmware_selected(self):
        self.firmwareInfo.hide()
        self.loadDefaultButton.hide()
        self.reset_editor()

    def populate_edit1Select(self, firmware_dir, selected_title='Default'):
        self.edit1Select.clear()
        for root, dirs, files in os.walk(firmware_dir):
            for file in [x for x in files if ".json" in x]:
                slug = file.replace('.json', '')
                try:
                    with open(os.path.join(root, file)) as setfile:
                        setinfo = json.load(setfile)
                        title = setinfo['title']
                        description = setinfo['description']
                    self.slugs_to_titles[slug] = title
                    self.titles_to_slugs[title] = slug
                    self.titles_to_descriptions[title] = description
                    self.edit1Select.insertItem(-1, title)
                except:
                    print("Issue loading " + file)
            break
        self.edit1Select.setCurrentIndex(self.edit1Select.findText(selected_title))

    def show_pb(self):
        self.progressBar.show()
        self.progressBarLabel.show()
        self.progressBarLabel.setText('')

    def hide_pb(self):
        self.progressBar.hide()
        self.progressBarLabel.hide()

# Remote firmware flashing flow
 
    def get_remote(self):
        self.firmware_manifest = self.read_remote_manifest(self.repo_url + '/manifest.json')
        if self.firmware_manifest:
            self.update_ui_remote_firmware()
        else: 
            self.update_status_bar('Cannot connect to network, local mode only')

    def detect_module(self):
        module_found, serial = self.dfu.detect_module()
        if module_found:
            self.via = ViaModule(serial, self.firmware_manifest)
            self.editSoftware = False
            self.update_status_bar('Via found with serial %s, looking for firmware..' % serial)
            self.update_ui_module_detected()
            self.read_option_bytes()
            self.update_ui_module_loaded()
        else:
            self.update_status_bar('No hardware detected -- Pushed DFU button?  Removed expander cable?')

    def read_option_bytes(self):
        # WCM DEBUG
        # import pdb; pdb.set_trace()
        self.get_stored_module_data()
        read_successful, ob_path = self.dfu.read_option_bytes()
        if read_successful:
            with open(ob_path, 'rb') as ob_file:
                self.via.parse_option_bytes(ob_file.read())
                #TODO: Mimic save as calibration logic
                if self.via.firmware == 'calibration':
                    if self.via.version == 255:
                        self.dfu.store_eeprom_data(self.via.firmware_key, self.via.version, self.via.serial)
                        self.update_status_bar('Via found with serial %s, calibration data updated' % self.via.serial)
                    else:
                        self.update_status_bar('Via found with serial %s, calibration process not completed' % self.via.serial)
                elif self.via.firmware == 'unknown':
                    self.update_status_bar('Via found in unknown state')
                else:
                    self.dfu.store_eeprom_data(self.via.firmware_key, self.via.version, self.via.serial)
                    self.update_status_bar('Via found with serial %s, %s, version %d, data saved' 
                                                % (self.via.serial, self.via.firmware.upper(), self.via.version))
                    #ugly hack to store as calibration
                    if self.via.serial not in self.stored_module_data: 
                        print(self.stored_module_data)
                        self.dfu.store_eeprom_data(254, self.via.version, self.via.serial)
                    # TODO FIX THIS
                    self.firmwareSelect.setCurrentIndex(self.firmwareSelect.findText(self.via.firmware.upper()))
                    self.on_firmwareSelect_activated()
        else:
            self.dfu.read_unprotect()
            self.update_status_bar('Device under read protection, restoring...')
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
        #TODO: implement default preset load for relevant firmwares

    def update_firmware_selection(self): 
        if 'token' in self.remote_firmware_selection:
            self.token = self.remote_firmware_selection['token']
            faceplate_path = '/img/' + self.token + '.png'
            fp_url = self.repo_url + faceplate_path
            path = self.app_path + faceplate_path
            self.download_blocking(fp_url, path)
            self.faceplate_image = QPixmap(path)
            if self.editSoftware is False:
                preset = self.get_latest_module_data(self.remote_firmware_selection['optionByte'])
                if 'path' in preset:
                    if preset['path'].split('-')[0] == '254':
                        self.update_status_bar('No saved data found, loading factory deaults')
                    else:
                        self.update_status_bar('Loading lastest saved data')
                else:
                    # TODO move and formalize
                    self.update_status_bar('No calibration info, please select and run CALIBRATION')
            self.update_ui_firmware_selected()
            self.init_set_editor()

        else:
            path = self.app_path + '/img/blank.png'
            self.update_ui_local_firmware_selected()


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
            bin_url = self.repo_url + bin_path
            path = self.app_path + bin_path
            firmware_key = self.remote_firmware_selection['optionByte']
            firmware_version = self.remote_firmware_selection['latestVersion']
            self.download_blocking(bin_url, path)
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
            return
            # Flash local
            
# Viatools compatible binary packing

    def flash_resources(self):
        token = self.remote_firmware_selection['token']
        if token in self.editor_data:
            self.editor1.set.load_set(self.titles_to_slugs[self.edit1Select.currentText()])
            resource_path = self.editor1.set.pack_binary()
            return self.dfu.start_resource_flash(self.editor_data[token]['resource1_address'], self.app_path + '/%s/binaries/%s.%s' % (token, self.editor1.set.slug, token)) 
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
        self.editor_data['osc3'] = {
            'object1_name': 'quantization',
            'editor1_object': Osc3QuantizationEditor,
            'resource1_address': '0x8020000'
        }       
        self.editor_data['scanner'] = {
            'object1_name': 'wavetable',
            'editor1_object': ScannerWavetableEditor,
            'resource1_address': '0x8020000'
        }       
        self.editor_data['meta'] = {
            'object1_name': 'wavetable',
            'editor1_object': MetaWavetableEditor,
            'resource1_address': '0x8020000'
        }       
        self.editor_data['sync'] = {
            'object1_name': 'wavetable',
            'editor1_object': SyncWavetableEditor,
            'resource1_address': '0x8020000'
        }       

    def init_set_editor(self):
        self.update_status_bar("Downloading remote resources")
        data_path = self.app_path + '/' + self.token
        if os.path.exists(data_path) is False:
            os.mkdir(data_path)
        self.reset_editor()
        if self.token in self.editor_data:
            self.slugs_to_titles = {}
            self.titles_to_slugs = {}
            self.titles_to_descriptions = {}
            self.firmware_dir = self.app_path + '/%s/' % self.token
            self.init_resource_sets()
            print("Set editor initialized")
            self.init_resource_set_editor()
        else:
            self.update_ui_no_editor()


    def init_resource_sets(self):
        manifest_url = self.repo_url + '/%s/manifest.json' % self.token
        manifest_read = self.read_remote_manifest(manifest_url)
        self.update_status_bar('Remote %s sets loaded' % self.editor_data[self.token]['object1_name'])
        firmware_bin_path = self.firmware_dir + '/binaries'
        if os.path.exists(firmware_bin_path) is False:
            os.mkdir(firmware_bin_path)
        self.remote_resources = {}
        self.remote_resources['sets'] = manifest_read
        self.remote_resources['resources'] = []
        for idx, set_slug in enumerate(self.remote_resources['sets']): 
            set_url = self.repo_url + '/%s/%s.json' % (self.token, set_slug)
            set_path = self.firmware_dir + '%s.json' % set_slug
            # WCM TODO this is ugggggg
            self.download_blocking(set_url, set_path)
            self.init_resource_set_data(set_path)


    def init_resource_set_data(self, set_path):
        object_name = self.editor_data[self.token]['object1_name']
        if object_name != 'wavetable':
            data_path = self.firmware_dir + '/' + object_name + 's'
            if os.path.exists(data_path) is False:
                os.mkdir(data_path)
            with open(set_path) as jsonfile:
                resources = json.load(jsonfile)['slug_list']
            for resource in resources:
                resource_url = (self.repo_url + '/%s/%s/%s.json' % (self.token, object_name + 's', resource)) # hacky pluralization of resource name
                resource_path = self.firmware_dir + '%s/%s.json' % (object_name + 's', resource)
                self.remote_resources['resources'].append(resource)
        else:
            table_dir = self.app_path + '/wavetables/'
            if os.path.exists(table_dir) is False:
                os.mkdir(table_dir)
            tables_url = self.repo_url + '/wavetables/tables.json'
            tables_path = table_dir + 'tables.json'
            self.download_blocking(tables_url, tables_path)
            slopes_url = self.repo_url + '/wavetables/slopes.json'
            slopes_path = table_dir + 'slopes.json'
            self.download_blocking(slopes_url, slopes_path)


    def init_resource_set_editor(self):
        self.populate_edit1Select(self.firmware_dir)
        self.on_edit1Select_activated()
        self.set_slug = self.titles_to_slugs[self.edit1Select.currentText()]     

###

    def read_remote_manifest(self, url):
        r = requests.get(url, timeout=20)
        if r.status_code == 200:
            return r.json()
        else:
            self.download_error()

    def download_blocking(self, url, path):
        dl_job = FileDownloader(url, path, self)
        dl_job.run()

    def download_async(self, url, path, finish_callback=None):
        dl_job = FileDownloader(url, path, self)
        if finish_callback:
            dl_job.signals.finished.connect(finish_callback)
        dl_job.signals.error.connect(self.download_error)
        self.threadpool.start(dl_job)

    def download_error(self):
        self.update_status_bar('Network error', 'Unable to load remote resource, please check internet connectivity and try again.')

        
