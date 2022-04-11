"""
荷兰国旗问题：
问题一： 给定一个数组arr， 和一个数num，请把小于等于num 的数放在数据组的左边，大于num的数放在数组的右边。要求额外空间复杂度O(1), 时间复杂度O(N)

问题二： （荷兰国旗问题）
问题一： 给定一个数组arr， 和一个数num，请把小于num 的数放在数据组的左边，等于的放中间，大于num的数放在数组的右边。要求额外空间复杂度O(1), 时间复杂度O(N)
"""
def func1(lis, num):
    left_boundary = -1
    for i in range(len(lis)):
        if lis[i] <= num:
            left_boundary += 1
            lis[i], lis[left_boundary] = lis[left_boundary], lis[i]
    return lis

lis = [1, 3, 2, 2, 5, 4, -1, 9]
print(func1(lis=lis, num=2))


def func2(lis, num):
    left_boundary = -1
    right_boundary = len(lis)
    i = 0
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
    return lis

print(func2(lis=lis, num=2))

    