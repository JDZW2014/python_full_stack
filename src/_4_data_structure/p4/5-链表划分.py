# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-11
Description :
【题目】： 将单向链表按某值划分成左边小，中间相等，右边大的形式
        给定一个单链表的头节点head, 节点的值类型是整形，在给定一个数num, 实现一个调整列表节点的函数，将链表调整为左边部分小于num,
    中间部分等于num， 右边部分大于num。

 【题目进阶】
    1. 调整后所有小于num 的节点之间的相对顺序和调整之前一样
    2. 调整后所有等于 。。。
    3. 调整后所有大于 。。。
    4. 时间复杂度 O(N), 额外空间复杂度 O(1)

auther : wcy
"""
# import modules
import os, typing
from src._4_data_structure.p4.base_model import SNode, DNode, get_single_node_list, get_double_node_list, \
    print_single_node, print_double_node


__all__ = []


# define function
def func(node: SNode, num: int) -> SNode:
    # 将 node list 划分为小于，等于，大于三部分
    less_first_node, equal_first_node, greater_first_node = split_node_list_by_num(node=node, num=num)

    # 将这三部分合并
    get_node_list_last_node(node=less_first_node).set_next_node(equal_first_node)
    get_node_list_last_node(node=equal_first_node).set_next_node(greater_first_node)
    return less_first_node


def split_node_list_by_num(node: SNode, num) -> typing.Tuple[SNode]:
    less_first_node = None
    equal_first_node = None
    greater_first_node = None

    while True:
        next_node = node.get_next_node()
        if node.get_value() < num:
            if less_first_node is None:
                less_first_node = node
            else:
                less_node.set_next_node(node)
            less_node = node
            less_node.set_next_node(None)
        elif node.get_value() == num:
            if equal_first_node is None:
                equal_first_node = node
            else:
                equal_node.set_next_node(node)
            equal_node = node
            equal_node.set_next_node(None)
        else:
            if greater_first_node is None:
                greater_first_node = node
            else:
                greater_node.set_next_node(node)
            greater_node = node
            greater_node.set_next_node(None)

        if next_node is None:
            break
        else:
            node = next_node

    return less_first_node, equal_first_node, greater_first_node


def get_node_list_last_node(node: SNode) -> SNode:
    while True:
        next_node = node.get_next_node()
        if next_node:
            node = next_node
        else:
            break
    return node


# define test
def test():
    node = get_single_node_list(lis=[1, 2, 3, 3, 1, 4, 5, 5])
    print_single_node(node)
    print("------------")
    node = func(node, num=3)
    print_single_node(node)


# main
if __name__ == '__main__':
    test()
