t = int(input())
lst = list(map(int, input().split()))

count = 0
minNum = lst[0]
maxNum = lst[0]

for i in range(1, t):
    if lst[i] < minNum:
        minNum = lst[i]
        count += 1
    elif lst[i] > maxNum:
        maxNum = lst[i]
        count += 1

print(count)
