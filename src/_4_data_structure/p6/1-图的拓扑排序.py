# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-13
Description :
【题目】： 拓扑排序算法
    适用范围：要求有向图，且有入度为零的节点，且没有环
auther : wcy
"""
# import modules
import os, typing
from src._4_data_structure.p6.graph import Graph, GraphOneData, Node, Edge

__all__ = []


# define function
def func(g: Graph):
    """
    图的拓扑排序：
        1. 找入度为零的点 A （第一个）
        2. 把A及其影响擦掉，继续找入度为零的点，。。。
    """
    data_sort: typing.List[Node] = []
    while len(g.node_map) > 0:

        _zero_in_degree_node: typing.List = []
        for _, node in g.node_map.items():
            if node.get_in_degree() == 0:
                _zero_in_degree_node.append(node)

        for node in _zero_in_degree_node:
            g.node_map.pop(node.get_value())
            for n_node in node.get_next_nodes():
                # n_node: Node
                n_node.add_in_degree(-1)
        data_sort.extend(_zero_in_degree_node)

    for node in data_sort:
        print(node.get_value())


# define test
def test1():
    print("----- test1 -----")
    data_list = [
        GraphOneData(from_=1, to_=2, weight=1, if_have_di=True),
        GraphOneData(from_=1, to_=3, weight=1, if_have_di=True),
        GraphOneData(from_=2, to_=3, weight=1, if_have_di=True),
        GraphOneData(from_=2, to_=4, weight=1, if_have_di=True),
        GraphOneData(from_=3, to_=4, weight=1, if_have_di=True),
        GraphOneData(from_=5, to_=1, weight=1, if_have_di=True),
        GraphOneData(from_=5, to_=2, weight=1, if_have_di=True),
    ]
    g = Graph()
    g.from_data_list(data_list=data_list)
    func(g)


# main
if __name__ == '__main__':
    test1()
