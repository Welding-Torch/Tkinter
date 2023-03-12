# Checkboxes
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Checkboxes")
root.iconbitmap('C:/Users/bhati/hello/Tkinter/home_house_icon_250568.ico')
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="Would you like to Supersize your order?", variable=var, onvalue="SuperSize", offvalue="RegularSize")
c.deselect()
c.pack()


myButton = Button(root, text="Show Selection", command=show).pack()

mainloop()