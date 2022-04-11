"""
分别实现反转单项链表和反转双向链表的函数
要求：如果链表长度为N，时间复杂度要求为O(N), 额外空间复杂度为O(1)
"""
import typing
from _4_data_structure.p4.base_model import SNode, DNode, get_single_node_list, get_double_node_list, print_single_node, print_double_node


def revert_single_node(node: SNode):
    last_node = node
    node = node.get_next_node()
    while node: 
        next_node = node.get_next_node()
        node.set_next_node(node=last_node)
        last_node, node = node, next_node
    return last_node


def revert_double_node(node: DNode):
    while node:
        last_node = node.get_last_node()
        next_node = node.get_next_node()
        node.set_last_node(node=next_node)
        node.set_next_node(node=last_node)

        node = next_node
    return last_node

# define func
def revert_single_list():
    node = get_single_node_list(lis=[2, 5, 6, 7, 10])
    print_single_node(node=revert_single_node(node=node))

def revert_double_list():
    node = get_double_node_list(lis=[2, 5, 6, 7, 10])
    print_double_node(node=revert_double_node(node=node))


# main
if __name__ == "__main__":
    revert_single_list()
    revert_double_list()

