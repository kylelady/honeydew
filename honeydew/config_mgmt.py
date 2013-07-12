#/usr/bin/env python


class ManagedConfig(object):
    '''wraps a ConfigParser() and automatically supplements w/ runtime args'''

    def __init__(self, cp, args):
        '''cp: ConfigParser w/ config; args: dict'''
        self._config = cp
        self._args = args

    def get(self, section, option, raw=False):
        return self._config.get(section, option, raw, self._args)

    def items(self, section, option, raw=False):
        return self._config.items(section, option, raw, self._args)

    @property
    def config(self):
        return self._config

    @propert
    def args(self):
        return self._args
