#!/usr/bin/env python

import honeydew.backends

from honeydew.memoized import memoized


class Database(object):
    '''
    Frontend interface to read/write projects and grades
    '''
    def __init__(self, config, backend_name):
        '''requires config and name of concrete implementation of Backend'''
        self._config = config
        backend_class = getattr(honeydew.backends, backend_name)
        self._db = backend_class(config)

    @memoized
    def list_students(self, proj_num):
        return self._db.list_students(proj_num)

    def grades(self, uniqname):
        return self._db.get_grades(self._config, uniqname)

    def submission(self, uniqname):
        return self._db.get_submission(self._config, uniqname)


class Backend(object):
    '''
    Interface for various backends to store/retrive student projects/records
    '''

    def __init__(self, config):
        '''init'''
        raise NotImplementedError()

    def get_grades(self, config, uniqname):
        raise NotImplementedError()

    def get_submission(self, config, uniqname):
        raise NotImplementedError()

    def list_students(self):
        raise NotImplementedError()

    class Grades(object):
        '''
        context-managed class for grades
        '''

        def __init__(self, config, uniqname, **kwargs):
            '''prepare to receive student data'''
            raise NotImplementedError()

        def __enter__(self):
            raise NotImplementedError()

        def __exit__(self, type, value, traceback):
            '''call any cleanup needed, including close()'''
            raise NotImplementedError()

        def close(self):
            '''
            write data out to disk or postgres or something

            don't implement this if you want to force use within a context
            manager
            '''
            raise NotImplementedError()

    class Submission(object):
        '''
        context-managed class for submissions
        '''

        def __init__(self, config, uniqname, **kwargs):
            '''access student files and prepare for grading'''
            raise NotImplementedError()

        def __enter__(self):
            raise NotImplementedError()

        def __exit__(self, type, value, traceback):
            '''call any cleanup needed, including close()'''
            raise NotImplementedError()

        def close(self):
            '''
            clean up or something

            don't implement this if you want to force use within a context
            manager
            '''
            raise NotImplementedError()
