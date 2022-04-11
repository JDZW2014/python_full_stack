def sort(lis):
    for i in range(1, len(lis)):
        for j in range(0, i):
            if lis[i-j] > lis[i-j-1]:
                lis[i-j], lis[i-j-1] = lis[i-j-1], lis[i-j]
            else:
                break
    return lis

lis = [2, 3, 2, 5, 6, 5, 7]
print(sort(lis))
