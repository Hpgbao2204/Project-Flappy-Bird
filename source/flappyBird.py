import pygame, sys, random
from pygame.locals import *

WINDOWWIDTH = 400 # Chiều dài cửa sổ
WINDOWHEIGHT = 600 # Chiều cao cửa sổ
BIRDWIDTH = 40
BIRDHEIGHT = 35
G = 0.5
SPEEDFLY = -8


COLUMNWIDTH = 60
COLUMNHEIGHT = 500
BLANK = 160
DISTANCE = 200
COLUMNSPEED = 2


pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()


DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Flappy Bird')

BACKGROUND = pygame.image.load('img\\background.png').convert_alpha()
BACKGROUND = pygame.transform.scale(BACKGROUND, (WINDOWWIDTH, WINDOWHEIGHT))

BIRDIMG = pygame.image.load('img\\icon.png')
BIRDIMG = pygame.transform.scale(BIRDIMG, (BIRDWIDTH, BIRDHEIGHT))

COLUMNIMG = pygame.image.load('img\\images.png')
COLUMNIMG = pygame.transform.scale(COLUMNIMG, (COLUMNWIDTH, COLUMNHEIGHT))

def main():
    bird = Bird()
    col = Column()
    while True:
        mouseClick = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mouseClick = True
                
        DISPLAYSURF.blit(BACKGROUND, (0, 0))
        
        bird.draw()
        bird.update(mouseClick)
        
        col.draw()
        
        pygame.display.update()
        fpsClock.tick(FPS)

class Bird():
    def __init__ (self):
        self.width = BIRDWIDTH
        self.height = BIRDHEIGHT
        self.x = (WINDOWWIDTH - self.width) / 2
        self.y = (WINDOWHEIGHT - self.height) / 2
        self.speed = 0
        self.suface = BIRDIMG
        
    def draw(self):
        DISPLAYSURF.blit(self.suface, (int(self.x), int(self.y)))
        
    def update(self, mouseClick):
        self.y += self.speed + 0.5 * G
        self.speed += G
        if mouseClick == True:
            self.speed = SPEEDFLY
            
class Column():
    def __init__(self):
        self.width = COLUMNWIDTH
        self.height = COLUMNHEIGHT
        self.blank = BLANK
        self.distance = DISTANCE
        self.speed = COLUMNSPEED
        self.surface = COLUMNIMG
        self.ls = []
        
        for i in range(3):
            x = i * self.distance
            y = random.randrange(60, WINDOWHEIGHT - self.blank - 60, 20)
            self.ls.append([x, y])
            
    def draw(self):
        for i in range(3):
            DISPLAYSURF.blit(self.surface, (self.ls[i][0], self.ls[i][1] - self.height))
            DISPLAYSURF.blit(self.surface, (self.ls[i][0], self.ls[i][1] + self.blank))
if __name__ == '__main__':
    main()