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
        return self._db.get_student(self._config, uniqname)


class Backend(object):
    '''
    Interface for various backends to store/retrive student projects/records
    '''

    def __init__(self, config):
        '''init'''
        raise NotImplementedError()

    class Student(object):
        '''
        context-managed class for student data
        '''

        def __init__(self, config, uniqname, **kwargs):
            '''prepare to receive student data'''
            raise NotImplementedError()

        def __enter__(self):
            raise NotImplementedError()

        def __exit__(self):
            '''call any cleanup needed, including close()'''
            raise NotImplementedError()

        def close(self):
            '''
            write data out to disk or postgres or something

            don't implement this if you want to force use within a context
            manager
            '''
            raise NotImplementedError()

