#!/usr/bin/env python

import argparse

import ioschedd
from ioschedconf import config

parser = argparse.ArgumentParser(description='IOScheduler Controller')
parser.add_argument('--conffile',
                    action='store',
                    dest='conffile',
                    default='/etc/ioschedd.conf',
                    )
args = parser.parse_args()

cfg = config.init(args.conffile)

Daemon = ioschedd.daemon(cfg)
Daemon.run()
