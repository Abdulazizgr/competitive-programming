from collections import defaultdict


x = int(input())

for _ in range(x):  
    n, k = map(int, input().split())
    dic = defaultdict(int)
    cos = []

    for _ in range(k):
        b, c = map(int, input().split())
        dic[b] += c
    for i in dic.values():
        cos.append(i)

    cos.sort(reverse=True)
   
    total_sum = sum(cos[:n])

    print(total_sum)
