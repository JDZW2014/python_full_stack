

# define function
def func(lis, start, end, num):
    mid = (start + end) // 2
    if lis[mid] == num:
        return mid
    elif lis[mid] > num:
        return func(lis, start, mid, num)
    else:
        return func(lis, mid, end, num)

lis = [1, 2, 3, 7, 11, 24]
print(func(lis=lis, start=0, end=len(lis), num=11))