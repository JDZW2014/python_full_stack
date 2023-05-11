# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2023/5/10
Description :
auther : wcy
"""
# import modules
import os
import numpy as np
import math

__all__ = []


# define function
def func1_1(lis: list, arr: np.ndarray):
    """
    求最长上升子序列: [1, 10, 3, 2, 4, 7]
    :return:
    """
    for i in range(len(lis)):
        for j in range(i):
            if lis[i] > lis[j]:
                arr[i] = max(arr[i], arr[j] + 1)
    return arr


def func1_2():
    """
    求最长上升子串: [1, 10, 3, 2, 4, 7]
    :return:
    """
    # 太简单，pass
    pass


def func2(lis: list, f_aim: int, arr: np.ndarray):
    """
    硬币组合问题, 可重复使用
    【题目】
        面值： [3， 5， 10， 2]
        凑成 100， 每个面值可以重复使用
        一共有多少种凑法
    :return:
    """
    for aim in range(1, f_aim+1):
        for idx in range(len(lis)):
            # 求出除数和余数
            chu_s = aim // lis[idx]
            yu_s = aim % lis[idx]

            total_ways = 0
            for i in range(chu_s+1):
                sheng_s = aim - lis[idx] * i
                total_ways += arr[sheng_s, idx]

            if yu_s == 0:
                total_ways += 1
            arr[aim, idx+1] = total_ways

    return arr


def func3(lis: list, f_aim: int, arr: np.ndarray):
    """
    硬币组合问题, 不可重复使用

    【问题】：
        data_list = [2, 3, 5, 7, 3]
        aim = 10
        问，组成aim 最少需要多少硬币
    :return:
    """
    for aim in range(1, f_aim+1):
        for idx in range(len(lis)):
            if aim > lis[idx]:
                aim2 = aim - lis[idx]

                v1 = arr[aim, idx]

                v2 = arr[aim2, idx]
                if v2 != -1:
                    v2 += 1

                if v1 != -1 and v2 != -1:
                    arr[aim, idx+1] = min(v1, v2)
                elif v1 != -1 and v2 == -1:
                    arr[aim, idx + 1] = v1
                elif v1 == -1 and v2 != -1:
                    arr[aim, idx + 1] = v2
                else:
                    arr[aim, idx + 1] = -1
            elif aim == lis[idx]:
                arr[aim, idx+1] = 1
            else:
                arr[aim, idx+1] = arr[aim, idx]
    return arr


def func4(s1: str, s2: str, arr: np.ndarray):
    """
    最长公共子串
    :return:
    """
    for i in range(len(s2)):
        for j in range(len(s1)):
            if s2[i] == s1[j]:
                arr[i+1, j+1] = arr[i, j] + 1
            else:
                arr[i+1, j+1] = 0
    return arr


def func5(s1: str, s2: str, arr: np.ndarray):
    """
    最长公共子序列
    :return:
    """
    for i in range(len(s2)):
        for j in range(len(s1)):
            if s2[i] == s1[j]:
                arr[i+1, j+1] = arr[i, j] + 1
            else:
                arr[i + 1, j + 1] = arr[i+1, j]
    return arr


def func6(start: int, end: int, scope: int, t_step: int, arr: np.ndarray):
    """
    左右走，方法数问题
    【题目】：
        int N = [0, 1, 2, ... N]
        int S 起始位置
        int E 终止位置
        int K 机器人必须走k步

        每次可以往左走，可以往右走
        求方法数
    :return:
    """
    for step in range(t_step):
        for pos in range(scope):
            if step == 0:
                if pos == end:
                    arr[step, pos+1] = 1
            else:
                arr[step, pos+1] = arr[step-1, pos] + arr[step-1, pos+2]
    return arr


def func7(start_row: int, start_col: int, row: int, col: int, t_step: int, arr: np.ndarray):
    """
    【题目】：
        m * n 的格子
        人 位置： 啊a,b 可以随机上下左右走，走k 步， 走出 m * n 的格子就死亡， 求人最终可以存活的概率
    :return:
    """
    for step in range(t_step):
        for r in range(row):
            for c in range(col):
                if step == 0:
                    if r == start_row and c == start_col:
                        arr[step, r+1, c+1] = 1
                else:
                    arr[step, r+1, c+1] = arr[step-1, r, c+1] + arr[step-1, r, c-1] + arr[step-1, r+1, c] + arr[step-1, r-1, c]

    # 计算所有的可能
    total = math.pow(4, step-1)
    return arr.sum(), total


def func8(end: tuple, t_step: int):
    """
    【题目】：
        10 * 10 的棋盘，
        马 在 （0， 0） 位置
        马要到 （a, b）位置
        马一定要挑k步

        求 方法数
    :return:
    """
    start = (0, 0)
    n_col, n_row = 10, 10

    arr = np.random.random((t_step, n_row+4, n_col+4))
    for step in range(t_step):
        for r in range(n_row):
            for c in range(n_col):
                if step == 0:
                    if r == end[0] and c == end[1]:
                        arr[step, r+2, c+2] = 1
                else:
                    r += 2
                    c += 2
                    arr[step, r, c] = arr[step - 1, r - 1, c - 2] + \
                                      arr[step - 1, r - 1, c + 2] + \
                                      arr[step - 1, r - 1, c + 2]
                            # todo 不是很难，未完成
    return arr


# define main
def main1():
    lis = [1, 10, 3, 2, 4, 7]
    arr = np.random.random((len(lis)))
    arr[:] = 1
    arr = func1_1(lis=lis, arr=arr)
    print(f"lis = {lis}")
    print(f"arr=\n{arr}")


def main2():
    lis = [2, 3, 5, 7]
    aim = 10
    arr = np.random.random((aim + 1, len(lis) + 1))
    arr[::] = 0
    func2(lis=lis, f_aim=aim, arr=arr)
    print(f"aim = {aim}, lis = {lis}")
    print(f"arr=\n{arr}")


def main3():
    lis = [2, 3, 5, 5, 7, 3]
    aim = 13
    arr = np.random.random((aim+1, len(lis) + 1))
    arr[::] = -1
    arr = func3(lis, f_aim=aim, arr=arr)
    print(f"lis = {lis}")
    print(f"arr = \n{arr}")


def main4():
    s1 = 'abfabzhh'
    s2 = 'abz'
    arr = np.random.random((len(s2) + 1, len(s1) + 1))
    arr[::] = 0
    arr = func4(s1=s1, s2=s2, arr=arr)
    print(f"s1 = {s1}, s2 = {s2}")
    print(f"arr = \n{arr}")


def main5():
    s1 = 'abfazbzhg'
    s2 = 'abzg'
    arr = np.random.random((len(s2) + 1, len(s1) + 1))
    arr[::] = 0

    arr = func5(s1=s1, s2=s2, arr=arr)
    print(f"s1 = {s1}, s2 = {s2}")
    print(f"arr = \n{arr}")


def main6():
    start = 2
    end = 5
    scope = 7
    step = 5

    arr = np.random.random((step, scope+2))
    arr[::] = 0
    arr = func6(start=start, end=end, scope=scope, t_step=step, arr=arr)
    print(f"start={start}, end={end}, scope={scope}, stop={step}")
    print(arr)


def main7():
    row = 5
    col = 7
    start = (1, 2)
    step = 6
    arr = np.random.random((step, row + 2, col + 2))
    arr[::] = 0

    ways, total = func7(start_row=start[0], start_col=start[1], row=row, col=col, t_step=step, arr=arr)

    print(f"row={row}, col={col}, start={start}, step={step}, ways={ways}, total={total}")
    print(f"arr=\n{arr}")


def main8():
    end = (5, 6)
    step = 6

    func8(end=end, step=step)


# main
if __name__ == '__main__':
    main7()
