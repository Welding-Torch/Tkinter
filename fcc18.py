#Using Databases
from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('Using Databases')
root.iconbitmap('C:/Users/bhati/hello/Tkinter/home_house_icon_250568.ico')
root.geometry("400x400")

# Create a Database or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
)""")

# Commit Changes
conn.commit()

#Close Connection
conn.close()
mainloop()