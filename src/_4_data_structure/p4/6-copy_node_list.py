# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-12
Description :
【题目】： 复制含有随机指针节点的链表
    class Node {
        int value;
        Node next;
        Node rand;
        Node(int val) {
            value = val
        }
    }
        rand 指针是单链表节点结构中新增的指针，rand 可能指向链表中的任意节点，也可能指向null。给定一个有Node节点类型组成的无环单链表的
    头节点head， 请实现一个函数完成这个链表的复制，并返回复制的新链表的头节点。
【要求】时间复杂度O(N), 额外空间复杂度O(1)
auther : wcy
"""
# import modules
import os, typing
from src._4_data_structure.p4.base_model import SNode, DNode, get_single_node_list, get_double_node_list, \
    print_single_node, print_double_node


__all__ = []


# define class
class Node(object):
    __slots__ = ["value", "next_node", "rand_node"]

    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.rand_node = None

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def get_rand_node(self):
        return self.rand_node

    def set_next_node(self, node):
        self.next_node = node
        return self

    def set_rand_node(self, node):
        self.rand_node = node
        return self


# define function
def get_node_list(lis: typing.List[int]) -> Node:
    # node list 的基础结构
    head = Node(value=lis[0])
    node = head
    for value in lis[1:]:
        node.set_next_node(Node(value=value))
        node = node.get_next_node()

    # 随机增加了一个 rand_node
    head.set_rand_node(head.get_next_node().get_next_node())
    return head


def copy_node(node) -> Node:
    # add addition in current node list
    add_addition_node(node=node)

    # set rand node
    set_rand_node(node=node)

    # split && copy
    copy_node: Node = None
    while True:
        c_node: Node = node.get_next_node()
        if copy_node is None:
            copy_node = c_node
        c_n_node: Node = c_node.get_next_node()

        if c_n_node:
            c_n_c_node: Node = c_n_node.get_next_node()
        else:
            c_n_c_node = None

        node.set_next_node(c_n_node)
        c_node.set_next_node(c_n_c_node)

        if c_n_node:
            node = c_n_node
        else:
            break
    return copy_node


def add_addition_node(node: Node):
    while node:
        next_node = node.get_next_node()
        add_node = Node(value=node.get_value())
        node.set_next_node(add_node)
        add_node.set_next_node(next_node)
        node = next_node


def set_rand_node(node: Node):
    while node:
        if node.get_rand_node():
            node.get_next_node().set_rand_node(node=node.get_rand_node().get_next_node())
        node = node.get_next_node().get_next_node()


# define test
def test():
    node = get_node_list(lis=[1, 2, 4, 6, 7, 11])
    print(node.get_rand_node().get_value())
    c_node = copy_node(node=node)
    print(c_node.get_rand_node().get_value())


# main
if __name__ == '__main__':
    test()
