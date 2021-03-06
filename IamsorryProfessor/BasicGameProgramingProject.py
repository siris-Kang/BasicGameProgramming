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

# Set Direction
NORTH_DIRECTION = Setting.NORTH_DIRECTION
SOUTH_DIRECTION = Setting.SOUTH_DIRECTION
WEST_DIRECTION = Setting.WEST_DIRECTION
EAST_DIRECTION = Setting.EAST_DIRECTION

# Load Image
main_surface_image = Setting.main_surface_image
stage1_surface_image = Setting.stage1_surface_image
stage2_surface_image = Setting.stage2_surface_image

door_image2 = ClassTemplate.SpriteSheet(Setting.door_image)
door_image = door_image2.get_image(0, 13, 48, 48, 1, (0, 0, 0))

stage_clear = False
stage_init = True

game_main_screen = main_surface_image
game_sub_screen = stage1_surface_image
game_screen = main_surface_image
is_main_screen = True
is_sub_screen = False

quest1:bool = False
quest2:bool = False
quest3:bool = False
quest4:bool = False
quest5:bool = False

skill_SB:bool = True # 기본 스킬
skill_E:bool = True # attract
skill_F:bool = False # attack
skill_R:bool = False # boom

stage_num = 0

player_position = [100, 100] # Player Init
player_trigger_size = 30
player_speed = 4
player_stamina = 78
character1_array = ConstructMap.make_player_sprite_array(Setting.player_image_base)
player = ClassTemplate.Player(character1_array, player_position, player_trigger_size, player_speed, player_stamina, 1)
num_caught_monster = [0, 0, 0, 0]
stage_clear_condition = [10, 10, 10, 10]

professor_position = [400, 300] # Professor Init
professor_trigger_size = 150
professor_speed = 2
professor_stamina = 100
professor_damage = 5
professor_npc_array = ConstructMap.make_professor_spite_array(Setting.professor_image_base, 2)
professor_mon_array = ConstructMap.make_professor_spite_array(Setting.professor_image_base, 5)
professor = ClassTemplate.Monster(professor_npc_array, professor_position, professor_trigger_size, professor_speed, professor_stamina, professor_damage)
is_professor_moster = False

door_position = [40, 200]
door_trigger_size = 50
door_to_sub_screen = ClassTemplate.TriggerObject(ConstructMap.make_skill_object_sprite_array(door_image, 1), door_position, door_trigger_size)

monster_num = 10
monster_trigger_size = 80

quest1_monster_stamina = 7
quest1_monster_damage = 1
quest1_monster_image_list = ConstructMap.make_monster_spite_array(Setting.snake_image)
quest1_monster_type = [quest1_monster_image_list, monster_trigger_size, 3, quest1_monster_stamina, quest1_monster_damage]

quest3_monster_stamina = 14
quest3_monster_damage = 3
quest3_monster_image_list = ConstructMap.make_flag_monster_spite_array(Setting.flag_image)
quest3_monster_type = [quest3_monster_image_list, monster_trigger_size, 1, quest1_monster_stamina, quest1_monster_damage]

apple_trigger_size = 100
skill_E_apple = ClassTemplate.SkillObject(ConstructMap.make_skill_object_sprite_array(Setting.apple_image, 2), door_position, apple_trigger_size)
boom_trigger_size = 30
skill_R_boom = ClassTemplate.SkillObject(ConstructMap.make_skill_object_sprite_array(Setting.boom_image, 1), door_position, boom_trigger_size)

# make skill image
skill_SB_image = ConstructMap.make_skill_SB_sprite_array(Setting.base_skill, 2)
Skill_SB = ClassTemplate.SkillObject(skill_SB_image, door_position, 5)
boom_skill_image = ConstructMap.make_skill_R_sprite_array(Setting.boom_skill, 3)
Skill_R = ClassTemplate.SkillObject(boom_skill_image, door_position, 5)
Skill_R_action = False

# UI Setting
health_bar_box = DrawGameUI.DrawUI(Setting.health_bar_box, [10, 10], Setting.health_bar_box.get_width(), Setting.health_bar_box.get_height(), 3)
health_bar = DrawGameUI.DrawUI(Setting.health_bar, [37, 19], Setting.health_bar_box.get_width(), Setting.health_bar_box.get_height(), 3)

text_file = DrawGameUI.GetTextFromFile(Setting.professor_said)
said_list = text_file.line_list # Professor said list

said_block = 0
said_num = 0
message_box_image = pygame.transform.scale(Setting.message_box_image, (600, 200))
message_ui = DrawGameUI.DrawMessageBox(message_box_image, Setting.basicFont, "Hello", [100, 250], 600, 300, 1)

tutorial = True
monster_list = ConstructMap.make_monster(quest1_monster_type)

