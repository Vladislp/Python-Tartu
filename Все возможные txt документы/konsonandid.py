def konsonandid(järjend):
    if len(järjend) == 0:
        return ''
    else:
        päis = järjend[0]
        saba = järjend[1:]
        elementid_sabas = konsonandid(saba)
        if päis == 'i' or päis == 'ü' or päis == 'u' or päis == 'e' or päis == 'ö' or päis == 'õ' or päis == 'o' or päis == 'ä' or päis == 'a':
            return elementid_sabas
        else:
            return päis + elementid_sabas 

konsonandid1 = input("Sisesta sõna: ")
print(konsonandid(konsonandid1))
