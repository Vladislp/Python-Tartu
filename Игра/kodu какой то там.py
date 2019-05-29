from random import randint

arv = randint(1,999)
arvamise_kordi = 0
n=int(input("Kui palju kordi, et proovida?: "))

def arvuming(arv,n):
    arvamus = int(input("Arva, millist tuhandest väiksemat arvu ma mõtlen: "))
    global arvamise_kordi
    arvamise_kordi +=1
    if arvamise_kordi !=n:
        if arvamus > arv:
            print("Minu arv on väiksem!")
            arvuming(arv,n)
        elif arvamus < arv:
            print("Minu arv on suurem!")
            arvuming(arv,n)
        else:
            print("Arvasid ära! Tubli!")
    else:
        print("{0} arvamisest ei piisanud, mida nüüd teed?".format(n))
arvuming(arv,n)