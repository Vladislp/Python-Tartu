# Siin on antud kõigepealt ülesande lahendus ilma ülesande lisa arvestamata.
# Allpool on kommentaarina öeldud, mida tuleks muuta, et ka lisas toodud nõuded
# oleks täidetud.

# Kõigepealt loen read failist listi, et oleks lihtsam uurida
# mitut rida korraga
f = open('sundmused.txt')
read = []
for rida in f:
    read = read + [rida.strip()]
f.close()

# Nüüd käin indeksite abil kõik sündmused läbi
# NB! Tsükkel teeb niipalju kordusi, nagu failis on *sündmusi*, mitte ridu!
i = 0
while i < len(read):
    # read[i] on mingi sündmuse päis
    päise_osad = read[i].split()
    
    # mõlema failiformaadi korral on kuupäev sündmuse päise viimane komponent
    kuupäev = päise_osad[-1] 
    
    # Kas pulm või matus?
    if read[i].startswith("Matus"):
        print("Matus", kuupäev + ", suri", read[i+1])
        # järgmine sündmus on 2 rida allpool
        i += 2
    else:
        print("Pulm", kuupäev + ", abiellusid", read[i+1], "ja", read[i+2])
        # järgmine sündmus on 3 rida allpool
        i += 3 

# Selleks, et lahendada ülesande lisa, pean ma sündmuse päise real olles kontrollima
# kas järgmine sündmuse päis (st. rida, mis sisaldab punkti) on 2 või 3 rida allpool
#
#    if read[i].startswith("Matus"):
#
# reaga
#
#    if "." in read[i+2]:
#
# See tekitaks aga probleeme viimase sündmuse juures, sest indeksit i+2 ei pruugi 
# eksisteerida. Seetõttu peame kontrollima ka seda, kas oleme jõudnud viimase sündmuse
# juurde:
#
#    if i+2 >= len(read) or "." in read[i+2]:
#
# NB! siin on tähtis, et indeksi võrdlemine ridade arvuga oleks eespool, kui me 
# kirjutaksime
#
#    if "." in read[i+2] or i+2 >= len(read):
# 
# siis listi lõpus olles teeks Python kõigepealt vigase indekseerimise ja or-i teine
# pool enam ei päästaks.