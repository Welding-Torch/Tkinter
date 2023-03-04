from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title('Radio Button Example')

frame = Frame(window)

book = StringVar()

radio_1=Radiobutton(frame, text = 'HTML5', variable=book, value = 'HTML5 in easy steps')
radio_2=Radiobutton(frame, text='CSS3', variable=book, value = 'CSS3 in easy steps')
radio_3=Radiobutton(frame, text='JavaScript', variable=book, value = 'JavaScript in easy steps')

radio_1.select()

def dialog():
    box.showinfo('Selection', 'Your Choice: \n' + book.get())
btn = Button(frame,text = 'Choose',command=dialog)

btn.pack(side=RIGHT, padx = 5)
radio_1.pack(side=LEFT)
radio_2.pack(side=LEFT)
radio_3.pack(side=LEFT)
frame.pack(padx=30,pady=30)

window.mainloop()
