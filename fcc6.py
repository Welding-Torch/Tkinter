# Images
from tkinter import *

root = Tk()
root.title('Learn to Code')
root.iconbitmap('C:/Users/bhati/hello/Tkinter/home_house_icon_250568.ico')

button_quit = Button(root,text='Exit Program',command=root.quit)
button_quit.pack()
root.mainloop()