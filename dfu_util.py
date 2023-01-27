from PySide6.QtCore import QObject, Signal, QRunnable

import subprocess
import datetime
import os

class DFUUtilSignals(QObject):
    showpb = Signal()
    progress = Signal(object)
    setrange = Signal(object, object)
    setcaption = Signal(object)
    hidepb = Signal()

class DfuUtil(QRunnable):
    
    def __init__(self, app_path, main_window):   
        self.app_path = app_path
        #TODO figure out for deployment and x platform, check for file existence
        self.bin_path = app_path + '/vendor/dfu-util'
        self.ob_path = app_path + '/optionbytes.temp'
        self.main_window = main_window
        self.signals = DFUUtilSignals()
        self.signals.showpb.connect(self.main_window.show_pb)
        self.signals.progress.connect(self.main_window.progressBar.setValue)
        self.signals.setrange.connect(self.main_window.progressBar.setRange)
        self.signals.setcaption.connect(self.main_window.progressBarLabel.setText)
        self.signals.hidepb.connect(self.main_window.hide_pb)

    def run_process_blocking(self, arguments):
        arguments = [self.bin_path] + arguments
        return subprocess.run(arguments, capture_output=True)
 
    def run_process_blocking_print(self, arguments):
        arguments = [self.bin_path] + arguments
        return subprocess.run(arguments, capture_output=False)

    def initiate_process(self, arguments):
        arguments = [self.bin_path] + arguments
        return subprocess.Popen(arguments, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def detect_module(self):
        dfu_process = self.run_process_blocking(['-l'])
        result = dfu_process.stdout.decode('utf-8')
        if 'Found DFU: [0483:df11]' in result:
            module_found = True
            serial = result.split("serial=")[-1].replace('"', '')
            serial = "".join(serial.split())
        else:
            module_found = False
            serial = ''
        return (module_found, serial)

    def read_option_bytes(self):
        if os.path.exists(self.ob_path):
            os.remove(self.ob_path)
        arguments = '--device 0483:df11 -a 1 -s 0x1FFFF804:4 -U %s' % self.ob_path
        dfu_process = self.run_process_blocking(arguments.split())
        result = dfu_process.stdout.decode('utf-8')        
        if '100%' in result:
            success = True
        else:
            success = False
        return (success, self.ob_path)

    def read_unprotect(self):
        # TODO make sure calibration binary is prepacked
        arguments = '--device 0483:df11 -a 0 -s 0x08000000:force:unprotect:will-reset -D binaries/calibration.bin'
        dfu_process = self.run_process_blocking_print(arguments.split())
        result = dfu_process.stdout.decode('utf-8')

    def store_eeprom_data(self, firmware_id, firmware_version, serial):
        arguments = '--device 0483:df11 -a 0 -s 0x0803F000:4096 -U '
        the_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        upload_path = self.app_path + ('/module_data/%s-%s-%s-%s.preset' % (firmware_id, firmware_version, serial, the_time))
        arguments += upload_path
        dfu_process = self.run_process_blocking(arguments.split())
        result = dfu_process.stdout.decode('utf-8')
        if '100%' in result:
            return True
        else:
            return False

    def monitor_flash_progress(self, dfu_process, caption='Flashing'):
        out_text = ''
        success = False
        self.signals.showpb.emit()
        self.signals.setcaption.emit("Erasing old data...")
        self.signals.setrange.emit(0, 100)
        while True:
            output = dfu_process.stdout.read(1).decode('utf-8')
            if dfu_process.poll() is not None:
                break
            if output:
                out_text += output
                if output == '%':
                    try:
                        progress = int(out_text[-4:-1])
                    except: # stray %
                        progress = 0
                    self.signals.progress.emit(progress)
                    if progress == 100:
                        self.signals.setcaption.emit('Flashing new data...')
        if '100%' in out_text:
            return True
        else:
            return False

    def flash_eeprom(self, path):
        arguments = '--device 0483:df11 -a 0 -s 0x0803F000:4096 -D %s -R' % path
        dfu_process = self.run_process_blocking(arguments.split())
        result = dfu_process.stdout.decode('utf-8')
        if '100%' in result:
            return True
        else:
            return False

    def start_firmware_flash(self, path):
        arguments = '--device 0483:df11 -a 0 -s 0x08000000 -D %s -R' % path
#        return self.run_process_blocking_print(arguments.split())
        dfu_process = self.initiate_process(arguments.split())
        return self.monitor_flash_progress(dfu_process, 'Flashing firmware')        

    def start_resource_flash(self, address, path):
        arguments = '--device 0483:df11 -a 0 -s %s -D %s -R' % (address, path)
        dfu_process = self.initiate_process(arguments.split())
        return self.monitor_flash_progress(dfu_process, 'Flashing resources')        

    def construct_optionbytes(self, firmware_key, firmware_version):
        ob = bytearray(16)
        ob[0] = 0xAA # The value of this byte defines the Flash memory protection level
        ob[1] = 0x55 # complement
        ob[2] = 0xFF # hardware watchdog/reset event configuration
        ob[3] = 0x00 # complement
        ob[4] = firmware_key
        ob[5] = ~firmware_key & 255 # complement
        ob[6] = firmware_version
        ob[7] = ~firmware_version & 255 # complement
        ob[8] = 0xFF # write protect flash memory region off
        ob[9] = 0x00 # complement
        ob[10] = 0xFF # write protect flash memory region off
        ob[11] = 0x00 # complement
        ob[12] = 0xFF # write protect flash memory region off
        ob[13] = 0x00 # complement
        ob[14] = 0xFF # write protect flash memory region off
        ob[15] = 0x00 # complement
        with open(self.ob_path, 'wb') as obfile:
            obfile.write(ob)
        
    def flash_optionbytes(self):
        arguments = '--device 0483:df11 -a 1 -s 0x1FFFF800:will-reset -D %s' % self.ob_path
        dfu_process = self.run_process_blocking(arguments.split())
        result = dfu_process.stdout.decode('utf-8')
        if '100%' in result:
            return True
        else:
            return False 
