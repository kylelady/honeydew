#!/usr/bin/env python

import os
import pkgutil

import honeydew.backends
import honeydew.config_mgmt
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

def make_database(args, config):
    '''factory to read args/config and return a database implementation'''
    managed_cfg = honeydew.config_mgmt.ManagedConfig(config, args)
    return honeydew.database.Database(managed_cfg, args.backend)

def get_students(args, config=None, db=None):
    '''
    get a list of students. requires args and either config or db

    if both are passed, prefer db
    '''
    if db is None:
        if config is not None:
            db = make_database(args, config)
        else:
            raise RuntimeError('either config or db needed')

    return db.list_students(args.n)

def grade_all(args, config):
    db = make_database(args, config)
    students = get_students(args, config)
    print students

def grade_one(args, config, backend=None):
    pass

def setup(args, config):
    pass
