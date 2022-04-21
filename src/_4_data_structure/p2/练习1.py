# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-21
Description :
auther : wcy
"""
# import modules
import os, typing

__all__ = []


# define function
def func1(data_list, left, right, val):
    """
    二分查找
    """
    if left >= right:
        return None
    mid = (left + right) // 2
    if data_list[mid] == val:
        return mid
    elif data_list[mid] > val:
        return func1(data_list=data_list, left=left, right=mid, val=val)
    else:
        return func1(data_list=data_list, left=mid+1, right=right, val=val)


def func2():
    """
    异或运算可以简单的即为无进位相加

    题目: 有一个arr, 其中只有一个数出现了奇数次，剩下的数出现了偶数次：
            a. 如何找到这个数？
            b. 如果有两数出现了奇数次呢？
        要求: 时间复杂度O(n), 空间复杂度 O(1)
    """
    pass


def func3(data_list: typing.List[int]):
    """
    小和问题：[1,2,4,3]
    1 的小和为 0
    2 的小和为 1
    4 的小和为 1+2=3
    ...
    所以这些数的和为最终的小和值， 要求时间复杂度为 O(N * log N)
    """
    sum = 0
    if len(data_list) <= 1:
        return sum, data_list
    else:
        mid = len(data_list) // 2
        sum1, data_list1 = func3(data_list=data_list[0: mid])
        sum2, data_list2 = func3(data_list=data_list[mid:])

        sum += sum1
        sum += sum2

        idx1 = 0
        idx2 = 0
        data_list = []
        while idx1 < len(data_list1) and idx2 < len(data_list2):
            if data_list1[idx1] < data_list2[idx2]:
                data_list.append(data_list1[idx1])
                sum += data_list1[idx1] * (len(data_list2) - idx2)
                idx1 += 1
            else:
                data_list.append(data_list2[idx2])
                idx2 += 1

        while idx1 < len(data_list1):
            data_list.append(data_list1[idx1])
            idx1 += 1

        while idx2 < len(data_list2):
            data_list.append(data_list2[idx2])
            idx2 += 1

        return sum, data_list


# main
if __name__ == '__main__':
    data_list = [1, 1, 2, 2, 3, 6, 7, 10, 101]
    val = 7
    print(func1(data_list=data_list, left=0, right=len(data_list), val=val))

    data_list = [1, 2, 4, 3]
    print(func3(data_list=data_list))
