import pygame
from classes import vector2
from config import globals as config
from classes import bullet as Bullet
from classes import boss as B

import math


class player:

    def __init__(self, position, image):

        #configuration variables
        self.speed = config._PLAYERSPEED
        self.timeForShooting = config._SHOOTINGSPEED #in mili seconds
        
        #construction variables
        

        #upgrade management
        self.upgrades = 0
        self.shotUpgrades = config._SHOT_UPGRADES
        self.velocityUpgrades = 0
        self.bombs = 0
        self.initTime = pygame.time.get_ticks()

        #position and movement
        self.position = vector2.Vec2d(position)
        self.velocity = vector2.Vec2d(0,0)
        self.vertical = 0
        self.horizontal = 0

        #image/collision
        self.img = pygame.image.load( image ).convert_alpha()
        self.radius = self.img.get_width()/2
        self.size = [int(x) for x in self.img.get_size()]

        #shooting data
        self.shootingTime = 0
        self.shooting = False
        self.bullets = []
        self.deletionArray = []
        self.shootSound = pygame.mixer.Sound(config._ASSET_DIR + config._BULLETSOUNDFILE)
        self.state ="neutral"
        self.crashSound = pygame.mixer.Sound(config._ASSET_DIR + "Jump.wav")


    def checkIfHit(self):
        for bullet in self.bullets:
            for spawn in config._ENEMYLIST:
                for enemy in spawn.enemies:
                    if (bullet.checkHit(enemy)):
                        enemy.die()
                        spawn.enemies.remove(enemy)


    def update(self, delta):

        # shooting timer management
        self.checkLastShot()
        
        #integrate position with velocity
        self.move(delta)
        self.position = self.position + (self.velocity * delta)
        self.checkWalls()
        self.horizontal = 0
        self.vertical = 0

        #update bullets as well
        for bullet in self.bullets: 
            bullet.update(delta)

        #Bullet Garbage collection
        i = 0
        for bullet in self.bullets:
            if(bullet.deleteMe):
                self.bullets.remove(bullet) 


        self.checkIfHit()
        #Check Collisions with enemies/upgrades
        self.checkCollide()

        if (self.state == "hit"):
            self.frame += 1
            if (self.frame >= 50):
                 self.img = config._SPACESHIP_SURFACE[0]
                 self.state = "neutral"   
        
    #Draw to screen
    def draw(self,screen):
        if(config._UPGRADE_SHIELD == 1):
            pygame.draw.circle(screen,(255,0,0), (int(self.position.x), int(self.position.y)),30,2)
            screen.blit( self.img, (self.position.x-self.size[0]/2, self.position.y-self.size[1]/2))
        else:
            screen.blit( self.img, (self.position.x-self.size[0]/2, self.position.y-self.size[1]/2))

        pygame.draw.circle(screen,(0,0,255),(int(config._BOSS.position.x + config._BOSS.radius),int(config._BOSS.position.y)),config._BOSS.radius+30)
        
        for bullet in self.bullets:
            bullet.draw(screen)
        
    #movement input management
    def move(self, delta):

        
        #inertia decay for stopping
        if (self.horizontal == 0 or self.vertical == 0):
            self.velocity = self.velocity * 0

        #movement code
        if (self.vertical > 0):
            self.velocity.y = -self.speed
        if (self.vertical < 0):
            self.velocity.y = self.speed
        if (self.horizontal > 0):
            self.velocity.x = self.speed
        if (self.horizontal < 0):
            self.velocity.x = -self.speed


        #account for compounding velocity
        if (self.horizontal <> 0  and self.vertical <> 0):
            self.velocity = self.velocity *.7

    def checkLastShot(self):
        #THIS IS TO CHECK IF YOU'RE ABLE TO SHOOT AGAIN
        if (pygame.time.get_ticks() > self.timeForShooting + self.shootingTime):
            self.shooting = False

    #pew pew. Modulized based on upgrades
    def shoot(self):
        if (self.shooting == False):

            #clerical stuff
            self.shootingTime = pygame.time.get_ticks()
            self.shooting = True

            #modular shots

            #level 0: pew, pew, pew
            if self.shotUpgrades == 0:
                newBullet = Bullet.Bullet(self.position, self.img, "0", False)
                self.bullets.append(newBullet)
                self.shootSound.play()

            #p-pew, p-pew, p-pew
            elif self.shotUpgrades == 1:
                newBullet = Bullet.Bullet(self.position, self.img, "1a", False)
                self.bullets.append(newBullet)
                newBullet = Bullet.Bullet(self.position, self.img, "1b", False)
                self.bullets.append(newBullet)
                self.shootSound.play()

            # shotgun pew pew
            elif self.shotUpgrades == 2:
                newBullet = Bullet.Bullet(self.position, self.img, "0", False)
                self.bullets.append(newBullet)
                newBullet = Bullet.Bullet(self.position, self.img, "2a", False)
                self.bullets.append(newBullet)
                newBullet = Bullet.Bullet(self.position, self.img, "2b", False)
                self.bullets.append(newBullet)
                self.shootSound.play()

            #shotgun pew pew, and a pew back too
            elif self.shotUpgrades == 3:
                newBullet = Bullet.Bullet(self.position, self.img, "0", False)
                self.bullets.append(newBullet)
                newBullet = Bullet.Bullet(self.position, self.img, "2a", False)
                self.bullets.append(newBullet)
                newBullet = Bullet.Bullet(self.position, self.img, "2b", False)
                self.bullets.append(newBullet)
                newBullet = Bullet.Bullet(self.position, self.img, "3", False)
                self.bullets.append(newBullet)
                self.shootSound.play()

            #shotgun p-pew p-pew, and a pew back too
            elif self.shotUpgrades == 4:
                newBullet = Bullet.Bullet(self.position, self.img, "1a", False)
                self.bullets.append(newBullet)
                newBullet = Bullet.Bullet(self.position, self.img, "1b", False)
                self.bullets.append(newBullet)
                newBullet = Bullet.Bullet(self.position, self.img, "2a", False)
                self.bullets.append(newBullet)
                newBullet = Bullet.Bullet(self.position, self.img, "2b", False)
                self.bullets.append(newBullet)
                newBullet = Bullet.Bullet(self.position, self.img, "3", False)
                self.bullets.append(newBullet)
                self.shootSound.play()

            #shotgun p-pew p-pew, and a pew back too, times two
            elif self.shotUpgrades >= 5:
                newBullet = Bullet.Bullet(self.position, self.img, "1a", True)
                self.bullets.append(newBullet)
                newBullet = Bullet.Bullet(self.position, self.img, "1b", True)
                self.bullets.append(newBullet)
                newBullet = Bullet.Bullet(self.position, self.img, "2a", True)
                self.bullets.append(newBullet)
                newBullet = Bullet.Bullet(self.position, self.img, "2b", True)
                self.bullets.append(newBullet)
                newBullet = Bullet.Bullet(self.position, self.img, "3", True)
                self.bullets.append(newBullet)
                self.shootSound.play()

    #collision detection
    def checkWalls(self):
        if self.position.x + self.radius >= config._SCREEN_WIDTH:
            self.position.x = config._SCREEN_WIDTH - self.radius
            self.velocity.x = 0
        elif self.position.x - self.radius <= config._GUI_WIDTH:
            self.position.x = self.radius + config._GUI_WIDTH
            self.velocity.x = 0
        #collides with the sidebar
        if self.position.y + self.radius >= config._SCREEN_HEIGHT:
            self.position.y = config._SCREEN_HEIGHT - self.radius
            self.velocity.y = 0
        elif self.position.y - self.radius <= 0:
            self.position.y = self.radius
            self.velocity.y = 0


    def upgrade(self, tag):
        if tag == "shoot":
            if config._SHOT_UPGRADES < 5:
                config._SHOT_UPGRADES += 1
                self.shotUpgrades += 1
        else:
            pass
    #check collisions with everything but walls
    def checkCollide(self):
        for spawn in config.masterspawn:
            for enemy in spawn.enemies:
                distance = math.sqrt((enemy.position.x - self.position.x)**2 + (enemy.position.y - self.position.y)**2)
                if(config._UPGRADE_SHIELD == 1):
                    #print "using this one"
                    distanceCheck = (self.radius + 10) + enemy.radius
                else:
                   # print "not thatother one"
                    distanceCheck = (self.radius) + enemy.radius
                
                if (distance < distanceCheck):
                    if config._SHOT_UPGRADES > 0:
                        if config._UPGRADE_SHIELD == 1:
                            print "shield is now zero"
                            config._UPGRADE_SHIELD = 0
                            spawn.enemies.remove(enemy)
                        else:
                            #maybe add a sound
                            ##YOU GET HIT BY AN ENEMY
                            if (self.state != "hit"):
                                self.state = "inithit"
                                self.crashSound.play()
                            if (self.state == "inithit"):
                                self.img = config._SPACESHIP_SURFACE[1]
                                self.frame = 0
                                self.state = "hit"
                            config._SHOT_UPGRADES -= 1
                            self.shotUpgrades -= 1
                            spawn.enemies.remove(enemy)
                    else:
                        if config._UPGRADE_SHIELD == 1:
                            print "shield is now zero"
                            config._UPGRADE_SHIELD = 0
                            spawn.enemies.remove(enemy)
                        else:
                            config._GAMEOVER = True

        for upgr in config._UPGRADE_ARRAY:
            distance = math.sqrt((upgr.position.x - self.position.x)**2 + (upgr.position.y - self.position.y)**2)
            distanceCheck = self.radius + upgr.radius
            if (distance < distanceCheck):
                if(upgr.tag == "shoot"):
                    print "tag is shoot"
                ## YOU GET AN UPGRADE!
                    self.upgrade(upgr.tag)
                    config._UPGRADE_ARRAY.remove(upgr)
                else:
                    if(upgr.tag == "shield"):
                        print "tag is shield"
                        self.upgrade(upgr.tag)
                        config._UPGRADE_SHIELD = 1
                        config._UPGRADE_ARRAY.remove(upgr)
        #boss check
        #BossCheck = B.boss((config._SCREEN_WIDTH/2,config._SCREEN_HEIGHT + 200), "theM.png")
        self.lastTouched = 3000

        distance = math.sqrt((config._BOSS.position.x + config._BOSS.radius - self.position.x)**2 + (config._BOSS.position.y - self.position.y)**2)
        
        distanceCheck = self.radius + config._BOSS.radius+25
        if(distance < distanceCheck):
                print "no upgrades collision"
                config._GAMEOVER = True

        for bossBullet in config._BOSS.bullets:
            distance = math.sqrt((bossBullet.position.x - self.position.x)**2 + (bossBullet.position.y - self.position.y)**2)
            if(config._UPGRADE_SHIELD == 1):
                #print "boss bull shield on"
                distanceCheck = (self.radius + 10 )+ bossBullet.radius
            else:
                #print "boss bull shield off"
                distanceCheck = (self.radius)+ bossBullet.radius
            if (distance < distanceCheck):
                if config._SHOT_UPGRADES > 0:
                    ##YOU GET HIT BY THE BOSS BULLET
                    if (bossBullet.tag == "boss"):
                        self.shotUpgrades = 0
                        config._SHOT_UPGRADES = 0
                        config._UPGRADE_SHIELD = 0
                    else:
                        if(config._UPGRADE_SHIELD == 1):
                            config._UPGRADE_SHIELD = 0
                        else:
                            self.shotUpgrades -= 1
                            config._SHOT_UPGRADES -= 1
                    bossBullet.deleteMe = True
                else:
                    if(bossBullet.tag != "boss" and config._UPGRADE_SHIELD == 1):
                        config._UPGRADE_SHIELD = 0
                        bossBullet.deleteMe = True
                    else:
                        if(bossBullet.tag == "boss" and config._UPGRADE_SHIELD == 1):
                            config._UPGRADE_SHIELD = 0
                            bossBullet.deleteMe = True
                        else:
                            config._GAMEOVER = True