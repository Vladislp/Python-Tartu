from asfe import words

def eng():
    eng_words=dict([[v, k] for k,v in words.items()])
    find_words=input('Enter word ' '')
    print(eng_words.get(find_word) or print('No such key'))
    
def est():
    key=input('Sisesta sõna ' '')
    print(words.get(key) or 'Sellist sõna pole')
    
if __name__ == '__main__':
    x=input('Pss, tahad tõlkitud sõna(y/n) ? ' '')
    if x == 'y':
        est()
    elif x == 'n':
        eng()
    else:
        print('Head päeva')