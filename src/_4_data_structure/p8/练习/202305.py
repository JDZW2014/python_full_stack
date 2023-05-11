# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2023/5/7
Description :
auther : wcy
"""
# import modules
import os

__all__ = []

# define class
class Heap(object):
    max_or_min = None

    def __init__(self):
        self.lis = list()
        self.size = 0

    def add(self, val):
        self.size += 1
        self.lis.append(val)

        idx = self.size - 1

        while idx > 0:
            father_idx = self.get_father(idx=idx)
            if father_idx is not None:
                if self.compare(self.lis[idx], self.lis[father_idx]):
                    self.lis[idx], self.lis[father_idx] = self.lis[father_idx], self.lis[idx]
                    idx = father_idx
                else:
                    break
            else:
                break

    def pop(self):
        self.lis[0], self.lis[-1] = self.lis[-1], self.lis[0]
        pop_val = self.lis.pop(-1)
        self.size -= 1

        idx = 0
        while idx < self.size:
            left_son, right_son = self.get_son(idx)

            if left_son is not None and right_son is not None:
                if self.compare(self.lis[idx], self.max_or_min(self.lis[left_son], self.lis[right_son])):
                    break

                elif self.compare(self.lis[left_son], self.max_or_min(self.lis[idx], self.lis[right_son])):
                    self.lis[idx], self.lis[left_son] = self.lis[left_son], self.lis[idx]
                    idx = left_son

                elif self.compare(self.lis[right_son], self.max_or_min(self.lis[idx], self.lis[left_son])):
                    self.lis[idx], self.lis[right_son] = self.lis[right_son], self.lis[idx]
                    idx = right_son
                else:
                    print("==========")


            elif left_son is not None and right_son is None:
                if self.compare(self.lis[idx], self.lis[left_son]):
                    break
                else:
                    self.lis[idx], self.lis[left_son] = self.lis[left_son], self.lis[idx]


            elif left_son is None and right_son is not None:
                if self.compare(self.lis[idx], self.lis[right_son]):
                    break
                else:
                    self.lis[idx], self.lis[right_son] = self.lis[right_son], self.lis[idx]

            else:
                break
        return pop_val

    def get_son(self, idx):
        left_son = idx * 2 + 1
        right_son = idx * 2 + 2

        if left_son >= self.size:
            left_son = None

        if right_son >= self.size:
            right_son = None

        return left_son, right_son

    def get_father(self, idx):
        father_idx = int((idx - 1) / 2)
        if father_idx < 0:
            father_idx = None

        return father_idx

    def compare(self, v1, v2):
        pass


class MaxHeap(Heap):
    max_or_min = max
    def compare(self, v1, v2):
        return v1 >= v2


class MinHeap(Heap):
    max_or_min = min
    def compare(self, v1, v2):
        return v1 <= v2




# define function
def func1(lis):
    """
    切金条
    :return:
    """
    pass

def func2():
    """
    项目规划
    :return:
    """
    pass

def func3():
    """
    会议室问题
    :return:
    """
    pass


def func4(lis: list):
    """
    中位数问题
    一个数据流中，随时可以取得中位数
    :return:
    """
    max_h = MaxHeap()
    min_h = MinHeap()

    val = lis.pop(0)
    max_h.add(val)

    while lis:
        val = lis.pop(0)
        # 根据两个堆的size 分情况讨论
        if min_h.size == max_h.size:
            if val <= max_h.lis[0]:
                max_h.add(val)
            else:
                min_h.add(val)

        elif min_h.size > max_h.size:
            if val < min_h.lis[0]:
                max_h.add(val)
            else:
                min_h.add(val)
                val = min_h.pop()
                max_h.add(val)
        else:
            if val > max_h.lis[0]:
                min_h.add(val)
            else:
                max_h.add(val)
                val = max_h.pop()
                min_h.add(val)

    # 返回中位数
    if max_h.size == min_h.size:
        return (max_h.lis[0], min_h.lis[0])

    elif max_h.size > min_h.size:
        return max_h.lis[0]
    else:
        return min_h.lis[0]


def func5(num, curr_line, total_lines, can_not_use_col: set):
    """
    n皇后问题
    :return:
    """
    # 递归停止条件
    if curr_line > total_lines:
        return 1

    # 递归调用
    valid_lis = []

    can_not_use_col
    for i in range(1, total_lines):
        if i not in can_not_use_col:

            # 更新不可用的col
            for val in list(can_not_use_col) + [i]:

                # 这个处理的逻辑有问题，需要修改
                new_can_not_use_col.add(val)
                new_can_not_use_col.add(val-1)
                new_can_not_use_col.add(val+1)

            ret = func5(num=num-1, curr_line=curr_line+1,
                        total_lines=total_lines,
                        can_not_use_col=new_can_not_use_col)
            valid_lis.append(ret)
    if sum(valid_lis) == 0:
        pass
    return sum(valid_lis)

# main
def main1():
    func1(lis=[10, 20, 30, 40])


def main4():
    lis = [1, 2, 3, 2, 5, 9]
    print("测试大顶堆")
    max_h = MaxHeap()
    for val in lis:
        max_h.add(val)

    sort_val = []
    while max_h.size > 0:
        sort_val.append(max_h.pop())
    print(sort_val)

    print("测试小顶堆")
    min_h = MinHeap()
    for val in lis:
        min_h.add(val)

    sort_val = []
    while min_h.size > 0:
        sort_val.append(min_h.pop())
    print(sort_val)

    print("数据流，求中位数")
    ret = func4(lis=lis.copy())
    print(lis, "的中位数是", ret)
    lis = [1, 2, 3, 2, 5, 9, 100]
    ret = func4(lis=lis.copy())
    print(lis, "的中位数是", ret)


def main5():
    ret = func5(num=9, curr_line=1, total_lines=9, can_not_use_col=set())
    print(ret)


# main
if __name__ == '__main__':
    main5()

