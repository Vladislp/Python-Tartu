f = open("palgad.txt")

for line in f.readlines():
    m = {'Nimi': '', 'väärtused':0}
    line = line.strip().split(";")
    if int(line[-1]) > m['väärtused']:
        m['väärtused'] = int(line[-1])
        m['Nimi'] = line[0]
        print(m['Nimi'], m['väärtused'])
print(line.index (2500))
    
    
    

    


