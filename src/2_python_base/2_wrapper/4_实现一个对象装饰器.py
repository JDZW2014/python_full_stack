# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2021-08-23
Description :
auther : wcy
"""
# import modules
import os

__all__ = []


# define class
class ObjectWrapper(object):
    def __init__(self, a_product, b_product):
        self.a_product = a_product
        self.b_product = b_product

    def __call__(self, func):

        def wrapper(**kwargs):
            a = kwargs.get("a")
            b = kwargs.get("b")
            a *= self.a_product
            b *= self.b_product
            return func(a, b)
        return wrapper


# define function
@ObjectWrapper(a_product=0, b_product=0.1)
def _sum(a, b):
    return a + b


# main
if __name__ == '__main__':
    print(_sum(a=100, b=10))
