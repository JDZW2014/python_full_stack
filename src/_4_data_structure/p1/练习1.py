# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-21
Description :
auther : wcy
"""
# import modules
import os, typing, random

__all__ = []


# define class
class MinStack(object):
    """
    实现一个小顶堆的结构
    """
    __slots__ = ["data_list", "heap_size"]

    def __init__(self):
        self.data_list = list()
        self.heap_size = 0

    def add_data(self, val):
        self.data_list.append(val)
        self.heap_size += 1

        idx = self.heap_size-1
        while idx > 0:
            h_idx = (idx-1 // 2)
            if h_idx >= 0:
                if self.data_list[idx] < self.data_list[h_idx]:
                    self.data_list[idx], self.data_list[h_idx] = self.data_list[h_idx], self.data_list[idx]
                    idx = h_idx
                else:
                    break
            else:
                break

    def head_pop(self, ):
        self.data_list[0], self.data_list[self.heap_size-1] = self.data_list[self.heap_size-1], self.data_list[0]
        ret_val = self.data_list.pop()
        self.heap_size -= 1

        idx = 0
        while True:
            if idx < self.heap_size:
                l_idx = idx * 2 + 1
                r_idx = idx * 2 + 2

                if l_idx < self.heap_size and r_idx < self.heap_size:
                    if self.data_list[l_idx] < self.data_list[r_idx]:
                        if self.data_list[l_idx] < self.data_list[idx]:
                            self.data_list[l_idx], self.data_list[idx] = self.data_list[idx], self.data_list[l_idx]
                            idx = l_idx
                        else:
                            break
                    else:
                        if self.data_list[r_idx] < self.data_list[idx]:
                            self.data_list[r_idx], self.data_list[idx] = self.data_list[idx], self.data_list[r_idx]
                            idx = r_idx
                        else:
                            break

                elif l_idx >= self.heap_size and r_idx < self.heap_size:
                    if self.data_list[r_idx] < self.data_list:
                        self.data_list[r_idx], self.data_list[idx] = self.data_list[idx], self.data_list[r_idx]
                        idx = r_idx
                    else:
                        break

                elif l_idx < self.heap_size and r_idx >= self.heap_size :
                    if self.data_list[l_idx] < self.data_list[idx]:
                        self.data_list[l_idx], self.data_list[idx] = self.data_list[idx], self.data_list[l_idx]
                        idx = l_idx
                else:
                    break
            else:
                break

        return ret_val

    def __len__(self):
        return self.heap_size


# define function
def func1(data_list: typing.List[int]):
    """
    冒泡排序
    """
    data_len = len(data_list)
    for i in range(data_len-1):
        for j in range(data_len-1-i):
            if data_list[j] > data_list[j+1]:
                data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
    return data_list


def func2(data_list: typing.List[int]):
    """
    插入排序
    """
    data_len = len(data_list)
    for i in range(1, data_len):
        while i - 1 >= 0:
            if data_list[i] < data_list[i-1]:
                data_list[i], data_list[i-1] = data_list[i-1], data_list[i]
                i -= 1
            else:
                break
    return data_list


def func3(data_list: typing.List[int]):
    """
    选择排序
    """
    pass


def func4(data_list: typing.List[int]):
    """
    归并排序
    """
    data_len = len(data_list)
    if data_len <= 1:
        return data_list
    else:
        mid = data_len // 2
        lis1 = func4(data_list[0: mid])
        lis2 = func4(data_list[mid:])

        data_list = []
        data1 = None
        data2 = None
        while lis1 and lis2:
            if data1 is None:
                data1 = lis1.pop(0)
            if data2 is None:
                data2 = lis2.pop(0)

            if data1 < data2:
                data_list.append(data1)
                data1 = None
            else:
                data_list.append(data2)
                data2 = None
        if data1:
            data_list.append(data1)
        if data2:
            data_list.append(data2)

        if lis1:
            data_list.extend(lis1)
        if lis2:
            data_list.extend(lis2)

        return data_list


def func5(data_list: typing.List[int], left_idx, right_idx):
    """
    快排
    """
    if right_idx - left_idx <= 1:
        return data_list
    else:
        random.shuffle(data_list[left_idx: left_idx])

        eql_idx_l = left_idx
        val = data_list[eql_idx_l]
        get_idx_l = right_idx - 1

        idx = left_idx
        while idx == get_idx_l:
            if data_list[idx] > val:
                data_list[idx], data_list[get_idx_l] = data_list[get_idx_l], data_list[idx]
                get_idx_l -= 1
            elif data_list[idx] == val:
                idx += 1
            else:
                data_list[idx], data_list[eql_idx_l] = data_list[eql_idx_l], data_list[idx]
                idx += 1

        func5(data_list=data_list, left_idx=left_idx, right_idx=eql_idx_l)
        func5(data_list=data_list, left_idx=get_idx_l, right_idx=right_idx)
        return data_list


def func6(data_list: typing.List[int]):
    """
    堆排
    """
    ms = MinStack()
    while data_list:
        ms.add_data(data_list.pop())

    while len(ms) > 0:
        data_list.append(ms.head_pop())

    return data_list


# main
if __name__ == '__main__':
    data_list = [3, 4, 1, 2, 4, 7, 9, 8]
    print(func1(data_list=data_list))
    print(func2(data_list=data_list))
    print(func3(data_list=data_list))
    print(func4(data_list=data_list))
    print(func5(data_list=data_list, left_idx=0, right_idx=len(data_list)))
    print(func6(data_list=data_list))
