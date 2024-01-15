import pygame, sys, random
from pygame.locals import *

WINDOWWIDTH = 400 # Chiều dài cửa sổ
WINDOWHEIGHT = 600 # Chiều cao cửa sổ
BIRDWIDTH = 60
BIRDHEIGHT = 45
G = 0.5
SPEEDFLY = -8
BIRDIMG = pygame.image.load('img\\icon.png')

pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()


DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Flappy Bird')

BACKGROUND = pygame.image.load('img\\background.png').convert_alpha()
BACKGROUND = pygame.transform.scale(BACKGROUND, (WINDOWWIDTH, WINDOWHEIGHT))


def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        DISPLAYSURF.blit(BACKGROUND, (0, 0))
        
        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == '__main__':
    main()