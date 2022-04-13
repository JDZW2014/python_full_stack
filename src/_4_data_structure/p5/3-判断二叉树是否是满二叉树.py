# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-12
Description :
【满二叉树】：
    满足： 2**层数 - 1 = 节点数
auther : wcy
"""
# import modules
import os, typing
from src._4_data_structure.p5.bt import BinTree, BTNode, BTNodeData

__all__ = []


# define test
def test1():
    data_list: typing.List[BTNodeData] = [
        BTNodeData(value=12, right=18, left=5, is_root=True),
        BTNodeData(value=5, right=9, left=2, is_root=False),
        BTNodeData(value=18, right=16, left=15, is_root=False),
        BTNodeData(value=2, right=None, left=None, is_root=False),
        BTNodeData(value=16, right=None, left=None, is_root=False),
        BTNodeData(value=9, right=None, left=None, is_root=False),
        BTNodeData(value=15, right=None, left=None, is_root=False)
    ]

    tree = BinTree().build_from_bt_node_data_list(data_list=data_list)
    print(tree.if_full_bt())


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
    print(tree.if_full_bt())


# main
if __name__ == '__main__':
    test1()
    test2()
