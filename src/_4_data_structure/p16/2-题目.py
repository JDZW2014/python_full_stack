# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-20
Description :
auther : wcy
【题目】：
    m * n 的格子

    人 位置： 啊a,b 可以随机上下左右走，走k 步， 走出 m * n 的格子就死亡， 求人最终可以存活的概率
"""
# import modules
import os
import numpy as np

__all__ = []


# define function
def func1(rows, colunms, s1, s2, k):
    val = 0
    if s1 < 0 or s1 >= rows or s2 < 0 or s2 >= colunms:
        pass
    else:
        if k == 0:
            val += 1
        else:
            val += func1(rows, colunms, s1+1, s2, k-1)
            val += func1(rows, colunms, s1-1, s2, k-1)
            val += func1(rows, colunms, s1, s2+1, k-1)
            val += func1(rows, colunms, s1, s2-1, k-1)

    return val


# main
if __name__ == '__main__':
    rows = 5
    colunms = 6
    s1 = 2
    s2 = 2
    k = 5
    print(func1(rows, colunms, s1, s2, k))
