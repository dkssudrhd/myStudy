import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("MG GUI")
root.geometry("680x480") 

values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values, state="readonly") # state를 통해 다른 값 선택 못하게 조절절
# combobox.set("카드 결제일") # 처음 보이는 내용 설정
combobox.current(0)
combobox.pack()

def btncmd():
    print(combobox.get())
    pass

btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()


