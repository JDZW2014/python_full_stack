# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2021-02-08
Description :
auther : wcy
"""
# import modules
import os

__all__ = []


# define class
class Typed(object):
    def __get__(self, obj, type=None) -> object:
        pass

    def __set__(self, obj, value) -> None:
        pass

    def __delete__(self, obj) -> None:
        pass

    def __set_name__(self, owner, name):
        pass
