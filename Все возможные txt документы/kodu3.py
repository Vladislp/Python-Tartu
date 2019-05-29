def seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"):
    f = open('nimed.txt')
    for rida in f.readlines():
        sõnastik = {}
        if rida.split()[0] == '47853062345':
            sõnastik[0] = rida.split()[0] 
        elif rida.split()[0] == '36512129874':
            sõnastik[1] = rida.split()[0]
        elif rida.split()[0] == '38504014543':
            sõnastik[2] = rida.split()[0]
        elif rida.split()[0] == '46906183451':
            sõnastik[3] = rida.split()[0]
        elif rida.split()[0] == '34105139833':
            sõnastik[4] = rida.split()[0]
        elif rida.split()[0] == '48708252344':
            sõnastik[5] = rida.split()[0]
        elif rida.split()[0] == '60907062342':
            sõnastik[6] = rida.split()[0]
        print(sõnastik)