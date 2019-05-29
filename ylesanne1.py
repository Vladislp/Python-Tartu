f = open("palgad.txt")

for line in f.readlines():
    if line == 'Aadu Suur;56;2500\n':
        print("Kõige suurema palga sai Aadu Suur, 2500 eurot")
        a = sum([2500, 1500, 700, 550, 870])
        print("Keskmine palk on " + str(a/5))
    elif line == 'Malle Kapsas;42;1500\n':
        print("Kaks inimest saavad rohkem, kui keskmise palka")
    elif line == 'Uudo Koba;32;700\n':
        print("Keskmine vanus, kes saavad vähem keskmist palga " + str(32 + 22 + 67 / 3))
        
        
        
        
    

    