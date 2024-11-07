n = int(input())
lst = [int(i) for i in input().split()]


max_index = lst.index(max(lst))


min_index = len(lst) - 1 - lst[::-1].index(min(lst))
# print(lst[::-1].index(min(lst)))


if max_index > min_index:
    
    count = max_index + (n - 1 - min_index) - 1
else:
    count = max_index + (n - 1 - min_index)

print( count)
