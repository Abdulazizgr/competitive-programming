# n = int(input())
# a = []
# for i in range(n):
#     y = input()
#     a.append(y)

# c = 0 
# for i in range(n - 1):
#     if a[i][1] != a[i + 1][0]:
#         c += 1

# print(c)


n = int(input())
pre = input()
count = 1

for _ in range(1, n):
    curr = input()
    if curr != pre:
        count += 1
    pre = curr

print(count)
