# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2021-02-10
Description :
auther : wcy
"""
# import modules
import os

__all__ = []


# define class
class ClassWrapper(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, **kwargs):
        a = kwargs.get("a")
        b = kwargs.get("b")
        a *= 10
        b *= 100
        return self.func(a, b)


# define function
@ClassWrapper
def sum(a, b):
    return a + b


# main
if __name__ == '__main__':
    print(sum(a=1, b=2))
