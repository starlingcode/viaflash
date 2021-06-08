import subprocess

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


