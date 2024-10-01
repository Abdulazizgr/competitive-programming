x= input()
x= list(x)

f = x.count('4')
s = x.count('7')
ct = f + s

ct = str(ct)
stat = "YES"
for i in ct:
    if i not in '47':
        stat = "NO"
        break
print(stat)

