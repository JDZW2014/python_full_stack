# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2023/5/7
Description :
auther : wcy
"""
# import modules
import os
import numpy as np

__all__ = []


# define class
class KMP(object):
    def __init__(self):
        pass

    @staticmethod
    def kmp(raw_s, patt_s):
        """
        kmp 字符串匹配
        :param raw_s:
        :param p_s:
        :return:
        """
        # 获取 patt_s 字符串的next arr
        p_next_arr = KMP.get_next_arr(patt_s)
        print(f"patt_s = {patt_s}, p_next_arr = {p_next_arr}")

        # 基于next arr 进行字符串匹配
        match_pos_list = []
        r_idx = 0
        p_idx = 0
        while r_idx < len(raw_s):
            if raw_s[r_idx] == patt_s[p_idx]:
                r_idx += 1
                p_idx += 1
            else:
                while True:
                    p_idx = p_next_arr[p_idx]
                    if raw_s[r_idx] == patt_s[p_idx]:
                        r_idx += 1
                        p_idx += 1
                        break

                    if p_idx <= 0:
                        r_idx += 1
                        p_idx = 0

                        break

            if p_idx == len(patt_s):
                match_pos_list.append(r_idx-len(patt_s))
                p_idx = 0

        return match_pos_list

    @staticmethod
    def get_next_arr(s: str):
        next_arr = list()
        for i in range(len(s)):
            if i == 0:
                next_arr.append(-1)
            elif i == 1:
                next_arr.append(0)
            elif i == 2:
                if s[0] == s[1]:
                    next_arr.append(1)
                else:
                    next_arr.append(0)
            else:
                nr_idx = next_arr[-1]
                while True:
                    if s[nr_idx] == s[i-1]:
                        next_arr.append(nr_idx+1)
                        break
                    else:
                        nr_idx = next_arr[nr_idx]
                        if nr_idx < 0:
                            next_arr.append(0)
                            break
        return next_arr


class Manacher(object):
    def __init__(self):
        pass

    @staticmethod
    def manacher(s: str):
        s = "#" + "#".join(list(s)) + "#"
        print(list(s))

        ret_arr = []
        idx = -1

        max_right = 2
        max_right_center = 1

        while idx < len(s):
            idx += 1
            if idx == 0:
                ret_arr.append(0)
                continue
            elif idx == 1:
                ret_arr.append(1)
                continue
            else:
                # 根据max_right_center 取到 对称位置取到的回文值
                idx_lll = max_right_center - (idx - max_right_center)
                # 对称位置的回文半径
                idx_lll_r = ret_arr[idx_lll]

                # todo 这个逻辑有问题，当 小于 r 的时候，不需要计算，知道当 > r 是才需要继续判断后续是否对称
                # 不需要处理的位置
                deal_start_pos = min(max_right, idx + idx_lll_r)
                # 起始半径
                r = deal_start_pos - idx

                # 开始处理的位置
                l_r_p = idx - r - 1
                r_r_p = idx + r + 1

                while l_r_p >= 0 and r_r_p < len(s):
                    if s[l_r_p] == s[r_r_p]:
                        # 相同，扩大半径
                        r += 1
                        l_r_p -= 1
                        r_r_p += 1
                    else:
                        break

                ret_arr.append(r)
                if (idx + r) > max_right:
                    max_right = idx + r
                    max_right_center = idx

        return ret_arr


# class Data(object):
#     def __init__(self, val, idx):
#         self.val = val
#         self.idx = idx


# define function
def func3(lis: list, window=3):
    """
    双端队列
    :return:
    """
    res = []
    d_q = []
    while lis:
        # 取出一个值
        val = lis.pop(0)

        # 将这个值更新到双端队列
        while d_q and val >= d_q[-1]:
            d_q.pop(-1)

        if len(d_q) > 3:
            d_q.pop(0)

        d_q.append(val)
        print(d_q)
        res.append(d_q[0])

    return res


def func4(lis: list):
    """
    单调栈1
    :return:
    """
    ret_list = []
    stack = list()

    # 在弹出栈时记录结果
    while lis:
        val = lis.pop(0)
        if len(stack) == 0:
            stack.append(val)
        else:
            while stack and val < stack[-1]:
                pop_val = stack.pop(-1)
                if len(stack) > 0:
                    ret_list.append((pop_val, stack[-1], val))
                else:
                    ret_list.append((pop_val, None, val))
            stack.append(val)

    while stack:
        pop_val = stack.pop(-1)

        if len(stack) > 0:
            ret_list.append((pop_val, stack[-1], None))
        else:
            ret_list.append((pop_val, None, None))
    return ret_list


def func5():
    """
    单调栈2
    :return:
    """
    pass


def func6():
    """
    实现一个栈，可以pop 和 push，返回 min O(1)
    :return:
    """
    pass


def func7(s1, s2, arr: np.ndarray):
    """
    返回两个字符串的最长公共子串

    最长公共子串 用 打表分析 更加容易理解
    :return:
    """
    for i in range(0, len(s2)):
        for j in range(0, len(s1)):
            if s2[i] == s1[j]:
                arr[i+1, j+1] = arr[i, j] + 1
            else:
                arr[i + 1, j + 1] = 0
    return arr


def func8(s1, s2, arr: np.ndarray):
    """
    返回两个字符串的最长公共子序列

    用打表推到更容易理解这个逻辑
    :return:
    """
    for i in range(len(s2)):
        for j in range(len(s1)):

            if s2[i] == s1[j]:
                arr[i+1, j+1] = arr[i, j] + 1
            else:
                arr[i+1, j+1] = max(arr[i, j+1], arr[i+1, j])

    return arr



def func9_bf(lis, arr: np.ndarray):
    """
    暴力打表
    :return:
    """
    for i in range(len(lis)):
        for j in range(len(lis)):
            if i < j:
                _func9_bf(lis[i:j])

    pass


def _func9_bf(lis):
    """
    暴力求上升子串
    :param lis: 
    :return: 
    """
    pass


def func9(lis: list, arr: np.ndarray):
    """
    返回最长上升子串
    :return:
    """
    for i in range(len(lis)):
        for j in range(len(lis)):
            if j < i:
                if lis[i] > lis[j]:
                    arr[i+1, j+1] = arr[i, j] + 1
                else:
                    arr[i+1, j+1] = arr[i, j]

    return arr


# define main
def main1():
    kmp = KMP()
    patt_s = 'abacabac'
    next_arr = kmp.get_next_arr(patt_s)
    print(patt_s, next_arr)

    raw_s = "abfffabacabacabzzzz"
    res = kmp.kmp(raw_s=raw_s, patt_s=patt_s)
    print(f"raw_s = {raw_s}")
    print(f"patt_s = {patt_s}")
    print(f"res = {res}")


def main2():
    mac = Manacher()
    s = "zabbabbcf"
    s = "abba"

    print(mac.manacher(s=s))


def main3():
    lis = [3, 2, 4, 1, 2, 6, 0, 1, 7]
    print(lis)
    print(func3(lis=lis, window=3))


def main4():
    lis = [1, 5, 4, 3, 7, 6, 9, 10]
    ret = func4(lis=lis.copy())
    print(lis)
    print(ret)


def main7():
    print("公共子串")
    s1 = '1AB2345ACD'
    s2 = '12345EF'
    arr = np.random.random(( len(s2)+1, len(s1)+1))
    arr[:, :] = 0
    ret = func7(s1=s1, s2=s2, arr=arr)
    print(f"s1 = {s1}, s2 = {s2}, ret = {ret}")


def main8():
    print("公共子序列")
    s1 = '1AB2345ACD'
    s2 = '12345EF'
    arr = np.random.random((len(s2) + 1, len(s1) + 1))
    arr[:, :] = 0
    ret = func8(s1=s1, s2=s2, arr=arr)
    print(f"s1 = {s1}, s2 = {s2}, ret = \n{ret}")


def main9():
    print("最长递增子序列")
    lis = [1, 6, 2, 5, 3, 4, 7, 2, 9, 1]
    lis.append(1000)
    arr = np.random.random((len(lis)+1, len(lis)+1))
    arr[:, :] = 0
    ret = func9(lis=lis, arr=arr)
    print(f"lis = \n{lis}, ret = \n{ret}")


# main
if __name__ == '__main__':
    main9()
