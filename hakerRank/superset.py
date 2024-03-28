# Enter your code here. Read input from STDIN. Print output to STDOUT

a = set(map(int, input().split()))
n = int(input())
flag = True

for _ in range(n):
    b = set(map(int, input().split()))
    if not (b.issubset(a) and len(b) < len(a)):
        flag = False
        break

print(flag)
