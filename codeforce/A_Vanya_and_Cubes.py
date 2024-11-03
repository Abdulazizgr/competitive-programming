x = int(input())
count = 0
num = 1
ans = 0

while x > 0:
    count += num
    if x >= count:
        ans += 1
        x -= count
    else:
        break
    num += 1

print( ans)
