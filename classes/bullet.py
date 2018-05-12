import pygame
from classes import vector2
from config import globals as G
import math
import random
class Bullet:
    def __init__(self, position, image, sType, maxed):
        self.img = G._BULLET_IMG_SURFACE[G._SHOT_UPGRADES]
        #bullets created based on upgrade type
        if maxed:
            self.radius = 10
        else:
            self.radius = 5

        #base bullet, also used in shotgun
        if sType == "0":
            self.velocity = vector2.Vec2d(0,-1)
            self.position = vector2.Vec2d(position.x, position.y)
            self.initTime = pygame.time.get_ticks()
            self.position.y -= image.get_height()/2
            self.deleteMe = False

        #Doubleshot 1
        elif sType == "1a":
            self.velocity = vector2.Vec2d(0,-1)
            self.position = vector2.Vec2d(position.x, position.y)
            self.initTime = pygame.time.get_ticks()
            self.position.y -= image.get_height()/2
            self.position.x -= 10
            self.deleteMe = False

        #Doubleshot 2
        elif sType == "1b":
            self.velocity = vector2.Vec2d(0,-1)
            self.position = vector2.Vec2d(position.x, position.y)
            self.initTime = pygame.time.get_ticks()
            self.position.y -= image.get_height()/2
            self.position.x += 10
            self.deleteMe = False

        #shotgun 1
        elif sType == "2a":
            self.velocity = vector2.Vec2d(-1,-1)
            self.position = vector2.Vec2d(position.x, position.y)
            self.initTime = pygame.time.get_ticks()
            self.position.y -= image.get_height()/2
            self.position.x -= 10
            self.deleteMe = False

        #shotgun 2
        elif sType == "2b":
            self.velocity = vector2.Vec2d(1,-1)
            self.position = vector2.Vec2d(position.x, position.y)
            self.initTime = pygame.time.get_ticks()
            self.position.y -= image.get_height()/2
            self.position.x += 10
            self.deleteMe = False

        #rearshot
        elif sType == "3":
            self.velocity = vector2.Vec2d(0,1)
            self.position = vector2.Vec2d(position.x, position.y)
            self.initTime = pygame.time.get_ticks()
            self.position.y += image.get_height()/2
            self.deleteMe = False


    #moving
    def update(self, delta):
        self.position += self.velocity * delta
        if (pygame.time.get_ticks() > (self.initTime + G._BULLET_LIFESPAN)):
            self.deleteMe = True
        self.checkWalls()

    #did I pew the things i want to pew? (Check collision)
    def checkHit(self, other):
        dist = self.position - other.position
        distMagnitude = math.sqrt(dist.x*dist.x + dist.y*dist.y)
        overlap = self.radius + other.radius - distMagnitude
        if overlap > 0:
            #YOU HIT SOMETHING
            if (other.alive):
                other.alive = False
                self.deleteMe = True
                return True
        return False   

    #I pewed the wrong pew... (wall collision)
    def checkWalls(self):
        
        if self.position.x + self.radius >= G._SCREEN_WIDTH:
            self.deleteMe = True
        elif self.position.x - self.radius <= 0:
            self.deleteMe = True

        if self.position.y + self.radius >= G._SCREEN_HEIGHT:
            self.deleteMe = True
        elif self.position.y - self.radius <= 0:
            self.deleteMe = True

    #show the pew (blit)
    def draw(self,screen):
        screen.blit(self.img, (int(self.position.x), int(self.position.y)))

