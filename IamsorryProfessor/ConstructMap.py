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


def make_player_sprite_array(image):
    sprite_sheet = ClassTemplate.SpriteSheet(image)   # .set_colorkey((0,0,0))
    image_array = [
                sprite_sheet.get_image(0, 1, 16, 18, 2, (0, 0, 0)), # index = 0, image = NORTH_DIRECTION
                sprite_sheet.get_image(1, 1, 16, 18, 2, (0, 0, 0)), # index = 1, image = NORTH_DIRECTION
                sprite_sheet.get_image(2, 1, 16, 18, 2, (0, 0, 0)), # index = 2, image = NORTH_DIRECTION

                sprite_sheet.get_image(0, 0, 16, 18, 2, (0, 0, 0)), # index = 3, image = SOUTH_DIRECTION
                sprite_sheet.get_image(1, 0, 16, 18, 2, (0, 0, 0)), # index = 4, image = SOUTH_DIRECTION
                sprite_sheet.get_image(2, 0, 16, 18, 2, (0, 0, 0)), # index = 5, image = SOUTH_DIRECTION
                
                sprite_sheet.get_image(0, 2, 16, 18, 2, (0, 0, 0)), # index = 6, image = WEST_DIRECTION
                sprite_sheet.get_image(1, 2, 16, 18, 2, (0, 0, 0)), # index = 7, image = WEST_DIRECTION
                sprite_sheet.get_image(2, 2, 16, 18, 2, (0, 0, 0)), # index = 8, image = WEST_DIRECTION

                sprite_sheet.get_image(0, 3, 16, 18, 2, (0, 0, 0)), # index = 9, image = EAST_DIRECTION
                sprite_sheet.get_image(1, 3, 16, 18, 2, (0, 0, 0)), # index = 10, image = EAST_DIRECTION
                sprite_sheet.get_image(2, 3, 16, 18, 2, (0, 0, 0)), # index = 11, image = EAST_DIRECTION
            ]
    return image_array

def make_professor_spite_array(image):
    sprite_sheet = ClassTemplate.SpriteSheet(image)
    image_array = [
                sprite_sheet.get_image(0, 1, 16, 18, 2, (0, 0, 0)), # index = 0, image = NORTH_DIRECTION
                sprite_sheet.get_image(1, 1, 16, 18, 2, (0, 0, 0)), # index = 1, image = NORTH_DIRECTION
                sprite_sheet.get_image(2, 1, 16, 18, 2, (0, 0, 0)), # index = 2, image = NORTH_DIRECTION

                sprite_sheet.get_image(0, 0, 16, 18, 2, (0, 0, 0)), # index = 3, image = SOUTH_DIRECTION
                sprite_sheet.get_image(1, 0, 16, 18, 2, (0, 0, 0)), # index = 4, image = SOUTH_DIRECTION
                sprite_sheet.get_image(2, 0, 16, 18, 2, (0, 0, 0)), # index = 5, image = SOUTH_DIRECTION
                
                sprite_sheet.get_image(0, 2, 16, 18, 2, (0, 0, 0)), # index = 6, image = WEST_DIRECTION
                sprite_sheet.get_image(1, 2, 16, 18, 2, (0, 0, 0)), # index = 7, image = WEST_DIRECTION
                sprite_sheet.get_image(2, 2, 16, 18, 2, (0, 0, 0)), # index = 8, image = WEST_DIRECTION

                sprite_sheet.get_image(0, 3, 16, 18, 2, (0, 0, 0)), # index = 9, image = EAST_DIRECTION
                sprite_sheet.get_image(1, 3, 16, 18, 2, (0, 0, 0)), # index = 10, image = EAST_DIRECTION
                sprite_sheet.get_image(2, 3, 16, 18, 2, (0, 0, 0)), # index = 11, image = EAST_DIRECTION
            ]
    return image_array

def make_skill_object_sprite_array(image, scale):
    image = pygame.transform.scale(image, (image.get_width()*scale, image.get_height()* scale))
    sprite_sheet = ClassTemplate.SpriteSheet(image)
    image_array = [
                image # index = 0
            ]
    return image_array