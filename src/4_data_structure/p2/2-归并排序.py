
def merge_sort(lis):
    length = len(lis)
    # 终止条件
    if length == 1:
        return lis
    
    # 递归调用
    mid = length // 2
    left_list = merge_sort(lis=lis[: mid])
    right_list = merge_sort(lis=lis[mid: ])
    
    # 结果合并
    new_list = []
    left_ele = None
    right_ele = None

    while True:
        if (left_ele is None and len(left_list) == 0) or (right_ele is None and len(right_list) == 0):
            break
        
        if not left_ele:
            left_ele = left_list.pop(0)
        if not right_ele:
            right_ele = right_list.pop(0)

        if left_ele <= right_ele:
            new_list.append(left_ele)
            left_ele = None
        else:
            new_list.append(right_ele)
            right_ele = None
    if left_ele:
        new_list.append(left_ele)
    if right_ele:
        new_list.append(right_ele)
    
    new_list += left_list + right_list
                 
    return new_list


if __name__ == '__main__':
    lis = [1, 1, 3, 2, 5, 4, 7, 3]
    lis = merge_sort(lis=lis)
    print(lis)
