# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-21
Description :
auther : wcy
"""
# import modules
import os

__all__ = []

# define class
class UnidirectionalNode(object):
    __slots__ = ["value", "next_node"]

    def __init__(self, value):
        self.value = value
        self.next_node = None

    def set_next_node(self, node):
        self.next_node = node
        return self


class DirectionalNode(object):
    __slots__ = ["value", "next_node", "last_node"]

    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.last_node = None

    def set_next_node(self, node):
        self.next_node = node
        return self

    def set_last_node(self, node):
        self.last_node = node
        return self


# define function
def func1(head: UnidirectionalNode):
    """
    反转单项链表
    """
    node = head
    last_node = None
    while True:
        next_node: UnidirectionalNode = node.next_node
        node.set_next_node(last_node)
        if next_node is not None:
            last_node = node
            node = next_node
        else:
            break

    return node


def func2(head: DirectionalNode):
    """
    反转双向链表
    """
    node = head
    while True:
        next_node = node.next_node
        last_node = node.last_node
        node.set_last_node(next_node)
        node.set_next_node(last_node)
        if next_node is None:
            break
        node = next_node
    return node


def func3(head1, head2):
    """
    查找链表的公共部分
    """
    # head1 的深度
    head1_size = get_depth(node=head1)
    head2_size = get_depth(node=head2)

    while head1_size > head2_size:
        head1 = head1.next_node
        head1_size -= 1

    while head2_size > head1_size:
        head2 = head2.next_node
        head2_size -= 1

    same_node_list = []
    while head1 is not None and head2 is not None:
        if id(head1) == id(head2):
            same_node_list.append(head1)
        head1 = head1.next_node
        head2 = head2.next_node

    return same_node_list


def get_depth(node):
    size = 0
    while True:
        if node is not None:
            size += 1
            node = node.next_node
        else:
            break
    return size


def func4(head):
    """
    判断一个链表是否为回文结构
    """
    p1 = head
    p2 = head.next_node

    while id(p1) != id(p2):
        p1 = p1.next_node
        p2 = p2.next_node.next_node
        if p2 is None:
            return False

    p1 = head
    p2 = p2.next_node
    while id(p1) != id(p2):
        p1 = p1.next_node
        p2 = p2.next_node

    return p1


def func5(head, num):
    """
    链表划分
    【题目】： 将单向链表按某值划分成左边小，中间相等，右边大的形式
        给定一个单链表的头节点head, 节点的值类型是整形，在给定一个数num, 实现一个调整列表节点的函数，将链表调整为左边部分小于num,
        中间部分等于num， 右边部分大于num。

    【题目进阶】
        1. 调整后所有小于num 的节点之间的相对顺序和调整之前一样
        2. 调整后所有等于 。。。
        3. 调整后所有大于 。。。
        4. 时间复杂度 O(N), 额外空间复杂度 O(1)
    """
    less_first_node = None
    less_node: UnidirectionalNode = None
    equal_first_node = None
    equal_node: UnidirectionalNode = None
    greater_first_node = None
    greater_node: UnidirectionalNode = None

    while head is not None:
        next_node = head.next_node
        head.set_next_node(None)
        if head.value < num:
            if less_first_node is None:
                less_first_node = head
            if less_node is None:
                less_node = head
            else:
                less_node.set_next_node(head)
                less_node = less_node.next_node

        elif head.value == num:
            if equal_first_node is None:
                equal_first_node = head
            if equal_node is None:
                equal_node = head
            else:
                equal_node.set_next_node(head)
                equal_node = equal_node.next_node

        else:
            if greater_first_node is None:
                greater_first_node = head

            if greater_node is None:
                greater_node = head
            else:
                greater_node.set_next_node(head)
                greater_node = greater_node.next_node
        head = next_node
    return less_first_node, equal_first_node, greater_first_node


def func6():
    """
    链表复制
    【题目】： 复制含有随机指针节点的链表
        class Node {
            int value;
            Node next;
            Node rand;
            Node(int val) {
                value = val
            }
        }
            rand 指针是单链表节点结构中新增的指针，rand 可能指向链表中的任意节点，也可能指向null。给定一个有Node节点类型组成的无环单链表的
        头节点head， 请实现一个函数完成这个链表的复制，并返回复制的新链表的头节点。
    【要求】时间复杂度O(N), 额外空间复杂度O(1)
    """
    pass


def func7():
    """
    node_list_intersect
    """
    pass


# define main
def main1():
    head = UnidirectionalNode(value=10)
    node1 = UnidirectionalNode(value=9)
    head.set_next_node(node1)

    node2 = UnidirectionalNode(value=8)
    node1.set_next_node(node2)

    node3 = UnidirectionalNode(value=6)
    node2.set_next_node(node3)

    node4 = UnidirectionalNode(value=5)
    node3.set_next_node(node4)

    node5 = UnidirectionalNode(value=4)
    node4.set_next_node(node5)

    node = func1(head=head)

    while node is not None:
        print(node.value)
        node = node.next_node


def main2():
    head = DirectionalNode(value=10)
    node1 = DirectionalNode(value=9)
    head.set_next_node(node1)
    node1.set_last_node(head)

    node2 = DirectionalNode(value=8)
    node1.set_next_node(node2)
    node2.set_last_node(node1)

    node3 = DirectionalNode(value=6)
    node2.set_next_node(node3)
    node3.set_last_node(node2)

    node4 = DirectionalNode(value=5)
    node3.set_next_node(node4)
    node4.set_last_node(node3)

    node5 = DirectionalNode(value=4)
    node4.set_next_node(node5)
    node5.set_last_node(node4)

    node = func2(head=head)
    print(node.value)


def main3():
    """
    打印两个有序链表的公共部分
    """
    head = UnidirectionalNode(value=10)
    node1 = UnidirectionalNode(value=9)
    head.set_next_node(node1)

    node2 = UnidirectionalNode(value=8)
    node1.set_next_node(node2)

    node3 = UnidirectionalNode(value=6)
    node2.set_next_node(node3)

    node4 = UnidirectionalNode(value=5)
    node3.set_next_node(node4)

    node5 = UnidirectionalNode(value=4)
    node4.set_next_node(node5)

    headb = UnidirectionalNode(value=41)
    nodeb1 = UnidirectionalNode(value=42)
    nodeb2 = UnidirectionalNode(value=43)
    headb.set_next_node(nodeb1)
    nodeb1.set_next_node(nodeb2)
    nodeb2.set_next_node(node3)

    same_node_list = func3(head1=head, head2=headb)
    for node in same_node_list:
        print(node.value)


def main4():
    head = UnidirectionalNode(value=10)
    node1 = UnidirectionalNode(value=9)
    head.set_next_node(node1)

    node2 = UnidirectionalNode(value=8)
    node1.set_next_node(node2)

    node3 = UnidirectionalNode(value=6)
    node2.set_next_node(node3)

    node4 = UnidirectionalNode(value=5)
    node3.set_next_node(node4)

    node5 = UnidirectionalNode(value=4)
    node4.set_next_node(node5)

    node6 = UnidirectionalNode(value=3)
    node5.set_next_node(node6)
    node6.set_next_node(node4)

    node = func4(head=head)
    print(node.value)
    pass


def main5():
    head = UnidirectionalNode(value=10)
    node1 = UnidirectionalNode(value=9)
    head.set_next_node(node1)

    node2 = UnidirectionalNode(value=8)
    node1.set_next_node(node2)

    node3 = UnidirectionalNode(value=6)
    node2.set_next_node(node3)

    node4 = UnidirectionalNode(value=5)
    node3.set_next_node(node4)

    node5 = UnidirectionalNode(value=4)
    node4.set_next_node(node5)

    less_first_node, equal_first_node, greater_first_node = func5(head=head, num=6)
    for node in [less_first_node, equal_first_node, greater_first_node]:
        while node is not None:
            print(node.value)
            node = node.next_node


def main6():
    pass


def main7():
    pass


# main
if __name__ == '__main__':
    print("------ main1 ------")
    main1()
    print("------ main2 ------")
    main2()
    print("------ main3 ------")
    main3()
    print("------ main4 ------")
    main4()
    print("------ main5 ------")
    main5()

