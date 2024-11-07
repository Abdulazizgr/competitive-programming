t = int(input())
for _ in range(t):
  
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    ans = s[-1] - s[0]
    for i in range(1, n):
        ans = min(ans, s[i] - s[i - 1])
    print(ans)
 
