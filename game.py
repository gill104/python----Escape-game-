#include everything
import sys
import random
import pygame
import math
from classes import player
from config import globals as config
from classes import GUI
from classes import enemy
from classes import spawner
from classes import vector2
from classes import bg
from classes import upgrade
from classes import boss

#init game
pygame.init()
screen = pygame.display.set_mode( (config._SCREEN_WIDTH,config._SCREEN_HEIGHT) )
pygame.display.set_caption( "ESCAPE" )
pygame.mixer.init()
pygame.mixer.music.load(config._ASSET_DIR + "theme.mp3")
pygame.mixer.music.play(-1,0.0)
running = True

#init classes and stuff
spaceship = player.player((config._STARTING_X,config._STARTING_Y), config._ASSET_DIR + config._SHIPS_DIR +config._SPACESHIP1[0])
config._PLAYER = spaceship
gui = GUI.GUI()

counter = 0
config.initEverything()
    
def getUserInput():
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        spaceship.vertical += 1
    if keys[pygame.K_DOWN]:
        spaceship.vertical -= 1
    if keys[pygame.K_LEFT]:
        spaceship.horizontal -=1
    if keys[pygame.K_RIGHT]:
        spaceship.horizontal += 1
    if keys[pygame.K_SPACE]:
        spaceship.shoot()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

#masterspawn = []  
config._ENEMYLIST = config.masterspawn
lastSpawn = pygame.time.get_ticks()
spawning = False


##SCENE 0 STUFF (START GAME SCREEN)
backgroundimg = pygame.image.load(config._ASSET_DIR + config._BACKGROUND_DIR + "escapebackgroundtitle.png").convert()
titleimg = pygame.image.load(config._ASSET_DIR + config._BACKGROUND_DIR + "ESCAPE.png").convert_alpha()
startimg = pygame.image.load(config._ASSET_DIR +config._BACKGROUND_DIR + "start.png").convert_alpha()
endimg = pygame.image.load(config._ASSET_DIR + config._BACKGROUND_DIR + "exit.png").convert_alpha()
arrowimg = pygame.image.load(config._ASSET_DIR + config._BACKGROUND_DIR + "arrow.png").convert_alpha()
config._ENEMYDEATHSOUND = pygame.mixer.Sound(config._ASSET_DIR + "enemyDie.wav")

#SCENE 1 stuff
bgrnd = bg.bg() 
bigBoss = boss.boss((config._SCREEN_WIDTH/2,config._SCREEN_HEIGHT + 200), "theM.png")
config._BOSS = bigBoss

#SCENE 2 STUFF (END GAME)
backgroundimg1 = pygame.image.load(config._ASSET_DIR + config._BACKGROUND_DIR + "/ENDING/badgameover.png")
returnimg = pygame.image.load(config._ASSET_DIR + config._BACKGROUND_DIR + "/ENDING/return.png")
gameoverplayed = False

