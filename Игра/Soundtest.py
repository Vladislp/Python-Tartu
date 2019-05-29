import pygame, sys, time
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Memes.')


pygame.mixer.Sound.load("click.mp3")
pygame.mixer.Sound.play()
time.sleep(2)
pygame.mixer.Sound.stop()

while True: # Main Loop

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click1.play()
    pygame.display.update()