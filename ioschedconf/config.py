import sys
import yaml


def init(file=None):
    try:
        conffile = open(file)
    except IOError:
        print 'Cannot open your config file'
        sys.exit()
    config = yaml.load(conffile)
    devices = config.get('devices')
    config.udevkeys = []
    for dev in devices:
        (key, value) = dev.split('=')
        if key not in config.udevkeys:
            config.udevkeys.append(key)
    return config
