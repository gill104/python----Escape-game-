from config import globals as G
import pygame

class upgrade:
    def __init__(self, position,tag):
        self.tag = tag
        self.img = pygame.image.load(  G._ASSET_DIR + G._WEAPONS_DIR + "greenorbpoweruptile.png").convert_alpha()
        self.img = pygame.transform.scale(self.img, (self.img.get_width() * 2, self.img.get_height()*2))
        self.myfont = pygame.font.SysFont("monospace", 20)

        self.position = position
        self.size = [int(x) for x in self.img.get_size()]
        self.initTime = pygame.time.get_ticks()
        self.deleteMe = False
        self.radius = self.img.get_width()/2

    def update(self, delta):
        if (pygame.time.get_ticks() > (self.initTime + G._UPGRADE_TIMER)):
            self.deleteMe = True
        if self.deleteMe:
            G._UPGRADE_ARRAY.remove(self)
            
    def draw(self, screen):
        print self.tag
        if(self.tag == "shield"):
        #    print "shield is true"
            label = self.myfont.render("S ", 1, (255,255,0))
            screen.blit(label,(int(self.position.x-self.size[0]), int(self.position.y - 7 -self.size[1])))
            pygame.draw.circle(screen,(255,0,0), (int(self.position.x - 1-self.size[0]/2), int(self.position.y-self.size[1]/2)),10,2)
        else:
        #    print "in the else"
            pygame.draw.circle(screen,(255,255,0),(int((self.position.x + 8)-self.size[0]/2), int((self.position.y + 5)-self.size[1]/2)),10, 1)
            screen.blit( self.img, (self.position.x-self.size[0]/2, self.position.y-self.size[1]/2))