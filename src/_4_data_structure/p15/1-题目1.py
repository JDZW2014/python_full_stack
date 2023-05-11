# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-19
Description :
auther : wcy

【题目】：
    int N = [0, 1, 2, ... N]
    int S 起始位置
    int E 终止位置
    int K 机器人必须走k步

    每次可以往左走，可以往右走
    求方法数
"""
# import modules
import os, typing
import numpy as np

__all__ = []


# define function
def func1(data_list: typing.List[int], s: int, e: int, k: int, cache_map: np.ndarray):
    if cache_map[s, k] != -1:
        return cache_map[s, k]
    if k == 0:
        res = s == e
    elif s == 0:
        res = func1(data_list=data_list, s=s+1, e=e, k=k-1, cache_map=cache_map)
    elif s == data_list[-1]:
        res = func1(data_list=data_list, s=s-1, e=e, k=k-1, cache_map=cache_map)
    else:
        res = func1(data_list=data_list, s=s+1, e=e, k=k-1, cache_map=cache_map) + \
               func1(data_list=data_list, s=s-1, e=e, k=k-1, cache_map=cache_map)
    cache_map[s, e] = res
    return res


def func2(data_list: typing.List[int], s: int, e: int, k: int, cache_map: np.ndarray):
    s_min = 0
    s_max = data_list[-1]
    k_min = 0
    k_max = k
    raw_s = s
    raw_k = k

    for s in data_list:
        if s == e:
            cache_map[s, 0] = 1
        else:
            cache_map[s, 0] = 0

    def get_value(s, k):
        if s_min <= s <= s_max and k_min <= k <= k_max:
            v = cache_map[s, k]
            assert v != -1
            return v
        else:
            return 0

    for k in range(1, 5):
        for s in data_list:
            arr[s, k] = get_value(s-1, k-1) + get_value(s+1, k-1)

    return arr[raw_s, raw_k]


# main
if __name__ == '__main__':
    data_list_len = 6
    data_list = list(range(data_list_len))
    s = 2
    e = 4
    k = 4
    arr = np.ones(shape=(6, k+1)) * -1
    print(func1(data_list=data_list, s=s, e=e, k=k, cache_map=arr))
    arr = np.ones(shape=(6, k + 1)) * -1
    print(func2(data_list=data_list, s=s, e=e, k=k, cache_map=arr))
