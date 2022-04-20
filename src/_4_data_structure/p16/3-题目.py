# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-20
Description :
auther : wcy
【题目】
    面值： [3， 5， 10， 2]
    凑成 100， 每个面值可以重复使用
    一共有多少种凑法
"""
# import modules
import os

__all__ = []


# define function
def func1(data_list, aim, idx1, idx1_max):
    if aim < 0:
        return 0

    val = 0
    # final case
    if idx1 == idx1_max:
        if aim == 0:
            val += 1
    else:
        for i in range(aim // data_list[idx1]+1):
            n_aim = aim-data_list[idx1] * i
            val += func1(data_list, aim=n_aim, idx1=idx1+1, idx1_max=idx1_max)
    return val


# main
if __name__ == '__main__':
    data_list = [3, 5, 10, 2]
    aim = 10
    idx1 = 0
    idx2 = 0
    print(func1(data_list=data_list, aim=aim, idx1=idx1, idx1_max=len(data_list)))
