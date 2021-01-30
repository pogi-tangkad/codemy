#!/usr/bin/env python3

from tkinter import Tk, Label, Frame, Button, Menu, PhotoImage, StringVar

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
#file_menu.add_command(label='New', command=fake_command)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)







root.mainloop()
