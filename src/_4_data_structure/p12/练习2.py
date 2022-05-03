# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-29
Description :
auther : wcy
"""
# import modules
import os

__all__ = []

# define class


# define function
def func1(s1, s2, i, j, cache):
    """最长公共子串"""
    _k = f"{i}_{j}"
    if _k in cache:
        return cache[_k]

    if i < 0 or j < 0:
        max_len = 0
    else:
        if s1[i] == s2[j]:
            max_len = func1(s1, s2, i-1, j-1, cache) + 1
        else:
            func1(s1, s2, i, j-1, cache)
            func1(s1, s2, i-1, j, cache)
            max_len = 0

    cache[_k] = max_len
    return max_len


def func2(s1, s2, i, j, cache):
    """最长公共子序列"""
    _k = f"{i}_{j}"
    if _k in cache:
        return cache[_k]

    if i < 0 or j < 0:
        max_len = 0
    else:
        if s1[i] == s2[j]:
            max_len = func2(s1, s2, i-1, j-1, cache) + 1
        else:
            max_len = max(func2(s1, s2, i, j-1, cache), func2(s1, s2, i-1, j, cache))

    cache[_k] = max_len
    return max_len


def func3(lis, i, cache):
    """最长上升子串"""
    if i in cache:
        return cache[i]

    if i == 0:
        max_len = 1
    else:
        max_len = 0
        for _i in range(i):
            l = func3(lis, _i, cache)
            if lis[i] > lis[_i]:
                if l + 1 > max_len:
                    max_len = l + 1
        if 1 > max_len:
            max_len = 1
    cache[i] = max_len
    return max_len


def func4(total, lis, idx, cache):
    """硬币凑钱问题：1 元，3 元，5 元的硬币若干（无限），现在需要凑出 11 元， 有多少中组合"""
    _k = f"{total}_{idx}"
    if _k in cache:
        return cache[_k]

    num = 0
    if idx >= len(lis):
        if total == 0:
            num += 1
    else:
        v = lis[idx]
        for i in range((total//v)+1):
            num += func4(total=total-i * v, lis=lis, idx=idx+1, cache=cache)
    cache[_k] = num
    return num


def func5():
    """机器人走路问题"""
    """
    int N = [0, 1, 2, ... N]
    int S 其实位置
    int E 终止位置
    int K 机器人必须走k步

    每次可以往左走，可以往右走
    求方法数
    """


# define
def main1():
    print("公共子串")
    s1 = '1AB2345ACD'
    s2 = '12345EF'
    cache = {}
    func1(s1, s2, i=len(s1)-1, j=len(s2)-1, cache=cache)
    print(max(cache.values()))


def main2():
    print("公共子序列")
    s1 = '1AB2345ACDF'
    s2 = 'AQ24CFF'
    cache = {}
    print(func2(s1, s2, i=len(s1)-1, j=len(s2)-1, cache=cache))


def main3():
    print("最长上升子序列")
    lis = [100, 1, 6, 2, 5, 3, 4, 7, 2, 9, 1]
    cache = {}
    func3(lis=lis, i=len(lis) - 1, cache=cache)
    print(max(cache.values()))


def main4():
    print("凑钱问题")
    lis = [6, 3, 5]
    cache = {}
    print(func4(total=11, lis=lis, idx=0, cache=cache))


# main
if __name__ == '__main__':
    main1()
    main2()
    main3()
    main4()

