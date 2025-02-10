import time
from PIL import ImageGrab


time.sleep(5) # 5초 대기

for i in range(1, 11):
    img = ImageGrab.grab()  # 현재 스크린 이미지를 가져옴
    img.save("gui_basic/project/images/image{}.png".format(i)) # 파일로 저장
    time.sleep(2) # 2초 단위
    