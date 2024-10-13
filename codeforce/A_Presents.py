x = int(input())

lis = [int(i) for i in input().split()]
dic = {}
for i in range(1,x+1):
    dic[lis[i-1]] = i
for i in range(1,x+1):
    print(dic[i],end=" ")