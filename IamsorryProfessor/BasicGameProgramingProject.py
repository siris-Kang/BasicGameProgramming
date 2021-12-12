import pygame, sys
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
character1 = pygame.image.load("Character1.png").convert_alpha()
# character1.set_colorkey(ClassTemplate.BLACK)
# character1.set_alpha(128)
# print(character1.get_alpha(), character1.get_colorkey())
# player = pygame.transform.scale(character1, (50, 50))
character2 = pygame.image.load("Character2.png").convert_alpha()
# print(character2.get_alpha(), character2.get_colorkey())
backgroundImage = pygame.image.load("ground.png").convert_alpha()
backgroundImage2 = pygame.transform.scale(backgroundImage, (800, 500))
backgroundImage3 = pygame.image.load("ground2.png").convert_alpha()
backgroundImage4 = pygame.transform.scale(backgroundImage3, (800, 500))

doorImage = pygame.image.load("MapImage2.png").convert_alpha()
doorImage2 = ClassTemplate.SpriteSheet(doorImage)
doorImage3 = doorImage2.get_image(0, 13, 48, 48, 1, (0, 0, 0))

snakeImage = pygame.image.load("snake.png").convert_alpha()
appleImage = pygame.image.load("apple.png").convert_alpha()
boomImage = pygame.image.load("fireball.png").convert_alpha()


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
character1_array = ConstructMap.make_player_sprite_array(character1)
player = ClassTemplate.Player(character1_array, player_position, player_trigger_size, player_speed, 10, 1)
num_caught_monster = [0, 0, 0]
stage_clear_condition = [10, 10, 10]

professor_position = [300, 300] # Professor Init
professor_trigger_size = 200
professor_speed = 2
professor_stamina = 20
professor_damage = 1
character2_array = ConstructMap.make_professor_spite_array(character2)
professor = ClassTemplate.Monster(character2_array, professor_position, professor_trigger_size, professor_speed, professor_stamina, professor_damage)
is_professor_moster = False

door_position = [0, 200]
door_trigger_size = 50
door_to_sub_screen = ClassTemplate.TriggerObject(ConstructMap.make_skill_object_sprite_array(doorImage3, 1), door_position, door_trigger_size)

monster_num = 10
# monster_list = [range(10)] # 10칸짜리 list
quest1_monster_type = [ConstructMap.make_skill_object_sprite_array(snakeImage, 1), professor_trigger_size, professor_speed, professor_stamina, professor_damage]
# quest2_monster_type = [image, trigger_size, speed, stamina, damage]
# quest3_monster_type = [image, trigger_size, speed, stamina, damage]
# quest4_monster_type = [image, trigger_size, speed, stamina, damage]

apple_trigger_size = 50
skill_E_apple = ClassTemplate.SkillObject(ConstructMap.make_skill_object_sprite_array(appleImage, 2), door_position, apple_trigger_size)
boom_trigger_size = 30
skill_R_boom = ClassTemplate.SkillObject(ConstructMap.make_skill_object_sprite_array(boomImage, 2), door_position, boom_trigger_size)



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

        
    # # Keyboard pressed
    if pressed[pygame.K_w]:
        player.transform_position(key_input[pygame.K_w])
    elif pressed[pygame.K_s]:
        player.transform_position(key_input[pygame.K_s])
    elif pressed[pygame.K_a]:
        player.transform_position(key_input[pygame.K_a])
    elif pressed[pygame.K_d]:
        player.transform_position(key_input[pygame.K_d])


    # Skill
    # Skill_SB
    for i in range(monster_num):
        if monster_list[i].is_collided_with(player) and pressed[pygame.K_SPACE]:
            monster_alive = monster_list[i].lose_stamina(player.damage)
            if monster_alive == False:
                num_caught_monster[stage_num] += 1
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
    windowSurface.fill(ClassTemplate.WHITE)
    windowSurface.blit(game_screen, (0, 0))
    windowSurface.blit(door_to_sub_screen.now_image, door_to_sub_screen.position)
 
    if game_screen == game_sub_screen:
        for i in range(monster_num):
            if monster_list[i].alive == False:
                monster_list[i].alive = True
                monster_list[i].refresh_monster()
            windowSurface.blit(monster_list[i].now_image, monster_list[i].position)
    elif game_screen == game_main_screen:
        windowSurface.blit(professor.now_image, professor.position)

    if skill_E_apple.alive == True:
        windowSurface.blit(skill_E_apple.now_image, skill_E_apple.position)
        skill_E_apple.existence_countdown()
    if skill_R_boom.alive == True:
        windowSurface.blit(skill_R_boom.now_image, skill_R_boom.position)
        skill_R_boom.existence_countdown()

    windowSurface.blit(player.now_image, player.position)

    # print(stage_num)
    # print(num_caught_monster[stage_num])

    # windowSurface.blit(skill_E_apple.now_image, player.position)

    pygame.display.update()
    mainClock.tick(50)
    # set_colorkey((56, 56, 94)) .convert_alpha().set_colorkey((255, 0, 255))

    # character image 고치기//
    # 교수님한테 가까이 가서 sb누르면 pygame ui 뜨게
    # ui는 text파일 순서대로 읽어오도록
    # 교수님 monster 동작

    # Map Image만들기
    # UI로 player 체력 바 추가
    # Monster position위에도 체력 바 하나씩 달아주기

    # 메인 화면
    # 튜토리얼과 게임 설명
    # Map Image에서 벽에 충돌 안하게
    # 게임 일시정지 기능
    # Player 이름 받아서 화면에 써주는 기능

    # 하 아예 방을 세개 만들어서 다시 들어가서 뱀을 잡으면 복습하는 의미로 알고 성적 올려주는 그런 이스터에그 있으면 좋을텐데
    # 시간이 없네
    # 종강하고 추가해볼까