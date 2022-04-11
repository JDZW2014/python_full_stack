"""
快排1.0
"""
import random
lis = [1, 3, 2, 2, 5, 4, -1, 9]
def func1(lis, num):

    pass



"""
快排2.0
"""
def func2(lis, num):
    pass



"""
快排3.0
"""
def func3_hl_flag(lis, start, end):
    # 终止递归条件
    if (end - start) <= 1:
        return 

    # 荷兰国旗
    num = lis[start]
    left_boundary = start - 1
    right_boundary = end
    i = start
    while True:
        if i >= right_boundary:
            break
        if lis[i] < num:
            left_boundary += 1
            lis[i], lis[left_boundary] = lis[left_boundary], lis[i]
            i += 1
        elif lis[i] > num:
            right_boundary -= 1
            lis[i], lis[right_boundary] = lis[right_boundary], lis[i]
        else:
            i += 1
    
    # 递归调用
    # print(num, lis)
    func3_hl_flag(lis, start, left_boundary+1)
    func3_hl_flag(lis, right_boundary, end)

def func3(lis):
    random.shuffle(lis)
    func3_hl_flag(lis, start=0, end=len(lis))
    return lis

print(func3(lis))

        




