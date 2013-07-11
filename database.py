#!/usr/bin/env python

class Database(object):
    pass



class Backend(object):
    '''
    Interface for various backends to store/retrive student projects/records
    '''

    class Student(object):
        '''
        context-managed class for student data
        '''

        def __init__(self, config, uniqname):
            self._config = config
            self._uniqname = uniqname

        def __enter__(self):
            '''prepare to receive student data'''
            raise NotImplementedError()

        def __exit__(self):
            '''write data out to disk or postgres or something'''
            raise NotImplementedError()

