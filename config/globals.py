import pygame


#DEFAULT VARIABLES:
spawntimer = 1000
lastscore = 4000
shootingspeed = 5000


#SCREEN VARIABLES
_SCREEN_WIDTH = 1024
_SCREEN_HEIGHT = 768




#PLAYER VARIABLES
_SHOOTINGSPEED = 200
_PLAYERSPEED = .5
_STARTING_X = 500
_STARTING_Y = 638
_SPACESHIP1 = ["theSS.png", "theSS_hit.png"]
_PLAYER = 0

_ASSET_DIR = "assets/"
_SHIPS_DIR = "ships/"
_WEAPONS_DIR = "weapons/"
_BACKGROUND_DIR = "background/"
_BULLET_LIFESPAN = 1000
_BULLETSOUNDFILE = "shoot.aiff"
_SCORE = 0
_LASTSCORE = lastscore
_INCREASESCORE = lastscore
_GUI_WIDTH = 215
_SHOT_UPGRADES = 0

#ENEMY VARIABLES
_CHANGEDIRECTION_INTERVAL = -1 #MILSECS
_ENEMY_SPEED = -0.1
_ENEMYTYPE = ["theBW.png","Untitled.png"]
_ENEMYTYPEWORTH = [100, 200]
_NUMBEROFENEMYTYPES = 2 - 1 #this is the number of enemy types we have right now
_ENEMYLIST = []

_MINENEMYSPAWNTIME = spawntimer
_MAXENEMYSPAWNTIME = spawntimer
_ENEMY_SHOOTINGSPEED = shootingspeed

#BULLETS
_BULLET_IMG = ["blastpowerup1.png", "iceblast1.png", "iceblast2.png", "blastpowerup1.png", "blastpowerup1.png", "blastpowerup1.png", "blastpowerup1.png", "enemyshot.png"]

#SCENE!
_CURRENTSCENE = 0
_ARROWPOS_X = _SCREEN_WIDTH/2 - 120
_ARROWPOS_Y = 380
_SELECTION = 0

#SCROLLING BG
_BACKGROUND_IMGS = ["tile1.png","tile2.png","tile3.png","tile4.png"]

##THIS IS GONNA HOLD ALL THE UPGRADES FLOATING
#UPGRADE HOLDER:
_UPGRADE_ARRAY = []
_UPGRADE_SHIELD = 0
_UPGRADESHEILDPROB = 2
_UPGRADE_TIMER = 5000 #milisecs
_UPGRADEPROBABILITY = 5 #PROBABILITY OF AN UPDATE APPEARING, IN PERCENTAGE (FROM 0 TO 100)

_GAMEOVER = False

#BOSS VARIABLES
_BOTTOMTHRESHOLD = _SCREEN_HEIGHT + 300
_LEFSCREENEDGE = _SCREEN_WIDTH - _GUI_WIDTH
_BOSSSHOOTINGTIME = 6000
_BOSSBULLETTIMER = 10000
_BOSS = 0
_BOSS_LEFT = 50
#i screwed up lol
masterspawn = []

_ENEMYDEATHSOUND = 0

_BULLET_IMG_SURFACE = []
_ENEMIES_SURFACE = []

_SPACESHIP_SURFACE = []

def initEverything():
    
    for img in _BULLET_IMG:
        imgx = pygame.image.load(_ASSET_DIR + _WEAPONS_DIR + img).convert_alpha()
        _BULLET_IMG_SURFACE.append(imgx)


    for img in _ENEMYTYPE:
        imgx = pygame.image.load(_ASSET_DIR + _SHIPS_DIR + img).convert_alpha()
        _ENEMIES_SURFACE.append(imgx)
      #  self.imgType = pygame.image.load( G._ASSET_DIR +  G._SHIPS_DIR + G._ENEMYTYPE[self.type] ).convert()
    
    for img in _SPACESHIP1:
        imgx = pygame.image.load(_ASSET_DIR + _SHIPS_DIR + img).convert_alpha()

        _SPACESHIP_SURFACE.append(imgx)
    pass

