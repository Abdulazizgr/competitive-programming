x = int(input())
ans =[]
for i in range(x):
    lis = [int(i) for i in input().split()]
    lis.sort()
    if lis[0] in lis[1:]:
        ans.append(lis[2])
    else:
        ans.append(lis[0])

for i in ans:
    print(i)