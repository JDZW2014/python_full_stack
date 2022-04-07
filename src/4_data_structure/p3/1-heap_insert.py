"""
始终保持大根堆
heap insert 
heapfiy
"""
import math


# define class
class Heap(object):
    def __init__(self):
        self.lis = list()
        self.heap_size = 0
    
    def add(self, v):
        self.lis.append(v)
        self.heap_size += 1
    
    def add_from_lis(self, lis):
        for v in lis:
            self.add(v)
    
    def left_children(self, idx):
        return self._index(self.left_children_idx(idx))

    def left_children_idx(self, idx):
        return 2 * idx + 1

    def right_children(self, idx):
        return self._index(self.right_children_idx(idx))
    
    def right_children_idx(self, idx):
        return 2 * idx + 2

    def father(self, idx):
        return self.lis[self.father_idx(idx=idx)]

    def father_idx(self, idx):
        return max(0, int((idx - 1) / 2))
    
    def exg_value(self, idx1, idx2):
        self.lis[idx1], self.lis[idx2] = self.lis[idx2], self.lis[idx1] 

    def _index(self, idx):
        if idx < self.heap_size:
            return self.lis[idx]
        else:
            return None

    def pprint(self, ):
        max_level = int(math.log2(self.heap_size))
        print('---')
        for i in range(max_level + 1):
            start = 2**i - 1
            end = min(start + start + 1, self.heap_size)
            print(self.lis[start: end], "\n")


class MaxHeap(Heap):
    def add(self, v):
        super().add(v)
        idx = self.heap_size - 1
        while idx > 0:
            val = self._index(idx)
            f_idx = self.father_idx(idx)
            f_val = self._index(f_idx)
            if self._rule_(val, f_val):
                self.exg_value(idx, f_idx)
                idx = f_idx
            else:
                break
    
    def _rule_(self, val, f_val):
        return val > f_val


class MinHeap(MaxHeap):
    def _rule_(self, val, f_val):
        return val < f_val


# define function
def test_heap():
    heap = Heap()
    lis = [2, 3, 1, 5, 4, 4, 2, 6, 9]

    # 添加数据
    heap.add_from_lis(lis=lis)

    # 打印堆
    print("---- 树的结构为 ----")
    heap.pprint()

    # 堆的左右子节点
    print("---- idx=2的 left_children----")
    print(heap.left_children(2))
    print("---- idx=3的 right_children----")
    print(heap.right_children(3))

    # 堆的左右子节点的父节点
    print("---- idx=5的 father----")
    print(heap.father(idx=5))

def test_max_heap():
    max_heap = MaxHeap()
    lis = [2, 3, 1, 5, 4, 4, 2, 6, 9]
    max_heap.add_from_lis(lis=lis)
    max_heap.pprint()

def test_min_heap():
    min_heap = MinHeap()
    lis = [2, 3, 1, 5, 4, 4, 2, 6, 9]
    min_heap.add_from_lis(lis=lis)
    min_heap.pprint()
 

# main
if __name__ == "__main__":
    # test_heap()
    # test_max_heap()
    test_min_heap()