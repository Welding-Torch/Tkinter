# Message boxes
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('Message Boxes')
root.iconbitmap('C:/Users/bhati/hello/Tkinter/home_house_icon_250568.ico')

def popup():
    response = messagebox.showinfo("This is my Popup!", "Hello World!")
    Label(root, text=response).pack()
    # if response == 1:
    #     Label(root,text="You clicked yes" ).pack()
    # else:
    #     Label(root,text="You clicked No").pack()
    #messagebox.showwarning("This is my Popup!", "Hello World!")
    #messagebox.showerror("This is my Popup!", "Hello World!")
    #messagebox.askquestion("This is my Popup!", "Hello World!")
    #messagebox.askokcancel("This is my Popup!", "Hello World!")
    #messagebox.askyesno("This is my Popup!", "Hello World!")

Button(root, text="Popup",command=popup).pack()

mainloop()