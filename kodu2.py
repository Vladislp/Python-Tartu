from random import randint
from itertools import count

def lause(a,b,c):
    f=open(a)
    f1=open(b)
    f2=open(c)
    alus=[]
    oeldis=[]
    sihitis=[]
    for rida in f:
        alus=alus+[rida]
    for rida in f1:
        oeldis=oeldis+[rida]
    for rida in f2:
        sihitis=sihitis+[rida]
    
    alus1=alus[randint(0,9)]
    oeldis1=oeldis[randint(0,9)]
    sihitis1=sihitis[randint(0,9)]
    suka=alus1+" "+oeldis1+" "+sihitis1
    return ''.join(suka.splitlines())
    
    





g=('alus.txt')
n=('oeldis.txt')
l=('sihitis.txt')

while True:
    print(lause(g,n,l))
    input(" ")


