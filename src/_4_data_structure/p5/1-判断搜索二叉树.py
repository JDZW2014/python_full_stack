# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-12
Description :
【判断搜索二叉树】: 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值
auther : wcy
"""
# import modules
import os, typing
from src._4_data_structure.p5.bt import BinTree, BTNode, BTNodeData

__all__ = []


# define function
def func(node: BTNode):
    left_node = node.get_left_node()
    right_node = node.get_right_node()

    is_bst = True
    if left_node is None and right_node is None:
        max_node = node

    elif left_node is not None and right_node is not None:
        left_max_node, l_is_bst = func(node=left_node)
        right_max_node, r_is_bst = func(node=right_node)

        if l_is_bst and r_is_bst:
            if left_max_node.get_value() < node.get_value() < right_max_node.get_value():
                max_node = right_max_node
            else:
                max_node = None
                is_bst = False
        else:
            is_bst = False
            max_node = None

    elif left_node is not None and right_node is None:
        left_max_node, l_is_bst = func(node=left_node)
        if l_is_bst:
            if left_max_node.get_value() < node.get_value():
                max_node = node
            else:
                is_bst = False
                max_node = None
        else:
            is_bst = False
            max_node = None

    else:
        is_bst = False
        max_node = None

    return max_node, is_bst


# define test
def test():
    data_list: typing.List[BTNodeData] = [
        BTNodeData(value=1, right=3, left=2, is_root=True),
        BTNodeData(value=2, right=5, left=4, is_root=False),
        BTNodeData(value=4, right=None, left=None, is_root=False),
        BTNodeData(value=5, right=None, left=8, is_root=False),
        BTNodeData(value=8, right=None, left=None, is_root=False),
        BTNodeData(value=3, right=7, left=6, is_root=False),
        BTNodeData(value=6, right=None, left=None, is_root=False),
        BTNodeData(value=7, right=10, left=9, is_root=False),
        BTNodeData(value=9, right=None, left=None, is_root=False),
        BTNodeData(value=10, right=None, left=None, is_root=False),
    ]

    tree = BinTree().build_from_bt_node_data_list(data_list=data_list)
    node = tree.get_root_node()
    max_node, is_bst = func(node=node)
    print(is_bst)


def test2():
    data_list: typing.List[BTNodeData] = [
        BTNodeData(value=12, right=18, left=5, is_root=True),
        BTNodeData(value=5, right=9, left=2, is_root=False),
        BTNodeData(value=18, right=None, left=15, is_root=False),
        BTNodeData(value=2, right=None, left=None, is_root=False),
        BTNodeData(value=9, right=None, left=None, is_root=False),
        BTNodeData(value=15, right=None, left=None, is_root=False)
    ]

    tree = BinTree().build_from_bt_node_data_list(data_list=data_list)
    node = tree.get_root_node()
    max_node, is_bst = func(node=node)
    print(is_bst)


# main
if __name__ == '__main__':
    test()
    test2()
