file = open("palgad.txt")
nimi = []
vanus = []
palgad = []
summa = 0
teenijate_arv1 = 0
teenijate_arv2 = 0
vanus1 = 0
vanus2 = 0
for i in file:
    a = i.strip().split(";")
    nimi.append(a[0])
    vanus.append(int(a[1]))
    palgad.append(float(a[-1]))
c = sorted(palgad)
suurem_palk = c[-1]
for palk in palgad:
    summa += palk
    keskmine_palk = summa/len(palgad)
    if palk > keskmine_palk:
        teenijate_arv1 += 1
        vanus1 +=  vanus[palgad.index(palk)]
        keskminevanus1 = vanus1/teenijate_arv1
    elif palk <= keskmine_palk:
        teenijate_arv2 += 1
        vanus2 += vanus[palgad.index(palk)]
        keskminevanus2 = vanus2/teenijate_arv2
print("Suurima palgaga töötaja: " + nimi[palgad.index(suurem_palk)] + ", " + str(suurem_palk))
print("Keskmine palk: " +str(keskmine_palk))
print("Keskmisest palgast rohkem teenijate arvu: " + str(teenijate_arv1))
print("Keskmine vanus nendel, kellel on palk keskmisest vähem või samapalju: "  + str(round(keskminevanus2,1)))
print("Keskmine vanus nendel, kellel on palk keskmisest suurem: " + str(round(keskminevanus1,1)))

file.close()
        