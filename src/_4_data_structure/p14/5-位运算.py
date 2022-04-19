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


# define function
def func_2(num):
    return num ^ (num & (~num + 1)) == 0


def func_4(num):
    # 判断二进制为是不是只有一个1
    if num ^ num & (~num + 1) == 0:
        num2 = int('01010101010101010101010101010101', 2)
        return bool(num & num2)
    return False



# main
if __name__ == '__main__':
    print(func_2(2))
    print(func_2(7))
    print(func_2(8))
    print(func_2(12))
    print(func_2(16))
    print(func_4(3))
    print(func_4(4))
    print(func_4(7))
    print(func_4(16))
