import argparse

from ioschedd.iosdaemon import IOSchedDaemon
from ioschedd import config


def main():
    parser = argparse.ArgumentParser(description='IOScheduler Controller')
    parser.add_argument('--conffile',
                    action='store',
                    dest='conffile',
                    default='/etc/ioschedd.conf',
                    )
    parser.add_argument('--background',
                    action='store_true',
                    dest='background',
                    default=False,
                    )
    args = parser.parse_args()

    cfg = config.init(args.conffile)

    IOSchedDaemon(cfg, args.background).run()


if __name__ == '__main__':
        main()
