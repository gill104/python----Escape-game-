from config import globals as G
from classes import vector2
import pygame

class bossBullet(object):
    """description of class"""
    def __init__(self, position, type, tag, direction):
        self.position = vector2.Vec2d(position)
        #self.img = pygame.image.load(G._ASSET_DIR + G._WEAPONS_DIR + img).convert_alpha()
        self.img = G._BULLET_IMG_SURFACE[type]
        self.img = pygame.transform.scale(self.img, (self.img.get_width()*2, self.img.get_height()*2))
        self.velocity = vector2.Vec2d(0, 0.3 * direction)
        self.radius = self.img.get_width()/2
        self.size = [int(x) for x in self.img.get_size()]
        self.initTime = pygame.time.get_ticks()
        self.deleteMe = False
        self.tag = tag

    def update(self, delta):
         self.position += self.velocity * delta
         if (pygame.time.get_ticks() > self.initTime + G._BOSSBULLETTIMER):
             self.deleteMe = True

    def draw(self, screen):
         screen.blit( self.img, (self.position.x-self.size[0]/2, self.position.y-self.size[1]/2))
