# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-28
Description :
auther : wcy
"""
# import modules
import os

__all__ = []


# define class
class KMP(object):
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.prefix_len_list = self._get_max_prefix()

    def _get_max_prefix(self, ):
        idx = 0
        s_len = len(self.str2)

        prefix_len_list = list()
        while idx < s_len:
            if idx < 3:
                prefix_len_list.append(idx-1)
            else:
                prefix_idx = idx-1
                self.__get_max_prefix__(prefix_len_list, prefix_idx, idx)
            idx += 1
        return prefix_len_list

    def __get_max_prefix__(self, prefix_len_list, prefix_idx, idx):
        # base case
        if prefix_idx == 0:
            if self.str2[0] == self.str2[idx-1]:
                prefix_len_list.append(1)
            else:
                prefix_len_list.append(0)
        # 递归调用
        else:
            if self.str2[prefix_len_list[prefix_idx]] == self.str2[idx - 1]:
                prefix_len_list.append(prefix_len_list[prefix_idx] + 1)
            else:
                prefix_idx = prefix_len_list[prefix_idx]
                self.__get_max_prefix__(prefix_len_list, prefix_idx, idx)

    def call(self, ):
        idx1 = 0
        idx2 = 0
        s1_len = len(self.str1)
        s2_len = len(self.str2)

        while idx1 < s1_len and idx2 < s2_len:
            if self.str1[idx1] == self.str2[idx2]:
                idx1 += 1
                idx2 += 1
            else:
                idx2 = self.prefix_len_list[idx2]
                if idx2 < 0:
                    idx1 += 1
                    idx2 = 0

        return idx2 == s2_len


# define function
def manacher(s):
    s = "#" + "#".join(list(s)) + "#"
    idx = 0
    s_len = len(s)
    boundary_center = -1
    boundary_right = -1

    result_list = []
    while boundary_right < s_len:
        if idx == 0:
            result_list.append(1)
            boundary_center = idx
            boundary_right = 1

        elif idx == 1:
            result_list.append(2)
            boundary_center = idx
            boundary_right = 3
        else:
            start = min(idx + result_list[2 * boundary_center - idx], boundary_right)
            while start < s_len:
                n_idx = 2 * idx - start
                if n_idx >= s_len:
                    break
                if s[start] == s[n_idx]:
                    boundary_center = idx
                    boundary_right = start
                    start += 1
                else:
                    break
                result_list.append(start-idx)
        idx += 1
        if idx > boundary_right:
            boundary_right = idx

    return max(result_list) // 2




# define main
def main1():
    s1 = "abcxyabcxzz"
    s2 = 'abcdgabcddfabcdgabcdghy'
    kmp = KMP(str1=s1, str2=s2)
    print(kmp.prefix_len_list)

    s1 = "abcxyabcxzz"
    s2 = 'cxz'
    print(KMP(s1, s2).call())
    s3 = 'cxa'
    print(KMP(s1, s3).call())


def main2():
    s = 'abcbdbcbxyz'
    print(manacher(s))


# main
if __name__ == '__main__':
    main1()
    main2()
