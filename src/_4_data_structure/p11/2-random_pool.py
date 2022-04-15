# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-15
Description :
auther : wcy
"""
# import modules
import os, random

__all__ = []


# define class
class RandomPool(object):
    def __init__(self):
        self.key_to_idx = {}
        self.idx_to_key = {}
        self.size = 0

    def insert(self, k):
        if k not in self.key_to_idx:
            self.key_to_idx[k] = self.size
            self.idx_to_key[self.size] = k
            self.size += 1

    def delete(self, k):
        if k in self.key_to_idx:
            d_idx = self.key_to_idx[k]

            l_idx = self.size - 1
            l_key = self.idx_to_key[l_idx]

            self.key_to_idx.pop(k)
            self.idx_to_key.pop(l_idx)

            if k != l_key:
                self.key_to_idx[l_key] = d_idx
                self.idx_to_key[d_idx] = l_key
                self.size -= 1

    def random_get(self):
        idx = int(random.random() * self.size)
        return self.idx_to_key[idx]


# main
if __name__ == '__main__':
    rp = RandomPool()
    for k in ["a", "b", "c", "d", "e", "f"]:
        rp.insert(k)

    rp.delete("c")
    rp.delete("e")

    for _ in range(10):
        print(rp.random_get())
