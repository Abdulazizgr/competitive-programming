x = int(input())
curr = 0
cap = 0

for i in range(x):
    a, b = map(int, input().split())
    curr -= a
    curr += b
    cap = max(cap, curr)

print(cap)
