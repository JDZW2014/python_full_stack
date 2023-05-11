# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2023/5/9
Description :
auther : wcy
"""
# import modules
import os
import numpy as np

__all__ = []


# define function
def func1_dp(n, s, e, k):
    """
    【题目】：
        int N = [0, 1, 2, ... N]
        int S 起始位置
        int E 终止位置
        int K 机器人必须走k步

        每次可以往左走，可以往右走
        求方法数
    :return:
    """
    # 终止条件


    # 递归调用
    func1_dp(n=n, s=s-1, e=e, k=k-1) # 网左走
    func1_dp(n=n, s=s-1, e=e, k=k-1) # 往右走
    pass


def func1_db(n_scope, start, end, step, arr: np.ndarray):
    """
    【题目】：
        int N = [0, 1, 2, ... N]
        int S 起始位置
        int E 终止位置
        int K 机器人必须走k步

        每次可以往左走，可以往右走
        求方法数

    arr 的行代表当前的step, arr 的列代表要走的步数
    :return:
    """
    for st in range(step+1):
        for ns in range(n_scope):
            if st == 0:
                if ns == start:
                    arr[ns, st] = 1
                else:
                    arr[ns, st] = 0
            else:
                ns1 = ns - 1
                ns2 = ns + 1
                if 0 <= ns1 < n_scope:
                    m1 = arr[ns1, st-1]
                else:
                    m1 = 0

                if 0 <= ns2 < n_scope:
                    m2 = arr[ns2, st-1]
                else:
                    m2 = 0

                arr[ns, st] = m1 + m2

    return arr, arr[end, step]


def func2_dp(lis, aim, start, arr: np.ndarray):
    """
    【问题】：
        data_list = [2, 3, 5, 7, 3]
        aim = 10
        问，组成aim 最少需要多少硬币
    :return:
    """
    # 查 cache
    cache_val = arr[aim, start]
    if cache_val >= 0:
        return True, cache_val
    elif cache_val == -1:
        return False, cache_val
    else:
        pass

    # 终止条件
    if start == len(lis):
        if aim == 0:
            return True, 0
        else:
            return False, 0

    # 递归调用
    val = lis[start]
    success1, num1 = False, None
    if aim - val > 0:
        success1, num1 = func2(lis=lis, aim=aim-val, start=start+1, arr=arr)
        if success1 is True:
            num1 += 1

    success2, num2 = func2(lis=lis, aim=aim, start=start+1, arr=arr)

    # 汇总结果
    if success1 is True and success2 is True:
        if num1 <= num2:
            arr[aim, start] = num1
            return success1, num1
        else:
            arr[aim, start] = num2
            return success2, num2
    elif success1 is True:
        arr[aim, start] = num1
        return success1, num1
    elif success2 is True:
        arr[aim, start] = num2
        return success2, num2
    else:
        arr[aim, start] = -1
        return False, None


def func2_db(lis, aim, arr: np.ndarray):
    """
    【问题】：
        data_list = [2, 3, 5, 7, 3]
        aim = 10
        问，组成aim 最少需要多少硬币
    用打表法解这个问题
    """
    for s in range(1, aim+1):
        for idx in range(len(lis)):
            # 情况1
            val = s - lis[idx]
            if val > 0:
                m1_ways = arr[val, idx]
                if m1_ways != 0:
                    m1_ways += 1
            elif val == 0:
                m1_ways = 1
            else:
                m1_ways = 0

            m2_ways = arr[s, idx]

            if m1_ways != 0 and m2_ways != 0:
                ways = min(m1_ways, m2_ways)
            elif m1_ways != 0 and m2_ways == 0:
                ways = m1_ways
            elif m1_ways == 0 and m2_ways != 0:
                ways = m2_ways
            else:
                ways = 0

            arr[s, idx + 1] = ways

    return arr


# define main
def main1():
    arr = np.random.random((10, 11))
    arr[:, :] = 0
    arr, m = func1_db(n_scope=10, start=2, end=4, step=10, arr=arr)
    print(arr)
    print(m)


def main2():
    lis = [2, 3, 5, 7, 3]
    aim = 10
    arr = np.random.random((aim+1, len(lis) + 1))
    arr[:, :] = 0

    # ret = func2(lis=lis.copy(), aim=aim, start=0, arr=arr)
    # print(f"lis = {lis}, ret = {ret}")
    # print(arr)

    # 用打表法解决这个问题
    ret = func2_db(lis=lis, aim=aim, arr=arr)
    print(ret)


# main
if __name__ == '__main__':
    main1()
