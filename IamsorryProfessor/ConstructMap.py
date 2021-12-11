import pygame
import random
from pygame.locals import *
import ClassTemplate

def make_monster(monster_type):
    monster_list = []    
    for i in range(0, 10):
        position0 = random.randrange(100, 700)
        position1 = random.randrange(100, 400)
        monster_list.append(ClassTemplate.Monster(monster_type[0], [position0, position1], monster_type[1], monster_type[2], monster_type[3], monster_type[4]))
    return monster_list