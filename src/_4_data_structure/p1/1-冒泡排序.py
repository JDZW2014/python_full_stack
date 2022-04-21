"""
它的基本思想是将一个记录插入到已经排好序的有序表中
"""

def sort(lis):
    for i in range(len(lis)-1):
        for j in range(0, len(lis)-1-i):
            if lis[j] > lis[j+1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]
            
    return lis


lis = [1, 3, 4, 2, 4]
print(sort(lis))