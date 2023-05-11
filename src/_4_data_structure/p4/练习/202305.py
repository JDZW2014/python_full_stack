# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2023/5/5
Description :
auther : wcy
"""
# import modules
import os

__all__ = []

# define class
class SingleNode(object):
    def __init__(self, val):
        self.val = val
        self.next_node = None

    def set_next_node(self, node):
        self.next_node = node

class SingleNodeR(object):
    def __init__(self, val):
        self.val = val
        self.next_node = None
        self.rand_node = None

    def __str__(self):
        if self.rand_node is not None:
            return f"{self.val}-{self.rand_node.val}"
        else:
            return f"{self.val}"


def get_single_node_list(lis: list) -> SingleNode:
    head = SingleNode(val=lis.pop(0))
    c_node = head

    while lis:
        next_node = SingleNode(val=lis.pop(0))
        c_node.set_next_node(node=next_node)
        c_node = next_node
    return head

def get_single_node_listR(lis: list) -> SingleNodeR:
    head = SingleNodeR(val=lis.pop(0))
    c_node = head

    while lis:
        next_node = SingleNodeR(val=lis.pop(0))
        c_node.next_node = next_node
        c_node = next_node
    return head


# define function
def func1(head: SingleNode):
    """
    反转单项链表和反转双向链表的函数
    要求：如果链表长度为N，时间复杂度要求为O(N), 额外空间复杂度为O(1)
    :return:
    """
    last_node = None
    c_node = head
    while c_node:
        # print(c_node.val)
        next_node = c_node.next_node
        c_node.next_node = last_node
        c_node, last_node = next_node, c_node
    return last_node

def func2(head1: SingleNode, head2: SingleNode):
    """
    Description :
    【题目】：给定两个有序链表的头指针 head1 和 head2, 打印两个链表的公共部分。
    【要求】：如果两个链表的长度之和为N， 时间复杂度要求为 O(N) 额外空间复杂度为 O(1)

    补充：面试链表题的方法论：
        1. 对于笔试，不用太在乎空间复杂度，一切为了时间复杂度
        2. 对于面试，时间复杂度依然安放在第一位，但是一定要找到空间最省的方法

    补充： 重要的技巧
        1. 额外数据结构记录
        2. 快慢指针


    result : 打印两个单向链表的公共部分
    :return:
    """
    # 判断链表是否有环
    if_have_loop1, enter_loop_node1 = func_2_loop(head=head1)
    if_have_loop2, enter_loop_node2 = func_2_loop(head=head2)

    # 有环的情况
    if if_have_loop1 and if_have_loop2:
        # 对入环点做一个判断
        if id(enter_loop_node1) == id(enter_loop_node2):
            # 如果入环点相同，那么一定是在一个环当中
            enter_loop_node1.next_node = None
            head1_len = func2_len(head=head1)
            head2_len = func2_len(head=head2)

            head1_point = head1
            head2_point = head2
            if head1_len > head2_len:
                for i in range(head1_len-head2_len):
                    head1_point = head1_point.next_node
            elif head1_len < head2_len:
                for i in range(head2_len-head1_len):
                    head2_point = head2_point.next_node
            else:
                pass

            # 找到公共部分的起点
            while head1_point is not None and head2_point is not None:
                if id(head1_point) == id(head2_point):
                    print(f"公共部分的起点是 {head1_point.val}")
                    break

            # 开始打印公共部分
            print("开始打印两个链表的公共部分")
            while head1_point is not None:
                print(head1_point.val)
                head1_point = head1_point.next_node

        else:
            # 如果入环的点不一样：1. 两个单链表是否有公共部分？2. 如果有公共部分，这个环就是他们的公共部分
            p1 = enter_loop_node1.next_node
            if_two_head_in_a_same_loop = False
            while True:
                if id(p1) == id(enter_loop_node1):
                    if_two_head_in_a_same_loop = False
                    break
                elif id(p1) == id(enter_loop_node2):
                    if_two_head_in_a_same_loop = True
                    break
                else:
                    p1 = p1.next_node

            if if_two_head_in_a_same_loop:
                # 如果在一个环当中，那个这个环就是公共部分
                p1 = enter_loop_node1.next_node
                enter_loop_node1.next_node = None
                # 开始打印公共部分
                print("开始打印两个链表的公共部分")
                while p1 is not None:
                    print(p1.val)
                    p1 = p1.next_node

            else:
                print("两个单链表没有公共部分")

    elif (if_have_loop1 and not if_have_loop2) or (not if_have_loop1 and if_have_loop2):
        # 一个有环，一个无环，则没有公共部分
        print("两个单链表没有公共部分")

    else:
        # 两个都没有环，可能有公共部分
        head1_len = func2_len(head=head1)
        head2_len = func2_len(head=head2)

        head1_point = head1
        head2_point = head2
        if head1_len > head2_len:
            for i in range(head1_len - head2_len):
                head1_point = head1_point.next_node
        elif head1_len < head2_len:
            for i in range(head2_len - head1_len):
                head2_point = head2_point.next_node
        else:
            pass

        # 找到公共部分的起点
        while head1_point is not None and head2_point is not None:
            if id(head1_point) == id(head2_point):
                print(f"公共部分的起点是 {head1_point.val}")
                break

        print(f"开始打印两个单链表的公共部分")
        while head1_point:
            print(head1_point.val)
            head1_point = head1_point.next_node


def func_2_loop(head: SingleNode):
    """
    1. 判断链表是否有环；
    2. 如果链表有环，找到入环点
    :param head:
    :return:
    """
    p1 = head
    p2 = head.next_node

    if_have_loop = False
    while p1 is not None and p2 is not None:
        if id(p1) == id(p2):
            if_have_loop = True
            break

        p1 = p1.next_node
        p2 = p2.next_node
        if p2 is not None:
            p2 = p2.next_node

    # 如果有环， 找到入环点
    enter_loop_node = None
    if if_have_loop:
        p1 = head
        p2 = p2.next_node
        while True:
            print(f"p1={p1.val}, p2={p2.val}")
            if id(p1) == id(p2):
                enter_loop_node = p1
                break
            p1 = p1.next_node
            p2 = p2.next_node

    return if_have_loop, enter_loop_node

def fun2_get_tail(head: SingleNode) -> SingleNode:
    p_tail = head
    while p_tail.next_node is not None:
        p_tail = p_tail.next_node
    return p_tail

def func2_len(head: SingleNode):
    """
    返回单链表的长度
    :param head:
    :return:
    """
    p = head

    length = 0
    while p is not None:
        length += 1
        p = p.next_node

    return length


def func3():
    """
    题目：判断单链表是否是回文结构，就是链表正着念和反着念一样
    :return:
    """
    pass

def func4():
    """
    获取一个单链表的 center node 和 last node
    :return:
    """
    pass

def func5(head: SingleNode, num):
    """
    【题目】： 将单向链表按某值划分成左边小，中间相等，右边大的形式
        给定一个单链表的头节点head, 节点的值类型是整形，在给定一个数num, 实现一个调整列表节点的函数，将链表调整为左边部分小于num,
    中间部分等于num， 右边部分大于num。

    【题目进阶】
        1. 调整后所有小于num 的节点之间的相对顺序和调整之前一样
        2. 调整后所有等于 。。。
        3. 调整后所有大于 。。。
        4. 时间复杂度 O(N), 额外空间复杂度 O(1)
    :return:
    """
    less_node_head = None
    less_node_tail = None
    equal_node_head = None
    equal_node_tail = None
    great_node_head = None
    great_node_tail = None

    c_node = head
    while True:
        if c_node is None:
            break

        if c_node.val < num:
            if less_node_head is None:
                less_node_head = c_node
                less_node_tail = c_node
            else:
                less_node_tail.set_next_node(c_node)
                less_node_tail = c_node
        elif c_node.val == num:
            if equal_node_head is None:
                equal_node_head = c_node
                equal_node_tail = c_node
            else:
                equal_node_tail.set_next_node(c_node)
                equal_node_tail = c_node
        else:
            if great_node_head is None:
                great_node_head = c_node
                great_node_tail = c_node
            else:
                great_node_tail.set_next_node(c_node)
                great_node_tail = c_node

        c_node = c_node.next_node

    less_node_tail.set_next_node(equal_node_head)
    equal_node_tail.set_next_node(great_node_head)
    return less_node_head

def func6(head: SingleNodeR):
    """
    next指针和正常单链表中next指针的意义 一 样，都指向下一个节点，
    rand指针是Node类中新增的指针，这个指针可能指向链表中的任意一个节点，也可能指向null。
     给定一个由 Node节点类型组成的无环单链表的头节点head，
     请实现一个 函数完成 这个链表中所有结构的复制，并返回复制的新链表的头节点。
    :return:
    """
    # 复制单链表
    p1 = head
    while p1:
        p1_n = p1.next_node
        new_p1 = SingleNodeR(val=p1.val)
        p1.next_node = new_p1
        new_p1.next_node = p1_n

        p1 = p1_n
        if p1 is None:
            break

    print("打印单链表")
    print_single_node(head)

    # 添加rand node
    p1 = head
    new_p1: SingleNodeR = head.next_node
    while True:
        if p1.rand_node is not None:
            new_p1.rand_node = p1.rand_node.next_node
        p1 = p1.next_node.next_node
        if p1 is None:
            break
        new_p1 = new_p1.next_node.next_node


    # 将复制的单链表拆分出来
    p1 = head
    new_head = head.next_node
    new_p1: SingleNodeR = new_head
    while True:
        print(p1.val, new_p1.val)
        old_next_node = p1.next_node.next_node
        new_new_node = new_p1.next_node.next_node

        p1.next_node = old_next_node
        new_p1.next_node = new_new_node

        p1 = p1.next_node
        new_p1 = new_p1.next_node

        if new_p1.next_node is None:
            p1.next_node = None
            break

    return new_head


def print_single_node(head: SingleNode):
    c_node = head
    while True:
        print(c_node.val)
        c_node = c_node.next_node
        if c_node is None:
            break


# define main
def main1():
    s_node_list = get_single_node_list(lis=[2, 3, 1, 4, 2, 5, 7])

    # 打印单项链表
    print("打印单链表")
    print_single_node(head=s_node_list)

    # 反转单向链表
    print("打印reverse 单链表")
    s_node_list = func1(s_node_list)
    print_single_node(head=s_node_list)
    pass

def main2():
    head1 = get_single_node_list(lis=[2, 3, 1, 4, 2, 5, 7])
    head2 = get_single_node_list(lis=[20, 30, 10, 40, 20, 50, 70])

    # 添加环
    p_loop = head1.next_node.next_node.next_node
    head1_tail = fun2_get_tail(head=head1)
    head1_tail.next_node = p_loop

    # 将head2 和 head1 拼接
    head2_tail = fun2_get_tail(head=head2)
    head2_tail.next_node = p_loop.next_node.next_node

    func2(head1=head1, head2=head2)

def main2_loop():
    """
    """
    s_node_list = get_single_node_list(lis=[2, 3, 1, 4, 2, 5, 7])

    # 添加环
    p_loop = s_node_list.next_node.next_node.next_node
    p_tail = s_node_list
    while p_tail.next_node is not None:
        p_tail = p_tail.next_node
    p_tail.next_node = p_loop

    # 判断是否有环，以及入环点
    if_have_loop, enter_loop_node = func_2_loop(head=s_node_list)
    print(if_have_loop)
    print(enter_loop_node.val)


def main5():
    s_node_list = get_single_node_list(lis=[2, 3, 1, 4, 4, 2, 5, 7])
    print("打印原始node")
    print_single_node(head=s_node_list)

    new_node_list = func5(head=s_node_list, num=4)
    print("打印处理后的node")
    print_single_node(head=new_node_list)
    pass

def main6():
    head = get_single_node_listR(lis=[2, 3, 1, 4, 2, 5, 7])

    new_head = func6(head=head)


# main
if __name__ == '__main__':
    main6()
