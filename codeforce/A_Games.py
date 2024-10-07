n = int(input())
    
h = []
a = []
number = 0

for i in range(n):
    home, away = map(int, input().split())
    h.append(home)
    a.append(away)
    for j in range(i):
        if h[i] == a[j]:
            number += 1
        if a[i] == h[j]:
            number += 1

print(number)
