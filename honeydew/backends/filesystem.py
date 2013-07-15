#!/usr/bin/env python

from honeydew.database import Backend


class Filesystem(Backend):
    '''Simple filesystem-based backend implementation'''
    pass

    def get_grades(self, config, uniqname):
        return self.FSGrades(config, uniqname)

    def get_submission(self, config, uniqname):
        return self.FSSubmission(config, uniqname)

    class FSGrades(Backend.Grades):
        def __init__(self, config, uniqname):
            self._config = config
            self._uniqname = uniqname
            self._open(uniqname)

        def __enter__(self):
            pass

        def __exit__(self):
            self.close()

        def _open(self, uniqname):
            pass

        def close(self):
            pass

    class FSSubmission(Backend.Submission):
        def __init__(self, config, uniqname):
            self._config = config
            self._uniqname = uniqname
            self._open(uniqname)

        def __enter__(self):
            pass

        def __exit__(self):
            self.close()

        def _open(self, uniqname):
            pass

        def close(self):
            pass
