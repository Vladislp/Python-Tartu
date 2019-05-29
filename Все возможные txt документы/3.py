import random

def minu_shuffle(list):
    list = [1, 2, 3, 4, 5, 6]
    uus = random.choices(list, k=6)
    print(uus)

    