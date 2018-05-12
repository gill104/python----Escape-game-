import pygame
from config import globals as G
from classes import player as P

class GUI:
    def __init__(self):
        self.myfont = pygame.font.SysFont("monospace", 25)
        self.myfont2 = pygame.font.SysFont("monospace",10)
        self.myfont3 = pygame.font.SysFont("monospace",10)
        self.myfont4 = pygame.font.SysFont("monospace",25)
        self.colorG = 255
        self.show_img = False
        self.frames = 0
        self.sidebar = pygame.image.load(G._ASSET_DIR + "sidebar.png").convert_alpha()

#   corrected this, now it takes in an array for the images to be loaded
    def get_img(self, x):
        The_img = pygame.image.load(G._ASSET_DIR+str(G._SHOT_UPGRADES)+".png").convert_alpha()
        self.size = [int(x*1) for x in The_img.get_size()]
        self.img = pygame.transform.scale(The_img, self.size)
        return self.img

   #made the blinking work when player has no upgrades
    def ifGotten_upgrades(self,screen,delta):
        if G._SHOT_UPGRADES == 0:
            #print "SHOOTING REGULAR"
            self.frames += delta
            #print self.frames
            wer = self.get_img(0)

            if self.show_img:
                #pygame.draw.circle(screen,(91,91,91),(25,500),10)
                screen.blit(wer,(15,500))
                if self.frames > 400:
                    self.frames = 0
                    self.show_img = False
            else:
                if self.frames > 200:
                    #pygame.draw.circle(screen,(91,91,91),(25,500),10)
                    screen.blit(wer,(15,500))
                    self.show_img = True

        
        else :
            wer = self.get_img(G._SHOT_UPGRADES)
            self.size1 = [int(x*1) for x in wer.get_size()]
            self.img1 = pygame.transform.scale(wer, self.size)
            screen.blit(self.img1,(25,526))

            Upgrd_img = pygame.image.load(G._ASSET_DIR + G._WEAPONS_DIR + "blastpowerup1.png").convert_alpha()
            self.size2 = [int(x*5) for x in Upgrd_img.get_size()]
            self.img2 = pygame.transform.scale(Upgrd_img, self.size)
            screen.blit(self.img2,(20,500))
            

    def ifGotten_Sheild(self,screen):
        if G._UPGRADE_SHIELD == 1:
            pygame.draw.circle(screen,(255,0,0), (100,510),15,2)            
        
    def ifGotten_Bomb(self, screen):

        pass          
              
    #draws on the screen        
    def draw(self, screen, delta):
        label = self.myfont.render("Score: " + str(G._SCORE), 1, (255,255,0))
        label2 = self.myfont2.render("Life:",1,(255,255,0))
        label3 = self.myfont3.render("Shield:",1,(255,255,0))
        #label4 = self.myfont4.render("S",1,(255,255,0))
        #screen.blit(label4,(100,510))
        #pygame.draw.line(screen,(255,255,255),)
        #sidebar = pygame.draw.rect(screen,(91,91,91),pygame.Rect(0,0,G._GUI_WIDTH,G._SCREEN_WIDTH),0)
        screen.blit(self.sidebar, (0,0))
        #screen.blit(self.imgback, (0,0))
        screen.blit(label, (10, 50))
        screen.blit(label2, (10,475))
        screen.blit(label3, (75,475))
        self.ifGotten_upgrades(screen, delta)
        self.ifGotten_Sheild(screen)