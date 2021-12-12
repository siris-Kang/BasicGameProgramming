import pygame
import math
import random
from pygame.locals import *
import Setting

# Setting
NORTH_DIRECTION = Setting.NORTH_DIRECTION
SOUTH_DIRECTION = Setting.SOUTH_DIRECTION
WEST_DIRECTION = Setting.WEST_DIRECTION
EAST_DIRECTION = Setting.EAST_DIRECTION


# get mini item image
class SpriteSheet():
    def __init__(self, image):
        self.sheet = image
    
    def get_image(self, num_x, num_y, width, height, scale, color):
        image = pygame.Surface((width, height))
        image.blit(self.sheet, (0, 0), Rect((num_x*width), (num_y*height), width, height))
        image = pygame.transform.scale(image, (width*scale, height* scale))
        return image


class TriggerObject():
    def __init__(self, image_array, position, triger_size):
        self.is_in_range: bool = False
        self.image_array = image_array
        self.position = position
        self.triger_size = triger_size
        self.now_image = self.image_array[0]

    def is_collided_with(self, other) -> bool:
        a = self.position[0] - other.position[0]
        b = self.position[1] - other.position[1]
        length = math.sqrt((a ** 2) + (b ** 2))
        if length < self.triger_size/2 + other.triger_size/2:
            self.is_in_range = True
        else:
            self.is_in_range = False
        return self.is_in_range


class Character(TriggerObject):
    def __init__(self, image_array, position, triger_size, speed, stamina, damage): #이미지 array, 위치, Trigger크기, 속도, 체력, 공격력
        super().__init__(image_array, position, triger_size)
        self.top_left = [self.position[0] - self.triger_size / 2, self.position[1] - self.triger_size / 2]
        self.speed = speed
        self.stamina = stamina
        self.fix_stamina = stamina
        self.damage = damage
        self.alive = True

        self.now_image = self.image_array[0]

    def transform_position(self, direction): # direction = [ , ]
        count = int(len(self.image_array)/4)
        if direction == NORTH_DIRECTION:
            self.now_image = self.image_array[0*count]
            if  self.position[1] - self.speed > 0:
                self.position[1] += direction[1]*self.speed

        elif direction == SOUTH_DIRECTION:
            self.now_image = self.image_array[1*count]
            if self.position[1] + self.speed < Setting.WINDOWHEIGHT - self.triger_size:
                self.position[1] += direction[1]*self.speed

        elif direction == WEST_DIRECTION:
            self.now_image = self.image_array[2*count]
            if  self.position[0] + direction[0]*self.speed > 0:
                self.position[0] += direction[0]*self.speed

        elif direction == EAST_DIRECTION:
            self.now_image = self.image_array[3*count]
            if self.position[0] +  direction[0]*self.speed < Setting.WINDOWWIDTH - self.triger_size:
                self.position[0] += direction[0]*self.speed

        # self.now_image.set_colorkey((255, 0, 255))

    def lose_stamina(self, other_damage):
        self.stamina -= other_damage
        if self.stamina <= 0:
            self.alive = False
        return self.alive

    def get_stamina(self):
        self.stamina += 1


class Player(Character):
    def __init__(self, image_array, position, triger_size, speed, stamina, damage):
        super().__init__(image_array, position, triger_size, speed, stamina, damage)
        self.score = 0.0
        


class Monster(Character):
    def __init__(self, image_array, position, triger_size, speed, stamina, damage):
        super().__init__(image_array, position, triger_size, speed, stamina, damage)

    # def move_randomly(self):
    #     self.transform_position(NORTH_DIRECTION)
    
    def attracted(self, other): #다른 물체에 이끌림
        position0 = self.position[0] - other.position[0]
        position1 = self.position[1] - other.position[1]
        # if abs(position0) > self.speed or abs(position1) > self.speed:
        if position1 > self.speed:
            self.transform_position(NORTH_DIRECTION)
        elif position1 < -self.speed:
            self.transform_position(SOUTH_DIRECTION)
        elif position0 > self.speed:
            self.transform_position(WEST_DIRECTION)
        elif position0 < -self.speed:
            self.transform_position(EAST_DIRECTION)
                

    def refresh_monster(self):
        self.stamina = self.fix_stamina
        position0 = random.randrange(100, 700)
        position1 = random.randrange(100, 400)
        self.position = [position0, position1]



class SkillObject(TriggerObject):
    def __init__(self, image_array, position, triger_size):
        super().__init__(image_array, position, triger_size)
        self.alive = False
        self.start_ticks = pygame.time.get_ticks()
        self.elapsed_time = (pygame.time.get_ticks() - self.start_ticks) / 1000

    def make_new_postion(self, x, y):
        self.position = [x, y]
        self.start_ticks = pygame.time.get_ticks()

    def existence_countdown(self):
        self.elapsed_time = (pygame.time.get_ticks() - self.start_ticks) / 1000
        # print(self.elapsed_time)
        if self.elapsed_time > 3:
            self.alive = False
