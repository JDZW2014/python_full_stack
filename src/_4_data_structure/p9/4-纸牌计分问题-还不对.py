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
def func(lis, a_score, b_score):
    if len(lis) == 2:
        if lis[0] > lis[1]:
            a_score += lis[0]
            b_score += lis[1]
        else:
            a_score += lis[1]
            b_score += lis[0]
        print(a_score, '', b_score)

    else:
        a = lis[0]
        b = lis[1]
        c = lis[-2]
        d = lis[-1]

        if min(a-b, a-d) > min(d-c, d-a):
            a_score += lis.pop(0)
            if a-b > a-d:
                b_score += lis.pop()
            else:
                b_score += lis.pop(0)
        else:
            a_score += lis.pop()
            if d-c > d-a:
                b_score += lis.pop()
            else:
                b_score += lis.pop(0)
        func(lis, a_score, b_score)


# # 暴力递归的写法
# def func2(lis, left, right):
#
#     a_score = func2(lis, left=left+1, right=right) + lis[left]
#

def funca(lis, left, right):
    if left == right:
        return lis[left]

    a_score1 = funca(lis, left+1, right) + lis[left]
    b_score1 = funcb(lis, left+1, right)

    a_score2 = funca(lis, left, right-1) + lis[right]
    b_score2 = funcb(lis, left, right-1)

    if a_score1 - b_score1 > a_score2 - b_score2:
        print("left")
        return a_score1
    else:
        print("right")
        return a_score2


def funcb(lis, left, right):
    if left == right:
        return lis[left]

    b_score1 = funcb(lis, left+1, right) + lis[left]
    a_score1 = funca(lis, left+1, right)

    b_score2 = funcb(lis, left, right-1) + lis[right]
    a_score2 = funca(lis, left, right-1)
    if b_score1 - a_score1 > b_score2 - a_score2:
        print("left")
        return b_score1
    else:
        print("right")
        return b_score2


# main
if __name__ == '__main__':
    # lis = [1, 2, 100, 4]
    # func(lis, a_score=0, b_score=0)
    lis = [1, 2, 100, 4]
    print(funca(lis, 0, len(lis)-1))

