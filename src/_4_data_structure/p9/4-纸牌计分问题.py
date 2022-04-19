# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-14
Description :
auther : wcy
"""
# import modules
import os
import numpy as np

__all__ = []


# define function
def func(lis, a_score, b_score):
    if len(lis) == 2:
        if lis[0] > lis[1]:
            a_score += lis[0]
            b_score += lis[1]
        else:
            a_score += lis[1]
            b_score += lis[0]
        print(a_score, '', b_score)

    else:
        a = lis[0]
        b = lis[1]
        c = lis[-2]
        d = lis[-1]

        if min(a-b, a-d) > min(d-c, d-a):
            a_score += lis.pop(0)
            if a-b > a-d:
                b_score += lis.pop()
            else:
                b_score += lis.pop(0)
        else:
            a_score += lis.pop()
            if d-c > d-a:
                b_score += lis.pop()
            else:
                b_score += lis.pop(0)
        func(lis, a_score, b_score)


# # 暴力递归的写法
# def func2(lis, left, right):
#
#     a_score = func2(lis, left=left+1, right=right) + lis[left]
#

def funca(lis, left, right, cache_map):
    cache_key = f'a_{left}_{right}'
    if cache_key in cache_map:
        return cache_map[cache_key]

    if left == right:
        v = lis[left]
    else:
        difa = lis[left] - funcb(lis, left=left+1, right=right, cache_map=cache_map)
        difb = lis[right] - funcb(lis, left=left, right=right-1, cache_map=cache_map)
        v = max(difa, difb)
    cache_map[cache_key] = v
    return v


def funcb(lis, left, right, cache_map):
    cache_key = f'b_{left}_{right}'
    if left == right:
        v = lis[left]
    else:
        difa = lis[left] - funca(lis=lis, left=left+1, right=right, cache_map=cache_map)
        difb = lis[right] - funcb(lis=lis, left=left, right=right-1, cache_map=cache_map)
        v = max(difa, difb)
    cache_map[cache_key] = v
    return v


# main
if __name__ == '__main__':
    # lis = [1, 2, 100, 4]
    # func(lis, a_score=0, b_score=0)
    lis = [1, 2, 100, 4]
    cache_map = {}
    print(funca(lis, 0, len(lis)-1, cache_map))

