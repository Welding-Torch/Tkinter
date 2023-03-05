from tkinter import *
import tkinter.messagebox as box

# root is an object (instance) of Tk() class.
root = Tk()

# Creating a Label Widget
myLable = Label(root, text='Hello World!')
# Shoving it onto the screen using pack() method.
myLable.pack()

root.mainloop()