while running:



    ##STARTING SCENE
    if (config._CURRENTSCENE == 0):
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        keys = pygame.key.get_pressed()
        
        pygame.event.pump()
        if (keys[pygame.K_RETURN]):
            if (config._SELECTION == 0):
                ##START GAME
                config._CURRENTSCENE += 1
                getTicksLastFrame = pygame.time.get_ticks();
            elif (config._SELECTION == 1):
                pygame.quit()

                sys.exit()

              
        if keys[pygame.K_UP]:
            if (config._SELECTION > 0):
                config._SELECTION -= 1
                config._ARROWPOS_Y -= 100
        if keys[pygame.K_DOWN]:
            if (config._SELECTION < 1):
                config._SELECTION += 1
                config._ARROWPOS_Y += 100

        screen.fill( (0,0,0) )
        screen.blit(backgroundimg, (0,0))
        screen.blit(titleimg, (100, 100))
        screen.blit(startimg, (config._SCREEN_WIDTH/2 - startimg.get_width()/2, 370))
        screen.blit(endimg, (config._SCREEN_WIDTH/2 - startimg.get_width()/2, 470))
        screen.blit(arrowimg, (config._ARROWPOS_X, config._ARROWPOS_Y))
        pygame.display.flip()

    #####GAME SCENE
    elif (config._CURRENTSCENE == 1):
       # get user events
        getUserInput()

        # do simulation stuff (line/image drawing in this case)
        #get deltaTime
        time = pygame.time.get_ticks()
        deltaTime = (time - getTicksLastFrame)
        getTicksLastFrame = time

        ########TRYING SOMETHING####### START
        if (spawning == False):
            randomCounter = random.randint(config._MINENEMYSPAWNTIME,config._MAXENEMYSPAWNTIME)
            #spawning = True


        if ((lastSpawn + randomCounter) < pygame.time.get_ticks()):
            spawn = spawner.spawner(random.randint(1,4), random.randint(0,config._NUMBEROFENEMYTYPES), ((random.randint(0,config._SCREEN_WIDTH), -10)))
            config.masterspawn.append(spawn)
            lastSpawn = pygame.time.get_ticks()
          ########TRYING SOMETHING####### END


        #bg
        bgrnd.update(deltaTime)

        #UPDATE PLAYER
        spaceship.update(deltaTime)

        bigBoss.update(deltaTime)



        #update enemies
        for spawn in config.masterspawn:
            if spawn.deleteMe == True:
                config.masterspawn.remove(spawn)
            spawn.update(deltaTime)

        counter = 0
        for spawn in config.masterspawn:
            for enemy in spawn.enemies:
                counter+= 1

        #print counter
        #UPDATE UPGRADES
        for upgr in config._UPGRADE_ARRAY:
            upgr.update(deltaTime)
        

        # draw to screen and flip
        screen.fill( (0,0,0) )

        #Draw background
        bgrnd.draw(screen)

        #DRAW PLAYER

        spaceship.draw(screen)
        bigBoss.draw(screen)

       #DRAW UPGRADES
        for upgr in config._UPGRADE_ARRAY:
            upgr.draw(screen)
#        upgrade.upgrade.draw(screen)

        #draw enemies
        for spawn in config.masterspawn:
            if(spawn.deleteMe):
                config.masterspawn.remove(spawn)
                print "spawn deleted"
            else:
                spawn.draw(screen)
 


        #DRAW GUI
        gui.draw(screen,deltaTime)
        pygame.display.flip()

        if (config._GAMEOVER):
            config._CURRENTSCENE = 2

    #####END SCREEN
    elif (config._CURRENTSCENE == 2):
        
        for spawn in config.masterspawn:
            config.masterspawn.remove(spawn)

        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        pygame.event.pump()
        if (keys[pygame.K_RETURN]):
            ## RESETING EVERYTHING (RESTART GAME)
            config._UPGRADE_SHIELD = 0
            config._CURRENTSCENE = 0
            config._SCORE = 0
            spaceship.position.x = config._STARTING_X
            spaceship.position.y = config._STARTING_Y
            config._SHOT_UPGRADES = 0
            config._GAMEOVER = False
            spaceship.shotUpgrades = config._SHOT_UPGRADES
            bigBoss.position.x = config._SCREEN_WIDTH/2
            bigBoss.position.y = config._SCREEN_HEIGHT + 200
            bigBoss.bullets = []
            config._UPGRADE_ARRAY = []
            config._LASTSCORE = config.lastscore
            config._INCREASESCORE = config.lastscore
            config._MINENEMYSPAWNTIME = config.spawntimer
            config._ENEMY_SHOOTINGSPEED = config.shootingspeed
            config._MAXENEMYSPAWNTIME = config.spawntimer
            print config.shootingspeed

        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        # draw to screen and flip
        screen.fill( (0,0,0) )

        screen.blit(backgroundimg1, (-200,-200))
        screen.blit(returnimg, (config._SCREEN_WIDTH/2 - returnimg.get_width()/2, 500))
        screen.blit(arrowimg, (390,510))

        pygame.display.flip()




