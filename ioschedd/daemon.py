import pyudev


class IOSchedDaemon:
    def __init__(self):
        self.context = context = pyudev.Context()

    def coldstart(self, config):
        for device in self.context.list_devices(subsystem='block',
                                                DEVTYPE='disk'):
            #print device.keys()
            print device.driver
            print str(device) + ' ' + device.get('DEVTYPE')
            print str(device) + ' ' + device.get('DEVNAME')
            for key in config.udevkeys:
                print 'looking for ' + key
                if device.get(key.upper()):
                    print key.upper() + ' ' + device.get(key.upper())
