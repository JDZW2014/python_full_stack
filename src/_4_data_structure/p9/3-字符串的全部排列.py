# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-14
Description :
auther : wcy
"""
# import modules
import os

__all__ = []


# define function
def func(s, l):
    if l == 1:
        print("".join(s))
    else:
        for i in range(l):
            s[i], s[l-1] = s[l-1], s[i]
            func(s, l-1)
            s[i], s[l - 1] = s[l - 1], s[i]


# main
if __name__ == '__main__':
    s = 'abc'
    func(s=list(s), l=len(s))














def func(s, l):
    if l == 1:
        print("".join(s))

    else:
        for i in range(l):
            s[i], s[l-1] = s[l-1], s[i]
            func(s, l-1)
            s[i], s[l-1] = s[l-1], s[i]
