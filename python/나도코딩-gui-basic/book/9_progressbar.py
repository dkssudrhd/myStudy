import tkinter.ttk as ttk
from tkinter import *
import time

root = Tk()
root.title("MG GUI")
root.geometry("680x480") 

# mode indeterminate는 결정되지 않아 계속 좌우로 움직임

progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
progressbar.start(10)

progressbar.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length = 150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(101):
        time.sleep(0.1)
        
        p_var2.set(i)
        progressbar2.update()

def btncmd():
    progressbar.stop()  # 작동 중지(값이 사라짐)
    print(p_var2.get())

btn = Button(root, text="중지", command=btncmd)
btn.pack()
btn2 = Button(root, text="시작", command=btncmd2)
btn2.pack()


root.mainloop()


