import random
import time

def Intro():
    print("Действия происходят параллельно комиксу и являются частью его канона")
    time.sleep(2)
    print("Центральным персонажем Вы, Ли Эверетт, специально созданный для нее")
    time.sleep(2)
    print("Некоторые из персонажей оригинального комикса так же присутствуют в игре")
    time.sleep(2)
    print("Выш путь начинается с того, что вас везут в тюрьму")
    time.sleep(2)
    print("Вы обвеняется в убийстве губернатора штата")
    time.sleep(2)
    print("По пути в тюрьму, полицейский крузер сбил человека на дороге")
    time.sleep(2)
    print("Произошла авария, в итоге вы потеряли сознание")
    time.sleep(2)
    print("Вы медленно открываете глаза, и слышите крики кого то")
    time.sleep(2)
    print("Вы не смогли сразу очнутся, и отключились, очнувшись вы почувствовали ужастную боль")
    time.sleep(2)
    print("У вас повреждена нога, но вы смогли выбраться из машины")
    time.sleep(2)
    print("Вы видите труп офицера, дробавик и один патрон")
    
    
def choosePath():
    path = ""
    while path != "1" and path != "2":
        path = input("Что вы будете делать? :")
        
    return path

def checkpath(chosenPath):
    print("Вы выбрали...")
    time.sleep(2)
    print("Вы с трудом смогли поднять патрон")
    time.sleep(2)
    print("Опять посмотрев на труп, вас бросает в дрожь")
    print()
    time.sleep(2)
    
    correctPath = random.randint(1, 2)
    
    if chosenPath == str(correctPath):
        print("Это дрожь явно не сулит ничего хорошего")
        time.sleep(2)
        print("Вы решаете подойти к трупу офицера")
    else:
        print("afaf")
        print("afafa")
        print("afafa")
        
playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    Intro()
    choice = choosePath()
    checkpath(choice)
    playAgain = input("Snovo: ")
        