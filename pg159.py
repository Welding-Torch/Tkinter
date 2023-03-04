from tkinter import *
import tkinter.messagebox as box

window=Tk()
window.title('Entry Example')

frame=Frame(window)
entry=Entry(frame)

def dialog():
    box.showinfo('Greetings', 'Welcome ' + entry.get())

btn = Button(frame, text='Enter Name',command=dialog)

btn.pack(side = RIGHT, padx=5)
entry.pack(side=LEFT)
frame.pack(padx=20,pady=20)

window.mainloop()