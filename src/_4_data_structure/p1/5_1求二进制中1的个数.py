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
def func1(num: int):
    """
    求一个数二进制中1出现的次数
    这个方法不太好，下面这个方法更好
    """
    n = 0
    while num:
        n += 1
        num = num >> (len(bin((~num + 1) & num)) - 2)
    return n


def func2(num: int):
    """
    方法2中，消除1的方式更加巧妙
    这个方法更好
    """
    n = 0
    while num:
        num = num & (num - 1)
        n += 1
    return n


def func3(num: int):
    """
    方法3提供了另外一种思路：建表法，这种方法在这不是最好的，但是解题的思路会用在其他类型的题目中
    """
    pass


# define main
def main1():
    print(func1(num=1029))


def main2():
    print(func2(num=1029))


def main3():
    print(func3(num=1029))


# main
if __name__ == '__main__':
    main1()
    main2()
