"""
小和问题：[1,2,4,3]
1 的小和为 0
2 的小和为 1
4 的小和为 1+2=3
...
所以这些数的和为最终的小和值， 要求时间复杂度为 O(N * log N)
"""


# define Function
def minimal_sum(lis):
    length = len(lis)
    # 终止条件
    if length == 1:
        return lis, 0
    
    # 递归调用
    mid = length // 2
    left_list, left_sum = minimal_sum(lis=lis[: mid])
    right_list, right_sum = minimal_sum(lis=lis[mid: ])
    
    # 合并结果
    new_list = []
    left_index = 0
    right_index = 0
    sum = left_sum + right_sum
    
    while  True:
        if left_index >= len(left_list) or right_index >= len(right_list):
            break
        
        if left_list[left_index] < right_list[right_index]:
            new_list.append(left_list[left_index])
            sum += (len(right_list) - right_index) * left_list[left_index]
            left_index += 1
        else:
            new_list.append(right_list[right_index])
            right_index += 1
    
    if left_index >= len(left_list):
        new_list += right_list[right_index:]
    else:
        new_list += left_list[left_index:]
                 
    return new_list, sum


if __name__ == '__main__':
    lis = [1, 1, 3, 2, 5, 4, 7, 3]
    lis, sum = minimal_sum(lis=lis)
    print(lis)
    print(sum)