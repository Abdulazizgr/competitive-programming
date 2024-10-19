x = input()

lis = [int(i) for i in input().split()]
pos = 0
neg = 0
for i in  range(len(lis)):
    if lis[i] > 0:
       pos += lis[i]
    #    print(pos,'pos')
    else:
        if pos > 0:
            pos += lis[i]
            # print(pos,'pos')
        else:
            neg += 1
            # print(neg)
print(neg)