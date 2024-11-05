x = int(input())
test = "codeforces"
for i in range(x):
    y = input()
    count = 0
    for i in range(10):
        if test[i] != y[i]:
            count += 1
    print(count)
        