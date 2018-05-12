import pygame
from classes import vector2
from config import globals as G

class asteroid:
    def __init__(self, screen, img):
        self.demoimg = pygame.draw.circle(screen,(255,255,225), G._SCREEN_HEIGHT,5)
        self.velocity = vector2.Vec2d(0,G._ENEMY_SPEED)
        self.position = vector2.Vec2d(position)
        self.radius = self.img.get_width()/2

    def draw(self, screen):
        screen.blit(self.demoimg, G._SCREEN_HEIGHT)
        
 
    def update(self, delta):
        pass
 
