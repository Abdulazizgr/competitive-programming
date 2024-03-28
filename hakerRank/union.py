
x = int(input())
an = set(map(int, input().split()))
y = int(input())
an1 = set(map(int, input().split()))

uni = an.union(an1)

print(len(uni))