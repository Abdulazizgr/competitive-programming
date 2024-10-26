x = int(input())

for i in range(x):
    y = input()
    n = len(y)
    if n % 2 != 0:
        print("NO")
    else:
        n = n // 2
        y = list(y)

        if y[:n] == y[n:]:
            print("YES")
        else:
            print("NO")