x = int(input())

for i in range(x):
    y = int(input())
    count = 0
    lst = [int(i) for i in input().split()]
    for i in range(1,y):
        if lst[i] - lst[i-1] == 5 or lst[i] - lst[i-1] == -5 or lst[i] - lst[i-1] == 7 or lst[i] - lst[i-1] == -7:
            count += 1
    # print(count)
    if count == y-1:
        print("YES")
    else:
        print("NO")           
        