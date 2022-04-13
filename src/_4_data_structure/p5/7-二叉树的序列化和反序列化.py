# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-13
Description :
auther : wcy
"""
# import modules
import os, typing
from src._4_data_structure.p5.bt import BinTree, BTNode, BTNodeData

__all__ = []


# define class
class BTNodeDataP(BinTree):
    split_char = "_"
    none_char = "#"

    def to_str(self, ):
        s = ''
        node_list: typing.List[BTNode] = [self.root]
        while node_list:
            node = node_list.pop()
            v = node.get_value()
            if v is None:
                v = self.none_char
            s += f"{v}{self.split_char}"

            if node.get_value() is not None:
                left_node = node.get_left_node()
                right_node = node.get_right_node()

                if right_node:
                    node_list.append(right_node)
                else:
                    node_list.append(BTNode())

                if left_node:
                    node_list.append(left_node)
                else:
                    node_list.append(BTNode())

        return s

    def from_str(self, s: str):
        node_s_list = s.split(self.split_char)
        self.root = self.__from_str__(node_s_list)
        return self

    @staticmethod
    def __from_str__(node_s_list: typing.List[str]):
        head = node_s_list.pop(0)
        if head == BTNodeDataP.none_char:
            return None
        head = BTNode(value=head)
        head.set_left_node(BTNodeDataP.__from_str__(node_s_list))
        head.set_right_node(BTNodeDataP.__from_str__(node_s_list))
        return head


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

    tree = BTNodeDataP().build_from_bt_node_data_list(data_list=data_list)
    s = tree.to_str()
    print(f"s1: {s}")
    tree_2 = BTNodeDataP().from_str(s)
    s2 = tree_2.to_str()
    print(f"s2: {s2}")


def test2():
    data_list: typing.List[BTNodeData] = [
        BTNodeData(value=12, right=18, left=5, is_root=True),
        BTNodeData(value=5, right=None, left=2, is_root=False),
        BTNodeData(value=18, right=16, left=15, is_root=False),
        BTNodeData(value=2, right=None, left=None, is_root=False),
        BTNodeData(value=16, right=None, left=None, is_root=False),
        BTNodeData(value=15, right=None, left=None, is_root=False)
    ]

    tree = BTNodeDataP().build_from_bt_node_data_list(data_list=data_list)
    s = tree.to_str()
    print(f"s1: {s}")
    tree_2 = BTNodeDataP().from_str(s)
    s2 = tree_2.to_str()
    print(f"s2: {s2}")


# main
if __name__ == '__main__':
    test1()
    test2()
