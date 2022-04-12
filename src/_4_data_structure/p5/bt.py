# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-12
Description :
【二叉树的结构】
    class Node<V>{
        V value;
        Node left;
        Node right
    }

【题目】 用递归和非递归两种方式实现二叉树的先序、中序和后序 遍历
    先序：头 左 右
    中序：左 头 右
    后续：左 右 头
auther : wcy
"""
# import modules
import os
import typing

__all__ = []


# define class
class BTNodeData(object):
    __slots__ = ["value", "right", "left", "is_root"]

    def __init__(self, value, right, left, is_root):
        self.value = value
        self.right = right
        self.left = left
        self.is_root = is_root


class BTNode(object):
    __slots__ = ["value", "left_node", "right_node"]

    def __init__(self, value=None):
        self.value = value
        self.left_node = None
        self.right_node = None

    def get_value(self,):
        return self.value

    def get_left_node(self):
        return self.left_node

    def get_right_node(self):
        return self.right_node

    def set_left_node(self, node):
        self.left_node = node
        return self

    def set_right_node(self, node):
        self.right_node = node
        return self


class BinTree(object):
    _first_order_type = "first"
    _middle_order_type = "middle"
    _last_order_type = "last"
    all_order_type = (_first_order_type, _middle_order_type, _last_order_type)

    def __init__(self, root: BTNode=None):
        self.root = root

    def build_from_bt_node_data_list(self, data_list: typing.List[BTNodeData]):
        node_dict = {}

        # 创建出不包含关系的节点
        for data in data_list:
            node = BTNode(value=data.value)
            node_dict[data.value] = node

            if data.is_root:
                if self.root is None:
                    self.root = node
                else:
                    raise ValueError("self.root can not sat twice")

        # 将节点的关系建立完全
        for data in data_list:
            node = node_dict[data.value]
            if data.left:
                node.set_left_node(node=node_dict[data.left])
            if data.right:
                node.set_right_node(node=node_dict[data.right])

        return self

    def get_root_node(self):
        return self.root

    def travel_tree(self, order_type, recursion, _print=False):
        assert order_type in self.all_order_type
        node_list = []
        if recursion:
            BinTree.__recursion_travel_tree__(node=self.root, node_list=node_list, order_type=order_type)
        else:
            BinTree.__not_recursion_travel_tree__(node=self.root, node_list=node_list, order_type=order_type)

        if _print:
            for node in node_list:
                print(node.get_value(), end=' ')
        return node_list

    @staticmethod
    def __recursion_travel_tree__(node: BTNode, node_list: typing.List[BTNode], order_type):
        left_node = node.get_left_node()
        right_node = node.get_right_node()

        if order_type == BinTree._first_order_type:
            node_list.append(node)
            if left_node:
                BinTree.__recursion_travel_tree__(node=left_node, node_list=node_list, order_type=order_type)
            if right_node:
                BinTree.__recursion_travel_tree__(node=right_node, node_list=node_list, order_type=order_type)
        elif order_type == BinTree._middle_order_type:
            if left_node:
                BinTree.__recursion_travel_tree__(node=left_node, node_list=node_list, order_type=order_type)
            node_list.append(node)
            if right_node:
                BinTree.__recursion_travel_tree__(node=right_node, node_list=node_list, order_type=order_type)

        elif order_type == BinTree._last_order_type:
            if left_node:
                BinTree.__recursion_travel_tree__(node=left_node, node_list=node_list, order_type=order_type)
            if right_node:
                BinTree.__recursion_travel_tree__(node=right_node, node_list=node_list, order_type=order_type)
            node_list.append(node)
        else:
            raise ValueError("order_type get wrong param")

    def not_recursion_travel_tree(self, order_type):
        """
        非递归的方法只不过是 把递归压栈 的流程手动实现
        """
        assert order_type in ()
        node = self.root
        if order_type == "first":
            print(node.get_value())

            pass

        elif order_type == "middle":
            pass

        elif order_type == "last":
            pass

        else:
            raise ValueError("order_type get wrong param")

    @staticmethod
    def __not_recursion_travel_tree__(node: BTNode, node_list: typing.List[BTNode], order_type):
        stack: typing.List = [node]
        if order_type == BinTree._first_order_type:
            while stack:
                node = stack.pop()
                left_node = node.get_left_node()
                right_node = node.get_right_node()

                node_list.append(node)
                if right_node:
                    stack.append(right_node)
                if left_node:
                    stack.append(left_node)

        elif order_type == BinTree._middle_order_type:
            stack_bott = False
            while stack:
                node = stack.pop()
                if not stack_bott:
                    if node.get_left_node():
                        stack.append(node)
                        stack.append(node.get_left_node())
                    else:
                        node_list.append(node)
                        stack_bott = True
                else:
                    node_list.append(node)
                    if node.get_right_node():
                        stack.append(node.get_right_node())
                        stack_bott = False

        elif order_type == BinTree._last_order_type:
            r_node_list = []
            while stack:
                node = stack.pop()
                left_node = node.get_left_node()
                right_node = node.get_right_node()

                r_node_list.append(node)
                if left_node:
                    stack.append(left_node)
                if right_node:
                    stack.append(right_node)
            for node in r_node_list[::-1]:
                node_list.append(node)
        else:
            raise ValueError("order_type get wrong param")


    def width_first_travel_tree(self, ):
        """
        """
        node_list: typing.List[BTNode] = [self.root]
        cl_most_right_node = self.root
        nl_most_right_node = None

        while node_list:
            node = node_list.pop(0)
            print(node.get_value(), end=' ')
            if node.get_left_node():
                node_list.append(node.get_left_node())
                nl_most_right_node = node.get_left_node()
            if node.get_right_node():
                node_list.append(node.get_right_node())
                nl_most_right_node = node.get_right_node()

            # 到了该层的结尾
            if id(node) == id(cl_most_right_node):
                print("\n")
                cl_most_right_node = nl_most_right_node

    def print_tree(self, ):
        """
        这不是一个严格遍历
        """
        self.width_first_travel_tree()


# define test
def test():
    data_list: typing.List[BTNodeData] = [
        BTNodeData(value="A", right='C', left='B', is_root=True),
        BTNodeData(value='B', right='E', left='D', is_root=False),
        BTNodeData(value='D', right=None, left=None, is_root=False),
        BTNodeData(value='E', right=None, left='H', is_root=False),
        BTNodeData(value='H', right=None, left=None, is_root=False),
        BTNodeData(value='C', right='G', left='F', is_root=False),
        BTNodeData(value='F', right=None, left=None, is_root=False),
        BTNodeData(value='G', right='J', left='I', is_root=False),
        BTNodeData(value='I', right=None, left=None, is_root=False),
        BTNodeData(value='J', right=None, left=None, is_root=False),
    ]

    tree = BinTree().build_from_bt_node_data_list(data_list=data_list)

    print(f"\n --- 递归 先序遍历 --- ")
    tree.travel_tree(order_type=BinTree._first_order_type, recursion=True, _print=True)
    print(f"\n  --- 递归 中序遍历 --- ")
    tree.travel_tree(order_type=BinTree._middle_order_type, recursion=True, _print=True)
    print(f"\n --- 递归 后序遍历 --- ")
    tree.travel_tree(order_type=BinTree._last_order_type, recursion=True, _print=True)

    print(f"\n --- 非递归 先序遍历 --- ")
    tree.travel_tree(order_type=BinTree._first_order_type, recursion=False, _print=True)
    print(f"\n  --- 非递归 中序遍历 --- ")
    tree.travel_tree(order_type=BinTree._middle_order_type, recursion=False, _print=True)
    print(f"\n --- 非递归 后序遍历 --- ")
    tree.travel_tree(order_type=BinTree._last_order_type, recursion=False, _print=True)


# main
if __name__ == '__main__':
    test()
