from tkinter import *
window = Tk()
window.title('Button Example')

btn_end = Button(window, text = 'Close', command=exit)
def tog():
    if window.cget('bg') == 'yellow':
        window.configure(bg = 'gray')
    else:
        window.configure(bg = 'yellow')
        
btn_tog = Button(window, text = 'Switch', command=tog)

btn_end.pack(padx = 150, pady = 20)
btn_tog.pack(padx = 150, pady = 20)

window.mainloop()