# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-11
Description :
    【题目】： 给定两个有序链表的头指针 head1 和 head2, 打印两个链表的公共部分。
    【要求】：如果两个链表的长度之和为N， 时间复杂度要求为 O(N) 额外空间复杂度为 O(1)

补充：面试链表题的方法论：
    1. 对于笔试，不用太在乎空间复杂度，一切为了时间复杂度
    2. 对于面试，时间复杂度依然安放在第一位，但是一定要找到空间最省的方法

补充： 重要的技巧
    1. 额外数据结构记录
    2. 快慢指针
auther : wcy
"""
# import modules
from src._4_data_structure.p4.base_model import SNode, DNode, get_single_node_list, get_double_node_list, \
    print_single_node, print_double_node

__all__ = []


# define function
def func(node1, node2):
    while node1 and node2:
        if node1.get_value() == node2.get_value():
            print(node1.get_value())
            node1 = node1.get_next_node()
            node2 = node2.get_next_node()
        elif node1.get_value() < node2.get_value():
            node1 = node1.get_next_node()
        else:
            node2 = node2.get_next_node()


# main
if __name__ == '__main__':
    head1 = get_single_node_list(lis=[1, 2, 3, 4, 5, 6])
    head2 = get_single_node_list(lis=[3, 5, 7])
    func(node1=head1, node2=head2)
