
# define class
class SNode(object):
    __slots__ = ("value", "next_node")
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def set_next_node(self, node):
        self.next_node = node
        return self
    
    def get_value(self, ):
        return self.value

    def get_next_node(self, ):
        return self.next_node

class DNode(object):
    __slots__ = ("value", "last_node", "next_node")
    def __init__(self, value, last_node=None, next_node=None):
        self.value = value
        self.last_node = last_node
        self.next_node = next_node
    
    def set_last_node(self, node):
        self.last_node = node
        return self

    def set_next_node(self, node):
        self.next_node = node
        return self
    
    def get_value(self, ):
        return self.value
    
    def get_next_node(self, ):
        return self.next_node

    def get_last_node(self, ):
        return self.last_node

# define class
def get_single_node_list(lis) -> SNode:
    first_node = SNode(value=lis[0])
    current_node = first_node
    for l in lis[1:]:
        _node = SNode(value=l)
        current_node.set_next_node(_node)
        current_node = _node
    return first_node

def get_double_node_list(lis) -> DNode:
    first_node = DNode(value=lis[0])
    current_node = first_node
    for l in lis[1:]:
        node = DNode(value=l)
        node.set_last_node(node=current_node)
        current_node.set_next_node(node)
        current_node = node

    return first_node


def print_single_node(node: SNode):
    while node:
        print(node.value)
        node = node.get_next_node()


def print_double_node(node: DNode):
    while node:
        _current = node.get_value()
        _last = node.get_last_node().get_value() if node.get_last_node() else None
        _next = node.get_next_node().get_value() if node.get_next_node() else None
        print(f"curent = {_current}, last = {_last}, next = {_next}")
        node = node.get_next_node()


# define test
def test1():
    lis = [2, 3, 4, 5, 6]
    node = get_single_node_list(lis)
    print_single_node(node=node)


def test2():
    lis = [2, 3, 4, 5, 6]
    node = get_double_node_list(lis)
    print_double_node(node=node)


# main test
if __name__ == "__main__":
    test1()
    test2()