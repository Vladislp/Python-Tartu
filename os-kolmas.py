from tkinter import *
import tkinter
from tkinter import ttk
from tkinter import messagebox

# Vastus küsimusele
# Küsimus : Kui lisaks oleks vaja mõne protsessi kettapäringuid eelistada teiste protsesside päringutele, siis missugust planeerijat soovitaksite?
# Vastus : Ma arvan, et siin võiks kasutada parem CFQ planeerijat. CFQ heakülg on see, et saab protsessid jagada kolme erinevasse prioriteetklassi.
# Kui vaadata eelistatud protsess ja paigutada seda "Real Time" prioriteediklassi, siis juhtub see, et selle päringud täidetakse alati enne teisi klasse.
# Selle algoritmi puhul võib tekkitada probleem, et hakkab protsesside näljutamine.
# Kuna esimesena täidetakse alati "Real Time" päringud.


def puhasta():
    tahvel.delete('all')
    
def joonista(jarjend, algjarjend):
    puhasta()
    k = []
    l = 0
    for i in range(50):
        Num = tahvel.create_text(20+l, 10, text=i)
        squere = tahvel.create_rectangle(10+l, 20, 30+l, 30)
        l += 20
    l = 0
    m = 0
    for i in range(len(jarjend)):
        l = 20*jarjend[i]
        punkt = tahvel.create_oval(17+l,40+m,22+l,35+m,fill="black")
        if jarjend[i] in algjarjend:
            x = tahvel.create_text(20+l, 24, text="x")
        k.append([19.5+l,37.5+m])
        try:
            if jarjend[i] != jarjend[i+1]:
                m += 20
        except IndexError:
            pass
    for i in range(len(k)-1):
        try:
            joon = tahvel.create_line(k[i][0],k[i][1],k[i+1][0],k[i+1][1])
        except IndexError:
            pass
        
        
def massiiviks(input_jarjend):
    valjund = []
    jupid = input_jarjend.split(",")
    for i in range(len(jupid)):
        valjund.append(int(jupid[i]))
    return valjund
        
def massiiviMeister():
    jarjend = []
    if var.get() == 1:
        return massiiviks(predef1)
    elif var.get() == 2:
        return massiiviks(predef2)
    elif var.get() == 3:
        return massiiviks(predef3)
    elif var.get() == 4:
        try:
            return massiiviks(kasutaja_jarjend.get())
        except:
            messagebox.showerror(title="Viga sisendis", message="Vigane kasutaja muster!")
            return massiiviks(predef1)
    else:
        return massiiviks(predef1)
    
def NOOP(jarjend):
    # Väljund alustatakse kogu aeg 10, öeldud kodutöös
    valjund = [10]
    # Teeme uue muutuja, mis pärast väljastaks meile summaarset_teepikkus
    summaarne_teepikkus = 0
    # Vaatame üle "jarjendid", ja paneme "valjund" sisse iga element
    for i in jarjend:
        # Lisame elem.
        valjund.append(i)
    # Kogu aeg lahutame viimasest punktist. Miks alustame 1, kuna kui alustada ühega siis ta peaks lahutama ise enneast. 
    for i in range(1, len(valjund)):
        if (valjund[i-1] - valjund[i]) < 0:
            summaarne_teepikkus += -(valjund[i-1] - valjund[i])
        else:
            summaarne_teepikkus += (valjund[i-1] - valjund[i])
    return (valjund, summaarne_teepikkus)
    
def SSTF(jarjend):
    valjund=[10]
    valjund1 = []
    valjund2 = []
    summaarne_teepikkus = 0
    
    for i in jarjend:
        valjund.append(i)
        
    for p in valjund:
        if p == 10:
            valjund.remove(p)
    
    
    
    for i in range(1, len(valjund)):
        if (valjund[i-1] - valjund[i]) < 0:
            summaarne_teepikkus += -(valjund[i-1] - valjund[i])
        else:
            summaarne_teepikkus += (valjund[i-1] - valjund[i])
    return (valjund, summaarne_teepikkus)

def SCAN(jarjend):
    valjund=[10]
    valjund1 = []
    valjund2 = []
    summaarne_teepikkus = 0
    
    for i in jarjend:
        valjund.append(i)
        
    for p in valjund:
        if p == 10:
            valjund.remove(p)
    for e in valjund:
        if e > 10:
            valjund1.append(e)
            valjund1.sort()
    for elem in valjund:
        if elem < 10:
            valjund2.append(elem)
            valjund2.sort(reverse = True)
    for o in valjund2:
        valjund1.append(o)
        
    
    valjund = valjund1
    valjund.insert(0, 10)
    valjund.insert(5, 49)
    
    #print(valjund2)
    #print(valjund1)
    print(valjund)
    
        
    #print(valjund)
    
    for i in range(1, len(valjund)):
        if (valjund[i-1] - valjund[i]) < 0:
            summaarne_teepikkus += -(valjund[i-1] - valjund[i])
        else:
            summaarne_teepikkus += (valjund[i-1] - valjund[i])
    return (valjund, summaarne_teepikkus)

