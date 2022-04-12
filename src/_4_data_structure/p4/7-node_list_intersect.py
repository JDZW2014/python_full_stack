# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-12
Description :
【两个列表相交的一系列问题】：
    给定两个可能有环也可能无环的单链表，头节点head1 和 head2, 请实现一个函数，如果两个链表相交，请返回相交的第一个节点。如果不相交，返回null
【要求】：
    如果两个链表的长度之和为N，时间复杂度请达到O(N), 额外空间复杂度请达到O(1)

auther : wcy
"""
# import modules
import os, typing
from src._4_data_structure.p4.base_model import SNode, DNode, get_single_node_list, get_double_node_list, \
    print_single_node, print_double_node, add_loop_on_node_list, get_last_node, get_certain_node, get_node_len

__all__ = []


# define function
def func(node1: SNode, node2: SNode) -> typing.Union[SNode, typing.NoReturn]:
    # 先判断 两个 node list 是否有环
    if_have_loop1, first_enter_loop_node1 = if_node_list_have_loop(node=node1)
    if_have_loop2, first_enter_loop_node2 = if_node_list_have_loop(node=node2)

    # 有无loop 情况相同
    if if_have_loop1 == if_have_loop2:
        # 都有loop
        if if_have_loop1 and if_have_loop2:
            # 对入环节点做一些判断
            if id(first_enter_loop_node1) == id(first_enter_loop_node2):
                first_enter_loop_node1.set_next_node(None)
                return find_two_no_loop_node_list_first_intersect_node(node1=node1, node2=node2)

            # 如果入环节点不同
            else:
                # return first_enter_loop_node2
                _node: SNode = first_enter_loop_node1.get_next_node()
                while True:
                    if id(_node) == id(first_enter_loop_node1):
                        in_a_same_loop = False
                        break
                    elif id(_node) == id(first_enter_loop_node2):
                        in_a_same_loop = True
                        break
                    else:
                        _node = _node.get_next_node()

                # 返回任何一个都可以
                if in_a_same_loop:
                    # return first_enter_loop_node1
                    return first_enter_loop_node2
                else:
                    return None

        # 都没有loop
        else:
            return find_two_no_loop_node_list_first_intersect_node(node1=node1, node2=node2)

    # 有无loop 情况不同
    else:
        return None


def if_node_list_have_loop(node: SNode):
    s_point: SNode = node
    f_point: SNode = node.get_next_node()

    # 判断有无环
    if_have_loop = False
    while s_point or f_point:
        if id(s_point) == id(f_point):
            if_have_loop = True
            break
        else:
            f_point = f_point.get_next_node()
            if f_point:
                f_point = f_point.get_next_node()
                s_point = s_point.get_next_node()
            else:
                break

    # 如果有环，找出第一个入环节点
    first_enter_loop_node = None
    if if_have_loop:
        first_enter_loop_node = find_first_enter_loop_node(node=node, meet_node=s_point)
    return if_have_loop, first_enter_loop_node


def find_first_enter_loop_node(node: SNode, meet_node: SNode) -> SNode:
    n_point: SNode = node
    meet_node = meet_node.get_next_node()
    while True:
        if id(n_point) == id(meet_node):
            return n_point
        else:
            n_point = n_point.get_next_node()
            meet_node = meet_node.get_next_node()


def find_two_no_loop_node_list_first_intersect_node(node1: SNode, node2: SNode) -> SNode:
    node1_length = get_node_len(node1)
    node2_length = get_node_len(node2)

    if node1_length > node2_length:
        _s = node1_length - node2_length
        while _s:
            node1 = node1.get_next_node()
            _s -= 1
    else:
        _s = node2_length - node1_length
        while _s:
            node2 = node2.get_next_node()
            _s -= 1

    while True:
        if id(node1) == id(node2):
            return node1
        else:
            node1 = node1.get_next_node()
            node2 = node2.get_next_node()
            if node1 and node2:
                pass

            else:
                return None


# define test
def test1():
    # 两个列表有环， 但是不相交
    node1 = get_single_node_list(lis=[1, 3, 4, 5, 6, 2])
    add_loop_on_node_list(node=node1, steps=3)

    node2 = get_single_node_list(lis=[-1, -3, -4, -5, -6, -2])
    add_loop_on_node_list(node=node2, steps=4)

    print(func(node1=node1, node2=node2))


def test2():
    # 两个列表有环，相交
    node1 = get_single_node_list(lis=[1, 3, 4, 5, 6, 2, 19, 100, 101])
    add_loop_on_node_list(node=node1, steps=5)

    node2 = get_single_node_list(lis=[-1, -3, -4])
    get_last_node(node2).set_next_node(get_certain_node(node=node1, steps=2))

    print(func(node1=node1, node2=node2))


# main
if __name__ == '__main__':
    test1()
    test2()
