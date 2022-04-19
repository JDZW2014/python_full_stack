# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-19
Description :
auther : wcy
"""
# import modules
import os

__all__ = []


# define class
class Compare(object):
    def __init__(self):
        pass

    def call(self, a: int, b: int):
        if self.if_same_sign(num1=a, num2=b):
            return self._call1_(a=a, b=b)
        else:
            a_sign = self.sign(a)
            b_sign = self.sign(b)
            return a * self.flip(a_sign) + b * self.flip(b_sign)

    def _call1_(self, a, b):
        c = a - b
        c_sign = self.sign(c)
        return a * self.flip(c_sign) + b * c_sign

    def if_same_sign(self, num1, num2):
        num1_sign = self.sign(num1)
        num2_sign = self.sign(num2)

        d_num = num1_sign ^ num2_sign
        return self.flip(d_num)


    def sign(self, num):
        return num >> 31 & 1

    def flip(self, num):
        return num ^ 1


# main
if __name__ == '__main__':
    compare = Compare()
    print(compare.call(a=11, b=202))
    print(compare.call(a=-10, b=100))
    print(compare.call(a=-10, b=-110))
