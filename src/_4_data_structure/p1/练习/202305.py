# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2023/5/2
Description :
auther : wcy
"""
# import modules
import os

__all__ = []

# define class


# define function
def func1(lis: list):
    """
    冒泡排序
    :return:
    """
    for i in range(len(lis), 1, -1):
        for j in range(1, i):
            if lis[j-1] > lis[j]:
                lis[j-1], lis[j] = lis[j], lis[j-1]
    return lis

def func2(lis: list):
    """
    有一个arr, 其中只有一个数出现了奇数次，剩下的数出现了偶数次：找到这个数
    :return:
    """
    val = lis.pop(0)
    while lis:
        val2 = lis.pop(0)
        val ^= val2
    return val


def func3(val):
    """
    求二进制中1的个数
    :return:
    """
    n = 0
    while val:
        print(bin(val))
        val = val >> (len(bin((~val + 1) & val))-2)
        n += 1
    return n



def func4(val: int):
    """
    给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false。
    :return:
    """
    if val >= 4:
        l = len(bin((~val + 1) & val))-2
        val = val >> l
        if val == 0 and (l % 2) == 1:
            return True
    return False


def func5():
    """

    :return:
    """
    pass


# define main func
def main1():
    """
    冒泡排序
    :return:
    """
    lis = [2, 3, 5, 1, 7, 6]
    lis = func1(lis=lis)
    print(lis)


def main2():
    """
    有一个arr, 其中只有一个数出现了奇数次，剩下的数出现了偶数次：找到这个数
    :return:
    """
    lis = [1, 2, 2, 1, 1, 3, 3, 90, 90]
    ret = func2(lis=lis)
    print(ret)


def main3():
    """
    求二进制中1的个数
    :return:
    """
    val = 1010
    ret = func3(val=val)
    print(f"val = {bin(val)}, result = {ret}")


def main4():
    """
    给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false。
    :return:
    """
    val = 64
    ret = func4(val=val)
    print(f"val = {bin(val)}, ret = {ret}")


# main
if __name__ == '__main__':
    main4()
