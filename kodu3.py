fail = open(input("Sisesta faili nimi: "))
choice = 'y'
lines=[0,40]
rida = 0
for rida in fail:
    print("Lugesin sellise rea: " + rida)
    if rida in lines:
        сhoice = input("Kas vaatame edasi ?: ")
        if choice == 'y':
            fail.read()

# Oli mingine selline mõtte, aga ei tulnud välja