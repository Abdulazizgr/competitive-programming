x = int(input())

for i in range(x):
    y = input()
    le = y[:3]
    r = y[3:]
    if  int(le[0]) + int(le[1]) + int(le[2]) == int(r[0]) + int(r[1]) + int(r[2]):
        print("YES")
    else:
        print("NO")
    