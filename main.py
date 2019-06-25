import sys, pygame, random, panda as pd
from ship import Ship
from as1 import Asteriod
from pygame.locals import *

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w*0.5).int(screen_info.current_h*0.5))

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color(30, 0, 30)
screen.fill(color)

df = pd.read_cvs('game_info.csv')

asteroids = pygame.sprite.Group()
numLevels = df['LevelNum'].max()
level = df['LevelNum'].min()
levelData = df.iloc[level]
asteroidsCount = levelData['AsteroidCount']
player = Ship((levelData['PlayerX'], level['PlayerY']))

def init():
    global asteroids, asteroids, levelData
    levelData = df.iloc[level]
    player.reset((levelData['PlayerX'],levelData['PlayerY']))
    asteroids.empty()
    asteroidCount = levelData['AsteroidCount']
    for i in range(asteroidCount):
        asteroids.add(Asteriod((random.randint(50, width-50), random.randint(50, height-50),random.ranint(15,60)))

def win():
    font = pygame.font.SysFont(None,70)
    text = font.render("you win", True,(255,0,0))
    text_rect = text.get_rect()
    text_rect.center = (width/2,height/2)
    while True
        screen.fill(color)
        screen.blit(text,text_rect)
        pygame.display.flip()