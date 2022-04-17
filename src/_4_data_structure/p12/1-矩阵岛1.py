# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-15
Description :
auther : wcy
"""
# import modules
import os, typing

__all__ = []


# define function
def func(m: typing.List[typing.List[int]]):
    island_num = 0

    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 1:
                island_num += 1
                _func_(m, i, j)
    print(m)
    return island_num


def _func_(m, i, j):
    if m[i][j] == 1:
        m[i][j] = 2
        _func_(m, i-1, j)
        _func_(m, i+1, j)
        _func_(m, i, j-1)
        _func_(m, i, j+1)


# define test
def main():
    m = [
        [0, 0, 1, 0, 1, 0],
        [1, 1, 1, 0, 1, 0],
        [1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    island_num = func(m=m)
    print(island_num)


# main
if __name__ == '__main__':
    main()
