#!/usr/bin/env python


class Database(object):
    '''
    Frontend interface to read/write projects and grades
    '''
    def __init__(self, config, backend):
        '''requires config and concrete implementation of Backend'''
        self._config = config
        self._db = backend

    def grades(self, uniqname):
        return self._db._student(self._config, uniqname)


class Backend(object):
    '''
    Interface for various backends to store/retrive student projects/records
    '''

    class Student(object):
        '''
        context-managed class for student data
        '''

        def __init__(self, config, uniqname, **kwargs):
            pass

        def __enter__(self):
            '''prepare to receive student data'''
            raise NotImplementedError()

        def __exit__(self):
            '''write data out to disk or postgres or something'''
            raise NotImplementedError()
