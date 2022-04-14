# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-14
Description :
auther : wcy
"""
# import modules
import os, typing

__all__ = ["Node_"]


# define class
class Node(object):
    __slots__ = ["value", "pass_", "end_", "next_node_map"]

    def __init__(self, value: str):
        self.value = value
        self.pass_ = 0
        self.end_ = 0
        self.next_node_map = {}

    def get_value(self, ):
        return self.value

    def get_pass(self, ):
        return self.pass_

    def get_end(self, ):
        return self.end_

    def add_pass(self, v: int=1):
        self.pass_ += v

    def add_end(self, v: int=1):
        self.end_ += v

    def get_next_node(self, word):
        return self.next_node_map.get(word, None)

    def add_next_node(self, k, v):
        self.next_node_map[k] = v


class Trie(object):
    def __init__(self):
        self.root = Node(value='')

    def add(self, s):
        s = list(s)
        node = self.root
        node.add_pass()
        while s:
            word = s.pop(0)
            next_node = node.get_next_node(word=word)
            # 如果没有这个next node 就新建
            if next_node is None:
                next_node = Node(value=word)
                node.add_next_node(word, next_node)
            next_node.add_pass()
            node = next_node
        node.add_end()

    def search_word(self, s):
        s = list(s)
        node = self.root
        while s:
            word = s.pop(0)
            next_node = node.get_next_node(word)
            if next_node is None:
                return 0
            else:
                node = next_node

        return node.get_end()

    def search_prefix(self, s):
        s = list(s)
        node = self.root
        while s:
            word = s.pop(0)
            next_node = node.get_next_node(word)
            if next_node is None:
                return 0
            else:
                node = next_node

        return node.get_pass()

    def delete(self, s):
        search_result = self.search_word(s)
        if search_result:
            self._delete_(s)

    def _delete_(self, s):
        s = list(s)
        node = self.root
        node.add_pass(-1)
        while s:
            word = s.pop(0)
            next_node = node.get_next_node(word)
            next_node.add_pass(-1)
            node = next_node
        node.add_end(-1)


# define test
def test():
    data_list = ["abc", "abd", "acd", "cda", "abcd"]
    trie = Trie()
    for data in data_list:
        trie.add(s=data)
    print(trie.search_word("abcd"))
    print(trie.search_word("abcde"))
    print(trie.search_prefix("ab"))

    print("--- 测试delete : 之前---")
    trie.add('abc')
    print(trie.search_word("abc"))
    print(trie.search_prefix("ab"))
    print("--- 测试delete : 之后---")
    trie.delete("abc")
    print(trie.search_word("abc"))
    print(trie.search_prefix("ab"))


# main
if __name__ == '__main__':
    test()
