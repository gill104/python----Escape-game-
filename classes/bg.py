import pygame
from config import globals as G
from classes import vector2
import random

import time
class tile:
    def __init__(self, img, position):
        self.img = pygame.image.load(G._ASSET_DIR + str(img))
        self.position = vector2.Vec2d(position)
        self.velocity = vector2.Vec2d(0,-G._ENEMY_SPEED)

    def update(self, delta):
        self.position += self.velocity * delta

class bg(object):
    """description of class"""

    def __init__(self):
        self.bg = []
        startpos = (0, -100)
        currentpos = startpos
        self.currentX = 0
        self.currentY = -100
        self.firstLine = -100
        self.yPos = -100
        self.yVelocity = G._ENEMY_SPEED
        self.img = pygame.image.load(G._ASSET_DIR + "background/bg.jpg").convert()

        #create the tile grid
        #for x in range(0,11):
        #    for y in range (0,11):
        #        currentpos = (self.currentX, self.currentY)
        #        position = currentpos
        #        t = tile(G._BACKGROUND_IMGS[random.randint(0,3)],position)
        #        self.bg.append(t)
        #        self.currentX += 100
        #    self.currentX = 0
        #    self.currentY += 100
        #self.currentX = 0
        #self.currentY = -100

    def update(self, delta):
        #self.img = pygame.transform.rotate(self.img, .01 * delta)
        pass
        #for tile in self.bg:
        #    tile.update(delta)
        
        
        #if (self.yPos >= 0):
        #    self.createNewLine()
        #    self.yPos = 0
        #print self.yPos
    
    def createNewLine(self):
        for x in range(0,11):
                currentpos = (self.currentX, self.currentY)
                position = currentpos
                t = tile(G._BACKGROUND_IMGS[random.randint(0,3)],position)
                self.bg.append(t)
                self.currentX += 100
    

    def draw(self, screen):
       # for img in self.bg:
            #screen.blit(img.img, img.position)
            #print img.position
       # time.sleep(1000)
       screen.blit(self.img, (0,0))
