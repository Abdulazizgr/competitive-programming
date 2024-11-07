t = int(input())

for _ in range(t):
    a , b = map(int,input().split())
    ans = (a - a)+ (b - a)
    for i in range(a,b):
        ans = min(ans ,(i - a)+ (b - i))
    print(ans)

         
