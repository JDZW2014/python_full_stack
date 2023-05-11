# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-09-06
Description :
auther : wcy
"""
# import modules
import os
import numpy as np

__all__ = []


# define function
def func1(arr: np.ndarray):
    """
    预处理的技巧
    """
    hang_pre_deal: np.ndarray = func1_pre_deal_hang(arr=arr)
    print(hang_pre_deal)
    lie_pre_deal: np.ndarray = func1_pre_deal_lie(arr=arr)
    print(lie_pre_deal)

    hang_num = arr.shape[0]
    lie_num = arr.shape[1]

    max_width = 0
    for h in range(hang_num):
        for l in range(lie_num):
            w = min(hang_pre_deal[h, l], lie_pre_deal[h, l]) - 1
            if w > 0 and hang_pre_deal[h + w, l] > w and lie_pre_deal[h, l + w] > w:
                max_width = max(w, max_width)
    return max_width + 1


def func1_pre_deal_hang(arr: np.ndarray):
    # 存储结果的array
    result_arr = np.zeros_like(arr)

    hang_num = arr.shape[0] - 1
    while hang_num >= 0:
        lie_num = arr.shape[1] - 1

        # 在每一行的末尾 添加初始值
        if arr[hang_num, lie_num] == 0:
            result_arr[hang_num, lie_num] = 0
        else:
            result_arr[hang_num, lie_num] = 1
        lie_num -= 1

        while lie_num >= 0:
            if arr[hang_num, lie_num] == 0:
                result_arr[hang_num, lie_num] = 0
            else:
                result_arr[hang_num, lie_num] = result_arr[hang_num, lie_num + 1] + 1
            lie_num -= 1

        hang_num -= 1
    return result_arr


def func1_pre_deal_lie(arr: np.ndarray):
    # 存储结果的array
    result_arr = np.zeros_like(arr)

    lie_num = arr.shape[1] - 1
    while lie_num >= 0:
        hang_num = arr.shape[1] - 1

        # 在每一列的末尾 添加初始值
        if arr[lie_num, hang_num] == 0:
            result_arr[hang_num, lie_num] = 0
        else:
            result_arr[hang_num, lie_num] = 1
        hang_num -= 1

        while hang_num >= 0:
            if arr[hang_num, lie_num] == 0:
                result_arr[hang_num, lie_num] = 0
            else:
                result_arr[hang_num, lie_num] = result_arr[hang_num + 1, lie_num] + 1
            hang_num -= 1

        lie_num -= 1
    return result_arr


# define main
def main():
    arr = np.array([[0, 1, 1, 1, 1],
                    [0, 1, 0, 0, 1],
                    [0, 1, 0, 0, 1],
                    [0, 1, 1, 1, 1],
                    [0, 1, 1, 0, 1]])
    print(func1(arr=arr))


# main
if __name__ == '__main__':
    main()
