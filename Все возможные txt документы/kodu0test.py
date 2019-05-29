import os.path

def kuva_failid(kaust):
    for nimi in os.listdir(kaust):
        täisnimi = os.path.join(kaust, nimi)
        for dirpath, dirnames, filenames in os.walk('C:\\Users\\Ximaks\\Desktop\\Всякие приложения'):
        print('Current path: ', dirpath)
        print('Directories: ', dirnames)
        print('Files: ', filenames)
            

kuva_failid("C:\\Users\\Ximaks\\Desktop\\Всякие приложения")

for dirpath, dirnames, filenames in os.walk('C:\\Users\\Ximaks\\Desktop\\Всякие приложения'):
    print('Current path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)