# Create New Windows
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Create New Windows')
root.iconbitmap('C:/Users/bhati/hello/Tkinter/home_house_icon_250568.ico')

def open():
    global my_image       
    top = Toplevel()
    top.title('Create New Windows')
    top.iconbitmap('C:/Users/bhati/hello/Tkinter/home_house_icon_250568.ico')

    my_image = ImageTk.PhotoImage(Image.open("images/redhood.jpg"))
    my_label = Label(top, image=my_image).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()

btn = Button(root, text='Open Second Window', command=open).pack()

mainloop()