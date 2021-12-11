import pygame, sys
import random
from pygame.locals import *
import ClassTemplate
import ConstructMap

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

# Load Image
character1 = pygame.image.load("Student.png").convert_alpha()
# player = pygame.transform.scale(character1, (50, 50))
character2 = pygame.image.load("Professor.png").convert_alpha()
backgroundImage = pygame.image.load("ground.png").convert_alpha()
backgroundImage2 = pygame.transform.scale(backgroundImage, (800, 500))
backgroundImage3 = pygame.image.load("ground2.png").convert_alpha()
backgroundImage4 = pygame.transform.scale(backgroundImage3, (800, 500))

doorImage = pygame.image.load("MapImage2.png").convert_alpha()
doorImage2 = ClassTemplate.SpriteSheet(doorImage)
doorImage3 = doorImage2.get_image(0, 13, 48, 48, 1, (0, 0, 0))

snakeImage = pygame.image.load("likesnake.png").convert_alpha()



# Pygame Init
pygame.init()
basicFont = pygame.font.SysFont(None, 48)
mainClock = pygame.time.Clock()

stage_clear = False
stage_init = True

game_main_screen = backgroundImage2
game_sub_screen = backgroundImage4
game_screen = backgroundImage2
is_main_screen = True
is_sub_screen = False

quest1:bool = True # 뱀 잡아오는 quest
quest2:bool = False # 벽돌 잡아오는 quest
quest3:bool = False # 깃발 잡아오는 quest
# quest4:bool = False
quest5:bool = False # Professor quest

skill_SB:bool = True # 기본 스킬
skill_E:bool = False # attract
skill_F:bool = False # attack
skill_R:bool = False # boom
# skill_RMB:bool = False #shoot

player_position = [50, 50] # Player Init
player_trigger_size = 30
player_speed = 4
player = ClassTemplate.Player(character1, player_position, player_trigger_size, player_speed, 10, 1)

professor_position = [300, 300] # Professor Init
professor_trigger_size = 200
professor_speed = 2
professor_stamina = 20
prifessor_damage = 1
professor = ClassTemplate.Monster(character2, professor_position, professor_trigger_size, professor_speed, professor_stamina, prifessor_damage)

door_position = [0, 200]
door_trigger_size = 50
door_to_sub_screen = ClassTemplate.TriggerObject(doorImage3, door_position, door_trigger_size)

# monster_list = [range(10)] # 10칸짜리 list
quest1_monster_type = [snakeImage, professor_trigger_size, professor_speed, professor_stamina, prifessor_damage]
# quest2_monster_type = [image, trigger_size, speed, stamina, damage]
# quest3_monster_type = [image, trigger_size, speed, stamina, damage]
# quest4_monster_type = [image, trigger_size, speed, stamina, damage]


# Game Loop
while True:
    windowSurface.fill(ClassTemplate.WHITE)

    # Map Surface Draw
    windowSurface.blit(game_screen, (0, 0))
    windowSurface.blit(door_to_sub_screen.now_image, door_to_sub_screen.position)

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


    # 단계 설정 code
    if (quest1 == True):
        if stage_init == True:
            monster_list = ConstructMap.make_monster(quest1_monster_type)
            stage_init = False

        # ...stage_clear = True
        if stage_clear == True:
            quest1 = False
            quest2 = True
            skill_F = True
            stage_clear = False
    elif (quest2 == True):
        if stage_init == True:
            monster_list = ConstructMap.make_monster(quest1_monster_type) #
            stage_init = False

        if stage_clear == True:
            quest2 = False
            quest3 = True
            skill_R = True
            stage_clear = False
    elif (quest3 == True):
        if stage_init == True:
            monster_list = ConstructMap.make_monster(quest1_monster_type) #
            stage_init = False

        if stage_clear == True:
            quest3 = False
            # quest4 = True
            quest5 = True
            # skill_RMB = True
            stage_clear = False
    # elif (quest4 == True):
    elif (quest5 == True):
        # 교수님을 몬스터로 바꿔주세요^^
        
        if stage_clear == True:
            quest1 = False
            skill_F = True
            stage_clear = False


    pressed = pygame.key.get_pressed()

    # player가 특정 맵에 들어가면
    if door_to_sub_screen.is_collided_with(player) and is_main_screen and pressed[pygame.K_SPACE]:
        game_screen = game_sub_screen
        door_to_sub_screen.position = [750, 200]
        player.position = [710, 200]
        is_main_screen = False
        is_sub_screen = True
    elif door_to_sub_screen.is_collided_with(player) and is_sub_screen and pressed[pygame.K_SPACE]:
        game_screen = game_main_screen
        door_to_sub_screen.position = [0, 200]
        player.position = [50, 200]
        is_main_screen = True
        is_sub_screen = False

    # 해당 맵의 Monster만드는 코드 만들기!
    if game_screen == game_sub_screen:
        # make_monster()
        pass
    
    if pressed[pygame.K_w]:
        player.transform_position(key_input[pygame.K_w])
    elif pressed[pygame.K_s]:
        player.transform_position(key_input[pygame.K_s])
    elif pressed[pygame.K_a]:
        player.transform_position(key_input[pygame.K_a])
    elif pressed[pygame.K_d]:
        player.transform_position(key_input[pygame.K_d])


    if player.is_collided_with(professor):
        professor.attracted(player)

    if game_screen == game_sub_screen:
        for i in range(10):
            windowSurface.blit(monster_list[i].now_image, monster_list[i].position)
            
            # monster_list[i].move_randomly()

    # NPC Surface Draw
    windowSurface.blit(player.now_image, player.position)
    windowSurface.blit(professor.now_image, professor.position)

    # windowSurface.blit(snakeImage, professor.position)

    pygame.display.update()
    mainClock.tick(50)

    # set_colorkey((56, 56, 94)) .convert_alpha().set_colorkey((255, 0, 255))