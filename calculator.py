from tkinter import *
import customtkinter
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

# Let's create the Tkinter window
window = customtkinter.CTk()

# Then, you will define the size of the window in width(312) and height(324) using the 'geometry' method
window.geometry("347x423")

# In order to prevent the window from getting resized you will call 'resizable' method on the window
#window.resizable(0, 0)

#Finally, define the title of the window
window.title("Calculator Custom Tkinter")


# Let's now define the required functions for the Calculator to function properly.

# 1. First is the button click 'btn_click' function which will continuously update the input field whenever a number is entered or any button is pressed it will act as a button click update.
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# 2. Second is the button clear 'btn_clear' function clears the input field or previous calculations using the button "C"
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

# 3. Third and the final function is button equal ("=") 'btn_equal' function which will calculate the expression present in input field. For example: User clicks button 2, + and 3 then clicks "=" will result in an output 5.
def btn_equal():
    global expression
    result = str(eval(expression)) # 'eval' function is used for evaluating the string expressions directly
    # you can also implement your own function to evalute the expression istead of 'eval' function
    input_text.set(result)
    expression = ""

expression = ""
# In order to get the instance of the input field 'StringVar()' is used
input_text = StringVar()

# CUSTOMTKINTER - DECLARE TILEBG IMAGE PATH
import os
from PIL import Image
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "C:/Users/bhati/hello/Tkinter")
tile = customtkinter.CTkImage(Image.open(os.path.join(image_path, "tilebg.png")), size=(87, 71))

# Once all the functions are defined then comes the main section where you will start defining the structure of the calculator inside the GUI.

# The first thing is to create a frame for the input field
input_frame = customtkinter.CTkFrame(window, width = 347, height = 70.5)
input_frame.pack(side = TOP)


# Then you will create an input field inside the 'Frame' that was created in the previous step. Here the digits or the output will be displayed as 'right' aligned
input_field = customtkinter.CTkEntry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 347, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10) # 'ipady' is an internal padding to increase the height of input field


# Once you have the input field defined then you need a separate frame which will incorporate all the buttons inside it below the 'input field'
btns_frame = customtkinter.CTkFrame(window, width = 312, height = 272.5)
btns_frame.pack()


# The first row will comprise of the buttons 'Clear (C)' and 'Divide (/)'
clear = customtkinter.CTkButton(btns_frame, text = "C", width = 260.25, height = 70.5, cursor = "hand2", command = lambda: btn_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = customtkinter.CTkButton(btns_frame, text = "/", width = 86.75, height = 70.5, cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)


# The second row will comprise of the buttons '7', '8', '9' and 'Multiply (*)'
seven = customtkinter.CTkButton(btns_frame, text = "7", width = 86.75, height = 70.5, cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = customtkinter.CTkButton(btns_frame, text = "8", width = 86.75, height = 70.5, cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = customtkinter.CTkButton(btns_frame, text = "9", width = 86.75, height = 70.5, cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = customtkinter.CTkButton(btns_frame, text = "*", width = 86.75, height = 70.5, cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)


# The third row will comprise of the buttons '4', '5', '6' and 'Subtract (-)'
four = customtkinter.CTkButton(btns_frame, text = "4", width = 86.75, height = 70.5, cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = customtkinter.CTkButton(btns_frame, text = "5", width = 86.75, height = 70.5, cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = customtkinter.CTkButton(btns_frame, text = "6", width = 86.75, height = 70.5, cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = customtkinter.CTkButton(btns_frame, text = "-", width = 86.75, height = 70.5, cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)


# The fourth row will comprise of the buttons '1', '2', '3' and 'Addition (+)'
one = customtkinter.CTkButton(btns_frame, text = "1", width = 86.75, height = 70.5, cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = customtkinter.CTkButton(btns_frame, text = "2", width = 86.75, height = 70.5, cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = customtkinter.CTkButton(btns_frame, text = "3", width = 86.75, height = 70.5, cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = customtkinter.CTkButton(btns_frame, text = "+", width = 86.75, height = 70.5, cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)


# Finally, the fifth row will comprise of the buttons '0', 'Decimal (.)', and 'Equal To (=)'
zero = customtkinter.CTkButton(btns_frame, text = "0", width = 173.5, height = 70.5, cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = customtkinter.CTkButton(btns_frame, text = ".", width = 86.75, height = 70.5, cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = customtkinter.CTkButton(btns_frame, text = "=", width = 86.75, height = 70.5, cursor = "hand2", command = lambda: btn_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)


window.mainloop()
