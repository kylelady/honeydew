#/usr/bin/env python

import argparse
import os
import sys

import honeydew.main


def main(argv):
    backends = honeydew.main.get_backends()

    parser = argparse.ArgumentParser()
    parser.add_argument('--backend', choices=backends, default='filesystem',
            help='select backend engine; defaults to filesystem')
    parser.add_argument('-c', '--config', default='eecs280.cfg', type=open,
            help='config file; see sample.cfg')
    parser.add_argument('n', metavar='project_num',
            help='which project the command should be run on')
    parser.parse_args(argv[1:])

if __name__ == '__main__':
    sys.exit(main(sys.argv))
