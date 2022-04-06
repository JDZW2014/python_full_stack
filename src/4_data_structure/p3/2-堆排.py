
def print_tree(lis):
    max_level = int(math.log2(len(lis)))
    print('---')
    for i in range(max_level + 1):
        start = 2**i - 1
        end = min(start + start + 1, len(lis))
        print(lis[start: end], "\n")