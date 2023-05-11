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


# define class
class DataNode(object):
    __slots__ = ["idx", "data"]

    def __init__(self, idx, data):
        self.idx = idx
        self.data = data


class MaxDQueue(object):
    def __init__(self, data_list: typing.List[int]):
        self.data_list = data_list
        self.data_list_len = len(data_list)
        self.max_d_queue: typing.List[DataNode] = []
        self.left_idx = 0
        self.right_idx = 0

    def move_left(self):
        if self.left_idx < self.right_idx:
            if self.max_d_queue[0].idx == self.left_idx:
                self.max_d_queue.pop(0)
            self.left_idx += 1
        else:
            raise ValueError("illegal move")

    def move_right(self):
        if self.right_idx < self.data_list_len - 1:
            data = DataNode(idx=self.right_idx, data=self.data_list[self.right_idx])
            while self.max_d_queue:
                if self.max_d_queue[-1].data <= data.data:
                    self.max_d_queue.pop()
                else:
                    break

            self.max_d_queue.append(data)
            self.right_idx += 1
        else:
            raise ValueError("illegal move")

    def current_max(self):
        return self.max_d_queue[0].data


# main
if __name__ == '__main__':
    data_list = [3, 2, 4, 1, 2, 6, 0, 1, 7]
    max_d_queue = MaxDQueue(data_list=data_list)

    # move left and right scope
    max_d_queue.move_right()
    max_d_queue.move_right()

    print([data.data for data in max_d_queue.max_d_queue])

    max_d_queue.move_left()
    print([data.data for data in max_d_queue.max_d_queue])

    max_d_queue.move_right()
    print([data.data for data in max_d_queue.max_d_queue])

    max_d_queue.move_right()
    max_d_queue.move_right()
    print([data.data for data in max_d_queue.max_d_queue])

    max_d_queue.move_left()
    max_d_queue.move_left()
    max_d_queue.move_left()
    print([data.data for data in max_d_queue.max_d_queue])




