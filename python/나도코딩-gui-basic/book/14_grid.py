from tkinter import *

root = Tk()
root.title("MG GUI")
root.geometry("680x480") 

# btn1 = Button(root, text="버튼1")
# btn2 = Button(root, text="버튼2")
# btn3 = Button(root, text="버튼3")
# btn4 = Button(root, text="버튼4")

# btn1.grid(row=0, column=0)
# btn2.grid(row=0, column=1)
# btn3.grid(row=1, column=0)
# btn4.grid(row=1, column=1)

# 맨 윗줄
btn_f16 = Button(root, text="F16", padx=10, pady=10)
btn_f17 = Button(root, text="F17", padx=10, pady=10)
btn_f18 = Button(root, text="F18", padx=10, pady=10)
btn_f19 = Button(root, text="F19", padx=10, pady=10)

btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)   # sticky는 원하는 방향으로 달라붙음
btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 두번째 줄
btn_clear = Button(root, text="clear", padx=10, pady=10)
btn_equla = Button(root, text="=", padx=10, pady=10)
btn_div = Button(root, text="/", padx=10, pady=10)
btn_mul = Button(root, text="*", padx=10, pady=10)

btn_clear.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_equla.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 세번째 줄
btn_7 = Button(root, text="7", padx=10, pady=10)
btn_8 = Button(root, text="8", padx=10, pady=10)
btn_9 = Button(root, text="9", padx=10, pady=10)
btn_sub = Button(root, text="-", padx=10, pady=10)

btn_7.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 네번째 줄
btn_4 = Button(root, text="4", padx=10, pady=10)
btn_5 = Button(root, text="5", padx=10, pady=10)
btn_6 = Button(root, text="6", padx=10, pady=10)
btn_add = Button(root, text="+", padx=10, pady=10)

btn_4.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_add.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 다섯번째 줄
btn_1 = Button(root, text="1", padx=10, pady=10)
btn_2 = Button(root, text="2", padx=10, pady=10)
btn_3 = Button(root, text="3", padx=10, pady=10)
btn_enter = Button(root, text="enter", padx=10, pady=10)

btn_1.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3) # 현재 위치로 부터 아래쪽으로 2개

# 마지막 줄
btn_0 = Button(root, text="0", padx=10, pady=10)
btn_point = Button(root, text=".", padx=10, pady=10)

btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3)
btn_point.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)



root.mainloop()


