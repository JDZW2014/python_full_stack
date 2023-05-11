# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-09-07
Description :
auther : wcy
"""
# import modules
import os
import math

__all__ = []


# define class
class Func1(object):
    """
    关于打表法的的补充题目：

    题目特征：
        1. 输入是int， 输出也是int
        2. 打表观察规律，总结规律
        3. 不是所有这类题目都可以使用打表法来求解，大概可以命中个40%

    """

    @staticmethod
    def dui_shu_qi(n):
        """
        暴力求解，观察规律
        """
        for i in range(0, int(math.log(n, 4))+1, 1):
            left_n = n-4**i
            if left_n == 0:
                return "先手"
            res = Func1.dui_shu_qi(n=left_n)
            if res == '后手':
                return '先手'
        return '后手'

    @staticmethod
    def rule(n):
        """
        总结规律
        """
        if n % 5 in [2, 0]:
            return "后手"
        else:
            return "先手"


# define main
def main1():
    # 1. 先使用对数器暴力求解，观察规律
    for i in range(1, 30):
        print(i, "  ", Func1.dui_shu_qi(i))

    # 2. 总结规律
    for i in range(1, 30):
        print(i, "  ", Func1.dui_shu_qi(i), Func1.rule(i))


# main
if __name__ == '__main__':
    main1()
