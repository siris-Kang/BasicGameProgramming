from typing import Set
import pygame, sys
from pygame.locals import *
import random
import Setting
import ClassTemplate
import ConstructMap
import DrawGameUI

# Set Window
WINDOWWIDTH = Setting.WINDOWWIDTH
WINDOWHEIGHT = Setting.WINDOWHEIGHT
# windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 16)
# pygame.display.set_caption('과제하는 게임')

# Set Direction
NORTH_DIRECTION = Setting.NORTH_DIRECTION
SOUTH_DIRECTION = Setting.SOUTH_DIRECTION
WEST_DIRECTION = Setting.WEST_DIRECTION
EAST_DIRECTION = Setting.EAST_DIRECTION

# Load Image
main_surface_image = Setting.main_surface_image
stage1_surface_image = Setting.stage1_surface_image


door_image2 = ClassTemplate.SpriteSheet(Setting.door_image)
door_image = door_image2.get_image(0, 13, 48, 48, 1, (0, 0, 0))

# Pygame Init
pygame.init()
basicFont = pygame.font.SysFont("NanumGothic.ttf", 32)
mainClock = pygame.time.Clock()

stage_clear = False
stage_init = True

game_main_screen = main_surface_image
game_sub_screen = stage1_surface_image
game_screen = main_surface_image
is_main_screen = True
is_sub_screen = False

quest1:bool = True # 뱀 잡아오는 quest # list로 만들면 좋을 듯
quest2:bool = False # 벽돌 잡아오는 quest
quest3:bool = False # 깃발 잡아오는 quest
# quest4:bool = False
quest5:bool = False # Professor quest

skill_SB:bool = True # 기본 스킬
# skill_E:bool = False # attract
# skill_F:bool = False # attack
# skill_R:bool = False # boom
# skill_RMB:bool = False #shoot
skill_E:bool = True # attract
skill_F:bool = True # attack
skill_R:bool = True # boom

stage_num = 0

player_position = [50, 50] # Player Init
player_trigger_size = 30
player_speed = 4
character1_array = ConstructMap.make_player_sprite_array(Setting.player_image_base)
player = ClassTemplate.Player(character1_array, player_position, player_trigger_size, player_speed, 10, 1)
num_caught_monster = [0, 0, 0]
stage_clear_condition = [10, 10, 10]

professor_position = [300, 300] # Professor Init
professor_trigger_size = 100
professor_speed = 2
professor_stamina = 20
professor_damage = 1
character2_array = ConstructMap.make_professor_spite_array(Setting.professor_image_base)
professor = ClassTemplate.Monster(character2_array, professor_position, professor_trigger_size, professor_speed, professor_stamina, professor_damage)
is_professor_moster = False

door_position = [0, 200]
door_trigger_size = 50
door_to_sub_screen = ClassTemplate.TriggerObject(ConstructMap.make_skill_object_sprite_array(door_image, 1), door_position, door_trigger_size)

monster_num = 10
# monster_list = [range(10)] # 10칸짜리 list
quest1_monster_stamina = 5
quest1_monster_damage = 1
quest1_monster_image_list = ConstructMap.make_monster_spite_array(Setting.snake_image)
quest1_monster_type = [quest1_monster_image_list, professor_trigger_size, professor_speed, quest1_monster_stamina, quest1_monster_damage]
# quest2_monster_type = [image, trigger_size, speed, stamina, damage]
# quest3_monster_type = [image, trigger_size, speed, stamina, damage]
# quest4_monster_type = [image, trigger_size, speed, stamina, damage]

apple_trigger_size = 80
skill_E_apple = ClassTemplate.SkillObject(ConstructMap.make_skill_object_sprite_array(Setting.apple_image, 2), door_position, apple_trigger_size)
boom_trigger_size = 30
skill_R_boom = ClassTemplate.SkillObject(ConstructMap.make_skill_object_sprite_array(Setting.boom_image, 2), door_position, boom_trigger_size)

