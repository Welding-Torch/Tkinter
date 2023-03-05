# Tkinter MASTER Document

# Intention: This Document is meant to be a CheatSheet of EVERYTHING I have learnt about Tkinter.

from tkinter import *
import tkinter.messagebox as box

# root is an object (instance) of Tk() class.
root = Tk()

# Creating a Label Widget
myLable = Label(root, text='Hello World!')
# Shoving it onto the screen using pack() method.
myLable.pack()

root.mainloop()

# root.mainloop()
#   ↑      ↑
# object  attribute

# Widgets - They always start with a capital letter.
# Here is a list of every Widget is alphabetical order:
1 = BitmapImage
2 = Button
3 = Canvas
4 = Checkbutton
5 = Entry
6 = Frame
7 = LabelFrame
8 = Grid
9 = PhotoImage
10 = Label
11 = Listbox
12 = Menubutton
13 = Menu
14 = OptionMenu
15 = Pack
16 = PanedWindow
17 = PhotoImage
18 = Place
19 = Radiobutton
20 = Scale
21 = Scrollbar
22 = Spinbox
23 = Text
24 = Toplevel
25 = Widget
26 = XView
27 = YView