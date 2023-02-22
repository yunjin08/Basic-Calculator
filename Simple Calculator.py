from tkinter import *
import math

root = Tk()
root.title("Simple Calculator")
root.configure(bg="navy blue")
root.iconbitmap("C:/Users/Acer/Downloads/icon.ico")
e = Entry(root, width=35, borderwidth=5,  bg="sky blue")
e.grid(column=0, row=0, columnspan=3, padx=10, pady=(20,20))

# Interaction Functions

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    try:
        if maths == "addition":
            e.insert(0, f_num + int(second_number))

        if maths == "subtraction":
            e.insert(0, f_num - int(second_number))

        if maths == "multiplication":
            e.insert(0, f_num * int(second_number))

        if maths == "division":
            e.insert(0, f_num / int(second_number))

        if maths == "sqrt":
            num = int(second_number)
            e.insert(0, math.sqrt(num))

    except NameError:
        e.insert(0, int(second_number))



def button_add():
    first_number = e.get()
    global f_num
    global maths
    maths ="addition"
    f_num = float(first_number)
    e.delete(0, END)

def button_subtraction():
    first_number = e.get()
    global f_num
    global maths
    maths = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)


def button_multiplication ():
    first_number = e.get()
    global f_num
    global maths
    maths = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

def button_division():
    first_number = e.get()
    global f_num
    global maths
    maths = "division"
    f_num = float(first_number)
    e.delete(0, END)

def button_sqrt():
    global maths
    maths = "sqrt"

def button_back():
    current = e.get()
    e.delete(0, END)
    e.insert(0, current[:-1])




# Define Buttons

button_1 = Button(root, text="1", padx=40, pady=20, bg="sky blue", borderwidth=4,font=("TkDefaultFont", 10, "bold"),   command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, bg="sky blue",borderwidth=4,font=("TkDefaultFont", 10, "bold"),  command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, bg="sky blue",borderwidth=4,font=("TkDefaultFont", 10, "bold"),  command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, bg="sky blue",borderwidth=4,font=("TkDefaultFont", 10, "bold"),  command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, bg="sky blue",borderwidth=4,font=("TkDefaultFont", 10, "bold"),  command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, bg="sky blue",borderwidth=4,font=("TkDefaultFont", 10, "bold"),  command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, bg="sky blue",borderwidth=4,font=("TkDefaultFont", 10, "bold"),  command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, bg="sky blue",borderwidth=4,font=("TkDefaultFont", 10, "bold"),  command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, bg="sky blue",borderwidth=4,font=("TkDefaultFont", 10, "bold"),  command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, bg="sky blue",borderwidth=4,font=("TkDefaultFont", 10, "bold"),  command=lambda: button_click(0))
button_add = Button(root, text="+", padx=37, pady=18, bg="sky blue",borderwidth=4,font=("TkDefaultFont", 11, "bold"),  command=button_add)
button_equal = Button(root, text="=", padx=38, pady=20, bg="sky blue",borderwidth=4,font=("TkDefaultFont", 10, "bold"),  command=button_equal)
button_clear = Button(root, text="CE", padx=33, pady=20, bg="sky blue",borderwidth=4,font=("TkDefaultFont", 10, "bold"),  command=button_clear)
button_sqrt = Button(root, text="\u221A", padx=37, pady=18, bg="sky blue",borderwidth=4,font=("TkDefaultFont", 11, "bold"),  command=button_sqrt)
button_back = Button(root, text="\u2190", padx=36, pady=20, bg="sky blue",borderwidth=4,font=("TkDefaultFont", 10, "bold"),  command=button_back)
button_subtraction = Button(root, text="-", padx=39, pady=18, bg="sky blue",borderwidth=4,font=("TkDefaultFont", 12, "bold"),  command=button_subtraction)
button_multiplication = Button(root, text="x", padx=38, pady=20, bg="sky blue",borderwidth=4,font=("TkDefaultFont", 10, "bold"),  command=button_multiplication)
button_division = Button(root, text="/", padx=40, pady=18, bg="sky blue",borderwidth=4,font=("TkDefaultFont", 11, "bold"),  command=button_division)

# Put the buttons on the Screen

button_7.grid(column=0, row=1, padx=(10,0))
button_4.grid(column=0, row=2, padx=(10,0))
button_1.grid(column=0, row=3, padx=(10,0))
button_0.grid(column=0, row=4, padx=(10,0))
button_sqrt.grid(column=0, row=5, padx=(10,0))
button_back.grid(column=0, row=6, padx=(10,0), pady=(0,10))

button_8.grid(column=1, row=1, padx=5)
button_5.grid(column=1, row=2, padx=5)
button_2.grid(column=1, row=3, padx=5)
button_add.grid(column=1, row=4, padx=5)
button_multiplication.grid(column=1, row=5, padx=5)
button_clear.grid(column=1, row=6, padx=5, pady=(0,10))

button_9.grid(column=2, row=1, padx=(0,10))
button_6.grid(column=2, row=2, padx=(0,10))
button_3.grid(column=2, row=3, padx=(0,10))
button_subtraction.grid(column=2, row=4, padx=(0,10))
button_division.grid(column=2, row=5, padx=(0,10))
button_equal.grid(column=2, row=6, pady=(0,10), padx=(0,10))


root.mainloop()