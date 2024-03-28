from collections import defaultdict

n, m = map(int, input().split())
an = defaultdict(list)
for i in range(1,n+1):
    a = input().strip()
    an[a].append(i)
for _ in range(m):
    b =input().strip()
    if b in an:
        print(*an[b])
    else:
        print(-1)
