# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-09-01
Description :
auther : wcy
"""
# import modules
import os

__all__ = []


# define function
def func1():
    """
    颠倒给定的 32 位无符号整数的二进制位。
    """
    pass


def func2(num: int):
    """
    给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
    """
    if num <= 1:
        return False
    else:
        num = num & num - 1
        if num == 0:
            return True
        else:
            return False


def func3():
    """
    给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false。
    """
    pass


def func4():
    """
    两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
    给出两个整数 x 和 y，计算它们之间的汉明距离。
    """
    pass


# define main
def main1():
    num = 16
    print(num, '-', func2(num=num))
    num = 18
    print(num, '-', func2(num=num))


def main2():
    pass


def main3():
    pass


# main
if __name__ == '__main__':
    main1()
    main2()
    main3()
