class ViaModule:


    def __init__(self, serial, manifest):
        self.serial = serial
        self.calibrated = False
        self.read_protected = False
        self.firmware = ''
        self.firmware_key = 0
        self.version = 0
        self.remote_firmwares = {}
        for item in manifest:
            self.remote_firmwares[item['optionByte']] = item


    def parse_option_bytes(self, option_bytes):
        firmware_key = option_bytes[0]
        if firmware_key in self.remote_firmwares:
            self.firmware = self.remote_firmwares[firmware_key]['token']
            self.firmware_key = firmware_key
        else:
            self.firmware = 'unknown'
        self.version = option_bytes[2]

