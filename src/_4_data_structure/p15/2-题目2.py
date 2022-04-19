# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-19
Description :
auther : wcy
【问题】：
    data_list = [2, 3, 5, 7, 3]
    aim = 10
    问，组成aim 最少需要多少硬币

"""
# import modules
import os
import numpy as np

__all__ = []


# define function
def func2(data_list, l_idx, r_idx, aim, idx, arr_map):
    if aim < 0:
        return -1, False

    # 有缓存用缓存
    v = arr_map[aim, idx]
    if v != -2:
        return v, v != -1

    # 没缓存，补充缓存
    if idx == r_idx:
        f_success = aim == 0
        if f_success:
            f_num = 0
        else:
            f_num = -1
    else:
        # 不要当前数值
        num1, success1 = func2(data_list=data_list, l_idx=l_idx, r_idx=r_idx, aim=aim, idx=idx + 1, arr_map=arr_map)

        # 要当前数值
        num2, success2 = func2(data_list=data_list, l_idx=l_idx, r_idx=r_idx, aim=aim - data_list[idx], idx=idx + 1, arr_map=arr_map)
        num2 += 1

        if success1 and success2:
            f_success = success1
            f_num = min(num1, num2)
        else:
            if success1:
                f_success = success1
                f_num = num1
            elif success2:
                f_success = success2
                f_num = num2
            else:
                f_success = success1
                f_num = -1
    arr_map[aim, idx] = f_num
    return f_num, f_success


def func2(data_list, l_idx, r_idx, aim, idx, arr_map):
    # todo not finish
    pass


# main
if __name__ == '__main__':
    data_list = [2, 3, 5, 7, 3, 10]
    aim = 1
    arr = np.ones(shape=(aim + 1, len(data_list)+1)) * -2
    print(func2(data_list=data_list, l_idx=0, r_idx=len(data_list), aim=aim, idx=0, arr_map=arr))
