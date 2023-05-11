# define function
def func1(lis):
    """
    有一个arr, 其中只有一个数出现了奇数次，剩下的数出现了偶数次：找到这个数
    """
    sum = lis.pop()
    while lis:
        sum ^= lis.pop()
    return sum


def to_bin(num):
    return bin(num)[2:]


def func2(lis):
    """
    有一个arr, 其中有两个数出现了奇数次，剩下的数出现了偶数次：找到这两个数
    """
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
    
    return s ^ s2, s2


def func2_2(lis):
    """
    有一个arr, 其中有两个数出现了奇数次，剩下的数出现了偶数次：找到这两个数
    """
    # 两个数的异或和
    s = lis[0]
    for ele in lis[1:]:
        s ^= ele

    # 确定二进制中第一个一出现的位置
    st = len(bin((~s + 1) & s)) - 2

    # 依据st 将这两个数分离
    s2 = s
    for l in lis:
        if (len(bin(l)) - 2) >= st and bin(l)[-st] == '1':
            s2 = s2 ^ l

    return s ^ s2, s2


# define main
def main1():
    lis1 = [1, 3, 1, 2, 2, 2, 3]
    print(func1(lis1))


def main2():
    # 方法一
    lis2 = [1, 3, 1, 2, 2, 2, 5, 3]
    print(func2(lis=lis2))
    # 方法二
    print(func2_2(lis=lis2))


# main
if __name__ == "__main__":
    main1()
    main2()
