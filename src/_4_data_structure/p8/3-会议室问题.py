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
    __slots__ = ("start", "end")

    def __init__(self, start, end):
        self.start = start
        self.end = end


class MinHeap(object):
    def __init__(self):
        self.data_list: typing.List[OneData] = []
        self.heap_size = 0

    def add_data(self, v: OneData):
        self.data_list.append(v)
        self.heap_size += 1
        self.heapify()

    def _get_data_(self, idx):
        return self.data_list[idx].end

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


# define function
def func(data_list: typing.List[OneData], min_start, max_end):
    min_heap = MinHeap()
    for data in data_list:
        min_heap.add_data(data)

    result_list: typing.List[OneData] = []
    while not min_heap.is_empty():
        data = min_heap.heap_pop()
        if data.start >= min_start and data.end <= max_end:
            result_list.append(data)
            min_start = data.end

    for data in result_list:
        print(f"{data.start} - {data.end}")


# define test
def test():
    data_list = [
        OneData(start=1, end=4),
        OneData(start=2, end=3),
        OneData(start=2, end=5),
        OneData(start=6, end=7),
        OneData(start=6, end=10),
        OneData(start=7, end=8)
    ]
    func(data_list=data_list, min_start=0, max_end=10)
    pass


# main
if __name__ == '__main__':
    test()
