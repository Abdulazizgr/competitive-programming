n = int(input())
p = set(map(int, input().split()[1:]))
q = set(map(int, input().split()[1:]))

both = p | q

if len(both) == n and all(level in both for level in range(1, n + 1)):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
