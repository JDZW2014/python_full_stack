# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-12
Description :
【平衡二叉树】：对于任意子树：左树的高度差和右树的高度差不超过1
auther : wcy
"""
# import modules
# import modules
import os, typing
from src._4_data_structure.p5.bt import BinTree, BTNode, BTNodeData

__all__ = []


# define function
def balance_tree(node: BTNode):
    if node is None:
        if_bt = True
        depth = 0

    else:
        if_left_bt, left_depth = balance_tree(node.get_left_node())
        if_right_bt, right_depth = balance_tree(node.get_right_node())

        if_bt = if_left_bt and if_right_bt and abs(left_depth - right_depth) <= 1
        depth = max(left_depth, right_depth) + 1

    return if_bt, depth


# define test
def test1():
    data_list: typing.List[BTNodeData] = [
        BTNodeData(value=12, right=18, left=5, is_root=True),
        BTNodeData(value=5, right=9, left=2, is_root=False),
        BTNodeData(value=18, right=None, left=15, is_root=False),
        BTNodeData(value=2, right=None, left=101, is_root=False),
        BTNodeData(value=101, right=None, left=102, is_root=False),
        BTNodeData(value=102, right=None, left=None, is_root=False),
        BTNodeData(value=9, right=None, left=None, is_root=False),
        BTNodeData(value=15, right=None, left=None, is_root=False)
    ]

    tree = BinTree().build_from_bt_node_data_list(data_list=data_list)
    node = tree.get_root_node()
    b = balance_tree(node=node)
    print(b)


def test2():
    data_list: typing.List[BTNodeData] = [
        BTNodeData(value=12, right=18, left=5, is_root=True),
        BTNodeData(value=5, right=9, left=2, is_root=False),
        BTNodeData(value=18, right=15, left=None, is_root=False),
        BTNodeData(value=2, right=None, left=None, is_root=False),
        BTNodeData(value=9, right=None, left=None, is_root=False),
        BTNodeData(value=15, right=None, left=None, is_root=False)
    ]

    tree = BinTree().build_from_bt_node_data_list(data_list=data_list)
    node = tree.get_root_node()
    b = balance_tree(node=node)
    print(b)


# main
if __name__ == '__main__':
    test1()
    test2()
