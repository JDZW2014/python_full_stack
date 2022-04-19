# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-18
Description :
auther : wcy
"""
# import modules
import os, typing

__all__ = []


# define class
class Node(object):
    __slots__ = ["value", "left_node", "right_node"]

    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

    def set_next_node(self, left_node, right_node):
        self.left_node = left_node
        self.right_node = right_node

    def set_left_node(self, node):
        self.left_node = node

    def set_right_node(self, node):
        self.right_node = node


class Morris(object):
    def __init__(self, head: Node):
        self.head = head

    def first_travel(self, if_print=False):
        travel_list: typing.List[Node] = []
        node = self.head
        while True:
            if node.left_node is not None:
                times, left_node_most_right_node = self.get_left_node_most_right_node(node, node.left_node)

                # 第一次到达的时候
                if times == 1:
                    travel_list.append(node)
                    left_node_most_right_node.set_right_node(node)
                    node = node.left_node

                # 第二次到达的时候
                else:
                    left_node_most_right_node.set_right_node(None)
                    node = node.right_node

            elif node.right_node is not None:
                travel_list.append(node)
                node = node.right_node
            else:
                travel_list.append(node)
                break
        if if_print:
            print([node.value for node in travel_list])
        return travel_list

    def middle_travel(self, if_print=False):
        travel_list: typing.List[Node] = []
        node = self.head
        while True:
            if node.left_node is not None:
                times, left_node_most_right_node = self.get_left_node_most_right_node(node, node.left_node)

                # 第一次到达的时候
                if times == 1:
                    left_node_most_right_node.set_right_node(node)
                    node = node.left_node

                # 第二次到达的时候
                else:
                    travel_list.append(node)
                    left_node_most_right_node.set_right_node(None)
                    node = node.right_node

            elif node.right_node is not None:
                travel_list.append(node)
                node = node.right_node
            else:
                travel_list.append(node)
                break
        if if_print:
            print([node.value for node in travel_list])
        return travel_list

    def last_travel(self, if_print=False):
        travel_list: typing.List[Node] = []
        node = self.head
        while True:
            if node.left_node is not None:
                times, left_node_most_right_node = self.get_left_node_most_right_node(node, node.left_node)

                # 第一次到达的时候
                if times == 1:
                    left_node_most_right_node.set_right_node(node)
                    node = node.left_node

                # 第二次到达的时候
                else:
                    # travel_list.append(node)
                    left_node_most_right_node.set_right_node(None)
                    node = node.right_node

            elif node.right_node is not None:
                travel_list.append(node)
                node = node.right_node
            else:
                travel_list.append(node)
                break
        if if_print:
            print([node.value for node in travel_list])
        return travel_list


    def get_left_node_most_right_node(self, head_node: Node, node: Node):
        while True:
            if node.right_node is None:
                return 1, node
            elif id(node.right_node) == id(head_node):
                return 2, node
            else:
                node = node.right_node


# main
if __name__ == '__main__':
    node0 = Node(value=0)

    node1 = Node(value=1)
    node2 = Node(value=2)

    node3 = Node(value=3)
    node4 = Node(value=4)
    node5 = Node(value=5)
    node6 = Node(value=6)

    node7 = Node(value=7)
    node8 = Node(value=8)
    node9 = Node(value=9)
    node10 = Node(value=10)

    node101 = Node(value=101)

    node0.set_next_node(node1, node2)

    node1.set_next_node(node3, node4)
    node2.set_next_node(node5, node6)

    node3.set_next_node(node7, node8)
    node4.set_next_node(node9, None)
    node5.set_next_node(node10, None)

    node9.set_right_node(node101)

    mt = Morris(head=node0)
    print("---- 先序遍历 ----")
    mt.first_travel(if_print=True)
    print("---- 中序遍历 ----")
    mt.middle_travel(if_print=True)
    # print("---- 后序遍历 ----")
    # mt.last_travel(if_print=True)
