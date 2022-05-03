# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-29
Description :
auther : wcy
"""
# import modules
import os

__all__ = []


# define function
def func1(num, start, end, other):
    """汉诺塔问题"""
    if num == 1:
        print(f"{num} {start} -> {end}")
    else:
        func1(num-1, start, other, end)
        print(f"{num} {start} -> {end}")
        func1(num - 1, other, start, end)


def func2(word_list, i):
    """字符串子序列问题"""
    ret_list = []
    if i == len(word_list):
        ret_list.append("")
    else:
        _ret_list = func2(word_list, i + 1)
        for _s in _ret_list:
            ret_list.append(_s)
            ret_list.append(f"{word_list[i]}{_s}")

    return ret_list


def func3():
    """字符串全排列问题"""
    pass


def func4():
    """汉诺塔问题"""
    pass


# define main
def main1():
    func1(num=3, start="start", end="end", other="other")


def main2():
    print(func2(word_list=list("abc"), i=0))
    print(func2(word_list=list("acsda"), i=0))

    pass


def main3():
    pass


def main4():
    pass


# main
if __name__ == '__main__':
    main1()
    main2()
    main3()
    main4()
