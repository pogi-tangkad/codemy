#!/usr/bin/env python3

from tkinter import Tk, Label, Frame, Button, Menu, PhotoImage, StringVar, IntVar, Radiobutton
from time import sleep

# Create the root window with title and size
root = Tk()
root.title('Hello World')
root.geometry('700x400')
# Create window logo
win_icon = PhotoImage(file = "Rlogo.png")
root.iconphoto(False, win_icon)

# Define a menu
my_menu = Menu(root)
root.config(menu=my_menu)
# Create Menu Items
file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='File', menu=file_menu)
##file_menu.add_command
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)

# Create the label to display the result
my_label = Label(root)

# Create Radio Button function
def radio():
    if v.get() not in [1,2]:
        return
    if my_label.winfo_exists():
        my_label.pack_forget()
    my_label['text'] = f'You clicked button {v.get()}'
    my_label.pack(pady=10)

def clear_selection():
    if my_label.winfo_exists():
        my_label.pack_forget()
    my_label['text'] = 'Selection Cleared'
    v.set(0)
    my_label.pack(pady=10)
    
# Radio Buttons
v = IntVar(0)

rbutton_1 = Radiobutton(root, text='One', variable=v, value=1, command=radio)
rbutton_2 = Radiobutton(root, text='Two', variable=v, value=2, command=radio)
rbutton_1.pack()
rbutton_2.pack()

my_button = Button(root, text='Clear Selection', command=clear_selection)
my_button.pack()






root.mainloop()
