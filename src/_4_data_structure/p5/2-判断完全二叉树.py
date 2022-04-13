# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-12
Description :
【完全二叉树】
    1. 任何节点，有右无左，false
    2. 在不违背1 的情况下，如果遇到了第一个左右不全，后续的节点全部是 叶节点
auther : wcy
"""
# import modules
import os, typing
from src._4_data_structure.p5.bt import BinTree, BTNode, BTNodeData

__all__ = []


# define function
def func(node: BTNode):
    catch_not_complete_leaf = False

    node_list: typing.List[BTNode] = [node]
    while node_list:
        node = node_list.pop(0)
        left_node = node.get_left_node()
        right_node = node.get_right_node()

        # 宽度有限遍历
        if left_node:
            node_list.append(left_node)
        if right_node:
            node_list.append(right_node)

        # 判断是否符合完全二叉树
        if left_node is not None and right_node is not None:
            if catch_not_complete_leaf:
                return False
            else:
                pass

        elif left_node is not None and right_node is None:
            if catch_not_complete_leaf:
                return False
            else:
                catch_not_complete_leaf = True

        elif left_node is None and right_node is not None:
            return False

        else:
            if not catch_not_complete_leaf:
                catch_not_complete_leaf = True
    return True


# define test
def test1():
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
    b = func(node=node)
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
    b = func(node=node)
    print(b)


# main
if __name__ == '__main__':
    test1()
    test2()
