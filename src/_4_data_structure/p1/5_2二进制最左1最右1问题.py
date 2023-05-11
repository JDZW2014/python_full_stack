# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-08-30
Description :
auther : wcy
"""
# import modules
import os

__all__ = []


# define function
def func1_1(num: int):
    """
    找到二进制中最左侧1的位置
    """
    pass


def func2_1(num: int):
    """
    找到二进制中最右侧1的位置
    """
    num = (~num + 1) & num
    n = 0
    while num:
        num = num >> 1
        n += 1
    return n


def func2_2(num: int):
    """
    找到二进制中最右侧1的位置
    """
    pass


# define main
def main1():
    pass


def main2():
    print(func2_1(num=20100))
    pass


# main
if __name__ == '__main__':
    main1()
    main2()
