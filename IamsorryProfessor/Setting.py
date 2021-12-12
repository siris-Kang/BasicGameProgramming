import pygame
from pygame.locals import *

#Setting

# Window Surface
WINDOWWIDTH = 800
WINDOWHEIGHT = 500
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 16)
pygame.display.set_caption('과제하는 게임')

# Direction
NORTH_DIRECTION = [0, -1]
SOUTH_DIRECTION = [0, 1]
WEST_DIRECTION = [-1, 0]
EAST_DIRECTION = [1, 0]

# Key input
key_input = { pygame.K_w: NORTH_DIRECTION, pygame.K_s: SOUTH_DIRECTION, pygame.K_a: WEST_DIRECTION, pygame.K_d:EAST_DIRECTION}

# Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (100,100,100)

# Image Load
player_image_base = pygame.image.load("Character1.png")
# character1.set_colorkey(ClassTemplate.BLACK)
# character1.set_alpha(128)
# print(character1.get_alpha(), character1.get_colorkey())
# player = pygame.transform.scale(character1, (50, 50))
professor_image_base = pygame.image.load("Character2.png")

# Background Image Load
backgroundImage = pygame.image.load("ground.png")
main_surface_image = pygame.transform.scale(backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))
backgroundImage1 = pygame.image.load("ground2.png")
stage1_surface_image = pygame.transform.scale(backgroundImage1, (WINDOWWIDTH, WINDOWHEIGHT))


# Asset Image Load
door_image = pygame.image.load("MapImage2.png")
message_box_image = pygame.image.load("health-bar.png")

# Monster Image
snake_image = pygame.image.load("snake.png")


# SKill Image
apple_image = pygame.image.load("apple.png")
boom_image = pygame.image.load("fireball.png")

# # Font
# pygame.init()
# font = pygame.font.SysFont("NanumGothic.ttf", 32)
