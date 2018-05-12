import pygame
from classes import vector2
from config import globals as G
from classes import bossBullet

class boss(object):
    """description of class"""
    def __init__(self, position, img):

        self.velocity = vector2.Vec2d(0,G._ENEMY_SPEED)
        self.img = pygame.image.load(G._ASSET_DIR + G._SHIPS_DIR + img).convert_alpha()
        self.radius = self.img.get_width()/2
        self.size = [int(x) for x in self.img.get_size()]
        self.img = pygame.transform.scale(self.img, (self.size[0]*2, self.size[1]*2))
        self.position = vector2.Vec2d(position)
        self.state = "up"
        self.lastShot = pygame.time.get_ticks()

        #array of boss bullets
        self.bullets = []

    def update(self, delta):
        if (self.position.y < (G._STARTING_Y + 100 ) and self.state == "up"):
            print "moving up"
            self.velocity = self.velocity * -1
            self.state = "down"
            self.shoot()
        if (self.position.y > G._BOTTOMTHRESHOLD and self.state == "down"):
            print "moving down"
            self.velocity = self.velocity * -1
            self.state = "up"
    


        self.position += self.velocity * delta

        for bullet in self.bullets:
            bullet.update(delta)
            if (bullet.deleteMe):
                self.bullets.remove(bullet)
        

    def shoot(self):
        bll1 = bossBullet.bossBullet((self.position.x -22, self.position.y - 52), 1, "boss", -1)
        bll2 = bossBullet.bossBullet((self.position.x + 180, self.position.y - 52),2, "boss", -1)
        self.bullets.append(bll1)
        self.bullets.append(bll2)

    def draw(self, screen):
        screen.blit( self.img, (self.position.x-self.size[0]/2, self.position.y-self.size[1]/2))
        for bullet in self.bullets:
            bullet.draw(screen)