Setting.start_sound.play()
# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == USEREVENT:
            print(event.message)

    # Stage setting
    if quest1 == False and quest2 == False and quest4 == False and quest5 == False:
        if tutorial == False:
            quest1 = True

    if quest1 == True:
        if stage_init == True:
            monster_list = ConstructMap.make_monster(quest1_monster_type)
            stage_init = False
            stage_clear = False
            said_block += 1
        if stage_clear == True:
            quest1 = False
            quest2 = True
            skill_R = True
            stage_num += 1
            stage_init = True
            stage_clear = False
            said_block += 1
    elif quest2 == True:
        if stage_init == True:
            monster_list = ConstructMap.make_monster(quest3_monster_type)
            game_sub_screen = stage2_surface_image
            stage_init = False
            stage_clear = False
        if stage_clear == True:
            quest2 = False
            quest4 = True
            # skill_R = True
            stage_num += 1
            stage_init = True
            stage_clear = False
            said_block += 1
    elif quest4 == True:
        if stage_init == True:
            is_professor_moster = True
            stage_init = False
            stage_clear = False
            professor.image_array = professor_mon_array
            professor.triger_size = professor_trigger_size*4
        if professor.stamina <= 0:
            stage_clear = True
        if stage_clear == True:
            is_professor_moster = False
            said_block += 1
            quest5 = True
            quest4 = False
    elif quest5 == True:
        professor.alive = True
        professor.stamina = 10
        professor.position = professor_position
        professor.image_array = professor_npc_array
        professor.triger_size = professor_trigger_size
        Setting.windowSurface.blit(professor.now_image, professor.position)
        # Game End

    if player.stamina <= 0:
        player.stamina = player_stamina

    pressed = pygame.key.get_pressed()

    # Main map and Sub map setting
    if door_to_sub_screen.is_collided_with(player) and is_main_screen and pressed[pygame.K_SPACE]:
        game_screen = game_sub_screen
        door_to_sub_screen.position = [710, 200]
        player.position = [670, 200]
        professor.alive = False
        is_main_screen = False
        is_sub_screen = True
    elif door_to_sub_screen.is_collided_with(player) and is_sub_screen and pressed[pygame.K_SPACE]:
        game_screen = game_main_screen
        door_to_sub_screen.position = [40, 200]
        player.position = [90, 200]
        professor.alive = True
        is_main_screen = True
        is_sub_screen = False

    # Professor의 동작
    if is_professor_moster == False:
        if player.is_collided_with(professor) and pressed[pygame.K_SPACE] and professor.alive == True:
            message_ui.is_draw = True
            if num_caught_monster[stage_num] >= stage_clear_condition[stage_num]:
                stage_clear = True

        elif player.is_collided_with(professor) == False:
            message_ui.is_draw = False
    else: # Monster로 동작하는 경우
        if player.is_collided_with(professor):
            professor.attracted(player)
            monster_list[0] = professor
        
    # Keyboard pressed
    if pressed[pygame.K_UP]:
        player.transform_position(Setting.key_input[pygame.K_UP])
    elif pressed[pygame.K_DOWN]:
        player.transform_position(Setting.key_input[pygame.K_DOWN])
    elif pressed[pygame.K_LEFT]:
        player.transform_position(Setting.key_input[pygame.K_LEFT])
    elif pressed[pygame.K_RIGHT]:
        player.transform_position(Setting.key_input[pygame.K_RIGHT])


    # monster의 일반 동작
    for i in range(monster_num):
        if monster_list[i].is_collided_with(player):
            if game_screen == game_sub_screen:
                monster_list[i].attack(player)
            elif game_screen == game_main_screen and is_professor_moster == True:
                monster_list[0].attack(player)

    # Skill
    # Skill_SB
    for i in range(monster_num):
        if monster_list[i].is_collided_with(player) and pressed[pygame.K_q]:
            monster_alive = monster_list[i].lose_stamina(player.damage)
            Skill_SB.alive = True
            Skill_SB.position = [player.position[0]+ player.direction[0]*40, player.position[1] + player.direction[1]*40]
            if monster_alive == False:
                num_caught_monster[stage_num] += 1
    if Skill_SB.alive:
        Skill_SB.play_skill()
        Setting.hit_sound.play()
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
        if monster_list[i].is_collided_with(skill_R_boom) and Skill_R_action == True:
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
            Setting.windowSurface.blit(professor.now_image, professor.position)
            pass

    if skill_E_apple.alive == True:
        Setting.windowSurface.blit(skill_E_apple.now_image, skill_E_apple.position)
        skill_E_apple.existence_countdown()
    if skill_R_boom.alive == True:
        Setting.windowSurface.blit(skill_R_boom.now_image, skill_R_boom.position)
        skill_R_boom.existence_countdown()
        if skill_R_boom.alive == False:
            Skill_R.position = skill_R_boom.position
            Skill_R_action = True
            Skill_R.alive = True
    if Skill_R.alive == True and Skill_R_action == True:
        Skill_R.play_skill()
        Setting.bomb_sound.play()

    if Skill_SB.alive == True:
        Setting.windowSurface.blit(Skill_SB.now_image, Skill_SB.position)
    if Skill_R.alive == True:
        Setting.windowSurface.blit(Skill_R.now_image, Skill_R.position)

    Setting.windowSurface.blit(player.now_image, player.position)

    # UI rendering
    health_bar.draw_cut_image(player.stamina)
    Setting.windowSurface.blit(health_bar_box.now_image, health_bar_box.position)
    Setting.windowSurface.blit(health_bar.now_image, health_bar.position)

    # DrawGamdUI(message_box_image, basicFont, "Hello", [200, 200], 100, 100)
    if message_ui.is_draw == True:
        if said_list[said_block][said_num] != 0:
            message_ui.draw_message(said_list[said_block][said_num])
            pygame.time.wait(150)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                said_num += 1
        else:
            message_ui.is_draw = False
            said_num = 0
            tutorial = False
    

    pygame.display.update()
    Setting.mainClock.tick(50)
