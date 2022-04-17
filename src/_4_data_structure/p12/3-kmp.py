# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-17
Description :
auther : wcy
"""
# import modules
import os

__all__ = []


# define class
class KMP(object):
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
        self.prefix_suffix_match_len = self.get_prefix_suffix_match_len(self.s2)

    @staticmethod
    def get_prefix_suffix_match_len(s):
        ret_list = []
        i = 0

        s_len = len(s)
        while i < s_len:
            if i == 0:
                ret_list.append(-1)
            elif i == 1:
                ret_list.append(0)
            elif i == 2:
                if s[0] == s[1]:
                    ret_list.append(1)
                else:
                    ret_list.append(0)
            else:
                KMP._get_prefix_suffix_match_len_(s=s, idx=i, ret_list=ret_list)
            i += 1
        return ret_list

    @staticmethod
    def _get_prefix_suffix_match_len_(s, idx, ret_list):
        c2_idx = idx - 1
        c1_idx = ret_list[c2_idx]
        while True:
            if s[c2_idx] == s[c1_idx]:
                ret_list.append(c1_idx + 1)
                break
            else:
                c1_idx = ret_list[c1_idx]
                if c1_idx < 0:
                    ret_list.append(0)
                    break

    def call(self):
        len_s1 = len(self.s1)
        len_s2 = len(self.s2)

        if len_s2 > len_s1:
            return 0

        idx1 = 0
        idx2 = 0

        while idx1 < len_s1 and idx2 < len_s2:
            if self.s1[idx1] == self.s2[idx2]:
                idx1 += 1
                idx2 += 1
            else:
                idx2 = self.prefix_suffix_match_len[idx2]
                if idx2 < 0:
                    idx1 += 1
                    idx2 = 0

        return idx2 == len_s2


# main
if __name__ == '__main__':
    s1 = "abcxyabcxzz"
    s2 = 'cxz'
    print(KMP(s1, s2).call())
    s3 = 'cxa'
    print(KMP(s1, s3).call())
