import pygame, pygame.mixer
import sys

pygame.init()

# --- constants ---

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

block_color = (53,115,255)



# --- functions ---

def text_objects(text, font, color=black):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, click, action=None):
    
    click1 = pygame.mixer.Sound('Sound.wav')

    mouse = pygame.mouse.get_pos()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click == 1 and action != None:# <-- click instead of click[0]
            pygame.mixer.music.stop()
            click1.play()
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

# --- scenes ---

# - scene Paused -

def unpause():
    global pause
    #pygame.mixer.music.unpause()

    pause = False

def paused():
    global pause

    pause = True
    
    sound = pygame.mixer.Sound('click.mp3')
    
    sound.play()

    background_image = pygame.Surface((display_width, display_height)).convert()
    background_rect = background_image.get_rect(center=(display_width//2, display_height//2))
    background_image.set_alpha(220)

    gameDisplay.blit(background_image, background_rect)

    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largeText, white)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:

        mouse_button = 0 # reset in every loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_button = event.button
                sound.play()
                

        button("Continue",150,450,100,50,green,bright_green, mouse_button, unpause)
        button("Quit",550,450,100,50,red,bright_red, mouse_button, quitgame)

        pygame.display.update()
        clock.tick(15)   

# - scene GameOver -

def GameOver():

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Game Over", largeText)
    TextRect.center = ((display_width/2),(display_height/2))

    gameDisplay.blit(TextSurf, TextRect)

    while True:

        mouse_button = 0 # reset in every loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_button = event.button

        button("Play Again",150,450,100,50,green,bright_green, mouse_button, game_loop)
        button("Quit",550,450,100,50,red,bright_red, mouse_button, quitgame)

        pygame.display.update()
        clock.tick(15) 

# - scene GameIntro -

def game_intro():

    # - objects -

    pilt1 = pygame.image.load('apoc2.jpg').convert()
    
    # - Sound -
    
    click1 = pygame.mixer.Sound('Sound.wav')
    
    # - loop -

    intro = True

    while intro:

        # - events -

        mouse_button = 0 # reset in every loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_button = event.button
                click1.play()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused()

        # - updates -

        button("Start",150,450,100,50,green,bright_green, mouse_button, game_loop)
        button("Quit",550,450,100,50,red,bright_red, mouse_button, quitgame)

        # - draws -

        #gameDisplay.blit(pilt1, [0,0])
        pygame.display.update()

# - scene GameLoop -

def goto_subscene(number):
    global display_subscene

    display_subscene = number

def game_loop():
    global display_subscene
###############################################################################
    # at start display subscene 1
    display_subscene = 1 

    #bg = pygame.image.load("natsalo.jpg")

    meie_font = pygame.font.SysFont("Arial Black", 15)
###############################################################################
    # - subscene 1 -

    tekst = "This game will go as far as you choose!"
    subscene_1_text_1 = meie_font.render(tekst, False, (50,50,155))

    tekst = "You are the smith of your destiny"
    subscene_1_text_2 = meie_font.render(tekst, False, (50,50,155))
###############################################################################
    # - subscene 2 -

    tekst = "You just finished school this year."
    subscene_2_text_1 = meie_font.render(tekst, False, (25,25,155))

    tekst = "Had to find some work before going to college in the capital"
    subscene_2_text_2 = meie_font.render(tekst, False, (25,25,155))

    tekst = "jlk"
    subscene_2_text_3 = meie_font.render(tekst, False, (25,25,155))

    tekst = "You just met them last monday"
    subscene_2_text_4 = meie_font.render(tekst, False, (25,25,155))

    tekst = "You are a nice person and you brought some food"
    subscene_2_text_5 = meie_font.render(tekst, False, (25,25,155))
###############################################################################
    # - subscene 3 -

    tekst = "You killed by viruses !"
    subscene_3_text_1 = meie_font.render(tekst, False, white)
###############################################################################
    # - subscene 4 -

    tekst = "You went to the bathroom, peasfully washing you hands"
    subscene_4_text_1 = meie_font.render(tekst, False, white)
    tekst = "You heard some noises, it was only wind"
    subscene_4_text_2 = meie_font.render(tekst, False, white)
###############################################################################
    # - subscene 5 -

    tekst = "Good Bye !"
    subscene_5_text_1 = meie_font.render(tekst, False, white)
###############################################################################
    # - subscene 6 -
    
    tekst = "Hello beatch"
    subscene_6_text_1 = meie_font.render(tekst, False, white)
###############################################################################
    # - subscene 7 -
    
    tekst = "Test"
    subscene_7_text_1 = meie_font.render(tekst, False, white)
###############################################################################
    # - subscene 8 -
    
    tekst = "Test"
    subscene_8_text_1 = meie_font.render(tekst, False, white)
################################################################################
    # - subscene 9 -
    
    tekst = "Test"
    subscene_9_text_1 = meie_font.render(tekst, False, white)
#################################################################################
    # - subscene 10 -
    
    tekst = "Test"
    subscene_10_text_1 = meie_font.render(tekst, False, white)
##################################################################################
    # - subscene 11 -
    
    tekst = "Test"
    subscene_11_text_1 = meie_font.render(tekst, False, white)
##################################################################################
    # - subscene 12 -
    
    tekst = "test"
    subscene_12_text_1 = meie_font.render(tekst, False, white)
###################################################################################
    # - subscene 13 -
    
    tekst = "test"
    subscene_13_text_1 = meie_font.render(tekst, False, white)
####################################################################################
    # - subscene 14 -
    
    tekst = "test"
    subscene_14_text_1 = meie_font.render(tekst, False, white)
####################################################################################
    # - subscene 15 -
    
    tekst = "test"
    subscene_15_text_1 = meie_font.render(tekst, False, white)
#####################################################################################
    # - subscene 16 -
    
    tekst = "test"
    subscene_16_text_1 = meie_font.render(tekst, False, white)
#####################################################################################
    # - subscene 17 -
    
    tekst = "test"
    subscene_17_text_1 = meie_font.render(tekst, False, white)
    
    # - loop -

    gameExit = False

    while not gameExit:

        mouse_button = 0 # reset in every loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_button = event.button
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused()

        if display_subscene == 1:
            gameDisplay.fill(white)

            gameDisplay.blit(subscene_1_text_1, (100, 250))
            gameDisplay.blit(subscene_1_text_2, (100, 270))

            button("Start playing", 300,500,150,50,green,bright_green, mouse_button, lambda:goto_subscene(2))

            pygame.display.update()

        elif display_subscene == 2:
            gameDisplay.fill(white)

            gameDisplay.blit(subscene_2_text_1, (100, 30))
            gameDisplay.blit(subscene_2_text_2, (50, 100))
            gameDisplay.blit(subscene_2_text_3, (25, 170))
            gameDisplay.blit(subscene_2_text_4, (100, 240))
            gameDisplay.blit(subscene_2_text_5, (100, 310))

            button("Wash your hands", 100,400,600,50,green,bright_green, mouse_button, lambda:goto_subscene(4))
            button("I am to lazy to wash hands, just sit", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(3))

            pygame.display.update()

        elif display_subscene == 3:
            gameDisplay.fill(black)

            gameDisplay.blit(subscene_3_text_1, (100, 30))
            button("Go forward", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(5))

            pygame.display.update()

        elif display_subscene == 4:
            gameDisplay.fill(black)

            gameDisplay.blit(subscene_4_text_1, (100, 30))
            gameDisplay.blit(subscene_4_text_2, (200, 60))
            button("Go forward", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(5))
            button("Go Back", 50,400,500,100,green,bright_green, mouse_button, lambda:goto_subscene(6))

            pygame.display.update()

        elif display_subscene == 5:
            gameDisplay.fill(black)

            gameDisplay.blit(subscene_5_text_1, (100, 30))
            button("Exit", 100,500,600,50,green,bright_green, mouse_button, quitgame)

            pygame.display.update()
            
        elif display_subscene == 6:
            gameDisplay.fill(black)
            
            gameDisplay.blit(subscene_6_text_1, (100, 30))
            button("Go forward", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(6))
            
            pygame.display.update()
            
        elif display_subscene == 7:
            gameDisplay.fill(black)
            
            gameDisplay.blit(subscene_7_text_1, (100, 30))
            button("Go forward", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(6))
            
            pygame.display.update()
            
        elif display_subscene == 8:
            gameDisplay.fill(black)
            
            gameDisplay.blit(subscene_8_text_1, (100, 30))
            button("Go forward", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(6))
            
            pygame.display.update()
            
        elif display_subscene == 9:
            gameDisplay.fill(black)
            
            gameDisplay.blit(subscene_9_text_1, (100, 30))
            button("Go forward", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(6))
            
            pygame.display.update()
            
        elif display_subscene == 10:
            gameDisplay.fill(black)
            
            gameDisplay.blit(subscene_10_text_1, (100, 30))
            button("Go forward", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(6))
            
            pygame.display.update()
            
        elif display_subscene == 11:
            gameDisplay.fill(black)
            
            gameDisplay.blit(subscene_11_text_1, (100, 30))
            button("Go forward", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(6))
            
            pygame.display.update()
            
        elif display_subscene == 12:
            gameDisplay.fill(black)
            
            gameDisplay.blit(subscene_12_text_1, (100, 30))
            button("Go forward", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(6))
            
            pygame.display.update()
            
        elif display_subscene == 13:
            gameDisplay.fill(black)
            
            gameDisplay.blit(subscene_13_text_1, (100, 30))
            button("Go forward", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(6))
            
            pygame.display.update()
            
        elif display_subscene == 14:
            gameDisplay.fill(black)
            
            gameDisplay.blit(subscene_14_text_1, (100, 30))
            button("Go forward", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(6))
            
            pygame.display.update()
            
        elif display_subscene == 15:
            gameDisplay.fill(black)
            
            gameDisplay.blit(subscene_15_text_1, (100, 30))
            button("Go forward", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(6))
            
            pygame.display.update()
            
        elif display_subscene == 16:
            gameDisplay.fill(black)
            
            gameDisplay.blit(subscene_16_text_1, (100, 30))
            button("Go forward", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(6))
            
            pygame.display.update()
            
        elif display_subscene == 17:
            gameDisplay.fill(black)
            
            gameDisplay.blit(subscene_17_text_1, (100, 30))
            button("Go forward", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(6))
            
            pygame.display.update()
        
            

# --- main ---

# - init -

pygame.init()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('One Day After')

# - m

clock = pygame.time.Clock() 
pause = False

game_intro()
game_loop()
pygame.quit()