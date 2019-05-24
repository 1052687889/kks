#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:taoke
import re


class NoneClass(object):
    '''
    None type
    '''

class __setting(object):
    def __init__(self):
        import setting
        for i in dir(setting):
            if not re.findall('^__(.*?)__$', i):
                setattr(self,i,setting.__dict__[i])

    def __getitem__(self, item):
        return getattr(self,item)

    def __getattr__(self, item):
        for i in self.__dict__:
            if i == item:
                return self.__dict__[i]
        else:
            raise ValueError('not found attr {}'.format(item))

    def get(self,key,default=NoneClass()):
        try:
            return self[key]
        except ValueError as e:
            if isinstance(default,NoneClass):
                raise ValueError(e)
            else:
                return default

setting = __setting()
