# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2023/5/7
Description :
auther : wcy
"""
# import modules
import os

__all__ = []


# define function
def func1(n: list, f, m, e):
    """
    汉诺塔问题
    :return:
    """
    # 递归的终止条件
    if len(n) == 1:
        print(f"{n[0]}, {f} -> {e}")
        return

    # 递归调用
    func1(n=n[1:], f=f, m=e, e=m)
    print(f"{n[0]}, {f} -> {e}")
    func1(n=n[1:], f=m, m=f, e=e)

def func2(s):
    """
    字符子序列：打印一个字符串的全部子序列
    :return:
    """
    if len(s) == 0:
        return ['']

    ret_list = []
    for res in func2(s[1:]):
        ret_list.append('' + res)
        ret_list.append(s[0] + res)
    return ret_list

def func3(word_list, start=0):
    """
    字符串的全排列
    :return:
    """
    if start == len(word_list) - 1:
        print("".join(word_list))
        return

    for i in range(start, len(word_list)):
        word_list[start], word_list[i] = word_list[i], word_list[start]
        print(f"change: {start} {i}")
        func3(word_list, start=start+1)
        word_list[start], word_list[i] = word_list[i], word_list[start]

def func4_a(arr, start, end):
    """
    纸牌计分问题
    :return:
    """
    # 递归终止条件
    if (end - start) == 1:
        return arr[start], 0


    # 递归调用
    a_score_l, b_score_l = func4_b(arr=arr, start=start+1, end=end)
    a_score_r, b_score_r = func4_b(arr=arr, start=start, end=end-1)

    a_score_l = a_score_l + arr[start]
    a_score_r = a_score_r + arr[end-1]

    if a_score_l >= a_score_r:
        return a_score_l, b_score_l
    else:
        return a_score_r, b_score_r

def func4_b(arr, start, end):
    # 递归终止条件
    if (end - start) == 1:
        return 0, arr[start]

    # 递归调用
    a_score_l, b_score_l = func4_a(arr=arr, start=start + 1, end=end)
    a_score_r, b_score_r = func4_a(arr=arr, start=start, end=end - 1)

    b_score_l = b_score_l + arr[start]
    b_score_r = b_score_r + arr[end - 1]

    if b_score_l >= b_score_r:
        return a_score_l, b_score_l
    else:
        return a_score_r, b_score_r


def main1():
    func1(n=list(range(3)), f='a', m='b', e='c')

def main2():
    ret = func2(s='abc')
    print(ret)

def main3():
    func3(word_list=["a", "b", "c"], start=0)

def main4():
    arr = [1, 2, 100, 4]
    ret = func4_a(arr, start=0, end=len(arr))
    print(ret)


# main
if __name__ == '__main__':
    main4()
