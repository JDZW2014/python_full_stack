# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-14
Description :

补充:
    对于贪心问题常常使用的策略就是：
        优化排序 和 使用堆
author : wcy
"""
# import modules
import os, typing


__all__ = []


# define class
class MinHeap(object):
    def __init__(self):
        self.data_list: typing.List[int] = []
        self.heap_size = 0

    def add_data(self, v: int):
        self.data_list.append(v)
        self.heap_size += 1
        self.heapify()

    def heapify(self, ):

        idx = self.heap_size - 1
        while idx > 0:
            f_idx = (idx - 1) // 2
            if self.data_list[idx] < self.data_list[f_idx]:
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
                if self.data_list[ls] <= self.data_list[rs]:
                    if self.data_list[ls] < self.data_list[idx]:
                        self.data_list[idx], self.data_list[ls] = self.data_list[ls], self.data_list[idx]
                        idx = ls
                    else:
                        break
                else:
                    if self.data_list[rs] < self.data_list[idx]:
                        self.data_list[idx], self.data_list[rs] = self.data_list[rs], self.data_list[idx]
                        idx = rs
                    else:
                        break

            elif ls < self.heap_size <= rs:
                if self.data_list[ls] < self.data_list[idx]:
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
def func(data_list: typing.List[int]):
    min_heap = MinHeap()
    cost = 0
    for data in data_list:
        min_heap.add_data(data)

    while not min_heap.is_empty():
        data1 = min_heap.heap_pop()
        data2 = min_heap.heap_pop()
        if data1 is not None and data2 is not None:
            cost += data1
            min_heap.add_data(data1 + data2)
        else:
            break
    print(f"data_list is {data_list}")
    print(cost)


# define test
def test():
    data_list = [10, 20, 30, 40, 70]
    func(data_list=data_list)


# main
if __name__ == '__main__':
    test()
