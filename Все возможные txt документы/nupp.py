nupp1 = pygame.Rect(150,450,100,50)
pygame.draw.rect(ekraani_pind, (red), nupp1)
pygame.display.flip()

nupp2 = pygame.Rect(550,450,100,50)
pygame.draw.rect(ekraani_pind, (green), nupp2)
pygame.display.flip()


ekraani_pind = pygame.display.set_mode( (800, 600))
pygame.display.set_caption("One Day After")
ekraani_pind.fill( (255,255,255) )