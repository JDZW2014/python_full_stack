# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-11
Description :

题目：回文结构，就是链表正着念和反着念一样

auther : wcy
"""
# import modules
import os
from src._4_data_structure.p4.base_model import SNode, DNode, get_single_node_list, get_double_node_list, \
    print_single_node, print_double_node

__all__ = []


# define function
def func1(node: SNode) -> bool:
    # 找到 中点 和 终点
    center_node, final_node = get_center_node_and_last_node(node=node)

    # 将中心之后的别表反转
    revert_node_list(node=center_node)

    # 分别从开始位置和结束位置往中心走一一比对
    while node and final_node:
        if node.get_value() == final_node.get_value():
            node = node.get_next_node()
            final_node = final_node.get_next_node()
        else:
            return False
    return True


def get_center_node_and_last_node(node: SNode):
    s_node: SNode = node
    f_node: SNode = node.get_next_node()

    # 先找到链表的中心
    while True:
        # fast 到了终点
        if f_node.get_next_node():
            f_node = f_node.get_next_node()
        else:
            break

        # fast 还没有到终点
        if f_node:
            s_node = s_node.get_next_node()

            if f_node.get_next_node():
                f_node = f_node.get_next_node()
            else:
                break
        else:
            break
    # center_node, last_node
    return s_node, f_node


def revert_node_list(node: SNode):
    last_node: SNode = node
    c_node: SNode = node.get_next_node()
    last_node.set_next_node(None)
    while True:
        if c_node.get_next_node():
            n_node = c_node.get_next_node()
            c_node.set_next_node(last_node)
            last_node, c_node = c_node, n_node
        else:
            c_node.set_next_node(last_node)
            break


# def test
def test1():
    node = get_single_node_list(lis=[1, 2, 3, 2, 1])
    center_node, last_node = get_center_node_and_last_node(node=node)
    print(f"center_node = {center_node.get_value()}, last_node = {last_node.get_value()}")

    node = get_single_node_list(lis=[1, 2, 3, 3, 2, 1])
    center_node, last_node = get_center_node_and_last_node(node=node)
    print(f"center_node = {center_node.get_value()}, last_node = {last_node.get_value()}")


def test2():

    pass


def test(lis):
    node = get_single_node_list(lis=lis)
    print_single_node(node)
    ret = func1(node=node)
    print(f"{ret}")


# main
if __name__ == '__main__':
    # test1()
    test([1, 2, 3, 2, 1])
    test([1, 2, 3, 3, 2, 1])
    test([1, 2, 3, 3, 2, 2, 1])
