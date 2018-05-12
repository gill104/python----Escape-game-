from classes import vector2
from config import globals as G
from classes import upgrade
from classes import boss
import pygame
import math
import random
from classes import bossBullet
class enemy(object):
    """description of class"""
    def __init__(self, position, type, worth):
        self.position = vector2.Vec2d(position)
        self.velocity = vector2.Vec2d(0,-G._ENEMY_SPEED)
        self.initTime = pygame.time.get_ticks()
       # self.img = pygame.image.load( img ).convert_alpha()
        self.img = G._ENEMIES_SURFACE[type]
        self.alive = True
        self.size = self.img.get_size()
        self.radius = self.img.get_width()/2
        self.worth = worth
        self.deleteMe = False
        self.tag = "enemy"
        self.crashSound = G._ENEMYDEATHSOUND
        self.lastShot = pygame.time.get_ticks()
        
        #DIRECTION: 1 down, 2 up, 3 left, 4 right
        self.direction = 2
        self.setRandomDirection = False

    def update(self, delta):
        #update movement
        self.position += self.velocity * delta
        self.checkWalls()
        thisTime = pygame.time.get_ticks()
        #if (self.setRandomDirection == True):

        #Unrandom Direction
        if (thisTime -self.initTime == -1):
            pass
        if ( thisTime - self.initTime > G._CHANGEDIRECTION_INTERVAL):
            self.changeDirection_straight()
            self.initTime = thisTime
            self.setRandomDirection = False
        self.shoot()


    def shoot(self):
        if ((pygame.time.get_ticks() > (self.lastShot + G._ENEMY_SHOOTINGSPEED))):
            r = random.randint(0, 100)
            if (r < 30):
                b = bossBullet.bossBullet((self.position.x, self.position.y), 7, "enemy", 1)
                G._BOSS.bullets.append(b)
            self.lastShot = pygame.time.get_ticks()

    def setRandomDir(self, direction):
        self.setRandomDirection = True
        self.direction = direction

    def draw(self, screen):

        if (self.alive):
            screen.blit( self.img, (self.position.x-self.size[0]/2, self.position.y-self.size[1]/2))

    def changeDirection_straight(self):
        if (self.direction > 5):
            self.direction = 1
        if (self.direction == 1):
            self.velocity.y = G._ENEMY_SPEED
            self.velocity.x = 0
        elif (self.direction == 2):
            self.velocity.y = -G._ENEMY_SPEED
            self.velocity.x = 0
        elif (self.direction == 3):
            self.velocity.y = 0
            self.velocity.x = -G._ENEMY_SPEED
        elif (self.direction == 4):
            self.velocity.y = 0
            self.velocity.x = G._ENEMY_SPEED

    def checkWalls(self):
        if self.position.x + self.radius >= G._SCREEN_WIDTH:
            self.position.x = G._SCREEN_WIDTH - self.radius
            self.velocity.x = 0
        elif self.position.x - self.radius <= G._GUI_WIDTH:
            self.position.x = self.radius + G._GUI_WIDTH
            self.velocity.x = 0

        if self.position.y + self.radius >= G._SCREEN_HEIGHT:
            #self.position.y = G._SCREEN_HEIGHT - self.radius
            #self.velocity.y = 0
            self.deleteMe = True
            
        elif self.position.y - self.radius <= 0:
            self.position.y = self.radius
            self.velocity.y = 0

    def die(self):
        G._SCORE += self.worth
        x = random.randint(0,100)
        y = random.randint(0,100)
        type = random.randint(0, 3)
        self.crashSound.play()

        if (x < G._UPGRADEPROBABILITY):
            upgr = upgrade.upgrade(self.position,"shoot")
            G._UPGRADE_ARRAY.append(upgr)
            self.deleteMe = True
        
        if(y < G._UPGRADESHEILDPROB):
            print "hwerwehrwehr"
            shield = upgrade.upgrade(self.position,"shield")
            G._UPGRADE_ARRAY.append(shield)
            #G._SHEILD_UPGRADE = 1
            self.deleteMe = True
                

        if G._SCORE > G._LASTSCORE:
            if G._ENEMY_SHOOTINGSPEED > 1000:
                G._ENEMY_SHOOTINGSPEED -= 1000
                G._LASTSCORE += G._INCREASESCORE
            if G._MINENEMYSPAWNTIME > 300:
                G._MINENEMYSPAWNTIME -= 100
                G._MAXENEMYSPAWNTIME -= 50
                print "update"
           