"""
计数排序

补充：
排序在工程上的优化：
    1. 不同排序策略的结合
    2. 面对不同用的情况还是需要考虑是否关注排序的稳定性
"""
from collections import defaultdict

def func1(lis):
    count = defaultdict(int)
    for i in lis:
        count[i] += 1

    lis = []
    _v = count.keys()
    for i in range(min(_v), max(_v) + 1):
        lis.extend([i] * count.get(i, 0))
    return lis

lis = [2, 3, 1, 5, 4, 4, 2, 6, 9]
print(func1(lis))