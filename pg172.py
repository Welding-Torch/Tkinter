# Planning The Program

# Widgets:
from tkinter import *

window = Tk()
img = PhotoImage(file='tilebg.png')

imgLbl = Label(window, image=img)
label1 = Label(window, relief='groove', width=2)
label2 = Label(window, relief='groove', width=2)
label3 = Label(window, relief='groove', width=2)
label4 = Label(window, relief='groove', width=2)
label5 = Label(window, relief='groove', width=2)
label6 = Label(window, relief='groove', width=2)
getBtn = Button(window)
rstBtn = Button(window)

# Geometry
imgLbl.grid()
label1.grid()
label2.grid()
label3.grid()
label4.grid()
label5.grid()
label6.grid()
getBtn.grid()
rstBtn.grid()

# Sustain window:
window.mainloop()