# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-12
Description :
auther : wcy
"""
# import modules
import os, typing
from src._4_data_structure.p5.bt import BinTree, BTNode, BTNodeData

__all__ = []


# define function
def func(head: BTNode, node1: BTNode, node2: BTNode):
    # 终止条件
    if head is None or id(head) == id(node1) or id(head) == id(node2):
        return head

    else:
        left_return = func(head.get_left_node(), node1, node2)
        right_return = func(head.get_right_node(), node1, node2)
        if left_return is not None and right_return is not None:
            return head
        elif left_return is not None and right_return is None:
            return left_return
        elif left_return is None and right_return is not None:
            return right_return
        else:
            return None


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
    node1 = tree.root.left_node.left_node
    node2 = tree.root.left_node.right_node.left_node

    print(func(head=tree.get_root_node(), node1=node1, node2=node2).get_value())


def test2():
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
    node1 = tree.root.left_node.left_node
    node2 = tree.root.right_node

    print(func(head=tree.get_root_node(), node1=node1, node2=node2).get_value())


# main
if __name__ == '__main__':
    test()
    test2()
