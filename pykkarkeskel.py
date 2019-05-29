from pykkar import *
#def - задаем размеры и местонахождение
def suurus():
    try:
        wurld=input("Sisesta maailma suurused: ").split(',')
        wx=int(wurld[0])
        wy=int(wurld[1])
        if wx <= 0 or wy <= 0:
            print("Vigane sisend! Proovi uuesti...")
            return suurus()
        else:
            return wx,wy
    except:
        print("Vigane sisend! Proovi uuesti...")
        return suurus()
mootmed=list(suurus())
x=mootmed[0]
y=mootmed[1]
#cord = koordinaadid
#px py = оси х и y
def asukoht(wx,wy):
    try:
        cord=input("Sisesta Pykkari koordinaadid: ").split(',')
        px=int(cord[0])
        py=int(cord[1])
        suund=input("Sisesta Pykkari suund: ")
        if px >= wx or py >= wy:
            print("Koordinaadid liiga suured! Proovi uuesti...")
            return asukoht(wx,wy)
        elif px <= 0 or py <= 0:
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
kord=list(asukoht(x,y))
x1=kord[0]
y1=kord[1]
way=kord[2]
#eval - читает строку и возвращает результат
#'\n' - следующая строка
def create(wx,wy,px,py,suund):
    return('#'*(wx+2)+'\n'
       +('#'+' '*(wx)+'#'+'\n')*(py-1)
       +'#'+' '*(px-1)+suund+' '*(wx-px)+'#'+'\n'
       +('#'+' '*(wx)+'#'+'\n')*(wy-py)
       +'#'*(wx+2)+'\n')
eval('create_world("""'+create(x,y,x1,y1,way)+'""")')
#Как найти место
def center_move(wx,wy,px,py):
    while py > (wy/2):
        while get_direction() != 'N':
            right()
            if get_direction() == 'N':
                break
        step()
        py-=1
        if py-1 == int(wy/2):
            break
    while py < (wy/2):
        while get_direction() != 'S':
            right()
            if get_direction() == 'S':
                break
        step()
        py+=1
        if py+1 == int(wy/2):
            break
    while px > (wx/2):
        while get_direction() != 'W':
            right()
            if get_direction() == 'W':
                break
        step()
        px-=1
        if px-1 == int(wx/2):
            break
    while px < (wx/2):
        while get_direction() != 'E':
            right()
            if get_direction() == 'E':
                break
        step()
        px+=1
        if px-1 == int(wx/2):
            break
    paint()
    if wx%2 == False or wy%2 == False:
        step()
        paint()
        if wx%2 == False and wy%2 == False:
            while get_direction() != 'N':
                right()
            step()
            paint()
            while get_direction() != 'W':
                right()
            step()
            paint()
center_move(x,y,x1,y1)
