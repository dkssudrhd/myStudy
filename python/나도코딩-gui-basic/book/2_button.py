from tkinter import *

root = Tk()
root.title("MG GUI")

btn1 = Button(root, text="버튼1")
btn1.pack() # 이걸 호출해줘야 보임임

# padx, pady는 text의 길이가 길어지면 같이 커짖ㅁ
# width, height는  text의 길이와 관계 없이 고정
btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")  
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file="gui_basic/img.png")
btn6 = Button(root, image=photo)
btn6.pack()


def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작버튼", command=btncmd)
btn7.pack()

root.mainloop()
