x = int(input())

for i in range(x):
    list1 = list(map(int, input().split()))
    if list1[0] + list1[1] == list1[2]:
        print("+")
    else:
        print("-")