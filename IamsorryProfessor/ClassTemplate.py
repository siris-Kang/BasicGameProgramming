import pygame
import math
from pygame.locals import *


#Setting
WINDOWWIDTH = 800
WINDOWHEIGHT = 500

NORTH_DIRECTION = [0, -1]
SOUTH_DIRECTION = [0, 1]
WEST_DIRECTION = [-1, 0]
EAST_DIRECTION = [1, 0]

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (100,100,100)


class characterClass:
    # 변수
    def __init__(slef):
        #초기화
        a = 0
#를 받는 player class


    
class MessageBox:
    def __init__(self):
        b = 0



class TriggerObject():
    def __init__(self, position, triger_size, speed, image):
        self.is_in_range: bool = False
        self.position = position
        self.triger_size = triger_size
        self.top_left = [self.position[0] - self.triger_size / 2, self.position[1] - self.triger_size / 2]
        self.speed = speed
        self.image = image  # 이미지는 로드 후 대입

        sprite_sheet = SpriteSheet(self.image)
        self.image_array = [
            sprite_sheet.get_image(0, 1, 16, 16, 2, (0, 0, 0)).convert_alpha(), # index = 0, image = NORTH_DIRECTION
            sprite_sheet.get_image(1, 1, 16, 16, 2, (0, 0, 0)).convert_alpha(), # index = 1, image = NORTH_DIRECTION
            sprite_sheet.get_image(0, 3, 16, 16, 2, (0, 0, 0)).convert_alpha(), # index = 2, image = SOUTH_DIRECTION
            sprite_sheet.get_image(1, 3, 16, 16, 2, (0, 0, 0)).convert_alpha(), # index = 3, image = SOUTH_DIRECTION
            sprite_sheet.get_image(0, 4, 16, 16, 2, (0, 0, 0)).convert_alpha(), # index = 4, image = WEST_DIRECTION
            sprite_sheet.get_image(1, 4, 16, 16, 2, (0, 0, 0)).convert_alpha(), # index = 5, image = WEST_DIRECTION
            sprite_sheet.get_image(0, 2, 16, 16, 2, (0, 0, 0)).convert_alpha(), # index = 6, image = EAST_DIRECTION
            sprite_sheet.get_image(1, 2, 16, 16, 2, (0, 0, 0)).convert_alpha(), # index = 7, image = EAST_DIRECTION
            sprite_sheet.get_image(2, 0, 16, 16, 2, (0, 0, 0)).convert_alpha() # index = 8, image = Stand Image
        ]
        self.now_image = self.image_array[8]

    def is_collided_with(self, other) -> bool:
        # if self.top_left[0] < other.top_left[0] + other.triger_size and \
        #     self.top_left[0] + self.triger_size > other.top_left[0] and \
        #     self.top_left[1] < other.top_left[1] + other.triger_size and \
        #     self.top_left[1] + self.triger_size > other.top_left[1]:
        a = self.position[0] - other.position[0]
        b = self.position[1] - other.position[1]
        length = math.sqrt((a ** 2) + (b ** 2))
        if length < self.triger_size/2 + other.triger_size/2:
            self.is_in_range = True
        else:
            self.is_in_range = False
        return self.is_in_range
    
    def transform_position(self, direction): # direction = [ , ]
        if direction == NORTH_DIRECTION:
            self.now_image = self.image_array[0]
            if  self.position[1] - self.speed != 0:
                self.position[1] += direction[1]*self.speed

        elif direction == SOUTH_DIRECTION:
            self.now_image = self.image_array[2]
            if self.position[1] + self.speed != WINDOWHEIGHT - self.triger_size:
                self.position[1] += direction[1]*self.speed

        elif direction == WEST_DIRECTION:
            self.now_image = self.image_array[4]
            if  self.position[0] - self.speed != 0:
                self.position[0] += direction[0]*self.speed

        elif direction == EAST_DIRECTION:
            self.now_image = self.image_array[6]
            if self.position[0] + self.speed != WINDOWWIDTH - self.triger_size:
                self.position[0] += direction[0]*self.speed
        
        self.now_image.set_colorkey((255, 0, 255))



class SpriteSheet():
    def __init__(self, image):
        self.sheet = image
    
    def get_image(self, num_x, num_y, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), Rect((num_x*height), (num_y*width), width, height))
        image = pygame.transform.scale(image, (width*scale, height* scale))
        return image