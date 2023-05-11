# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2023/5/6
Description :
auther : wcy
"""
# import modules
import os

__all__ = []

# define class
class BTree(object):
    def __init__(self, head):
        self.head = head
        self.left = None
        self.right = None


# define function
def func1(node: BTree):
    """
    判断搜索二叉树
    :return:
    """
    # 递归终止条件
    if node is None:
        return True, None

    # 递归调用
    left_bool, left_max = func1(node=node.left)
    right_bool, right_max = func1(node=node.right)

    print(f"left_bool = {left_bool}, left_max = {left_max}, right_bool = {right_bool}, right_max={right_max}")

    if left_bool and right_bool:
        # 分情况讨论
        if left_max is not None and right_max is not None:
            if node.head > left_max and node.head < right_max:
                return True, right_max

        elif left_max is not None and right_max is None:
            if node.head > left_max:
                return True, node.head

        elif left_max is None and right_max is not None:
            if node.head < right_max:
                return True, right_max
        else:
            return True, node.head

    return False, None

def func2(node: BTree):
    """
    二叉树，宽度优先遍历
    :return:
    """
    node_list = [node]
    while node_list:
        node = node_list.pop(-1)
        print(node.head)
        if node.left is not None:
            node_list = [node.left] + node_list

        if node.right is not None:
            node_list = [node.right] + node_list

def func2_wan_quan_er_cha_shu(node: BTree):
    not_complete_node = False

    node_list = [node]
    while node_list:
        node = node_list.pop(-1)
        # print(node.head)

        if not_complete_node is False:
            if node.left is not None and node.right is not None:
                node_list = [node.left] + node_list
                node_list = [node.right] + node_list

            elif node.left is not None and node.right is None:
                node_list = [node.left] + node_list
                not_complete_node = True

            elif node.left is None and node.right is not None:
                return False
        else:
            if node.left is not None or node.right is not None:
                return False

    return True


def func3(head: BTree):
    """
    二叉树，深度优先遍历
    其实深度遍历就是上面的前序、中序和后序。但是为了保证与广度优先遍历相照应，也写在这。代码也比较好理解，其实就是前序遍历，代码如下：
    :return:
    """
    node_list = [head]
    while node_list:
        node = node_list.pop(-1)
        print(node.head)

        if node.right is not None:
            node_list = node_list + [node.right]

        if node.left is not None:
            node_list = node_list + [node.left]

def func4_qian(head: BTree):
    """
    前序遍历：根结点 ---> 左子树 ---> 右子树
    :return:
    """
    travel_list = []
    if_bott = False

    node_list = [head]
    while node_list:
        node = node_list.pop(-1)
        travel_list.append(node)

        if node.right is not None:
            node_list = node_list + [node.right]

        if node.left is not None:
            node_list = node_list + [node.left]

    print([node.head for node in travel_list])
    return travel_list

def func4_zhong(head: BTree):
    """
    中序遍历：左子树---> 根结点 ---> 右子树
    :return:
    """
    travel_list = []
    if_bott = False

    node_list = [head]
    while node_list:
        node = node_list.pop(-1)

        if if_bott is False:
            # 没有到底
            if node.left is not None:
                node_list.append(node)
                node_list.append(node.left)
            else:
                travel_list.append(node)
                if node.right is not None:
                    node_list.append(node.right)
                else:
                    if_bott = True

        else:
            # 已经到低
            travel_list.append(node)
            if node.right is not None:
                node_list.append(node.right)
                if_bott = False
    return travel_list

def func4_zhong_rec(head: BTree):
    """
    中序遍历：左子树---> 根结点 ---> 右子树
    :return:
    """
    travel_list = []
    # 递归停止条件
    if head.left is None and head.right is None:
        travel_list.append(head)
        return travel_list

    # 递归调用
    if head.left is not None:
        travel_list = travel_list + func4_zhong_rec(head.left)

    travel_list.append(head)

    if head.right is not None:
        travel_list = travel_list + func4_zhong_rec(head.right)

    return travel_list

def func4_hou(head: BTree):
    """
    后序遍历：左子树 ---> 右子树 ---> 根结点
    :return:
    """
    ret = func4_qian(head=head)
    travel_list = []
    for node in ret[::-1]:
        travel_list.append(node)
    return travel_list

def func4_hou_2(head: BTree):
    """
    中序遍历：左子树---> 根结点 ---> 右子树
    :return:
    """
    travel_list = []
    if_bott = False

    node_list = [head]
    while node_list:
        node = node_list.pop(-1)

        if if_bott is False:
            # 没有到底
            if node.left is not None:
                node_list.append(node)
                node_list.append(node.left)
            else:
                if node.right is not None:
                    travel_list.append(node)
                    node_list.append(node.right)
                else:
                    travel_list.append(node)
                    if_bott = True

        else:
            # 已经到低
            if node.right is not None:
                node_list.append(node)
                node_list.append(node.right)
                if_bott = False
            else:
                travel_list.append(node)

    return travel_list

def func5(node: BTree):
    """
    判断二叉树是否是满二叉树
    :param node:
    :return:
    """
    # 递归终止条件
    tree_d = func5_d(node)
    tree_node_num = len(func4_qian(node))
    return tree_node_num == (tree_d ** 2 - 1)

def func5_d(node: BTree):
    """
    判断二叉树是否是满二叉树
    :param node:
    :return:
    """
    # 递归终止条件
    if node.left is None and node.right is None:
        return 1

    # 递归调用
    if node.left is not None:
        left_d = func5(node.left)
    else:
        left_d = 0

    if node.right is not None:
        right_d = func5(node.right)
    else:
        right_d = 0

    return max(left_d, left_d) + 1

def func6(head: BTree, node1: BTree, node2: BTree):
    """
    最低公共祖先节点
    :return:
    """
    # 递归终止条件
    if head.left is None and head.right is None:
        if id(head) == id(node1):
            return node1, None
        elif id(head) == id(node2):
            return node2, None
        else:
            return None, None

    # 递归调用
    find_node_left, co_node_left = None, False
    if head.left is not None:
        find_node_left, co_node_left = func6(head=head.left, node1=node1, node2=node2)

    find_node_right, co_node_right = None, False
    if head.right is not None:
        find_node_right, co_node_right = func6(head=head.right, node1=node1, node2=node2)


    # 下面节点已经找到
    if co_node_left is not None:
        return None, co_node_left
    if co_node_right is not None:
        return None, co_node_right

    # 当前节点找到
    if (id(find_node_left) == id(node1) and id(find_node_right) == id(node2)) or \
        (id(find_node_left) == id(node2) and id(find_node_right) == id(node1)):
        return None, head

    # 当前节点找到一个
    if find_node_left is not None:
        return find_node_left, None
    if find_node_right is not None:
        return find_node_right, None

    # 当前节点一个也没有找到
    return None, None

def func7_to_str(head: BTree):
    """
    二叉树序列化: 宽度优先遍历，包括返回None 的那种
    :return:
    """
    node_list = [head]
    travel_list = []

    while node_list:
        node = node_list.pop(-1)

        travel_list.append(node)

        if node:
            if node.left is not None:
                node_list = [node.left] + node_list
            else:
                node_list = [None] + node_list

            if node.right is not None:
                node_list = [node.right] + node_list
            else:
                node_list = [None] + node_list

    node_list_val = []
    for node in travel_list:
        if node:
            node_list_val.append(str(node.head))
        else:
            node_list_val.append(str(node))

    return "#".join(node_list_val)


def func7_from_str(tree_s: str):
    """
    二叉树反序列化
    :return:
    """
    travel_list = [eval(v) for v in tree_s.split("#")]

    head = travel_list.pop(0)
    head = BTree(head=head)

    node_list = [head]
    while travel_list:
        curr_node = node_list.pop(-1)

        left_node = travel_list.pop(0)
        right_node = travel_list.pop(0)

        if left_node is not None:
            left_node = BTree(head=left_node)
            node_list = [left_node] + node_list
            curr_node.left = left_node

        if right_node is not None:
            right_node = BTree(head=right_node)
            node_list = [right_node] + node_list
            curr_node.right = right_node
    return head

def func9(level, left_or_right):
    """
    折纸问题
    :return:
    """
    # 终止条件
    if level == 1:
        if left_or_right == 'left':
            print(1)
        else:
            print(0)
        return

    # 递归调用，中序遍历
    func9(level=level-1, left_or_right="left")

    if left_or_right == 'left':
        print(1)
    else:
        print(0)

    func9(level=level - 1, left_or_right="right")

# main
def main1():
    node0 = BTree(head=10)

    node1 = BTree(5)
    node2 = BTree(14)

    node3 = BTree(120)
    node4 = BTree(6)
    node5 = BTree(11)
    node6 = BTree(17)

    node0.left = node1
    node0.right = node2

    node1.left = node3
    node1.right = node4

    node2.left = node5
    node2.right = node6

    # node = get_b_tree1()
    ret = func1(node=node0)
    print(ret)


def main2():
    node0 = BTree(head=10)

    node1 = BTree(5)
    node2 = BTree(14)

    node3 = BTree(120)
    node4 = BTree(6)
    node5 = BTree(11)
    node6 = BTree(17)

    node0.left = node1
    node0.right = node2

    node1.left = node3
    node1.right = node4

    node2.left = node5
    node2.right = node6

    func2(node=node0)

def main2_wang_quan_er_cha_shu():
    node0 = BTree(head=10)

    node1 = BTree(5)
    node2 = BTree(14)

    node3 = BTree(120)
    node4 = BTree(6)
    node5 = BTree(11)
    node6 = BTree(17)

    node0.left = node1
    node0.right = node2

    node1.left = node3
    node1.right = node4

    node2.left = node5
    # node2.left = None
    node2.right = node6

    ret = func2_wan_quan_er_cha_shu(node=node0)
    print(ret)


def main3():
    node0 = BTree(head=10)

    node1 = BTree(5)
    node2 = BTree(14)

    node3 = BTree(120)
    node4 = BTree(6)
    node5 = BTree(11)
    node6 = BTree(17)

    node0.left = node1
    node0.right = node2

    node1.left = node3
    node1.right = node4

    node2.left = node5
    # node2.left = None
    node2.right = node6

    ret = func3(head=node0)


def main4():
    node0 = BTree(head=1)

    node1 = BTree(2)
    node2 = BTree(3)

    node3 = BTree(4)
    node4 = BTree(5)
    node5 = BTree(6)

    node6 = BTree(7)
    node7 = BTree(8)

    node0.left = node1
    node0.right = node2

    node1.left = node3
    node1.right = node4

    node2.right = node5

    node4.left = node6
    node4.right = node7
    print("前序遍历")
    ret = func4_qian(head=node0)
    print("中序遍历")
    ret = func4_zhong(head=node0)
    print([node.head for node in ret])
    print("中序遍历-递归方式")
    ret = func4_zhong_rec(head=node0)
    print([node.head for node in ret])
    print("后序遍历")
    ret = func4_hou(head=node0)
    print([node.head for node in ret])
    print("后序遍历2")
    ret = func4_hou_2(head=node0)
    print([node.head for node in ret])

def main6():
    node0 = BTree(head=1)

    node1 = BTree(2)
    node2 = BTree(3)

    node3 = BTree(4)
    node4 = BTree(5)
    node5 = BTree(6)

    node6 = BTree(7)
    node7 = BTree(8)

    node0.left = node1
    node0.right = node2

    node1.left = node3
    node1.right = node4

    node2.right = node5

    node4.left = node6
    node4.right = node7

    _, ret = func6(head=node0, node1=node3, node2=node6)
    print(ret.head)

def main7():
    node0 = BTree(head=1)

    node1 = BTree(2)
    node2 = BTree(3)

    node3 = BTree(4)
    node4 = BTree(5)
    node5 = BTree(6)

    node6 = BTree(7)
    node7 = BTree(8)

    node0.left = node1
    node0.right = node2

    node1.left = node3
    node1.right = node4

    node2.right = node5

    node4.left = node6
    node4.right = node7

    tree_s = func7_to_str(head=node0)
    print(tree_s)
    head2 = func7_from_str(tree_s)
    print(func7_to_str(head=head2))

    pass

def main9():
    print("level 3")
    func9(level=3, left_or_right="right")
    print("level 4")
    func9(level=4, left_or_right="right")



# main
if __name__ == '__main__':
    main9()
