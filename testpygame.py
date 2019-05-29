pygame.init()
myname=input('What is your name')

#set the window size
window= pygame.display.set_mode((800,600) ,0,24)
pygame.display.set_caption("Fruit Catch")

#game variables
gameover=pygame.image.load('gameover.jpg')
myscore=0
file = 'score.txt'
eating=pygame.mixer.Sound('data/eating.wav')
die=pygame.mixer.Sound('die.wav')
mylives=3
mouth_x=300
fruit_x=250
fruit_y=75
fruitlist=['broccoli.gif','chicken.gif']
keyclicks=0
#prepare for screen
myfont=pygame.font.SysFont("Britannic Bold", 55)
label1=myfont.render(myname, 1, (240, 0, 0))
label3=myfont.render(str(mylives), 1, (20, 255, 0))
#grapchics
fruit=pygame.image.load('data/chicken.png')
mouth=pygame.image.load('data/v.gif')
backGr=pygame.image.load('data/kfc.jpg')
backGr1=pygame.image.load('sj.jpg')
#endless loop
running=True
while running:
    if fruit_y>=460:#check if at bottom, if so prepare new fruit
       fruit_x=random.randrange(50,530,1)
       fruit_y=75
       fruit=pygame.image.load('data/'+fruitlist[random.randrange(0,2,1)])
       caught= fruit_x>=mouth_x and fruit_x<=mouth_x+500
    else:fruit_y+=5

   #check collision
    if fruit_y>=456:
       mylives-=1
    if fruit_y>=440:
            if fruit_x>=mouth_x and fruit_x<=mouth_x+300 :
                    myscore+=1
                    fruit_y=600#move it off screen
                    eating.play()

    pygame.mouse.get_pressed() 
    for event in pygame.event.get():
            if (event.type==pygame.KEYDOWN):
                if (event.key==pygame.K_LEFT):
                        mouth_x-=55
                        keyclicks+=1
                if (event.key==pygame.K_RIGHT):
                        mouth_x+=55
                        keyclicks+=1 
            if event.type==MOUSEBUTTONDOWN and keyclicks>=2 :
                pygame.quit()
    label3=myfont.render(str(mylives), 1, (20, 255, 0))
    label2=myfont.render(str(myscore), 1, (20, 255, 0))
    text1='You caught'+str(myscore)
    text3='Press the mouse to close the game'
    label4=myfont.render(text1, 1, (135, 206, 250))
    myfont1=pygame.font.SysFont("Britannic Bold", 40)
    label5=myfont1.render(text3, 1, (255, 0, 0))

    if mylives==0:
       window.blit(gameover, (0,0))
       window.blit(label4, (500,400))
       die.play()
       pygame.time.get_ticks
       pygame.display.update()
       running=False
       webbrowser.open(file)

    else:

        window.blit(backGr,(0,0))
        window.blit(mouth, (mouth_x,440))
        window.blit(fruit,(fruit_x, fruit_y))
        window.blit(label1, (174, 537))
        window.blit(label2, (700, 157))
        window.blit(label3, (700, 400))
        window.blit(label5, (10, 0))
        pygame.display.update()