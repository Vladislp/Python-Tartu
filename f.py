from pykkar import *
def suurus():
    try:
        world-input("Sisesta maailma suurused: ").split(',')
        wx=int(world[0])
        wy=int(world[1])
        if wx <= 0 or wy <=0:
            print("Vigane sisend! Proovi uuesti...")
            return suurus()
        else:
            return wx,wy
    except:
        print("Vigane sisend! Proovi uuesti...")
        return suurus()
mõõtmed=list(suurus())
x=mõõtmed[0]
y=mõõtmed[1]
def asukoht(wx,wy):
    try:
        cord=input("Sisesta Pykkari koordinaadid: ").split(',')
        px=int(cord[0])
        py=int(cord[1])
        suund=input("Sisesta Pykkari suund: ")
        if px >=wx or py >= wy:
            print("Koordinaadid liiga suured! Proovi uuesti...")
            return asukoht(wx,wy)
        elif px <= 0 or py <=0:
            print("Koordinaadid liiga väikesed! Proovi uuesti...")
            return asukoht(wx,wy)
        if suund == 'N' or suund == 'S' or suund == 'E' or suund == 'W':
            return px,py,suund
        else:
            print("Vigane suund! Proovi uuesti...")
            return asukoht(wx,wy)
        except:
            print("Midagi läks valesti! Proovi uuesti...")
            return asukoht(wx,wy)
kurd=list(asukoht(x,y))
x1=kurd[0]
y1=kurd[1]
way=kurd[2]
def create(wx,wy,px,py,suund):
    i=1
    print('#' * (wx+2))
    while i<=(wy):
        if i==py:
            print('#'+' '*(px-1)+suund+' '*(wx-px)+'#')
            i +=1
            else:
                print('#'+' '*(wx)+'#')
                i +=1
                print('#'*(wx+2))
create(x,y,x1,y1,way)
          