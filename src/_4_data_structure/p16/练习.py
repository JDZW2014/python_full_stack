# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-05-03
Description :
auther : wcy
"""
# import modules
import os

__all__ = []


# define function
def main1():
    print("--- 1. 一共有多少种凑法 ---")
    """
    【题目】
        面值： [3， 5， 10， 2]
        凑成 100， 每个面值可以重复使用
        一共有多少种凑法
    """
    def func(lis, idx, num, cache):
        _key = f"{idx}_{num}"
        if _key in cache:
            return cache[_key]
        method_num = 0

        if idx == len(lis):
            if num == 0:
                method_num += 1
        else:
            for i in range(num // lis[idx] + 1):
                method_num += func(lis, idx=idx+1, num=num-i * lis[idx], cache=cache)
        cache[_key] = method_num
        return method_num

    lis = [3, 5, 10, 2]
    num = 100
    num = 10
    cache = {}
    print(func(lis, 0, num, cache))


def main2():
    print("--- 2. 问，组成aim 最少需要多少硬币 ---")
    """
    【问题】：
        data_list = [2, 3, 5, 7, 3]
        aim = 10
        问，组成aim 最少需要多少硬币
    """
    def func(lis, idx, aim, cache):
        _key = f"{idx}_{aim}"
        if _key in cache:
            return cache[_key]

        if idx == len(lis):
            if aim == 0:
                min_num = 0
            else:
                min_num = 9999999999
        else:
            min_num1 = func(lis=lis, idx=idx+1, aim=aim-lis[idx], cache=cache) + 1
            min_num2 = func(lis=lis, idx=idx+1, aim=aim, cache=cache)
            min_num = min(min_num1, min_num2)
        cache[_key] = min_num
        return min_num

    lis = [2, 3, 5, 7, 3]
    aim = 10
    aim = 9
    cache = {}
    print(func(lis=lis, idx=0, aim=aim, cache=cache))


def main3():
    print("--- 3. 求 s1 和 s2 的最长公共子串 ---")
    """
    s1 = '1AB2345ACD'
    s2 = '12345EF'
    求 s1 和 s2 的最长公共子串
    """
    def func(s1, s2, idx1, idx2, cache):
        _key = f"{idx1}_{idx2}"
        if _key in cache:
            return cache[_key]
        if idx1 < 0 or idx2 < 0:
            max_len = 0
        else:
            if s1[idx1] == s2[idx2]:
                max_len = func(s1, s2, idx1-1, idx2-1, cache) + 1
            else:
                func(s1, s2, idx1 - 1, idx2, cache)
                func(s1, s2, idx1, idx2 - 1, cache)
                max_len = 0
        cache[_key] = max_len
        return max_len

    s1 = '1AB2345ACD'
    s2 = '12345EF'
    cache = {}
    func(s1=s1, s2=s2, idx1=len(s1) - 1, idx2=len(s2) - 1, cache=cache)
    print(max(cache.values()))


def main4():
    print("--- 4. 求s1 和 s2 的最长公共子序列 ---")
    """
    s1 = '1AB2345ACDF'
    s2 = 'AQ24CFF'
    求s1 和 s2 的最长公共子序列
    """
    def func(s1, s2, idx1, idx2, cache):
        _key = f"{idx1}_{idx2}"
        if _key in cache:
            return cache[_key]

        if idx1 < 0 or idx2 < 0:
            max_len = 0
        else:
            if s1[idx1] == s2[idx2]:
                max_len = func(s1, s2, idx1-1, idx2-1, cache) + 1
            else:
                max_len = max(func(s1, s2, idx1-1, idx2, cache), func(s1, s2, idx1, idx2-1, cache))

        cache[_key] = max_len
        return max_len

    s1 = '1AB2345ACDF'
    s2 = 'AQ24CFF'
    cache = {}
    print(func(s1, s2, len(s1)-1, len(s2)-1, cache))


def main5():
    print("--- 5. 求 lis 的 最长上升子序列 ---")
    """
    lis = [100, 1, 6, 2, 5, 3, 4, 7, 2, 9, 1]
    求 lis 的 最长上升子序列
    """
    def func(lis, idx, cache):
        _key = idx
        if idx in cache:
            return cache[_key]

        max_len = 0
        if idx == 0:
            max_len = 1
        else:
            for i in range(idx):
                l = func(lis=lis, idx=i, cache=cache)
                if lis[idx] > lis[i] and l + 1 > max_len:
                    max_len = l + 1
            if 1 > max_len:
                max_len = 1
        cache[_key] = max_len
        return max_len
    lis = [100, 1, 6, 2, 5, 3, 4, 7, 2, 9, 1]
    cache = {}
    func(lis=lis, idx=len(lis)-1, cache=cache)
    print(max(cache.values()))


def main6():
    print("--- 6.KMP ---")
    """
    kmp:
        string1 是否包含 string2
    """
    class KMP(object):
        def __init__(self, s1, s2):
            self.s1 = s1
            self.s2 = s2
            self.s2_lis = self.prepare_s2(self.s2)

        @staticmethod
        def prepare_s2(s):
            pass


def main7():
    print("--- 7. manacher ---")
    pass


def main8():
    print("--- 8. 单调栈 ---")
    pass


def main9():
    print("--- 9. 打印一个字符串的全部子序列，包括空字符串 ---")
    def func(s, idx):
        lis = list()
        if idx == -1:
            lis.append('')
        else:
            lis.extend(func(s, idx=idx-1))
            n_lis = [f"{s[idx]}{_}" for _ in lis]
            lis = lis + n_lis
        return lis

    s = 'aabc'
    print(func(s, idx=len(s) - 1))


def main10():
    print("--- 10. 打印一个字符串的全排列， 没有重复排列 ---")
    def func(s, idx):
        if idx == len(s):
            print("".join(s))
        else:
            for i in range(idx, len(s)):
                if s[idx] != s[i]:
                    s[idx], s[i] = s[i], s[idx]
                    func(s, idx+1)
                    s[idx], s[i] = s[i], s[idx]
            func(s, idx+1)

    s = list('aabc')
    func(s=s, idx=0)


# main
if __name__ == '__main__':
    main1()
    main2()
    main3()
    main4()
    main5()
    main6()
    main7()
    main8()
    main9()
    main10()
