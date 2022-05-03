# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-29
Description :
auther : wcy
"""
# import modules
import os

__all__ = []


# define class
class NewCls(object):
    def __init__(self, data_list):
        self.data_list: list = data_list
        self.max_len = len(self.data_list)
        self.stack = list()
        self.left = -1
        self.right = 0

    def move_left(self):
        if self.left < self.right:
            v = self.data_list[self.left]
            if v == self.stack[0]:
                self.stack.pop(0)
            self.right += 1
        else:
            raise ValueError("can not move")

    def move_right(self):
        if self.right < len(self.data_list):
            v = self.data_list[self.right]
            while self.stack:
                if self.stack[-1] < v:
                    self.stack.pop(-1)
                else:
                    self.stack.append(v)
                    break

            if len(self.stack) == 0:
                self.stack.append(v)
            self.right += 1
        else:
            raise ValueError("can not move")

    def get_max(self):
        return self.stack[0]


# define function
def func1():
    """单调栈"""
    """
    data_list = [1, 5, 4, 3, 7, 6, 9, 10]
    找左边和右边都比这个数小的的最近的数
    """
    pass


# define main
def main1():
    print("单调栈")

    pass


def main2():
    print("双端队列")
    data_list = [3, 2, 4, 1, 2, 6, 0, 1, 7]
    nc = NewCls(data_list=data_list)
    nc.move_right()
    nc.move_right()
    print(nc.get_max())
    print(nc.stack)
    nc.move_right()
    print(nc.get_max())
    print(nc.stack)
    pass


# main
if __name__ == '__main__':
    main1()
    main2()