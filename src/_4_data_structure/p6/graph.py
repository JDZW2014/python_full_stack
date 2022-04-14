# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-13
Description :
auther : wcy
"""
# import modules
import os
import typing
import numpy as np

__all__ = []


# define class
class Node_(object):
    __slots__ = ["value", "in_degree", "out_degree"]

    def __init__(self, value):
        self.value = value
        self.in_degree: int = 0
        self.out_degree: int = 0

    def get_value(self):
        return self.value

    def get_in_degree(self):
        return self.in_degree

    def get_out_degree(self):
        return self.out_degree

    def add_in_degree(self, _v=1):
        self.in_degree += _v

    def add_out_degree(self, _v=1):
        self.out_degree += _v

    def __hash__(self, ):
        return self.value


class Edge(object):
    __slots__ = ["from_", "to_", "weight", "if_have_di"]

    def __init__(self, from_: typing.Type[Node_], to_: typing.Type[Node_], weight, if_have_di):
        self.from_ = from_
        self.to_ = to_
        self.weight = weight
        self.if_have_di = if_have_di


class Node(Node_):
    __slots__ = ["value", "next_nodes", "edges"]

    def __init__(self, value: int):
        super().__init__(value=value)
        self.next_nodes: typing.Set[typing.Type[Node_]] = set()
        self.edges: typing.Set[Edge] = set()

    def get_next_nodes(self, ) -> typing.Set[typing.Type[Node_]]:
        return self.next_nodes

    def add_next_nodes(self, node: typing.Type[Node_]):
        self.next_nodes.add(node)

    def get_next_edges(self, ) -> typing.Set[Edge]:
        return self.edges

    def add_next_edge(self, edge: Edge):
        self.edges.add(edge)


class GraphOneData(object):
    __slots__ = ["from_", "to_", "weight", "if_have_di"]

    def __init__(self, from_, to_, weight, if_have_di=True):
        self.from_ = from_
        self.to_ = to_
        self.weight = weight
        self.if_have_di = if_have_di


class Graph(object):
    def __init__(self,):
        self.node_map: typing.Dict[int, Node] = {}
        self.edges_list: typing.List[Edge] = []

    def from_adjacent_matrix(self, m: typing.List[typing.List]):
        data_list: typing.List[GraphOneData] = list()
        for from_, lis in enumerate(m):
            for to_, w in enumerate(lis):
                if w:
                    data_list.append(GraphOneData(from_=from_, to_=to_, weight=w, if_have_di=True))
        self.from_data_list(data_list=data_list)
        return self

    def from_data_list(self, data_list: typing.List[GraphOneData]):

        for data in data_list:
            # 是否要新建节点
            if data.from_ not in self.node_map:
                self.node_map[data.from_] = Node(value=data.from_)
            if data.to_ not in self.node_map:
                self.node_map[data.to_] = Node(value=data.to_)

            from_node = self.node_map[data.from_]
            to_node = self.node_map[data.to_]

            # degree
            edge = Edge(from_=from_node, to_=to_node, weight=data.weight, if_have_di=data.if_have_di)
            self.edges_list.append(edge)

            # 修改node的一些信息
            from_node.add_out_degree()
            to_node.add_in_degree()
            from_node.add_next_nodes(node=to_node)
            from_node.add_next_edge(edge=edge)
            if data.if_have_di is False:
                to_node.add_out_degree()
                from_node.add_in_degree()
                to_node.add_next_nodes(node=from_node)
                to_node.add_next_edge(edge=edge)

        return self

    def __len__(self):
        return len(self.node_map)

    def get_one_node(self, node_value: int) -> Node:
        return self.node_map[node_value]

    def travel(self, node_value: int, travel_type, if_print=False):
        """
        宽度优先遍历
        """
        if travel_type == 'bfs':
            result = Graph.__bfs__(node=self.get_one_node(node_value))
        elif travel_type == 'dfs':
            result = Graph.__dfs__(node=self.get_one_node(node_value))
        else:
            raise ValueError("travel_type get wrong param")

        if if_print:
            print(f"---- {travel_type} ----")
            for node in result:
                print(node.get_value())
        return result

    @staticmethod
    def __bfs__(node: Node):
        queue: typing.List[Node] = [node]
        travel_result: typing.List[Node] = list()
        occur_set = set()
        while queue:
            node = queue.pop(0)

            # 记录
            if node not in occur_set:
                travel_result.append(node)
                occur_set.add(node)

            for n_node in node.get_next_nodes():
                if n_node not in occur_set:
                    queue.append(n_node)
        return travel_result

    @staticmethod
    def __dfs__(node: Node):
        stack: typing.List[Node] = [node]
        travel_result: typing.List[Node] = [node]
        occur_set = set()
        occur_set.add(node)

        while stack:
            node = stack.pop()
            for n_node in node.get_next_nodes():
                if n_node not in occur_set:
                    travel_result.append(n_node)
                    occur_set.add(n_node)
                    stack.append(node)
                    stack.append(n_node)
                    break

        return travel_result


# define function


# define test
def test1():
    print("----- test1 -----")
    data_list = [
        GraphOneData(from_=1, to_=2, weight=1, if_have_di=False),
        GraphOneData(from_=1, to_=3, weight=2, if_have_di=True),
        GraphOneData(from_=1, to_=6, weight=2, if_have_di=True),
        GraphOneData(from_=2, to_=3, weight=3, if_have_di=True),
        GraphOneData(from_=3, to_=4, weight=1, if_have_di=True),
        GraphOneData(from_=5, to_=4, weight=5, if_have_di=False),
    ]
    g = Graph()
    g.from_data_list(data_list=data_list)
    g.travel(travel_type='bfs', if_print=True, node_value=1)
    g.travel(travel_type='dfs', if_print=True, node_value=1)


def test2():
    print("----- test2 -----")
    data = [
        [0, 1, 2, None, None],
        [1, 0, 3, None, None],
        [None, None, 0, 1, None],
        [None, None, None, 0, 5],
        [None, None, None, 5, 0],
    ]
    g = Graph()
    g.from_adjacent_matrix(m=data)
    g.travel(travel_type='bfs', if_print=True, node_value=0)
    g.travel(travel_type='dfs', if_print=True, node_value=0)


# main
if __name__ == '__main__':
    test1()
    test2()
