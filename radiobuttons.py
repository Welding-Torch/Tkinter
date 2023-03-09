# Radio Buttons 
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Radio Buttons')
root.iconbitmap('C:/Users/bhati/hello/Tkinter/home_house_icon_250568.ico')

r=IntVar()
r.set("2")

def clicked(value):
    global myLabel
    myLabel.pack_forget()
    myLabel = Label(root,text=value)
    myLabel.pack()

Radiobutton(root, text="Option 1",padx=100,variable=r,value=1,command=lambda:clicked(r.get())).pack()
Radiobutton(root, text="Option 2",padx=100,variable=r,value=2,command=lambda:clicked(r.get())).pack()

myLabel = Label(root,text=r.get())
myLabel.pack()

mainloop()