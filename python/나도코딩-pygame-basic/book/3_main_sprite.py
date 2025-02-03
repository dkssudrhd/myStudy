import pygame

pygame.init() # 초기화 ***반드시 필요

screen_width = 480 # 가로 크기
screen_heigth = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_heigth))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 이미지 불러오기
background = pygame.image.load("nano_coding_pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("nano_coding_pygame_basic/character.png")
character_size = character.get_rect().size # 이미지의 크기를 넣기
character_width = character_size[0]                     # 캐릭터의 가로
character_height = character_size[1]                    # 캐릭터의 세로
character_x_pos = (screen_width - character_width) / 2                      # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_heigth - character_height      # 화면 세로 크기 가장 아래에 해당하는 곳에 위치


# 이벤트 루프
running = True
while running:
    for event in pygame.event.get(): # 어떠한 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False

    # 배경 그리기
    # screen.fill((0, 0, 255)) # 임의로 색 넣어주기 
    screen.blit(background, (0,0)) # 이미지 출력  

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기  

    pygame.display.update() # 게임화면 다시 그리기

# pygame 종료
pygame.quit()