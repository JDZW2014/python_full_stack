"""
基数排序：以需要从小到大排序为例

正常人在排序时是从高位数到地位数依次比较，基数则刚好是一个反过来的过程。

桶排序思想下的排序：计数排序和基数排序

分析：
    1. 桶排序思想下的排序都是不急于比较的排序；
    2. 时间复杂度为 O(N), 额外空间复杂度为O(M)；
    3. 应用范围有限，需要样本的数据状况满足桶的划分；
"""
from collections import defaultdict
def func1(lis):
    _n = len(str(lis))
    for i in range(_n):
        lis = func2(lis, _n = i)
    return lis

def func2(lis, _n):
    num = 10 ** _n
    count = defaultdict(list)
    for l in lis:
        count[l % num].append(l)
    
    keys = count.keys()
    lis = []
    for k in range(min(keys), max(keys) + 1):
        lis.extend(count.get(k, [])[::-1])
    return lis

lis = [22, 13, 41, 52, 45, 44, 21, 6, 91, 101]
print(func1(lis))
