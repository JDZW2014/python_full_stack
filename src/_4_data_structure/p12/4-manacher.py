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


# define function
def manacher(s):
    s = "#" + "#".join(list(s)) + "#"
    s_len = len(s)

    pali_arr = []
    idx = 0
    most_right_idx = 0
    while idx < s_len:
        if idx == 0:
            pali_arr.append(1)
            most_right_idx = idx + pali_arr[-1]
            most_center_idx = idx
            idx += 1
        elif idx == 1:
            pali_arr.append(2)
            most_right_idx = idx + pali_arr[-1]
            most_center_idx = idx
            idx += 1
        else:
            idx, most_right_idx, most_center_idx = _manacher_(s=s, idx=idx, most_right_idx=most_right_idx,
                                                         most_center_idx=most_center_idx, pali_arr=pali_arr)

    return pali_arr


def _manacher_(s, idx, most_right_idx, most_center_idx, pali_arr):
    len_s = len(s)
    r2 = max(idx + pali_arr[most_center_idx - (idx-most_center_idx)], most_right_idx)
    r1 = idx - (r2 - idx)
    r = r2 - idx

    while r1 >= 0 and r2 < len_s:
        if s[r1] == s[r2]:
            r1 -= 1
            r2 += 1
            r += 1
            most_right_idx += 1
            most_center_idx = idx
        else:
            break

    pali_arr.append(r)
    idx += 1
    return idx, most_right_idx, most_center_idx


# main
if __name__ == '__main__':
    s = 'abcbd'
    print(manacher(s))