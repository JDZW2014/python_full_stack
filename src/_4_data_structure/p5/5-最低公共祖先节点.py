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
def func(node: BTNode):
    pass


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
    pass


# main
if __name__ == '__main__':
    test()
