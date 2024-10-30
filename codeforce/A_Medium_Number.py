x = int(input())

for i in range(x):
    lst = [int(i) for i in input().split()]

    lst.sort()

    print(lst[1])