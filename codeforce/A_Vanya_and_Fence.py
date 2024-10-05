x, y = map(int, input().split())


lis = [int(i) for i in input().split()]
count = 0
for i in lis:
    if i > y:
        count += 2
    else:
        count += 1
print(count)
