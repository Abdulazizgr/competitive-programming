n = int(input())

ope , num = 0,2

while num <= n:
    if n % num == 0:
        ope += num 
        n = n/num
        num -= 1
    num += 1
print(ope)