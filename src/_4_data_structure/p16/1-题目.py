# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-20
Description :
auther : wcy

【题目】：
    10 * 10 的棋盘，
    马 在 （0， 0） 位置
    马要到 （a, b）位置
    马一定要条k步

    求 方法数
"""
# import modules
import os, time
import numpy as np

__all__ = []


# define function
def func1(rows, colunms, s1, s2, e1, e2, k):
    val = 0
    if k == 0:
        if s1 == e1 and s2 == e2:
            val += 1
        else:
            val += 0
    else:
        if s1 < 0 or s1 >= rows or s2 < 0 or s2 >= colunms:
            val += 0
        else:
            val += func1(rows, colunms, s1+1, s2+2, e1, e2, k-1)
            val += func1(rows, colunms, s1+2, s2+1, e1, e2, k-1)

            val += func1(rows, colunms, s1-1, s2-2, e1, e2, k-1)
            val += func1(rows, colunms, s1-2, s2-1, e1, e2, k-1)

            val += func1(rows, colunms, s1+1, s2-2, e1, e2, k-1)
            val += func1(rows, colunms, s1-1, s2+2, e1, e2, k-1)

            val += func1(rows, colunms, s1-2, s2+1, e1, e2, k-1)
            val += func1(rows, colunms, s1+2, s2-1, e1, e2, k-1)

    return val


def func2(rows, colunms, s1, s2, e1, e2, k, arr_cache):
    val = 0

    if k == 0:
        if s1 == e1 and s2 == e2:
            val += 1
        else:
            val += 0
    else:
        if s1 < 0 or s1 >= rows or s2 < 0 or s2 >= colunms:
            val += 0
        else:
            # 如果有cache
            _v, if_have = func2_get_value(s1, s2, k, arr_cache)
            if if_have:
                val += _v

            else:
                # 如果没有cache
                val += func2(rows, colunms, s1+1, s2+2, e1, e2, k-1, arr_cache)
                val += func2(rows, colunms, s1+2, s2+1, e1, e2, k-1, arr_cache)

                val += func2(rows, colunms, s1-1, s2-2, e1, e2, k-1, arr_cache)
                val += func2(rows, colunms, s1-2, s2-1, e1, e2, k-1, arr_cache)

                val += func2(rows, colunms, s1+1, s2-2, e1, e2, k-1, arr_cache)
                val += func2(rows, colunms, s1-1, s2+2, e1, e2, k-1, arr_cache)

                val += func2(rows, colunms, s1-2, s2+1, e1, e2, k-1, arr_cache)
                val += func2(rows, colunms, s1+2, s2-1, e1, e2, k-1, arr_cache)
                arr_cache[e1, e2, k] = val

    return val


def func2_get_value(r, c, k, arr_cache):
    val = arr_cache[r, c, k]
    return val, val != -2


def func3(rows, colunms, s1, s2, e1, e2, k, arr_cache):
    raw_k = k
    # 补充k==0的base case, k = 0 的情况
    for r in range(rows):
        for c in range(colunms):
            if r == e1 and c == e2:
                arr_cache[r, c, 0] = 1
            else:
                arr_cache[r, c, 0] = 0

    # 开始补充其他的值
    k = 1
    while k <= raw_k:
        for r in range(rows):
            for c in range(colunms):
                val = \
                    + func3_get_value(r+1, c+2, k-1, max_r=rows, max_c=colunms, max_k=raw_k, arr_cache=arr_cache) \
                    + func3_get_value(r+2, c+1, k-1, max_r=rows, max_c=colunms, max_k=raw_k, arr_cache=arr_cache) \
                    + func3_get_value(r-1, c-2, k-1, max_r=rows, max_c=colunms, max_k=raw_k, arr_cache=arr_cache) \
                    + func3_get_value(r-2, c-1, k-1, max_r=rows, max_c=colunms, max_k=raw_k, arr_cache=arr_cache) \
                    + func3_get_value(r+1, c-2, k-1, max_r=rows, max_c=colunms, max_k=raw_k, arr_cache=arr_cache) \
                    + func3_get_value(r-1, c+2, k-1, max_r=rows, max_c=colunms, max_k=raw_k, arr_cache=arr_cache) \
                    + func3_get_value(r-2, c+1, k-1, max_r=rows, max_c=colunms, max_k=raw_k, arr_cache=arr_cache) \
                    + func3_get_value(r+2, c-1, k-1, max_r=rows, max_c=colunms, max_k=raw_k, arr_cache=arr_cache)
                arr_cache[r, c, k] = val
        k += 1
    return arr_cache[s1, s2, raw_k]


def func3_get_value(r, c, k, max_r, max_c, max_k, arr_cache):
    if 0 <= r < max_r and 0 <= c < max_c and 0 <= k < max_k:
        val = arr_cache[r, c, k]
        assert val != -2
        return val

    else:
        return 0


# main
if __name__ == '__main__':
    rows = 10
    colunms = 10
    k = 3
    ts = time.time()
    print(func1(rows=rows, colunms=colunms, s1=0, s2=0, e1=1, e2=2, k=k), time.time() - ts)
    ts = time.time()
    arr = np.ones(shape=(rows + 1, colunms + 1, k + 1)) * -2
    print(func2(rows=rows, colunms=colunms, s1=0, s2=0, e1=1, e2=2, k=k, arr_cache=arr), time.time() - ts)

    ts = time.time()
    arr = np.ones(shape=(rows + 1, colunms + 1, k + 1)) * -2
    print(func3(rows=rows, colunms=colunms, s1=0, s2=0, e1=1, e2=2, k=k, arr_cache=arr), time.time() - ts)
