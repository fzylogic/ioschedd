import pyudev
import daemon


class IOSchedDaemon:
    def __init__(self, config, background):
        self.context = pyudev.Context()
        self.config = config
        self.background = background

    def _coldstart(self):
        for device in self.context.list_devices(subsystem='block',
                                                DEVTYPE='disk'):
            print device.keys()
            print 'driver = ' + str(device.driver)
            print 'sysname = ' + str(device.sys_name)
            print 'sysnum = ' + str(device.sys_number)
            print 'syspath = ' + str(device.sys_path)
            print 'devtype = ' + str(device.device_type)
            print 'subsystem = ' + str(device.subsystem)
            print 'devnode = ' + str(device.device_node)
            print 'action = ' + str(device.action)
            for key in self.config['udevkeys']:
                print 'looking for ' + key
                if key.upper() in device:
                    print key.upper() + ' ' + device.get(key.upper())

    def _loop(self):
        monitor = pyudev.Monitor.from_netlink(self.context)
        monitor.filter_by('block')
        monitor.start()
        for device in iter(monitor.poll, None):
            print dir(device)
            for key in self.config['udevkeys']:
                if key.upper() in device:
                    print key.upper() + ' ' + device.get(key.upper())

    def run(self):
        self._coldstart()
        if self.background:
            with daemon.DaemonContext():
                self._loop()
        else:
            self._loop()
