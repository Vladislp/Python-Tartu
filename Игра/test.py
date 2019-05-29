import pygame

pygame.init()

FPS = 60

#Scales
GAMEBOY         = 1        #240x160  (Standard gameboy resolution)
FOUREIGHTYP     = 2        #480x320  (480p resolution)
SEVENTWENTYP    = 4        #960x640  (720p resolution)
TENEIGHTYP      = 6        #1440x960 (1080p resolution)

scale = GAMEBOY

resolution = (240*scale, 160*scale)

clock = pygame.time.Clock()

pygame.mixer.quit()

screen = pygame.display.set_mode(resolution)

movie = pygame.movie.Movie('MELT.MPG')

surface = pygame.Surface(movie.get_size()).convert()

#Gamestates
introsequence = 1
mainmenu      = 2

def introsequence(screen, surface):
    movie1Playing = True
    movie2Playing = False
    playedEarly = False
    frames = 0
    earlyCounter = 0

    movie = pygame.movie.Movie('MELT.MPG')
    movie.set_display(surface)
    movie.play()
    movie.set_volume(0.5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                movie.stop()
                pygame.quit()   #<---- Here
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if frames > 300 and movie1Playing:
                        movie.stop()
                        playedEarly = True
                        movie1Playing = False
                        movie2Playing = True
                        movie = pygame.movie.Movie('MELT.MPG')
                        movie = pygame.movie.Movie('MELT.MPG')
                        surface = pygame.Surface(movie.get_size()).convert()
                        movie.set_display(surface)
                        movie.play()
                        movie.set_volume(0)
                        frames = 0
                    elif movie2Playing:
                        pygame.quit()    #<----- Here

        if movie.get_busy() == 0:
            if movie1Playing == True:
                movie.stop()
                movie1Playing = False
                movie2Playing = True
                movie = pygame.movie.Movie('MELT.MPG')
                movie = pygame.movie.Movie('MELT.MPG')
                surface = pygame.Surface(movie.get_size()).convert()
                movie.set_display(surface)
                movie.play()
                movie.set_volume(0.5)
                frames = 0
            else:
                movie.stop()
                movie1Playing = True
                movie2Playing = False
                movie = pygame.movie.Movie('MELT.MPG')
                movie = pygame.movie.Movie('MELT.MPG')
                surface = pygame.Surface(movie.get_size()).convert()
                movie.set_display(surface)
                movie.play()
                movie.set_volume(0.5)
                frames = 0

        if playedEarly:
            earlyCounter += 1
            if earlyCounter > 67:
                movie.set_volume(0.5)
                playedEarly = False
                earlyCounter = 0
        frames += 1

        screen.blit(surface,(0,0))
        pygame.display.update()
        clock.tick(FPS)



def mainMenu(screen, surface):
    pass

def main(screen, surface):
    currentGamestate = introsequence
    pygame.mixer.quit()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()         #<---- and here

        if currentGamestate == introsequence:
            introsequence(screen, surface)
        else:
            pygame.mixer.init()
            if currentGamestate == mainmenu:
                mainMenu(screen, surface)

if __name__ == "__main__":
    main(screen, surface)