# Matplotlib Charts
from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('Matplotlib Charts')
root.iconbitmap('C:/Users/bhati/hello/Tkinter/home_house_icon_250568.ico')
root.geometry('400x400')

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.polar(house_prices)
    plt.show()

my_button = Button(root, text="Graph It!", command=graph)
my_button.pack()

root.mainloop()