message_box_image = pygame.transform.scale(Setting.message_box_image, (600, 200))
ui1 = DrawGameUI.DrawMessageBox(message_box_image, basicFont, "Hello", [100, 250], 600, 300)

# make skill image
skill_SB_image = ConstructMap.make_skill_SB_sprite_array(Setting.base_skill, 2)
Skill_SB = ClassTemplate.SkillObject(skill_SB_image, door_position, 5)
boom_skill_image = ConstructMap.make_skill_R_sprite_array(Setting.boom_skill, 1)
Skill_R = ClassTemplate.SkillObject(boom_skill_image, door_position, 5)


# Game Loop
while True:
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


    # Stage setting
    if (quest1 == True):
        if stage_init == True:
            monster_list = ConstructMap.make_monster(quest1_monster_type)
            stage_init = False
        if num_caught_monster[stage_num] >= stage_clear_condition[stage_num] and stage_clear == True:# and 교수님 허락으로 인한 stage clear == True
            quest1 = False
            quest2 = True
            skill_F = True
            stage_num += 1
            stage_clear = False
    elif (quest2 == True):
        if stage_init == True:
            monster_list = ConstructMap.make_monster(quest1_monster_type) #
            stage_init = False
        if num_caught_monster[stage_num] >= stage_clear_condition[stage_num] and stage_clear == True: # and 교수님 허락으로 인한 stage clear == True
            quest2 = False
            quest3 = True
            skill_R = True
            stage_num += 1
            stage_clear = False
    elif (quest3 == True):
        if stage_init == True:
            monster_list = ConstructMap.make_monster(quest1_monster_type) #
            stage_init = False
        if num_caught_monster[stage_num] >= stage_clear_condition[stage_num] and stage_clear == True: # and 교수님 허락으로 인한 stage clear == True
            quest3 = False
            # quest4 = True
            quest5 = True
            # skill_RMB = True
            stage_num += 1
            stage_clear = False
    # elif (quest4 == True):
    elif (quest5 == True):
        # 교수님을 몬스터로 바꿔주세요^^
        is_professor_moster = True
        # 교수님도 랜덤으로 움직이며
        # Player를 공격하고
        # 스페이스바와 연결된 UI 기능이 사라진다
        
        if stage_clear == True:
            is_professor_moster = False
            # Game End Code

    # if professor.alive == True:
    #     if player.is_collided_with(professor):
    #         stage_clear = True

    pressed = pygame.key.get_pressed()

    # Main map and Sub map setting
    if door_to_sub_screen.is_collided_with(player) and is_main_screen and pressed[pygame.K_SPACE]:
        game_screen = game_sub_screen
        door_to_sub_screen.position = [750, 200]
        player.position = [710, 200]
        professor.alive = False
        is_main_screen = False
        is_sub_screen = True
    elif door_to_sub_screen.is_collided_with(player) and is_sub_screen and pressed[pygame.K_SPACE]:
        game_screen = game_main_screen
        door_to_sub_screen.position = [0, 200]
        player.position = [50, 200]
        professor.alive = True
        is_main_screen = True
        is_sub_screen = False

    # Professor의 동작
    if is_professor_moster == False:
        if player.is_collided_with(professor) and pressed[pygame.K_SPACE] and professor.alive == True:
            ui1.is_draw = True
    else:
        pass

        
    # # Keyboard pressed
    if pressed[pygame.K_w]:
        player.transform_position(Setting.key_input[pygame.K_w])
    elif pressed[pygame.K_s]:
        player.transform_position(Setting.key_input[pygame.K_s])
    elif pressed[pygame.K_a]:
        player.transform_position(Setting.key_input[pygame.K_a])
    elif pressed[pygame.K_d]:
        player.transform_position(Setting.key_input[pygame.K_d])


    # Skill
    # Skill_SB
    for i in range(monster_num):
        if monster_list[i].is_collided_with(player) and pressed[pygame.K_SPACE]:
            monster_alive = monster_list[i].lose_stamina(player.damage)
            Skill_SB.alive = True
            Skill_SB.position = [player.position[0]+ player.direction[0]*40, player.position[1] + player.direction[1]*40]
            if monster_alive == False:
                num_caught_monster[stage_num] += 1
    if Skill_SB.alive:
        Skill_SB.play_skill()
    # Skill_E
    if pressed[pygame.K_e] and skill_E == True and skill_E_apple.alive == False: # 지금은 사과 하나만 만들 수 있음
        skill_E_apple.make_new_postion(player.position[0], player.position[1])
        skill_E_apple.alive = True
    for i in range(monster_num):
        if monster_list[i].is_collided_with(skill_E_apple) and skill_E_apple.alive == True:
            monster_list[i].attracted(skill_E_apple)
    # Skill_F
    for i in range(monster_num):
        if monster_list[i].is_collided_with(player) and pressed[pygame.K_f] and skill_F == True:
            monster_alive = monster_list[i].lose_stamina(3*player.damage)
            if monster_alive == False:
                num_caught_monster[stage_num] += 1
    # Skill_R
    if pressed[pygame.K_r] and skill_R == True and skill_R_boom.alive == False: 
        skill_R_boom.make_new_postion(player.position[0], player.position[1])
        skill_R_boom.alive = True
    for i in range(monster_num):
        if monster_list[i].is_collided_with(skill_R_boom) and skill_R_boom.alive == False:
            monster_alive = monster_list[i].lose_stamina(5*player.damage)
            if monster_alive == False:
                num_caught_monster[stage_num] += 1

    
    # Surface Draw
    Setting.windowSurface.fill(Setting.WHITE)
    Setting.windowSurface.blit(game_screen, (0, 0))
    Setting.windowSurface.blit(door_to_sub_screen.now_image, door_to_sub_screen.position)
 
    if game_screen == game_sub_screen:
        for i in range(monster_num):
            if monster_list[i].alive == False:
                monster_list[i].refresh_monster()
            else:
                monster_list[i].transform_position_randomly()
                Setting.windowSurface.blit(monster_list[i].now_image, monster_list[i].position)
    elif game_screen == game_main_screen:
        if professor.alive == True:
            # Setting.windowSurface.blit(professor.now_image, professor.position)
            pass

    if skill_E_apple.alive == True:
        Setting.windowSurface.blit(skill_E_apple.now_image, skill_E_apple.position)
        skill_E_apple.existence_countdown()
    if skill_R_boom.alive == True:
        Setting.windowSurface.blit(skill_R_boom.now_image, skill_R_boom.position)
        skill_R_boom.existence_countdown(Skill_R)

    if Skill_SB.alive == True:
        Setting.windowSurface.blit(Skill_SB.now_image, Skill_SB.position)
    if Skill_R.alive == True:
        Setting.windowSurface.blit(Skill_R.now_image, Skill_R.position)

    Setting.windowSurface.blit(player.now_image, player.position)

    # print(stage_num)
    # print(num_caught_monster[stage_num])

    # Setting.windowSurface.blit(Setting.boom_skill, professor.position)

    # DrawGamdUI(message_box_image, basicFont, "Hello", [200, 200], 100, 100)
    if ui1.is_draw == True:
        ui1.draw_message()

    pygame.display.update()
    mainClock.tick(50)
    # set_colorkey((56, 56, 94)) .convert_alpha().set_colorkey((255, 0, 255))

    # 교수님한테 가까이 가서 sb누르면 pygame ui 뜨게
    # ui는 text파일 순서대로 읽어오도록
    # 교수님 monster 동작

    # Map Image만들기
    # UI로 player 체력 바 추가
    # Monster position위에도 체력 바 하나씩 달아주기

    # 튜토리얼과 게임 설명