# Using Icons, Images, and Exit Buttons
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn to Code')
root.iconbitmap('C:/Users/bhati/hello/Tkinter/home_house_icon_250568.ico')

my_img = ImageTk.PhotoImage(Image.open('tilebg.png'))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root,text='Exit Program',command=root.quit)
button_quit.pack()
root.mainloop()