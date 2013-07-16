#!/usr/bin/env python

import os
import pkgutil

import honeydew.backends
import honeydew.database


def main(args):
    '''
    Requires a dict of runtime configuration

    Minimum configuration:
    --pass--
    '''
    pass

def get_backends():
    '''return a list of available backend implementations'''
    backend_path = os.path.dirname(honeydew.backends.__file__)
    return [name for _, name, _ in pkgutil.iter_modules([backend_path,])]
