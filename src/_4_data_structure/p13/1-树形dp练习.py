# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-18
Description :
auther : wcy
"""
# import modules
import os

__all__ = []


# define class
class Staff(object):
    __slots__ = ["name", "happiness_value", "next_node"]

    def __init__(self, name, happiness_value):
        self.name = name
        self.happiness_value = happiness_value
        self.next_node = []

    def add_next_node(self, node):
        if isinstance(node, list):
            self.next_node.extend(node)
        else:
            self.next_node.append(node)


# define function
def func(head: Staff):
    # final case
    if len(head.next_node) == 0:
        max_c = head.happiness_value
        max_nc = 0
        return [max_c], [max_nc]

    r_max_c_list = [head.happiness_value]
    r_max_nc_list = []
    for next_node in head.next_node:
        n_max_c_list, n_max_nc_list = func(next_node)
        r_max_c_list.extend(n_max_nc_list)
        if sum(n_max_c_list) > sum((n_max_nc_list)):
            r_max_nc_list.extend(n_max_c_list)
        else:
            r_max_nc_list.extend(n_max_nc_list)

    return r_max_c_list, r_max_nc_list


# main
if __name__ == '__main__':
    head = Staff(name="boss", happiness_value=3)
    l10 = Staff(name="l12", happiness_value=20)
    l11 = Staff(name="l12", happiness_value=10)
    l12 = Staff(name="l12", happiness_value=300)
    l13 = Staff(name="l12", happiness_value=70)

    l20 = Staff(name="l20", happiness_value=1000)
    l21 = Staff(name="l21", happiness_value=20)
    l22 = Staff(name="l22", happiness_value=30)
    l23 = Staff(name="l23", happiness_value=300)
    l24 = Staff(name="l24", happiness_value=1)
    l25 = Staff(name="l25", happiness_value=10)
    l26 = Staff(name="l26", happiness_value=20)
    l27 = Staff(name="l27", happiness_value=90)
    l28 = Staff(name="l28", happiness_value=900)

    head.add_next_node([l10, l11, l12, l13])

    l10.add_next_node([l20, l21, l22])
    l11.add_next_node([l23, l24])
    l12.add_next_node([l25, l26])
    l13.add_next_node([l27, l28])

    print(func(head=head))