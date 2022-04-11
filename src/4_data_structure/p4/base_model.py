class SNode(object()):
    __slots__ = ("value", "next_node")
    def __init__(value, next_node):
        self.value = value
        self.next_node = next_node

class DNode(object):
    __slots__ = ("value", "last_node", "next_node")
    def __init__(self, value, last_node, next_node):
        self.value = value
        self.last_node = last_node
        self.next_node = next_node