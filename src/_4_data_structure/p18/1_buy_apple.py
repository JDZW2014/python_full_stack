# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-07-18
Description :
auther : wcy
"""
# import modules
import os

__all__ = []


# define function
def func_buy_apple(num):
    """
    只能使用 6 个的袋子和 8 个的袋子，
    给定 n 个苹果，如果能恰好使用这两种袋子装下，返回最少的袋子数
    如果不能返回 -1
    :param num:
    :return:
    """
    k1 = num // 8
    k2 = num - 8 * k1
    for i in range(0, 4):


    pass


# main
if __name__ == '__main__':
    print(func_buy_apple())