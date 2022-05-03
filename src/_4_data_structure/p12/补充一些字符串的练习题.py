# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-28
Description :
auther : wcy
"""
# import modules
import os

__all__ = []


# define class
class Func1Ret(object):
    def __init__(self):
        self.max_len = 0
        self.start = -1
        self.end = -1


# define function
def func1(str1, str2, i, j, max_len_list, cache):
    """
    求两个字符串的最长公共子串
    """
    _s = str2[i:j]
    if _s in cache:
        v = cache[_s]
        return v[0], v[1]

    ret_list = []
    if i == j-1:
        for idx, ele in enumerate(str1):
            if ele == str2[i]:
                ret_list.append((idx, idx+1))
        if len(ret_list) > 0:
            max_len = 1
        else:
            max_len = 0

    else:
        ret_list1, _ = func1(str1, str2, i+1, j, max_len_list, cache)
        for (s, e) in ret_list1:
            if str1[s-1] == str2[i]:
                ret_list.append((s-1, e))

        ret_list2, _ = func1(str1, str2, i, j-1, max_len_list, cache)
        for (s, e) in ret_list2:
            if str1[e+1] == str2[j]:
                ret_list.append((s, e+1))

        if len(ret_list) > 0:
            max_len = j-i
        else:
            max_len = 0

    if max_len > 0:
        max_len_list.append(max_len)

    cache[_s] = (ret_list, max_len)
    return ret_list, max_len


def func12(str1, str2, i, max_len_list):
    # base case
    ret_list = []
    if i == len(str2) - 1:
        for idx, ele in enumerate(str1):
            if ele == str2[i]:
                ret_list.append((idx, idx+1, 1))
            else:
                ret_list.append((idx, idx, 0))
    else:
        _ret_list = func12(str1, str2, i+1, max_len_list)
        for (s, e, l) in _ret_list:
            if str1[s-1] == str2[i]:
                ret_list.append((s-1, e, l+1))
            else:
                ret_list.append((s-1, s-1, 0))

    max_len_list.append(max([dat[-1] for dat in ret_list]))
    return ret_list


def func13(str1, str2, i, j, cache):
    _k = f"{i}_{j}"
    if _k in cache:
        return cache[_k]

    if i < 0 or j < 0:
        max_len = 0
    else:
        if str1[i] == str2[j]:
            max_len = func13(str1, str2, i-1, j-1, cache) + 1
        else:
            func13(str1, str2, i-1, j, cache)
            func13(str1, str2, i, j - 1, cache)
            max_len = 0
    cache[_k] = max_len
    return max_len


def func2(str1, str2, i, j, cache):
    """
    求两个字符串的最长公共子序列
    """
    _k = f"{i}_{j}"
    if _k in cache:
        return cache[_k]
    # base case
    if i < 0 or j < 0:
        max_len = 0
    else:
        if str1[i] == str2[j]:
            max_len = func2(str1, str2, i-1, j-1, cache) + 1
        else:
            max_len = max(func2(str1, str2, i - 1, j, cache), func2(str1, str2, i, j - 1, cache))
    cache[_k] = max_len
    return max_len


def func3(lis, i, cache):
    """
    最长递增子序列
    """
    if i in cache:
        return cache[i]

    max_len = 0
    if i == 0:
        max_len = 1
    else:
        for _i in range(i):
            l = func3(lis, _i, cache)
            if lis[i] > lis[_i]:
                if l+1 > max_len:
                    max_len = l+1
    if 1 > max_len:
        max_len = 1
    cache[i] = max_len
    return max_len


# define main
def main1():
    s1 = '1AB2345ACD'
    s2 = '12345EF'
    max_len_list = list()
    ret_list, max_len = func1(str1=s1, str2=s2, i=0, j=len(s2), max_len_list=max_len_list, cache={})
    print(max(max_len_list))

    max_len_list2 = list()
    func12(str1=s1, str2=s2, i=0,  max_len_list=max_len_list2)
    print(max(max_len_list))

    cache = {}
    func13(s1, s2, i=len(s1)-1, j=len(s2)-1, cache=cache)
    print(max(list(cache.values())))


def main2():
    s1 = '1AB2345ACDF'
    s2 = 'Q24CFF'
    cache = {}
    print(func2(str1=s1, str2=s2, i=len(s1)-1, j=len(s2)-1, cache=cache))


def main3():
    lis = [100, 1, 6, 2, 5, 3, 4, 7, 2, 9, 1]
    cache = {}
    func3(lis=lis, i=len(lis) - 1, cache=cache)
    print(max(cache.values()))


# main
if __name__ == '__main__':
    main1()
    main2()
    main3()
