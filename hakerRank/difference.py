
x = int(input())
an = set(map(int, input().split()))
y = int(input())
an1 = set(map(int, input().split()))

diff = an.difference(an1)

print(len(diff))