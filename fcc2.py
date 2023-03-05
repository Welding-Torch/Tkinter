from tkinter import *
import tkinter.messagebox as box

# root is an object (instance) of Tk() class.
root = Tk()

# Creating a Label Widget
myLable = Label(root, text='Hello World!')
myLable2 = Label(root, text='My name is Siddharth Bhatia.')
myLable3 = Label(root, text='                            ')
# Shoving it onto the screen using pack() method.
myLable.grid(row=0,column=0)
myLable2.grid(row=1,column=5)
myLable3.grid(row=1,column=1)

root.mainloop()