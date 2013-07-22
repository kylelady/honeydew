#!/usr/bin/env python

import os

import honeydew.database


class Filesystem(honeydew.database.Backend):
    '''Simple filesystem-based backend implementation'''
    def __init__(self, config):
        self._config = config

    def get_grades(self, config, uniqname):
        return self.FSGrades(config, uniqname)

    def get_submission(self, config, uniqname):
        return self.FSSubmission(config, uniqname)

    def list_students(self, proj_num):
        '''returns a list of students for that proj_num

        this assumes that all the subdirs of the submission dir are students
        '''
        sub_dir = self._config.get('Filesystem', 'submissions_dir')
        students_path = sub_dir.format(n=proj_num)

        students = []

        for file in os.listdir(students_path):
            if os.path.isdir(os.path.join(students_path, file)):
                uniqname = os.path.basename(file.rstrip(os.sep))
                students.append(uniqname)

        return sorted(students)


    class FSGrades(honeydew.database.Backend.Grades):
        def __init__(self, config, uniqname):
            self._config = config
            self._uniqname = uniqname
            self._open(uniqname)

        def __enter__(self):
            pass

        def __exit__(self, type, value, traceback):
            self.close()

        def _open(self, uniqname):
            pass

        def close(self):
            pass

    class FSSubmission(honeydew.database.Backend.Submission):
        def __init__(self, config, uniqname):
            self._config = config
            self._uniqname = uniqname
            self._open(uniqname)

        def __enter__(self):
            pass

        def __exit__(self, type, value, traceback):
            self.close()

        def _open(self, uniqname):
            pass

        def close(self):
            pass
