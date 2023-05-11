# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2023/5/3
Description :
auther : wcy
"""
# import modules
import os

__all__ = []

import random


# define function
def func1(lis: list, start: int, end: int):
    """
    归并排序, 从小到大
    :return:
    """
    # 终止条件
    if end - start <= 1:
        return lis[start: end]

    # 递归调用
    mid = int((start + end) / 2)
    ret1: list = func1(lis=lis, start=start, end=mid)
    ret2: list = func1(lis=lis, start=mid, end=end)

    # 合并递归的结果
    ret = []
    while ret1 and ret2:
        if ret1[0] <= ret2[0]:
            ret.append(ret1.pop(0))
        else:
            ret.append(ret2.pop(0))

    if ret1:
        ret = ret + ret1

    if ret2:
        ret = ret + ret2

    print(f"ret = {ret}")
    return ret


def func2(lis: list, start: int, end: int):
    """
    小和问题
    在一个数组中，每一个数左边比当前数小的数累加起来，叫做这个数组的小和。求一个数组的小和称为小和问题。
    input: [2,4,5,1,7,3]
    2 左侧比 2 小的数，没有；
    4 左侧比 4 小的数，2；
    5 左侧比 5 小的数，2,4；
    1 左侧比 1 小的数，没有；
    7 左侧比 7 小的数，2,4,5,1；
    3 左侧比 3 小的数，2,1。

    output: 2+2+4+2+4+5+1+2+1=23
    所以这些数的和为最终的小和值， 要求时间复杂度为 O(N * log N)

    扩展：
    逆序对问题
    :return:
    """
    # 终止条件
    if (end - start) <= 1:
        return lis[start: end], 0

    # 递归调用
    mid = int((start + end) / 2)
    ret1, sum1 = func2(lis=lis, start=start, end=mid)
    ret2, sum2 = func2(lis=lis, start=mid, end=end)

    new_list = []
    ts = 0
    # 排序，计算小和
    print(f"ret1 = {ret1}, sum1 = {sum1}, ret2 = {ret2}, sum2 = {sum2}")
    while ret1 and ret2:
        if ret1[0] >= ret2[0]:
            new_list.append(ret2.pop(0))
        else:
            new_list.append(ret1.pop(0))
            ts += new_list[-1] * len(ret2)
    new_list = new_list + ret1 + ret2
    print(f"ts = {ts}")

    return new_list, ts + sum1 + sum2


def func3(lis: list, num: int):
    """
    问题一： 给定一个数组arr， 和一个数num，请把小于num 的数放在数据组的左边，等于的放中间，大于num的数放在数组的右边。要求额外空间复杂度O(1), 时间复杂度O(N)
    :return:
    """
    l_idx = -1
    m_idx = len(lis)

    idx = 0
    while idx < m_idx:
        print(lis)
        if lis[idx] < num:
            l_idx += 1
            lis[idx], lis[l_idx] = lis[l_idx], lis[idx]
            idx += 1
        elif lis[idx] == num:
            idx += 1
        else:
            m_idx -= 1
            lis[idx], lis[m_idx] = lis[m_idx], lis[idx]
    return lis


def func4(lis: list, start: int, end: int):
    """
    快速排序
    :return:
    """
    # 终止条件
    if (end - start) <= 1:
        return


    # 递归调用
    val = random.choice(lis[start: end])

    l_idx = start - 1
    m_idx = end

    idx = start
    while idx < m_idx:
        if lis[idx] > val:
            m_idx -= 1
            lis[idx], lis[m_idx] = lis[m_idx], lis[idx]

        elif lis[idx] == val:
            idx += 1

        else:
            l_idx += 1
            lis[idx], lis[l_idx] = lis[l_idx], lis[idx]
            idx += 1
    print(f"val = {val}, lis = {lis}, {start}, {l_idx+1}, {m_idx}, {end}")

    func4(lis=lis, start=start, end=l_idx+1)
    func4(lis=lis, start=m_idx, end=end)


# main
def main1():
    lis = [1, 2, 5, 3, 6, 4]
    ret = func1(lis=lis.copy(), start=0, end=len(lis))
    print(f"lis = {lis}, ret = {ret}")


def main2():
    lis = [2,4,5,1,7,3]
    ret = func2(lis=lis, start=0, end=len(lis))
    print(f"lis = {lis}, ret = {ret}")


def main3():
    lis = [1, 2, 5, 3, 3, 6, 4]
    num = 3
    ret = func3(lis=lis, num=num)
    print(f"lis = {lis}, num = {num}, ret = {ret}")


def main4():
    lis = [1, 2, 5, 3, 3, 6, 4]
    func4(lis=lis, start=0, end=len(lis))
    print(f"排序结果：lis = {lis}")


# main
if __name__ == '__main__':
    main4()
