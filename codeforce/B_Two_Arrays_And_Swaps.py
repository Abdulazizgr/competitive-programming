t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    a.sort()
    b.sort(reverse=True)

    for i in range(k):
        if a[i] < b[i]:
            a[i] = b[i]
    print(sum(a))
        

