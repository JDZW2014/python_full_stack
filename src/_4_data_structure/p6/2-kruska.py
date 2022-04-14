# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-13
Description :
【kruska 算法】
    最小联通图
    适用范围： 要求无向图
auther : wcy
"""
# import modules
import os, typing
from src._4_data_structure.p6.graph import Graph, GraphOneData, Node, Edge

__all__ = []


# define class
class MaxHeap(object):
    def __init__(self):
        self.data_list = []
        self.heap_size = 0

    def add_data(self, v):
        self.data_list.append(v)
        self.heap_size += 1
        self.heapify()

    def heapify(self, ):

        idx = self.heap_size - 1
        while idx > 0:
            f_idx = (idx - 1) // 2
            if self.data_list[idx] > self.data_list[f_idx]:
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

        # 将堆继续调整为大顶堆
        idx = 0
        while idx < self.heap_size:
            ls = idx * 2 + 1
            rs = idx * 2 + 2

            if rs < self.heap_size:
                if self.data_list[ls] >= self.data_list[rs]:
                    if self.data_list[ls] > self.data_list[idx]:
                        self.data_list[idx], self.data_list[ls] = self.data_list[ls], self.data_list[idx]
                        idx = ls
                    else:
                        break
                else:
                    if self.data_list[rs] > self.data_list[idx]:
                        self.data_list[idx], self.data_list[rs] = self.data_list[rs], self.data_list[idx]
                        idx = rs
                    else:
                        break

            elif ls < self.heap_size <= rs:
                if self.data_list[ls] > self.data_list[idx]:
                    self.data_list[ls], self.data_list[idx] = self.data_list[idx], self.data_list[ls]
                else:
                    break
            else:
                break

        return return_value

    @staticmethod
    def __max_heap_pop__(idx, data_list):
        if idx >= len(data_list):
            return None


class MinHeap(MaxHeap):
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

        # 将堆继续调整为大顶堆
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


# define function
def kruska(g: Graph):
    # 这个其实是要求了距离补充存在重复的，在这偷懒了
    # 适用小顶堆每次弹出一个最短的距离

    # weight_edge_map
    edge_map = {}
    for edge in g.edges_list:
        edge_map[edge.weight] = edge

    # 小顶堆
    edge_min_heap = MinHeap()
    for k in edge_map:
        edge_min_heap.add_data(v=k)

    edge_list: typing.List[Edge] = []
    node_set = set()
    while True:
        ew = edge_min_heap.heap_pop()
        if ew:
            edge = edge_map[ew]
            if edge.from_ in node_set and edge.to_ in node_set:
                continue
            else:
                edge_list.append(edge)
                node_set.add(edge.from_)
                node_set.add(edge.to_)
        else:
            break
    return edge_list


# define test
def test1():
    print("----- test1 -----")
    data_list = [
        GraphOneData(from_=1, to_=2, weight=1, if_have_di=False),
        GraphOneData(from_=1, to_=3, weight=10, if_have_di=False),
        GraphOneData(from_=1, to_=4, weight=5, if_have_di=False),
        GraphOneData(from_=2, to_=3, weight=20, if_have_di=False),
        GraphOneData(from_=2, to_=4, weight=100, if_have_di=False),
    ]
    g = Graph()
    g.from_data_list(data_list=data_list)
    edge_list: typing.List[Edge] = kruska(g)
    for edge in edge_list:
        print(edge.weight)


def test2():
    # 测试大顶堆 && 测试大顶堆排序
    max_heap = MinHeap()
    for data in [2, 3, 1, 4, 5, 6]:
        max_heap.add_data(data)

    while True:
        v = max_heap.heap_pop()
        if v:
            print(v)
        else:
            break


# main
if __name__ == '__main__':
    test1()
    # test2()