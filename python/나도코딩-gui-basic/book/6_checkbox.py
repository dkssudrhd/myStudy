from tkinter import *

root = Tk()
root.title("MG GUI")
root.geometry("680x480") 

chkvar = IntVar() # chkcvar 에 int 형으로 값을 저장한다
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select() # 자동 선택 처리
# chkbox.deselect() # 선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0 일때 체크 해제 1 일때 체크
    print(chkvar2.get())
    
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()


