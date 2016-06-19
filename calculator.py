#coding=utf-8
from Tkinter import *

def sayHello():
    print("Hello_World")
root = Tk()
root.title("计算器")
root.geometry('400x200')

com = Button(root,text="打招呼",command=sayHello)
com.pack(side=BOTTOM)

root.mainloop()

