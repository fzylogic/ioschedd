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
    udevkeys = []
    for dev in devices:
        (key, value) = dev.split('=')
        if key not in udevkeys:
            udevkeys.append(key)
    config['udevkeys'] = udevkeys
    return config
