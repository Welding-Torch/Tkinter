# Tkinter MASTER Document

# Intention: This Document is meant to be a CheatSheet of EVERYTHING I have learnt about Tkinter.

from tkinter import *
import tkinter.messagebox as box

# root is an object (instance) of Tk() class.
root = Tk()

# Creating a Label Widget
myLable = Label(root, text='Hello World!')
#   ↑      ↑      ↑         
# Object  Class  Arguments



myButton = Button(root, text='Click Me!',state=DISABLED)
#   ↑      ↑      ↑                                ↑
# Object  Class  Arguments                     Literal

# Shoving the Widgets onto the screen using pack() method.
myLable.pack()
myButton.pack()

def myClick():
    myLabel2 = Label(root, text = "Look! I clicked a Button!!")
    myLabel2.pack()
myButton2 = Button(root, text='Click Me!', padx=50,pady=50, command=myClick, fg='blue', bg='black')
myButton2.pack()

'''
# FCC4.py
e = Entry(root, width=50, bg='black',fg='orange',borderwidth=50)
e.pack()
e.insert(0,'Enter Your Name: ')


def myClick():
    hello = 'Hello ' + e.get()
    myLabel = Label(root, text = hello)
    myLabel.pack()
myButton = Button(root, text='Enter Your Name', padx=50,pady=50, command=myClick, fg='blue', bg='black')
myButton.pack()
'''
root.mainloop()

# root.mainloop()
#   ↑      ↑
# object  attribute

# CAPITALIZATION GUIDE IN TKINTER
Objects = camelCase - starts with a lowercase letter and the first letter of every new subsequent word has its first letter capitalized.
Classes = PascalCase - PascalCase has every word starts with an uppercase letter
Arguments = lowercase
Literal = UPPERCASE

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

# Methods

# There are 3 Ways To Place Widgets on Screen:
# Pack
# Grid
# Place

'''
Tkinter has three built-in layout managers that use geometric methods to position widgets in an application frame: 

pack() organizes widgets in horizontal and vertical boxes that are limited to left, right, top, bottom positions. Each box is offset and relative to each other.
place() places widgets in a two dimensional grid using x and y absolute coordinates. 
grid() locates widgets in a two dimensional grid using row and column absolute coordinates. 
Important: pack(), place(), and grid() should not be combined in the same master window. Instead choose one and stick with it.
'''
# https://www.activestate.com/resources/quick-reads/how-to-position-widgets-in-tkinter/

Label Arguments
bd=10
relief=SUNKEN
anchor=E

.grid Arguments
sticky=W+E