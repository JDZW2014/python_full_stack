# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-17
Description :
auther : wcy
"""
# import modules
import os, typing

__all__ = []


# define function
def func(data_list: typing.List[int]):
    """
    这个函数方法只是适用于没有重复数据的情况，

    重点思考： 如果遇到了重复的情况 要怎么做？？？
    """
    stack = list()
    result_list = []
    while data_list:
        print(stack)
        data = data_list.pop(0)
        if len(stack) == 0:
            stack.append(data)
        else:
            if data > stack[-1]:
                stack.append(data)
            else:
                while len(stack) > 0 and stack[-1] > data:
                    pop_data = stack.pop()
                    if len(stack) > 0:
                        lm = stack[-1]
                    else:
                        lm = None
                    result_list.append((pop_data, lm, data))
                stack.append(data)

    while stack:
        data = stack.pop()
        if len(stack) > 0:
            lm = stack[-1]
        else:
            lm = None
        result_list.append((data, lm, None))

    return result_list


# main
if __name__ == '__main__':
    data_list = [1, 5, 4, 3, 7, 6, 9, 10]
    print(func(data_list=data_list))
