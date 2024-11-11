t = int(input())  
ans = []

for _ in range(t):
    n = int(input())  
    a = list(map(int, input().split()))  
    total = sum(a)  

    if total % 2 != 0:
        ans.append("NO")
    else:
        ans.append("YES")


print("\n".join(ans))
