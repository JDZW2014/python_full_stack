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
class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_dict = {}

class PrefixTree(object):
    def __init__(self):
        self.root = Node(key='root', value=0)

    def add_words(self, words):
        words = list(words)

        # 找到起始的第一个点
        node = self.root
        node.value += 1

        while words:
            w = words.pop(0)
            if w not in node.next_dict:
                new_node = Node(key=w, value=0)
                node.next_dict[w] = new_node
            node = node.next_dict[w]
            node.value += 1

            print(f"{node.key} -- {node.next_dict.keys()}")

    def get_prefix_freq(self, prefix):
        prefix = list(prefix)

        node = self.root

        freq = 0
        while prefix:
            w = prefix.pop(0)
            if w in node.next_dict:
                node = node.next_dict[w]
                freq = node.value
            else:
                freq = 0
                break
        return freq


# define function
def main1():
    pt = PrefixTree()
    pt.add_words('abc')
    pt.add_words('aba')
    pt.add_words('aaa')

    ret = pt.get_prefix_freq("ab")
    print(ret)



# main
if __name__ == '__main__':
    main1()
