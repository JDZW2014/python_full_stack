# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-17
Description :
auther : wcy
"""
# import modules
import os, typing, json

__all__ = []


# define class
class Data(object):
    __slots__ = ["value", "index_list"]

    def __init__(self, value):
        self.value = value
        self.index_list = []

    def add_index(self, idx_list):
        self.index_list.extend(idx_list)

    def to_str(self):
        return json.dumps([self.value, self.index_list])


# define function
def func(data_list: typing.List[Data]):
    stack: typing.List[Data] = list()
    data_len = len(data_list)

    ret_list = []
    while data_list:
        data = data_list.pop(0)

        if len(stack) == 0:
            stack.append(data)
        else:
            while len(stack) > 0 and stack[-1].value > data.value:
                pop_data = stack.pop()
                if len(stack) > 0:
                    l_idx = max(stack[-1].index_list) + 1
                else:
                    l_idx = 0

                ret_list.append((pop_data.to_str(), l_idx, data.index_list[0]))
            if len(stack) > 0 and stack[-1].value == data.value:
                stack[-1].add_index(data.index_list)
            else:
                stack.append(data)

    while stack:
        pop_data = stack.pop()
        if len(stack) > 0:
            l_idx = max(stack[-1].index_list) + 1
        else:
            l_idx = 0

        ret_list.append((pop_data.to_str(), l_idx, data_len))

    # todo 基于ret_list 的结果获取最终值就可以

    return ret_list


# main
if __name__ == '__main__':
    data_list = []
    for i, d in enumerate([5, 2, 3, 2, 1, 6, 7, 8, 4]):
        data = Data(value=d)
        data.add_index([i])
        data_list.append(data)

    print(func(data_list=data_list))
