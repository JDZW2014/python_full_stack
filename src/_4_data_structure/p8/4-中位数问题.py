# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-14
Description :
auther : wcy
"""
# import modules
import os, typing

__all__ = []


# define class
class OneData(object):
    __slots__ = ("value", )

    def __init__(self, value):
        self.value = value


class MinHeap(object):
    def __init__(self):
        self.data_list: typing.List[OneData] = []
        self.heap_size = 0

    def get_min(self):
        return self.data_list[0]

    def add_data(self, v: OneData):
        self.data_list.append(v)
        self.heap_size += 1
        self.heapify()

    def _get_data_(self, idx):
        return self.data_list[idx].value

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


class MaxHeap(MinHeap):
    def get_max(self):
        return self.data_list[0]

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


class GetMidNum(object):
    def __init__(self):
        self.min_heap = MinHeap()
        self.max_heap = MaxHeap()

    def add(self, data: OneData):
        self.min_heap.add_data(data)

        if self.min_heap.heap_size > self.max_heap.heap_size + 1:
            self.max_heap.add_data(self.min_heap.heap_pop())

    def get_mid_data(self) -> int:
        if self.min_heap.heap_size == self.max_heap.heap_size:
            return (self.min_heap.get_min().value + self.max_heap.get_max().value) / 2
        elif self.min_heap.heap_size > self.max_heap.heap_size:
            return self.min_heap.get_min().value
        else:
            return self.max_heap.get_max().value


# define test
def test():
    data_list = [
        OneData(value=2),
        OneData(value=2),
        OneData(value=4),
        OneData(value=1),
        OneData(value=7),
        OneData(value=100),
        OneData(value=-1),
        OneData(value=9),
        OneData(value=5),
    ]
    get_mid_num = GetMidNum()
    for data in data_list:
        get_mid_num.add(data)
    print(get_mid_num.get_mid_data())
    get_mid_num.add(OneData(value=9))
    print(get_mid_num.get_mid_data())


# main
if __name__ == '__main__':
    test()
