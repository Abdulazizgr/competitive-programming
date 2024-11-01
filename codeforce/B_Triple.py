x = int(input())
ans = []
for _ in range(x):
    y = int(input())
    lst = [int(i) for i in input().split()]
    count = {}
    found = -1
    for num in lst:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
        
        if count[num] == 3:
            found = num
            break
    ans.append(found)

for res in ans:
    print(res)
