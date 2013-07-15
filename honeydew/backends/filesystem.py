#!/usr/bin/env python

from honeydew.database import Backend

class Filesystem(Backend):
    '''Simple filesystem-based backend implementation'''
    pass

    class FSStudent(Backend.Student):
        def __init__(self, config, uniqname):
            self._config = config
            self._uniqname = uniqname
            self._open(uniqname)

        def __enter__(self):
            pass

        def __exit__(self):
            self.close()

        def _open(self, uniqname):


        def close(self):

