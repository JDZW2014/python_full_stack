# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-21
Description :
auther : wcy
"""
# import modules
import os
from collections import defaultdict


__all__ = []


# define function
def func1(data_list):
    """
    计数排序
    """

    pass


def func2(data_list):
    """
    基数排序
    """
    idx = 0
    max_idx = len(str(max(data_list)))
    while idx < max_idx:
        _map = defaultdict(list)

        for data in data_list:
            _map[_get_val_(idx=idx, num=data)].append(data)

        data_list = []
        for i in range(10):
            for data in _map[i]:
                data_list.append(data)
        idx += 1
    return data_list


def _get_val_(idx, num):
    s = str(num)
    if len(s) > idx:
        return int(s[len(s)-idx-1])
    else:
        return 0


# main
if __name__ == '__main__':
    data_list = [2, 3, 1, 5, 3, 6]
    print(func1(data_list=data_list))

    data_list = [102, 13, 101, 52, 39, 601]
    print(func2(data_list=data_list))
