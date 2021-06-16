import subprocess
import datetime
import os

class DfuUtil:
    
    def __init__(self, app_path):   
        print(app_path) 
        self.app_path = app_path
        #TODO figure out for deployment and x platform, check for file existence
        self.bin_path = app_path + '/vendor/dfu-util'
        self.ob_path = app_path + '/optionbytes.temp'

    def run_process_blocking(self, arguments):
        arguments = [self.bin_path] + arguments
        return subprocess.run(arguments, capture_output=True)

    def detect_module(self):
        dfu_process = self.run_process_blocking(['-l'])
        result = dfu_process.stdout.decode('utf-8')
        if 'Found DFU: [0483:df11]' in result:
            module_found = True
            serial = result[-14:-2]
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

    def store_eeprom_data(self, firmware_id, firmware_version, serial):
        arguments = '--device 0483:df11 -a 0 -s 0x0803F000:4096 -U '
        the_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        upload_path = self.app_path + ('/module_data/%s-%s-%s-%s.preset' % (firmware_id, firmware_version, serial, the_time))
        arguments += upload_path
        dfu_process = self.run_process_blocking(arguments.split())
        result = dfu_process.stdout.decode('utf-8')

    def flash_eeprom(self, path):
        arguments = '--device 0483:df11 -a 0 -s 0x0803F000:4096 -D %s -R' % path
        dfu_process = self.run_process_blocking(arguments.split())
        result = dfu_process.stdout.decode('utf-8')
        if '100%' in result:
            success = True
        else:
            success = False

    def flash_firmware(self, path, firmware_key):
        arguments = '--device 0483:df11 -a 0 -s 0x08000000 -D %s -R' % path
        dfu_process = self.run_process_blocking(arguments.split())
        result = dfu_process.stdout.decode('utf-8')
        if '100%' in result:
            # finalize option bytes
        else:
            success = False

       return
