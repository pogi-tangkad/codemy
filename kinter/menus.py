#!/usr/bin/env python3

from tkinter import Tk, Label, Frame, Button, Menu, PhotoImage

# Create the root window with title and size
root = Tk()
root.title('Hello World')
root.geometry('700x400')

win_icon = PhotoImage(file = "Rlogo.png")
root.iconphoto(False, win_icon)

# Define variables/labels to use in functions
my_label = Label(root)
counter = 0

# Define Fake Command
def fake_command():
    global counter
    counter += 1
    if my_label.winfo_exists():
        my_label.grid_forget()
    my_label['text'] = 'You clicked a menu item ' + str(counter) + ' times'
    my_label.grid(row=2,column=0, columnspan=2)

def show():
    my_frame.grid(row=1, column=0, columnspan=2, padx=20,pady=20)

def hide():
    my_frame.grid_forget()

# Define a menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Menu Items
file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=fake_command)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)

# Create another sub menu (Edit)
edit_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Cut', command=fake_command)
edit_menu.add_command(label='Copy', command=fake_command)
edit_menu.add_command(label='Paste', command=fake_command)

show_button = Button(root, text='Show', command=show)
hide_button = Button(root, text='Hide', command=hide)

show_button.grid(row=0, column=0)
hide_button.grid(row=0, column=1)

my_frame = Frame(root, width=200, height=200, bd=1,bg='blue')
my_frame.grid(row=1, column=0, columnspan=2, padx=20,pady=20)

frame_label = Label(my_frame, text='Hello World!')
frame_label.pack(padx=10, pady=10)

root.mainloop()
