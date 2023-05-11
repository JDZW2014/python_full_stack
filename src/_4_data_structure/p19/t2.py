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
def func1(num: int):
    """
    很重要！！！！
    注意：重要的不是这个题怎么做，而是这一类题怎么做：
        输入是int, 输出是int
        第一步：先用对数器跑出前top 的数据，观察规律
        第二部：总结规律；
        第三步：根据规律，写出新的逻辑结果
    整个流程就叫打表法

    不是所有这种类型的题都可以这个做，但是能解决4成左右的题目
    """
    if num >= 6:
        dic = {6: 1, 8: 1, 12: 2, 14: 2, 16: 2, 18: 3, 20:3, 22: 3}
        n1 = (num // 24) * 3
        n2 = num % 24
        if n2 in dic:
            return n1 + dic[n2]
    return -1


class Func2(object):
    """
    打表法的技巧

    题目：
    """

    @staticmethod
    def dui_shu_qi(n):
        """
        先写个暴力的方法，观察规律
        """
        if n < 6:
            return -1
        max_8 = n // 8
        left_num = n - max_8 * 8
        while max_8 >= 0:
            if left_num % 6 == 0:
                return max_8 + (left_num // 6)
            else:
                max_8 -= 1
                left_num += 8
        return -1

    @staticmethod
    def rule(n):
        dic = {0: -1, 2: -1, 4: -1, 6: 1, 8: 1, 10: -1}
        if (n % 2) == 0:
            if n in dic:
                return dic[n]
            max_8 = n // 8
            if (n % 8) > 0:
                max_8 += 1
            return max_8

        return -1


# define main
def main1():
    num = 102
    res = func1(num=num)
    print(num, "-", res)


def main2():
    # 1. 先用对数器观察规律
    for i in range(100):
        if (i % 2) == 0:
            print(i, "  ", Func2.dui_shu_qi(n=i))

    # 2. 总结规律，写出代码
    for i in range(100):
        if (i % 2) == 0:
            print(i, "  ", Func2.dui_shu_qi(n=i), "  ", Func2.rule(n=i))
    pass


# main
if __name__ == '__main__':
    main1()
    main2()
