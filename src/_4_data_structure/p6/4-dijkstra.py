# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-14
Description :
【问题】： Dijkstra 算法
    要求图中不能有累加为负数的环
author : wcy
"""
# import modules
import os

# import modules
import os, typing, sys
from src._4_data_structure.p6.graph import Graph, GraphOneData, Node, Edge

__all__ = []


# define class
class NNode(object):
    __slots__ = ["node", "dist"]

    def __init__(self, node: Node, dist: int=None):
        self.node: Node = node
        if dist is not None:
            self.dist = dist
        else:
            self.dist = float('inf')

    def set_dist(self, d):
        self.dist = d


class MaxHeap(object):
    def __init__(self):
        self.data_list: typing.List[NNode] = []
        self.heap_size = 0

    def add_data(self, v: NNode):
        self.data_list.append(v)
        self.heap_size += 1
        self.heapify()

    def heapify(self, ):

        idx = self.heap_size - 1
        while idx > 0:
            f_idx = (idx - 1) // 2
            if self.data_list[idx].dist > self.data_list[f_idx].dist:
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
                if self.data_list[ls].dist >= self.data_list[rs].dist:
                    if self.data_list[ls].dist > self.data_list[idx].dist:
                        self.data_list[idx], self.data_list[ls] = self.data_list[ls], self.data_list[idx]
                        idx = ls
                    else:
                        break
                else:
                    if self.data_list[rs].dist > self.data_list[idx].dist:
                        self.data_list[idx], self.data_list[rs] = self.data_list[rs], self.data_list[idx]
                        idx = rs
                    else:
                        break

            elif ls < self.heap_size <= rs:
                if self.data_list[ls].dist > self.data_list[idx].dist:
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
            if self.data_list[idx].dist < self.data_list[f_idx].dist:
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
                if self.data_list[ls].dist <= self.data_list[rs].dist:
                    if self.data_list[ls].dist < self.data_list[idx].dist:
                        self.data_list[idx], self.data_list[ls] = self.data_list[ls], self.data_list[idx]
                        idx = ls
                    else:
                        break
                else:
                    if self.data_list[rs].dist < self.data_list[idx].dist:
                        self.data_list[idx], self.data_list[rs] = self.data_list[rs], self.data_list[idx]
                        idx = rs
                    else:
                        break

            elif ls < self.heap_size <= rs:
                if self.data_list[ls].dist < self.data_list[idx].dist:
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

    def reset_one_value_and_heapify(self, nnode: NNode):
        is_change = False
        for idx, data in enumerate(self.data_list):
            if data.node.value == nnode.node.value:
                if nnode.dist < data.dist:
                    self.data_list[idx] = nnode
                    is_change = True
                    break

        while is_change and idx > 0:
            f_idx = (idx - 1) // 2
            if self.data_list[idx].dist < self.data_list[f_idx].dist:
                self.data_list[idx], self.data_list[f_idx] = self.data_list[f_idx], self.data_list[idx]
                idx = f_idx
            else:
                break


# define function
def func1(g: Graph, node_value: int):
    # 小顶堆
    min_heap = MinHeap()
    for node in g.node_map.values():
        nnode = NNode(node=node)
        min_heap.add_data(nnode)

    # 准备数据
    node = g.get_one_node(node_value=node_value)
    min_heap.reset_one_value_and_heapify(nnode=NNode(node=node, dist=0))

    min_dis_result: typing.List[NNode] = list()
    while not min_heap.is_empty():
        nnode = min_heap.heap_pop()
        min_dis_result.append(nnode)
        for edge in nnode.node.get_next_edges():
            if edge.from_.value != nnode.node.value:
                next_node = edge.from_
            else:
                next_node = edge.to_

            next_nnode = NNode(node=next_node, dist=nnode.dist + edge.weight)
            min_heap.reset_one_value_and_heapify(next_nnode)

    for nnode in min_dis_result:
        print(f"{nnode.node.value} - {nnode.dist}")


# define test
def test():
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
    func1(g, node_value=3)


# main
if __name__ == "__main__":
    test()
