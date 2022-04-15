# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-15
Description :
 100 亿条url 的黑名单，设置一个过滤器，可以有误判，但是误判率要比较低
auther : wcy
"""
# import modules
import os
import hashlib

__all__ = []


# define class
class BitArr(object):
    INT_LEN = 32
    __slots__ = ("data", "total_len")

    def __init__(self, int_num):
        self.data = [0, ] * int_num
        self.total_len = int_num * self.INT_LEN

    def _idx_(self, num):
        num = num % self.total_len
        idx1 = num // self.INT_LEN
        idx2 = num % self.INT_LEN
        return int(idx1), int(idx2)

    def insert(self, num):
        idx1, idx2 = self._idx_(num=num)
        self.data[idx1] = self.data[idx1] | 1 << idx2

    def get(self, num):
        idx1, idx2 = self._idx_(num=num)
        return bool(self.data[idx1] >> idx2 & 1)


class BloomFilter(object):
    def __init__(self, int_num):
        self.bit_arr = BitArr(int_num=int_num)

    def update(self, s: str):
        hash_int = self._get_hash_int_(s=s)
        self.bit_arr.insert(hash_int)

    @staticmethod
    def _get_hash_int_(s) -> int:
        md5 = hashlib.md5()
        md5.update(s.encode("utf8"))
        return int(md5.hexdigest(), 16)

    def query(self, s):
        hash_int = self._get_hash_int_(s=s)
        return self.bit_arr.get(num=hash_int)


# main
if __name__ == '__main__':
    bf = BloomFilter(int_num=10)
    for s in ["a", "b", "c", "ac", "abc"]:
        bf.update(s)

    print(bf.query("ac"))
    print(bf.query("acb"))



