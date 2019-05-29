import pygame, pygame.mixer

pygame.init()

red = (200,0,0)
black = (0,0,0)

white = (255,255,255)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

pygame.mixer.music.load('Invincible.mp3')
pygame.mixer.music.play()

ekraani_pind = pygame.display.set_mode( (800, 600))
pygame.display.set_caption("One Day After")
ekraani_pind.fill( (255,255,255) )

pilt1 = pygame.image.load('apoc2.jpg').convert()
ekraani_pind.blit(pilt1, [0,0])
pygame.display.flip()

mouse = pygame.mouse.get_pos()

nupp1 = pygame.Rect(150,450,100,50)
pygame.draw.rect(ekraani_pind, (red), nupp1)
pygame.display.flip()

nupp2 = pygame.Rect(550,450,100,50)
pygame.draw.rect(ekraani_pind, (green), nupp2)
pygame.display.flip()

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break


pygame.quit()
