arv=list(range(200))
arv=list(map(int, arv))
paarisarvud=0
for i in arv:
    if i%2 == False:
        paarisarvud+=1
print(paarisarvud)
