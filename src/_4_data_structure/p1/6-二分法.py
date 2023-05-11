"""
题目1: 在一个有序数组中查找某个数是否存在
题目2: 在一个有序数组中查找 >= 某个数最左侧的位置
题目3: 局部最小值问题: 一个数组无序，相邻的数一定不相等，
"""
from typing import List, Dict, Tuple


def func1(iis: List, num: int, start: int, end: int):
    # 终止条件
    if len(lis) == 0:
        return -1
    if len(lis) == 1:
        if lis[start] == num:
            return start
        else:
            return -1

    # 递归调用
    mid = len(start + end) // 2
    if lis[mid] == num:
        return mid
    elif lis[mid] < num:
        func(lis[mid+1: end])
    else:
        func(lis[start: mid])
    return -1

lis = [1, 2, 5, 7, 9, 11]
num = 2
