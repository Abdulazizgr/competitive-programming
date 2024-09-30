
x, y = map(int, input().split()) 
z = list(map(int, input().split()))  

yth_score = z[y - 1]  


advancers = 0
for score in z:
    if score >= yth_score and score > 0:
        advancers += 1


print(advancers)
