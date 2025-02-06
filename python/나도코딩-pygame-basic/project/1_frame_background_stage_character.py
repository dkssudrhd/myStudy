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

running = True
while running:
    dt = clock.tick(30)

    # 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    # 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_heigth - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

# 종료
pygame.quit()

    