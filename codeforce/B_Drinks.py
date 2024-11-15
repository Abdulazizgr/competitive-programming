n = int(input())
a = list(map(int, input().split()))
sum_values = sum(a)
ans = sum_values / n
print(f"{ans:.12f}")
