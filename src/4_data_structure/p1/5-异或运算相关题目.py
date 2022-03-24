"""
异或运算可以简单的即为无进位相加

题目: 有一个arr, 其中只有一个数出现了奇数次，剩下的数出现了偶数次：
        a. 如何找到这个数？
        b. 如果有两数出现了奇数次呢？
    要求: 时间复杂度O(n), 空间复杂度 O(1)
"""
def func1(lis):
    sum = lis.pop()
    while lis:
        sum ^= lis.pop()
    return sum


lis1 = [1, 3, 1, 2, 2, 2, 3]
print(func1(lis1))


def to_bin(num):
    return bin(num)[2:]


def func2(lis):
    s = lis[0]
    for ele in lis[1:]:
        s ^= ele
    
    for idx, ele in enumerate(to_bin(s)):
        if ele == 0:
            break
    s2 = s
    for ele in lis:
        if len(to_bin(ele)) <= idx or to_bin(ele)[idx] == 0:
            s2 ^= ele
    
    return s^s2, s2

lis2 = [1, 3, 1, 2, 2, 2, 5, 3]
print(func2(lis=lis2))



