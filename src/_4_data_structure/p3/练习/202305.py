# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2023/5/4
Description :
auther : wcy
"""
# import modules
import os

__all__ = []

# define class
class Heap(object):
    """
    实现一个大顶堆
    """
    def __init__(self):
        self.size = 0
        self.lis = []

    def add(self, val):
        self.lis.append(val)
        self.size += 1
        c_idx = len(self.lis)-1

        f_idx = self.get_father_idx(idx=c_idx)
        while f_idx >= 0:
            if self.lis[c_idx] > self.lis[f_idx]:
                self.lis[c_idx], self.lis[f_idx] = self.lis[f_idx], self.lis[c_idx]

                c_idx = f_idx
                f_idx = self.get_father_idx(idx=c_idx)
            else:
                break
        print(self.lis)

    def pop_head(self):
        if self.size == 1:
            self.size -= 1
            return self.lis[0]
        elif self.size > 1:
            self.lis[0], self.lis[-1] = self.lis[-1], self.lis[0]
            val = self.lis.pop(-1)
            self.size -= 1

            c_idx = 0
            c_val = self.lis[0]
            while True:
                l_son_idx, l_son_val, r_son_idx, r_son_val = self.get_son_idx(idx=c_idx)
                # 分情况讨论
                if l_son_idx is not None and r_son_idx is not None:
                    if c_val >= max(l_son_val, r_son_val):
                        break
                    elif l_son_val >= max(c_val, r_son_val):
                        self.lis[l_son_idx], self.lis[c_idx] = self.lis[c_idx], self.lis[l_son_idx]
                        c_idx = l_son_idx
                    else:
                        self.lis[r_son_idx], self.lis[c_idx] = self.lis[c_idx], self.lis[r_son_idx]
                        c_idx = r_son_idx

                elif l_son_idx is not None and r_son_idx is None:
                    if c_val >= l_son_val:
                        break
                    else:
                        self.lis[l_son_idx], self.lis[c_idx] = self.lis[c_idx], self.lis[l_son_idx]
                        c_idx = l_son_idx

                elif l_son_idx is None and r_son_idx is not None:
                    if c_val >= r_son_val:
                        break
                    else:
                        self.lis[r_son_idx], self.lis[c_idx] = self.lis[c_idx], self.lis[r_son_idx]
                        c_idx = r_son_idx

                else:
                    break
            print(self.lis)
            return val
        else:
            return None


    def get_father_idx(self, idx: int):
        f_idx = int((idx - 1) / 2)
        if f_idx >= 0:
            return f_idx
        return None

    def get_son_idx(self, idx: int):
        l_son_idx = idx * 2 + 1
        r_son_idx = idx * 2 + 2

        if l_son_idx >= self.size:
            l_son_idx = None
            l_son_val = None
        else:
            l_son_val = self.lis[l_son_idx]

        if r_son_idx >= self.size:
            r_son_idx = None
            r_son_val = None
        else:
            r_son_val = self.lis[r_son_idx]

        return l_son_idx, l_son_val, r_son_idx, r_son_val


# define function
def func1():
    """
    堆排序
    :return:
    """
    heap = Heap()
    for val in [1, 2, 4, 2, 5, 7, 3]:
        heap.add(val=val)

    val = heap.pop_head()
    while val:
        print(val)
        val = heap.pop_head()
        if val is None:
            break


# define main
def main1():
    func1()



# main
if __name__ == '__main__':
    main1()
