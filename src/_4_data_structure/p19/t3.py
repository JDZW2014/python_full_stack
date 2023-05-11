# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-09-06
Description :
auther : wcy
"""
# import modules
import os
import typing

__all__ = []


# define function
def func1(lis: typing.List[int]):
    """
    预处理的技巧，把一些需要反复呗调用到的过程进行预处理，降低整体的复杂度
    左全0 右全1
    """
    num_0 = 0
    num_1 = 0

    pre_cal_lis = []
    for i in lis:
        if i == 0:
            num_0 += 1
        elif i == 1:
            num_1 += 1
        else:
            raise ValueError("get wrong element")
        pre_cal_lis.append((num_0, num_1))

    # 如果在第一个数字的左边
    change_num_list = [(-1, pre_cal_lis[-1][0])]

    for i in range(len(lis)):
        cm = pre_cal_lis[i][1] + pre_cal_lis[-1][0] - pre_cal_lis[i][0]
        change_num_list.append((i, cm))
    return change_num_list



# define main
def main1():
    lis = [0, 1, 0, 1, 1]
    print(lis, ' ', func1(lis=lis))
    pass


# main
if __name__ == '__main__':
    main1()
