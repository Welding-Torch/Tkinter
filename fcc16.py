# Dropdown Menus
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Dropdown Menus")
root.iconbitmap('C:/Users/bhati/hello/Tkinter/home_house_icon_250568.ico')
root.geometry("400x400")

def show():
    myLabel = Label(root, text=clicked.get()).pack()

options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()
mainloop()