
# define function
def func(lis):
    for i in range(1, len(lis)):
        for j in range(0, i-1):
            if lis[i-j] < lis[i-j-1]:
                lis[i-j], lis[i-j-1] = lis[i-j-1], lis[i-j]

    return lis

lis = [1, 3, 9, 5, 6, 10]
print(func(lis=lis))