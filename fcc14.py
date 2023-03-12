# Open Files Dialog Box
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title('Open Files Dialog Box')
root.iconbitmap('C:/Users/bhati/hello/Tkinter/home_house_icon_250568.ico')

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/bhati/hello/Tkinter", title='Select A File', filetypes=(("png files", "*.png"),("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()

    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

    
my_btn = Button(root, text='Open File', command=open).pack()
mainloop()