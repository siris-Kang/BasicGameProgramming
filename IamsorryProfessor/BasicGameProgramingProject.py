import pygame, sys
from pygame.locals import *
import ClassTemplate

# Set Window
WINDOWWIDTH = ClassTemplate.WINDOWWIDTH
WINDOWHEIGHT = ClassTemplate.WINDOWHEIGHT
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 16)
pygame.display.set_caption('과제하는 게임')

# Set Direction
NORTH_DIRECTION = ClassTemplate.NORTH_DIRECTION
SOUTH_DIRECTION = ClassTemplate.SOUTH_DIRECTION
WEST_DIRECTION = ClassTemplate.WEST_DIRECTION
EAST_DIRECTION = ClassTemplate.EAST_DIRECTION

key_input = { pygame.K_w: NORTH_DIRECTION, pygame.K_s: SOUTH_DIRECTION, pygame.K_a: WEST_DIRECTION, pygame.K_d:EAST_DIRECTION}

# Image Load
character1 = pygame.image.load("Farmer.png").convert_alpha()
# player = pygame.transform.scale(character1, (50, 50))
character2 = pygame.image.load("drunkard0.png").convert_alpha()
backgroundImage = pygame.image.load("ground2.png").convert_alpha()
backgroundImage2 = pygame.transform.scale(backgroundImage, (800, 500))



# Pygame Init
pygame.init()
basicFont = pygame.font.SysFont(None, 48)
mainClock = pygame.time.Clock()

player_position = [50, 50]
player_speed = 5
player_trigger_size = 30
player = ClassTemplate.TriggerObject(player_position, player_trigger_size, player_speed, character1)

professor_position = [300, 300]
professor_speed = 6
professor_trigger_size = 50
professor = ClassTemplate.TriggerObject(professor_position, professor_trigger_size, professor_speed, character2)


# Game Loop
while True:
    windowSurface.fill(ClassTemplate.WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == USEREVENT:
            print(event.message)
    # pressed = pygame.key.get_pressed()
    # if pressed[pygame.K_p]:
    #     # pygame.event.post(pygame.event.Event(USEREVENT, message="heymama"))
    #     pygame.time.set_timer(pygame.event.Event(USEREVENT, message="heymama"), 1000)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        player.transform_position(key_input[pygame.K_w])
    elif pressed[pygame.K_s]:
        player.transform_position(key_input[pygame.K_s])
    elif pressed[pygame.K_a]:
        player.transform_position(key_input[pygame.K_a])
    elif pressed[pygame.K_d]:
        player.transform_position(key_input[pygame.K_d])


    if player.is_collided_with(professor):
        print("교수님: 아야")

    # draw_block(windowSurface, BLACK, playerPosition)
    character1.set_colorkey(pygame.Color(255, 0, 255))
    # print(character1.get_colorkey())
    windowSurface.blit(backgroundImage2, (0, 0)) # 배경 그리기(background 가 표시되는 위치)
    # windowSurface.blit(character1, player.position)
    windowSurface.blit(player.now_image, player.position)
    windowSurface.blit(professor.now_image, professor.position)
    
    pygame.display.update()
    mainClock.tick(50)

    # set_colorkey((56, 56, 94)) .convert_alpha().set_colorkey((255, 0, 255))