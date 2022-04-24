# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-21
Description :
auther : wcy
"""
# import modules
import os, typing

__all__ = []


# define class
class Node(object):
    __slots__ = ["value", "left_node", "right_node"]

    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

    def set_left_node(self, node):
        self.left_node = node
        return self

    def set_right_node(self, node):
        self.right_node = node
        return self


class BinaryTree(object):
    to_str_sep = "#"

    def __init__(self, head):
        self.head = head

    def travel(self, order_type, travel_style, if_print=False):
        travel_list: typing.List[Node] = []
        if travel_style == 'rec':
            self._tree_travel_rec_(head=self.head, order_type=order_type, travel_list=travel_list)
        else:
            self._tree_travel_unrec_(head=self.head, order_type=order_type, travel_list=travel_list)
        if if_print:
            print(f"--- {order_type} --- {travel_style} ---")
            lis = [node.value for node in travel_list]
            print(lis)
        return travel_list

    @staticmethod
    def _tree_travel_rec_(head: Node, order_type, travel_list: typing.List[Node]):
        if order_type == 'first':
           travel_list.append(head)
           if head.left_node is not None:
               BinaryTree._tree_travel_rec_(head=head.left_node, order_type=order_type, travel_list=travel_list)
           if head.right_node is not None:
               BinaryTree._tree_travel_rec_(head=head.right_node, order_type=order_type, travel_list=travel_list)

        elif order_type == 'middle':
            if head.left_node is not None:
                BinaryTree._tree_travel_rec_(head=head.left_node, order_type=order_type, travel_list=travel_list)
            travel_list.append(head)
            if head.right_node is not None:
                BinaryTree._tree_travel_rec_(head=head.right_node, order_type=order_type, travel_list=travel_list)
        else:
            if head.left_node is not None:
                BinaryTree._tree_travel_rec_(head=head.left_node, order_type=order_type, travel_list=travel_list)
            if head.right_node is not None:
                BinaryTree._tree_travel_rec_(head=head.right_node, order_type=order_type, travel_list=travel_list)
            travel_list.append(head)

    @staticmethod
    def _tree_travel_unrec_(head, order_type, travel_list):
        stack = list()
        if order_type == 'first':
            stack.append(head)
            while stack:
                node: Node = stack.pop()
                travel_list.append(node)
                if node.right_node is not None:
                    stack.append(node.right_node)
                if node.left_node is not None:
                    stack.append(node.left_node)

        elif order_type == 'middle':
            stack.append(head)
            stack_bott = False
            while stack:
                node = stack.pop()
                if stack_bott is False:
                    if node.left_node is not None:
                        stack.append(node)
                        stack.append(node.left_node)
                    else:
                        travel_list.append(node)
                        stack_bott = True
                else:
                    travel_list.append(node)
                    if node.right_node is not None:
                        stack.append(node.right_node)
                        stack_bott = False

        else:
            new_travel_list: typing.List[None] = []
            stack.append(head)
            while stack:
                node: Node = stack.pop()
                new_travel_list.append(node)
                if node.left_node is not None:
                    stack.append(node.left_node)
                if node.right_node is not None:
                    stack.append(node.right_node)
            for node in new_travel_list[::-1]:
                travel_list.append(node)

    def width_first_travel(self, if_print=False):
        node = self.head
        travel_list: typing.List[Node] = list()
        stack = list()
        stack.append(node)
        while stack:
            node = stack.pop(0)
            travel_list.append(node)
            if node.left_node is not None:
                stack.append(node.left_node)
            if node.right_node is not None:
                stack.append(node.right_node)
        if if_print:
            print("--- width_first_travel ---")
            print([node.value for node in travel_list])

    def morris_travel(self, ):
        pass

    def to_str(self, ):
        s = ""
        stack = [self.head]
        while stack:
            node = stack.pop(0)
            if node is not None:
                s += f"{node.value}_"
            else:
                s += f"{self.to_str_sep}_"
                continue
            if node.left_node is not None:
                stack.append(node.left_node)
            else:
                stack.append(None)
            if node.right_node is not None:
                stack.append(node.right_node)
            else:
                stack.append(None)
        return s

    def from_str(self, s: str):
        stack = []
        def _func(w):
            if w == self.to_str_sep:
                return w
            else:
                return int(w)
        s: list = [_func(w) for w in s.split("_") if w]
        self.head = Node(value=s.pop(0))

        head = self.head
        # 处理特殊情况
        if s[0] == self.to_str_sep:
            return head

        while s:
            w = s.pop(0)
            node = Node(value=w)
            if head.left_node is None:
                head.set_left_node(node)
            else:
                head.set_right_node(node)

            if s[0] == self.to_str_sep and s[1] == self.to_str_sep:
                head = stack.pop()
            else:
                stack.append(node)

        return head

# define function
def func1(head: Node):
    """
    判断是否搜索二叉树
    """
    if head.left_node is not None:
        left_bool, left_max, left_min = func1(head=head.left_node)
    else:
        left_bool, left_max, left_min = True, None, None

    if head.right_node is not None:
        right_bool, right_max, right_min = func1(head=head.right_node)
    else:
        right_bool, right_max, right_min = True, None, None

    if left_bool and right_bool:
        if left_max is not None and right_max is not None:
            if left_max < head.value < right_min:
                return True, right_max, left_min
        elif left_max is None and right_max is not None:
            if head.value < right_min:
                return True, right_max, head.value
        elif left_max is not None and right_max is None:
            if left_max < head.value:
                return True, head.value, left_min
        else:
            return True, head.value, head.value

    return False, -1, -1


def func2(head: Node):
    """
    判断是否是满二叉树
    """
    if head.left_node is not None:
        left_bool, left_depth, left_node_num = func2(head=head.left_node)
    else:
        left_bool, left_depth, left_node_num = True, 0, 0

    if head.right_node is not None:
        right_bool, right_depth, right_node_num = func2(head=head.right_node)
    else:
        right_bool, right_depth, right_node_num = True, 0, 0

    if left_bool and right_bool:
        depth = max(left_depth, right_depth) + 1
        node_num = left_node_num + right_node_num + 1
        if 2 ** depth - 1 == node_num:
            return True, depth, node_num

    return False, -1, -1


def func3(head: Node):
    """
    判断是否是平衡二叉树
    """
    if head.left_node is not None:
        left_bool, left_depth = func3(head=head.left_node)
    else:
        left_bool, left_depth = True, 0

    if head.right_node is not None:
        right_bool, right_depth = func3(head=head.right_node)
    else:
        right_bool, right_depth = True, 0

    return left_bool and right_bool and abs(left_depth - right_depth) <= 1, max(left_depth, right_depth) + 1


def func4(head: Node, node1, node2):
    """
    找最低公共祖先节点
    """
    if head.left_node is not None:
        left_node, left_find_node = func4(head=head.left_node, node1=node1, node2=node2)
    else:
        left_node, left_find_node = None, None

    if head.right_node is not None:
        right_node, right_find_node = func4(head=head.right_node, node1=node1, node2=node2)
    else:
        right_node, right_find_node = None, None

    if left_find_node:
        return None, left_find_node
    elif right_find_node:
        return None, right_find_node
    else:
        if id(head) == id(node1):
            if id(left_node) == id(node2) or id(right_node) == id(node2):
                return None, head
            else:
                return head, None
        elif id(head) == id(node2):
            if id(left_node) == id(node1) or id(right_node) == id(node1):
                return None, head
            else:
                return head, None
        else:
            if id(left_node) == id(node1) and id(right_node) == id(node2):
                return None, head
            elif id(left_node) == id(node2) and id(right_node) == id(node1):
                return None, head
            elif id(left_node) == id(node1) or id(left_node) == id(node2):
                return left_node, None
            elif id(right_node) == id(node1) or id(right_node) == id(node2):
                return right_node, None
            else:
                return None, None


def func5(head: Node):
    """
    折纸问题
    """
    pass


# define main
def main1():
    node0 = Node(value=0)
    node1 = Node(value=1)
    node2 = Node(value=2)
    node3 = Node(value=3)
    node4 = Node(value=4)
    node5 = Node(value=5)
    node6 = Node(value=6)

    node0.set_left_node(node1)
    node0.set_right_node(node2)

    node1.set_left_node(node3)
    node1.set_right_node(node4)

    node2.set_left_node(node5)

    node3.set_left_node(node6)

    bt = BinaryTree(head=node0)
    bt.travel(order_type='first', travel_style="rec", if_print=True)
    bt.travel(order_type='first', travel_style="unrec", if_print=True)
    bt.travel(order_type='middle', travel_style="rec", if_print=True)
    bt.travel(order_type='middle', travel_style="unrec", if_print=True)
    bt.travel(order_type='last', travel_style="rec", if_print=True)
    bt.travel(order_type='last', travel_style="unrec", if_print=True)
    bt.width_first_travel(if_print=True)

    print("--- to str ---")
    bt_s = bt.to_str()
    print(bt_s)
    bt2 = BinaryTree(head=None)
    bt2.from_str(bt_s)
    print(bt2.to_str())
    print("--- to str ---")


def main2():
    node0 = Node(value=10)
    node1 = Node(value=7)
    node2 = Node(value=20)
    node3 = Node(value=6)
    node4 = Node(value=8)
    node5 = Node(value=19)
    node6 = Node(value=21)

    node0.set_left_node(node1)
    node0.set_right_node(node2)

    node1.set_left_node(node3)
    node1.set_right_node(node4)

    node2.set_left_node(node5)

    node2.set_right_node(node6)

    print(func1(head=node0))
    node5.value = 9
    print(func1(head=node0))


def main3():
    node0 = Node(value=0)
    node1 = Node(value=1)
    node2 = Node(value=2)
    node3 = Node(value=3)
    node4 = Node(value=4)
    node5 = Node(value=5)
    node6 = Node(value=6)

    node0.set_left_node(node1)
    node0.set_right_node(node2)

    node1.set_left_node(node3)
    node1.set_right_node(node4)

    node2.set_left_node(node5)
    node2.set_right_node(node6)
    print(func2(head=node0))
    node2.set_left_node(None)
    print(func2(head=node0))


def main4():
    node0 = Node(value=0)
    node1 = Node(value=1)
    node2 = Node(value=2)
    node3 = Node(value=3)
    node4 = Node(value=4)
    node5 = Node(value=5)
    node6 = Node(value=6)

    node7 = Node(value=7)
    node8 = Node(value=8)

    node0.set_left_node(node1)
    node0.set_right_node(node2)

    node1.set_left_node(node3)
    node1.set_right_node(node4)

    node2.set_left_node(node5)
    node2.set_right_node(node6)

    print(func3(head=node0))
    node6.set_left_node(node7)
    node7.set_left_node(node8)
    print(func3(head=node0))


def main5():
    node0 = Node(value=0)
    node1 = Node(value=1)
    node2 = Node(value=2)
    node3 = Node(value=3)
    node4 = Node(value=4)
    node5 = Node(value=5)
    node6 = Node(value=6)
    node7 = Node(value=7)

    node0.set_left_node(node1)
    node0.set_right_node(node2)

    node1.set_left_node(node3)
    node1.set_right_node(node4)

    node2.set_left_node(node5)
    node2.set_right_node(node6)

    node3.set_left_node(node7)
    _, find_node = func4(head=node0, node1=node7, node2=node4)
    print(find_node.value)


# main
if __name__ == '__main__':
    main1()
    main2()
    main3()
    main4()
    main5()
