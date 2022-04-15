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
def func(num, start, end, other):
    if num == 1:
        print(f"移动 {num} {start} -> {end}")
    else:
        func(num=num-1, start=start, end=other, other=end)
        print(f"移动 {num} {start} -> {end}")
        func(num=num-1, start=other, end=end, other=start)


# main
if __name__ == '__main__':
    func(num=3, start="start", end="end", other="other")