def LOOK(jarjend):
    valjund=[10]
    valjund1 = []
    valjund2 = []
    summaarne_teepikkus = 0
    
    for i in jarjend:
        valjund.append(i)
        
    for p in valjund:
        if p == 10:
            valjund.remove(p)
    for e in valjund:
        if e > 10:
            valjund1.append(e)
            valjund1.sort()
    for elem in valjund:
        if elem < 10:
            valjund2.append(elem)
            valjund2.sort(reverse = True)
    for o in valjund2:
        valjund1.append(o)
        
    
    valjund = valjund1
    valjund.insert(0, 10)
    
    for i in range(1, len(valjund)):
        if (valjund[i-1] - valjund[i]) < 0:
            summaarne_teepikkus += -(valjund[i-1] - valjund[i])
        else:
            summaarne_teepikkus += (valjund[i-1] - valjund[i])
    return (valjund, summaarne_teepikkus)
    
def massiiviTeavitaja(massiiv):
    text.delete(1.0, END)
    for jupp in massiiv:
        text.insert(INSERT, str(jupp) + "\n")
        
def kasuvalija(jarjend, algoritm):
    if algoritm == "NOOP":
        return NOOP(jarjend)
    elif algoritm == "SSTF":
        return SSTF(jarjend)
    elif algoritm == "SCAN":
        return SCAN(jarjend)
    elif algoritm == "LOOK":
        return LOOK(jarjend)

def jooksuta_algoritmi(algoritm):
    jarjend = massiiviMeister()
    massiiviTeavitaja(jarjend)
    (valjund, summaarne_teepikkus) = kasuvalija(jarjend, algoritm)
    joonista(valjund, jarjend)
    Summ_summaarne_teepikkus = tahvel.create_text(80, 40, text="Summaarne_teepikkus:  " + str(summaarne_teepikkus))
    
predef1 = "2,5,13,29,7,1,18,40,49,4"
predef2 = "1,10,44,2,12,3,13,20"
predef3 = "45,6,16,9,33,28,11,37,49,25"

raam = Tk()
raam.title("Planeerimisalgoritmid")
raam.resizable(False, False)
raam.geometry("1024x500")

var = IntVar()
var.set(1)
Radiobutton(raam, text="Esimene", variable=var, value=1).place(x=10,y=40)
Radiobutton(raam, text="Teine", variable=var, value=2).place(x=10,y=70)
Radiobutton(raam, text="Kolmas", variable=var, value=3).place(x=10,y=100)
Radiobutton(raam, text="Enda oma", variable=var, value=4).place(x=10,y=130)

silt_vali = ttk.Label(raam, text="Vali või sisesta järjend (kujul 1,10,4,2,12,3,13,2)")
silt_vali.place(x=10, y=10)

silt1 = ttk.Label(raam, text=predef1)
silt1.place(x=120, y=40)

silt2 = ttk.Label(raam, text=predef2)
silt2.place(x=120, y=70)

silt3 = ttk.Label(raam, text=predef3)
silt3.place(x=120, y=100)

silt_run = ttk.Label(raam, text="Algoritmi käivitamiseks klõpsa nupule")
silt_run.place(x=10, y=160)

silt_tahvel = ttk.Label(raam, text="Käsil olevad protsessid:")
silt_tahvel.place(x=450, y=10)

kasutaja_jarjend = ttk.Entry(raam)
kasutaja_jarjend.place(x=120, y=130, height=25, width=240)

tahvel = Canvas(raam, width=1024, height=180, background="white")
tahvel.place(x=0, y=220)

NOOP_nupp = ttk.Button(raam, text="NOOP", command = lambda : jooksuta_algoritmi("NOOP"))
NOOP_nupp.place(x=10, y=190,height=25, width=80)

SSTF_nupp = ttk.Button(raam, text="SSTF", command = lambda : jooksuta_algoritmi("SSTF"))
SSTF_nupp.place(x=100, y=190,height=25, width=80)

SCAN_nupp = ttk.Button(raam, text="SCAN", command = lambda : jooksuta_algoritmi("SCAN"))
SCAN_nupp.place(x=190, y=190,height=25, width=80)

LOOK_nupp = ttk.Button(raam, text="LOOK", command = lambda : jooksuta_algoritmi("LOOK"))
LOOK_nupp.place(x=280, y=190,height=25, width=80)

puhasta_nupp = ttk.Button(raam, text="Puhasta väljund", command = lambda : puhasta() )
puhasta_nupp.place(x=500, y=190,height=25, width=130)

text = Text(raam, width=25, height=9)
text.place(x=450, y=30)

raam.mainloop()
