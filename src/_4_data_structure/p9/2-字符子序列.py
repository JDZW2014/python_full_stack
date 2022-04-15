# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-14
Description :
auther : wcy
"""
# import modules
import os

__all__ = []


# define function
def func(s: str):
    if len(s) == 0:
        print(s)
        return [s]

    sub_s_list = func(s[1:])
    new_sub_s_list = list()
    for sub_s in sub_s_list:
        new_sub_s_list.append(sub_s)
        new_sub_s_list.append(s[0] + sub_s)

    return new_sub_s_list


# main
if __name__ == '__main__':
    print(func(s="abc"))
    print(func(s="acsda"))
