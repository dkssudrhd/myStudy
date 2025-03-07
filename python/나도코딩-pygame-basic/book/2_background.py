import pygame

pygame.init() # 초기화 ***반드시 필요

screen_width = 480 # 가로 크기
screen_heigth = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_heigth))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 이미지 불러오기
background = pygame.image.load("C:/Users/us/Desktop/python/nano_coding_pygame_basic/background.png")
# 이벤트 루프
running = True
while running:
    for event in pygame.event.get(): # 어떠한 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False

    screen.fill((0, 0, 255)) # 임의로 색 넣어주기 
    # screen.blit(background, (0,0)) # 이미지 출력    

    pygame.display.update() # 게임화면 다시 그리기

# pygame 종료
pygame.quit()