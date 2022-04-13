# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-13
Description :
auther : wcy
"""
# import modules
import os, typing

__all__ = []


# define function
def func(num: int, status: int):
    if num > 0:
        # left
        func(num-1, status=0)
        print(status)
        # right
        func(num-1, status=1)


# define teat
def test():
    num = 2
    print(f" --- {num} ---")
    func(num=num, status=0)

    num = 3
    print(f" --- {num} ---")
    func(num=num, status=0)

    num = 4
    print(f" --- {num} ---")
    func(num=num, status=0)


# main
if __name__ == '__main__':
    test()
