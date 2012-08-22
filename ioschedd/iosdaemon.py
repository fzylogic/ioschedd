import daemon
import pyudev
from ioschedd import device


class IOSchedDaemon:
    def __init__(self, config, background):
        self.context = pyudev.Context()
        self.config = config
        self.background = background

    def _coldstart(self):
        for udevice in self.context.list_devices(subsystem='block',
                                                DEVTYPE='disk'):
            print udevice.keys()
            print udevice
            scheduler = device.get_scheduler(self.config, udevice)
            if not scheduler:
                scheduler = self.config['default']
            print udevice.device_node + ' using ' + scheduler
            device.write_schedfile(udevice, scheduler)

    def _loop(self):
        monitor = pyudev.Monitor.from_netlink(self.context)
        monitor.filter_by('block', device_type='disk')
        monitor.start()
        for udevice in iter(monitor.poll, None):
            scheduler = device.get_scheduler(self.config, udevice)
            if not scheduler:
                scheduler = self.config['default']
            print udevice.device_node + ' using ' + scheduler
            device.write_schedfile(udevice, scheduler)

    def run(self):
        self._coldstart()
        if self.background:
            with daemon.DaemonContext():
                self._loop()
        else:
            self._loop()
