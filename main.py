#/usr/bin/env python

import argparse
import os
import sys

import honeydew.main


def main(argv):
    backends = honeydew.main.get_backends()

    parser = argparse.ArgumentParser()
    parser.add_argument('--backend', '-b', choices=backends, default='filesystem',
            help='select backend engine; defaults to filesystem')
    parser.add_argument('--config', '-c', default='eecs280.cfg', type=open,
            help='config file; see sample.cfg')
    parser.add_argument('n', metavar='N',
            help='which project the command should be run on')
    subparsers = parser.add_subparsers()

    p_gradeall = subparsers.add_parser('gradeall')
    p_gradeall.set_defaults(func=honeydew.main.grade_all)

    p_gradeone = subparsers.add_parser('gradeone')
    p_gradeone.add_argument('uniqname',
            help='uniqname of project to grade')
    p_gradeone.set_defaults(func=honeydew.main.grade_one)

    p_setup = subparsers.add_parser('setup')
    p_setup.set_defaults(func=honeydew.main.setup)

    args = parser.parse_args(argv[1:])

    config = ConfigParser.SafeConfigParser()
    with open(args.config) as f:
        config.readfp(f)

    #args.func(args, config)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
