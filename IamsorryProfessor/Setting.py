import pygame
from pygame.locals import *

#Setting

# Window Surface
WINDOWWIDTH = 800
WINDOWHEIGHT = 500
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 16)
pygame.display.set_caption('Thank you Professor')

# Direction
NORTH_DIRECTION = [0, -1]
SOUTH_DIRECTION = [0, 1]
WEST_DIRECTION = [-1, 0]
EAST_DIRECTION = [1, 0]

# Key input
key_input = { pygame.K_UP: NORTH_DIRECTION, pygame.K_DOWN: SOUTH_DIRECTION, pygame.K_LEFT: WEST_DIRECTION, pygame.K_RIGHT:EAST_DIRECTION}
key_input_list = [NORTH_DIRECTION, SOUTH_DIRECTION, WEST_DIRECTION, EAST_DIRECTION]

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
professor_image_base = pygame.image.load("Character2.png")

# Background Image Load
professor_lab = pygame.image.load("professor_lab.png")
main_surface_image = pygame.transform.scale(professor_lab, (WINDOWWIDTH, WINDOWHEIGHT))
tree_ground = pygame.image.load("tree_ground.png")
stage1_surface_image = pygame.transform.scale(tree_ground, (WINDOWWIDTH, WINDOWHEIGHT))
wlfhl_ground = pygame.image.load("land_ground.png")
stage2_surface_image = pygame.transform.scale(wlfhl_ground, (WINDOWWIDTH, WINDOWHEIGHT))


# Asset Image Load
door_image = pygame.image.load("MapImage2.png")
message_box_image = pygame.image.load("confirm_bg.png")

# Monster Image
snake_image = pygame.image.load("snake3.png")
flag_image = pygame.image.load("flags.png")

# SKill Image
apple_image = pygame.image.load("apple.png")
boom_image = pygame.image.load("Bomb.png")

base_skill = pygame.image.load("base_skill.png")
boom_skill = pygame.image.load("Boomb_image.png")

# UI Image
health_bar_box = pygame.image.load("health-bar-box.png")
health_bar =  pygame.image.load("health-bar.png")

# Professor Said File open
professor_said = open("ProfessorSaid.txt", 'r', encoding='UTF8')

pygame.init()
basicFont = pygame.font.SysFont("휴먼매직체",20)
mainClock = pygame.time.Clock()

start_sound = pygame.mixer.Sound("start_sound.flac")
hit_sound = pygame.mixer.Sound("hit_sound.flac")
monster_attack_sound = hit_sound = pygame.mixer.Sound("monster_attack_sound.flac")
bomb_sound = pygame.mixer.Sound("bomb_sound.wav")