from tkinter import *

root = Tk()
root.title("MG GUI")
root.geometry("680x480") 

# Text는 여러줄 Entry는 한줄만 가능능

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요.")   # 미리 글자 넣기기

e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 1 : 첫번째 라인을 의미, 0 : 0번째 column 위치
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()


