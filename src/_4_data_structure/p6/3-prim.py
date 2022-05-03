# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-13
Description :
    【prim】
    要求：无向图
auther : wcy
"""
# import modules
import os, typing
from src._4_data_structure.p6.graph import Graph, GraphOneData, Node, Edge

__all__ = []


# define class
# define class
class MaxHeap(object):
    def __init__(self):
        self.data_list: typing.List[Edge] = []
        self.heap_size = 0

    def add_data(self, v: Edge):
        self.data_list.append(v)
        self.heap_size += 1
        self.heapify()

    def heapify(self, ):

        idx = self.heap_size - 1
        while idx > 0:
            f_idx = (idx - 1) // 2
            if self.data_list[idx].weight > self.data_list[f_idx].weight:
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
                if self.data_list[ls].weight >= self.data_list[rs].weight:
                    if self.data_list[ls].weight > self.data_list[idx].weight:
                        self.data_list[idx], self.data_list[ls] = self.data_list[ls], self.data_list[idx]
                        idx = ls
                    else:
                        break
                else:
                    if self.data_list[rs].weight > self.data_list[idx].weight:
                        self.data_list[idx], self.data_list[rs] = self.data_list[rs], self.data_list[idx]
                        idx = rs
                    else:
                        break

            elif ls < self.heap_size <= rs:
                if self.data_list[ls].weight > self.data_list[idx].weight:
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
            if self.data_list[idx].weight < self.data_list[f_idx].weight:
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
                if self.data_list[ls].weight <= self.data_list[rs].weight:
                    if self.data_list[ls].weight < self.data_list[idx].weight:
                        self.data_list[idx], self.data_list[ls] = self.data_list[ls], self.data_list[idx]
                        idx = ls
                    else:
                        break
                else:
                    if self.data_list[rs].weight < self.data_list[idx].weight:
                        self.data_list[idx], self.data_list[rs] = self.data_list[rs], self.data_list[idx]
                        idx = rs
                    else:
                        break

            elif ls < self.heap_size <= rs:
                if self.data_list[ls].weight < self.data_list[idx].weight:
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
def prim(g: Graph, start_node_value):
    """
    最小生成树算法： prim， P算法
    """

    node = g.get_one_node(start_node_value)
    min_head = MinHeap()
    for edge in node.get_next_edges():
        min_head.add_data(edge)

    edge_list: typing.List[Edge] = []
    node_set = set()
    node_set.add(node)

    while not min_head.is_empty():
        edge = min_head.heap_pop()
        if edge.from_ not in node_set:
            node_set.add(edge.from_)
            edge_list.append(edge)
            for edge in edge.from_.get_next_edges():
                min_head.add_data(edge)

        elif edge.to_ not in node_set:
            node_set.add(edge.to_)
            edge_list.append(edge)
            for edge in edge.to_.get_next_edges():
                min_head.add_data(edge)
        else:
            continue

    for edge in edge_list:
        print(edge.weight)


# define test
def test1():
    print("----- test1 -----")
    data_list = [
        GraphOneData(from_=1, to_=2, weight=1, if_have_di=False),
        GraphOneData(from_=1, to_=3, weight=10, if_have_di=False),
        GraphOneData(from_=1, to_=4, weight=5, if_have_di=False),
        GraphOneData(from_=2, to_=3, weight=20, if_have_di=False),
        GraphOneData(from_=2, to_=4, weight=100, if_have_di=False),
        GraphOneData(from_=4, to_=3, weight=1000, if_have_di=False),
    ]

    g = Graph()
    g.from_data_list(data_list=data_list)
    prim(g, 1)


# main
if __name__ == '__main__':
    test1()
