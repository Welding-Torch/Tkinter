# Initializing dynamic properties

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
imgLbl.grid(row=1,column=1,rowspan=2)
label1.grid(row=1,column=2,padx=10)
label2.grid(row=1, column=3, padx=10)
label3.grid(row=1, column=4, padx=10)
label4.grid(row=1, column=5, padx=10)
label5.grid(row=1, column=6, padx=10)
label6.grid(row=1, column=7, padx=(10, 20)) # Add 10 pixels of padding to the left side and 20 pixels of padding to the right side
getBtn.grid(row=2, column=2, columnspan=4)
rstBtn.grid(row=2, column=6, columnspan=2)

# Static Properties:
window.title('Lotto Number Picker')
window.resizable(0,0)
getBtn.configure(text='Get My Lucky Numbers')
rstBtn.configure(text='Reset')

# Initial Properties:
label1.configure(text='...') # This '...' is called an ellipsis
label2.configure(text='...')
label3.configure(text='...')
label4.configure(text='...')
label5.configure(text='...')
label6.configure(text='...')
rstBtn.configure(state=DISABLED)

# Sustain window:
window.mainloop()