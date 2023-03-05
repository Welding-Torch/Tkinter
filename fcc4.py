# Creating Input Fields
from tkinter import *

root = Tk()

e = Entry(root, width=50, bg='black',fg='orange',borderwidth=50)
e.pack()
e.insert(0,'Enter Your Name: ')


def myClick():
    hello = 'Hello ' + e.get()
    myLabel = Label(root, text = hello)
    myLabel.pack()

myButton = Button(root, text='Enter Your Name', padx=50,pady=50, command=myClick, fg='blue', bg='black')
myButton.pack()


root.mainloop()