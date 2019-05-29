# Tegin koos informaatikuga ( Katrin Kulik )
import sys

def loe_faili_sisu(failinimi):
    sudoku_list = []
    file = open(failinimi)
    Loe_Fail = file.read().split("\n")
    for i in Loe_Fail:
        sudoku_list.append(i.split(" "))
    return sudoku_list
    file.close()

def rea_kontroll(sudoku_list):
    for rida in sudoku_list:
        i = 1
        while i <= 9:
            if str(i) in rida:
                i +=1
            else:
                return False
    return True

def veeru_kontroll(sudoku_list):
    indeks = 0
    veeru_indeks = 0
    veeru_tabel = []
    while veeru_indeks < 9:
        while indeks < 9:
            if sudoku_list[indeks][veeru_indeks] in veeru_tabel:
                return False
            else:
                veeru_tabel.append(sudoku_list[indeks][veeru_indeks])
                indeks += 1
        veeru_indeks += 1
        indeks = 0
        veeru_tabel = []
    return True


def ruudu_kontroll(sudoku_list):
    if rea_kontroll(sudoku_list) and veeru_kontroll(sudoku_list) == True:
        ruudu_list = []
        ruudu_list1 = []
        ruudu_list2 = []
        list = []
        arv = 0
        number = 9
        for i in sudoku_list:
            ruudu_list += i[0] + i[1] + i[2]
            ruudu_list1 += i[3] + i[4] + i[5]
            ruudu_list2 += i[6] + i[7] + i[8]
        Üldine_list = ruudu_list, ruudu_list1, ruudu_list2

        while number <= 27:
            for i in Üldine_list:
                esimene_ruut = i[arv:number]
                for i in esimene_ruut:
                     if i in list:
                        return False
                     else:
                        list.append(i)
                list = []
            number += 9
            arv += 9
        return True

    else:
        return False

failinimi = sys.argv[1]

if ruudu_kontroll(loe_faili_sisu(failinimi)) == True:
    print("OK")
else:
    print("Viga")