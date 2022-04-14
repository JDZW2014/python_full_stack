# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-14
Description :
auther : wcy
"""
# import modules
import os
import os, typing

__all__ = []


# define class
class OneData(object):
    __slots__ = ("cost", "earnings")

    def __init__(self, cost, earnings):
        self.cost = cost
        self.earnings = earnings


class MinHeap(object):
    def __init__(self):
        self.data_list: typing.List[OneData] = []
        self.heap_size = 0

    def add_data(self, v: OneData):
        self.data_list.append(v)
        self.heap_size += 1
        self.heapify()

    def _get_data_(self, idx):
        return self.data_list[idx].cost

    def heapify(self, ):
        idx = self.heap_size - 1
        while idx > 0:
            f_idx = (idx - 1) // 2
            if self._get_data_(idx) < self._get_data_(f_idx):
                self.data_list[idx], self.data_list[f_idx] = self.data_list[f_idx], self.data_list[idx]
                idx = f_idx
            else:
                break

    def heap_pop(self):
        if self.heap_size == 0:
            return None

        self.data_list[0], self.data_list[-1] = self.data_list[-1], self.data_list[0]
        return_value = self.data_list.pop()
        self.heap_size -= 1

        # 继续调整为小顶堆
        idx = 0
        while idx < self.heap_size:
            ls = idx * 2 + 1
            rs = idx * 2 + 2

            if rs < self.heap_size:
                if self._get_data_(ls) <= self._get_data_(rs):
                    if self._get_data_(ls) < self._get_data_(idx):
                        self.data_list[idx], self.data_list[ls] = self.data_list[ls], self.data_list[idx]
                        idx = ls
                    else:
                        break
                else:
                    if self._get_data_(rs) < self._get_data_(idx):
                        self.data_list[idx], self.data_list[rs] = self.data_list[rs], self.data_list[idx]
                        idx = rs
                    else:
                        break

            elif ls < self.heap_size <= rs:
                if self._get_data_(ls) < self._get_data_(idx):
                    self.data_list[ls], self.data_list[idx] = self.data_list[idx], self.data_list[ls]
                else:
                    break
            else:
                break

        return return_value

    def is_empty(self):
        if len(self.data_list) == 0:
            return True
        else:
            return False


class MaxHeap(object):
    def __init__(self):
        self.data_list: typing.List[OneData] = []
        self.heap_size = 0

    def add_data(self, v: OneData):
        self.data_list.append(v)
        self.heap_size += 1
        self.heapify()

    def _get_data_(self, idx):
        return self.data_list[idx].earnings

    def heapify(self, ):
        idx = self.heap_size - 1
        while idx > 0:
            f_idx = (idx - 1) // 2
            if self._get_data_(idx) > self._get_data_(f_idx):
                self.data_list[idx], self.data_list[f_idx] = self.data_list[f_idx], self.data_list[idx]
                idx = f_idx
            else:
                break

    def heap_pop(self):
        if self.heap_size == 0:
            return None

        self.data_list[0], self.data_list[-1] = self.data_list[-1], self.data_list[0]
        return_value = self.data_list.pop()
        self.heap_size -= 1

        # 继续调整为小顶堆
        idx = 0
        while idx < self.heap_size:
            ls = idx * 2 + 1
            rs = idx * 2 + 2

            if rs < self.heap_size:
                if self._get_data_(ls) >= self._get_data_(rs):
                    if self._get_data_(ls) > self._get_data_(idx):
                        self.data_list[idx], self.data_list[ls] = self.data_list[ls], self.data_list[idx]
                        idx = ls
                    else:
                        break
                else:
                    if self._get_data_(rs) > self._get_data_(idx):
                        self.data_list[idx], self.data_list[rs] = self.data_list[rs], self.data_list[idx]
                        idx = rs
                    else:
                        break

            elif ls < self.heap_size <= rs:
                if self._get_data_(ls) > self._get_data_(idx):
                    self.data_list[ls], self.data_list[idx] = self.data_list[idx], self.data_list[ls]
                else:
                    break
            else:
                break

        return return_value

    def is_empty(self):
        if len(self.data_list) == 0:
            return True
        else:
            return False


# define function
def func(data_list: typing.List[OneData], M, max_project_num):
    min_heap = MinHeap()
    for data in data_list:
        min_heap.add_data(data)

    max_heap = MaxHeap()
    while max_project_num > 0:
        while True:
            p = min_heap.heap_pop()
            if p and p.cost <= M:
                max_heap.add_data(p)
            else:
                if p:
                    min_heap.add_data(p)
                break

        p = max_heap.heap_pop()
        M += p.earnings
        max_project_num -= 1

    print(M)


# define test
def test():
    data_list = [
        OneData(cost=1, earnings=1),
        OneData(cost=1, earnings=3),
        OneData(cost=3, earnings=2),
        OneData(cost=5, earnings=2),
        OneData(cost=5, earnings=10),
        OneData(cost=7, earnings=6)
    ]
    func(data_list=data_list, M=2, max_project_num=4)
    pass


# main
if __name__ == '__main__':
    test()
