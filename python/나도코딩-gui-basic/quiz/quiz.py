# tkinter를 이용한 메모장 프로그램

'''
1. title : 제목 없음 - Windows 메모장
2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
3. 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
3-1. 열기 : mynote.txt 파일 내용 열어서 보이기
3-2. 저장 : mynote.txt 파일에 현재 내용을 저장하기
3-3. 끝내기 : 프로그램 종료
4. 프로그램 시작 시 본문은 비어 있는 상태
5. 하단 status 바는 필요 없음
6. 프로그램 크기, 위치는 자유롭게 하되 크기 조정 가능해야 함
6. 본문 우측에 상하 스크롤바 넣기
'''

from tkinter import *
import os

# 기본 크기 및 root 설정 + 제목까지
root = Tk()
root.title("제목없음 - Windows 메모장")
root.geometry("680x480") 

# 메모 공간과 스크롤을 넣을 공간 설정
# 실습에서는 frame을 따로 만들지 않고 넣을수도 있음음
frame = Frame(root)
frame.pack(fill="both", expand=True)

txt = Text(frame)

# 스크롤 과 txt 연결
scrollbar = Scrollbar(frame)
scrollbar.config(command=txt.yview_scroll)
txt.config(yscrollcommand=scrollbar.set)

# 스크롤과 메모를 보여주기
scrollbar.pack(side="right", fill="y")
txt.pack(side="left", fill="both", expand=True)

# 메뉴
menu = Menu(root)
menu_file = Menu(menu, tearoff=0)


filename = "mynote.txt"
# 파일 열기
# 내용을 읽기 -> 이전 내용 지우기 -> 읽은 내용 적기기
def file_open():
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf-8") as file:
            print("파일 열기")
            content = file.read()
            print(content)
            txt.delete("1.0", END)
            txt.insert(END, content)

            file.close()
    else:
        print("파일을 찾을 수 없습니다.")

def file_storage():
    if os.path.isfile(filename):
        with open(filename, "w", encoding="utf-8") as file:
            content = txt.get("1.0", END)
            print(content)
            file.write(content)

            file.close()

def file_exit():
    print("프로그램이 종료되었습니다.")
    root.quit()

menu_file.add_command(label="열기", command=file_open)
menu_file.add_command(label="저장", command=file_storage)
menu_file.add_command(label="닫기", command=file_exit)
menu.add_cascade(label="파일", menu=menu_file)
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")



root.config(menu=menu)

root.mainloop()
