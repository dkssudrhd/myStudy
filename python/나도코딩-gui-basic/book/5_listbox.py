from tkinter import *

root = Tk()
root.title("MG GUI")
root.geometry("680x480") 

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # listbox.delete(END) # 맨 뒤에 항목을 삭제
    # listbox.delete(0)   # 맨 앞 항목을 삭제

    # 항목의 갯수 구하기
    # print("리스트에는 ", listbox.size(), "개가 있어요")

    # 원하는 항목가져오기
    # print("1번째부터 3번째 까지의 항목 : ", listbox.get(0, 2))

    # 선택된 항목 확인 (index 값으로 반환)
    print("선택된 항목 : ", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()


