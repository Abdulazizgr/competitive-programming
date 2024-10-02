x= int(input())
name = input()

a= name.count("A")
d = name.count("D")

if a > d:
    print("Anton")
elif d > a:
    print("Danik")
else:
    print("Friendship")
