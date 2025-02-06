import pygame
import os 
# 프레임을 만들고 배경과 스테이지 캐릭터를 만든다.

##################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() # 초기화 ***반드시 필요

screen_width = 640 # 가로 크기
screen_heigth = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_heigth))

# 화면 타이틀 설정
pygame.display.set_caption("MG Pang") # 게임 이름

# FPS
clock = pygame.time.Clock()
##################################################################

current_path = os.path.dirname(__file__) # 현재 파일의 위치를 반환
impage_path = os.path.join(current_path, "images") # images 폴더 위치 반환

# 배경만들기
background = pygame.image.load(os.path.join(impage_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(impage_path, "stage.png"))
stage_size = stage.get_rect().size
stage_width = stage_size[0]        # 스테이지 높이를 위해
stage_height = stage_size[1]         # 스테이지

# 캐릭터 만들기
character = pygame.image.load(os.path.join(impage_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_heigth - character_height - stage_height

# 캐릭터 이동 방향
character_to_x = 0

# 캐릭터 이동 스피드
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(impage_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한번에 여러 발 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 10


running = True
while running:
    dt = clock.tick(30)

    # 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_LEFT:          # 캐릭터 왼쪽
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:       # 캐릭터 오른쪽
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:       # 무기 발사
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0 

    # 게임 캐릭터 위치 정의
    character_x_pos += character_to_x 

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    # 무기 위치 조정
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]

    # 천장에 닿은 무기 없애기
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0 ]

    # 화면에 그리기
    screen.blit(background, (0, 0))
    for weapon_x_pos, weapon_y_pos in weapons :
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos)) 
    screen.blit(stage, (0, screen_heigth - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

\
    pygame.display.update()

# 종료
pygame.quit()

    