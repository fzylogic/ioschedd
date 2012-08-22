import re


def get_scheduler(config, Device):
    for devrule in config['devices'].keys():
        print 'checking ' + devrule
        try:
            black = config['devices'][devrule]['blacklist']
        except KeyError:
            black = ''
        if _matches(Device, devrule, black):
            print devrule + ' matches '
            return config['devices'][devrule]['scheduler']
    return


def _matches(Device, rule, blacklist):
    (key, val) = rule.split('=')
    if _compare(Device, rule):
        if _compare(Device, blacklist):
            print Device.device_node + ' blacklisted'
            return False
        else:
            return True
    return False


def _compare(Device, rule):
    if rule:
        for r in rule.split(','):
            (key, val) = r.strip().split('=')
            if (key == 'devpath'):
                print 'comparing ' + Device.device_node + ' to ' + val
                if re.search(val, Device.device_node):
                    return True
            elif (key == 'syspath'):
                if re.search(val, Device.sys_path):
                    return True
    return False


def write_schedfile(Device, scheduler):
    schedfile = Device.sys_path + '/queue/scheduler'
    print 'writing ' + scheduler + ' to ' + schedfile
    try:
        schedfh = open(schedfile, 'w')
    except IOError:
        print 'cannot write to ' + schedfile
        return
    schedfh.write(scheduler)
