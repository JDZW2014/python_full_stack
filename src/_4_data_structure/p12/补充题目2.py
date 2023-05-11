# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2023/5/8
Description :
auther : wcy
"""
# import modules
import os

__all__ = []


# define class
class Stack(object):
    def __init__(self):
        self.lis = list()
        self.min_lis = list()

    def get_min(self):
        return self.min_lis[-1]

    def pop(self):
        val = self.lis.pop(-1)
        if val == self.min_lis[-1]:
            self.min_lis.pop(-1)
        return val

    def push(self, val):
        self.lis.append(val)
        if len(self.min_lis) > 0:
            if val <= self.min_lis[-1]:
                self.min_lis.append(val)
        else:
            self.min_lis.append(val)


# define main
def main1():
    lis = [3, 2, 5, 1, 6]
    stack = Stack()
    stack.push(3)
    print(stack.lis, stack.get_min())
    stack.push(2)
    print(stack.lis, stack.get_min())
    stack.push(5)
    print(stack.lis, stack.get_min())
    stack.pop()
    print(stack.lis, stack.get_min())
    stack.push(1)
    print(stack.lis, stack.get_min())


# main
if __name__ == '__main__':
    main1()
