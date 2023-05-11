# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-08-30
Description :

auther : wcy
"""
# import modules
import os

__all__ = []


# define function
def func1(length: int, lis: list):
    """
    窗口法的技巧：

    滑动窗口的最大值最小值问题
    给定一个有序数组arr, 代表数轴上从左到右有n个点arr[0], arr[1], ... arr[n-1]
    给定一个正数L，代表一根长度为L的绳子，求绳子最多能覆盖其中的几个点。
    """
    left_idx = 0
    right_idx = None

    # 先将右侧填满
    for idx, value in enumerate(lis):
        if value <= lis[left_idx] + length:
            right_idx = idx
        else:
            break
    max_p_num = right_idx - left_idx + 1

    # 开始移动左侧的开始位置
    while True:
        left_idx += 1
        if left_idx >= len(lis):
            break

        while True:
            if (right_idx + 1) < len(lis) and lis[right_idx+1] <= lis[left_idx] + length:
                right_idx = right_idx + 1
            else:
                break

        max_p_num = max(max_p_num, right_idx - left_idx + 1)
        print((left_idx, right_idx))
        if right_idx + 1 == len(lis):
            break
    return max_p_num


# define main
def main1():
    print(func1(length=10, lis=[1, 10, 11, 18, 19, 20, 21, 30]))


# main
if __name__ == '__main__':
    main1()
