from classes import enemy
from config import globals as G
from classes import vector2
import pygame 
import random
class spawner(object):
    
    def __init__(self, count, type, startingPos):
        self.deleteMe = False
        self.enemies = []
        self.countX = count
        self.countY = 1
        self.type = type
        self.startingpos = vector2.Vec2d(startingPos)
        #self.imgType = pygame.image.load( G._ASSET_DIR +  G._SHIPS_DIR + G._ENEMYTYPE[self.type] ).convert()
        self.imgType = G._ENEMIES_SURFACE[self.type]
        self.size = self.imgType.get_size()
        self.initTime = pygame.time.get_ticks()
        self.initialize()

    def initialize(self):
        #set positions
        x = self.startingpos.x - self.size[0]/2 - 10
        counter = 0
        for i in range(0, self.countX/1):
            y = self.startingpos.y - self.size[1]/2 - 10
            for j in range (0, self.countY/1):
                Enemy = enemy.enemy((x,y), self.type, G._ENEMYTYPEWORTH[self.type])                
                self.enemies.append(Enemy)
                y += 100
            x += 100

    def update(self, delta):        
        randomDir = random.randint(1,4)
        for enemy in self.enemies:
            enemy.update(delta)
            if enemy.deleteMe == True:
                self.enemies.remove(enemy)
                self.deleteMe == True

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)






