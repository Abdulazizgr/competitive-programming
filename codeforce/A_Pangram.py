x = input()

y = input().lower()
abc = set('abcdefghijklmnopqrstuvwxyz')

count = 0

for i in abc:
    if i in y:
        count += 1



if count == 26:
    print("YES")
else:
    print("NO")
