import pygame
import sys

 
pygame.init()
#############
pygame.mixer.music.load('Invincible.mp3')
pygame.mixer.music.play()

#############
clock = pygame.time.Clock() 
 
display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)
 
block_color = (53,115,255)
 
 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('One Day After')
clock = pygame.time.Clock()

gameIcon = pygame.image.load('gameicon.jpg')
pygame.display.set_icon(gameIcon)

pause = False
 
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 
 
def GameOver():
    ####################################
    pygame.mixer.Sound.play("smb_gameover.wav")
    pygame.mixer.music.stop()
    ####################################
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Game Over", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        

        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15) 

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            pygame.mixer.music.stop()
            action()

    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    

def quitgame():
    pygame.quit()
    sys.exit()
    quit()
    
def hide_text():
    global display_text
    global display_button_1
    global display_button_2

    display_text = False
    display_button_1 = False
    display_button_2 = True

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False
    

def paused():
    ############
    pygame.mixer.music.pause()
    #############
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)   


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
          
        pilt1 = pygame.image.load('apoc2.jpg').convert()
        gameDisplay.blit(pilt1, [0,0])
         
        button("Start",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()

def game_loop():
    global display_text
    global display_button_1
    global display_button_2

    gameExit = False
    display_text = True
    display_button_1 = True
    display_button_2 = False

    meie_font = pygame.font.SysFont("Arial", 36)

    tekst = "This game will go as far as you choose!"
    teksti_pilt1 = meie_font.render(tekst, False, (50,50,155))

    tekst2 = "You are the smith of your destiny"
    teksti_pilt = meie_font.render(tekst2, False, (50,50,155))
########################################################################
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        gameDisplay.fill(white)
########################################################################
        if display_text:
            gameDisplay.blit(teksti_pilt1, (100, 250))
            gameDisplay.blit(teksti_pilt, (100, 400))
########################################################################
        if display_button_1:
            button("Start playing", 300,500,150,50,green,bright_green, hide_text)
########################################################################
        if display_button_2:
            #gameDisplay.fill(white)
            bg = pygame.image.load("natsalo.jpg")
            gameDisplay.blit(bg, (0, 0))
            
            tekst = "You, just have a friendly dinner with your family!"
            meie_font = pygame.font.SysFont("Arial", 36)
            teksti_pilt = meie_font.render(tekst, False, (25,25,155))
            gameDisplay.blit(teksti_pilt, (100, 30))
            
            tekst = "It wasn't so usualy as always, it was always something...!"
            meie_font = pygame.font.SysFont("Arial", 36)
            teksti_pilt = meie_font.render(tekst, False, (25,25,155))
            gameDisplay.blit(teksti_pilt, (50, 100))
            
            tekst = "You are Lee Everett, you are a professor who taught history"
            meie_font = pygame.font.SysFont("Arial", 36)
            teksti_pilt = meie_font.render(tekst, False, (25,25,155))
            gameDisplay.blit(teksti_pilt, (25, 170))
            
            tekst = "For over six years at the University of Georgia"
            meie_font = pygame.font.SysFont("Arial", 36)
            teksti_pilt = meie_font.render(tekst, False, (25,25,155))
            gameDisplay.blit(teksti_pilt, (100, 240))
            
            tekst = "You, just have a friendly dinner with your family!"
            meie_font = pygame.font.SysFont("Arial", 36)
            teksti_pilt = meie_font.render(tekst, False, (25,25,155))
            gameDisplay.blit(teksti_pilt, (100, 310))
            
            button("I am to lazy to wash hands, just sit", 100,500,600,50,green,bright_green, hide_text)
            button("Wash your hands", 100,400,600,50,green,bright_green, next_screen)
            
        def next_screen():
            gameDisplay.fill( (0,0,0) )
            

        pygame.display.update()


                           
game_intro()
game_loop()
pygame.quit()
quit()