#!/usr/bin/env python3

# Same as input.py but this time passing the Entry box value into
# the function using lambda

from tkinter import Tk, Label, Button, Entry, PhotoImage
# from tkinter.ttk import *
from random import randint

# Create the root window with title and size
root = Tk()
root.title('Input Tester')
root.geometry('1000x800')
win_icon = PhotoImage(file = 'Rlogo.png')
root.iconphoto(False, win_icon)

# Create a label for the root screen
my_label = Label(root, text='Input Name', font = ('Z003', 30))
my_label.pack(pady=40)

#Create a function for the button/entry box 
def clicked(e_val):
    if my_label2.winfo_exists():
        my_label2.pack_forget()
    my_label2['text'] = 'Hello, ' + e_val
    my_label2.pack(pady=10)
    e.delete(0, 'end')

# Create an Entry widget
e = Entry(root, width = 20, font = ('', 15))
e.pack(pady = 10)

my_label2 = Label(root, font = ('Z003', 32))

# Create a button to use the Entry box
my_button = Button(root, text = 'Click Me!', command = lambda: clicked(e.get()))
my_button.pack(pady = 30)


root.mainloop()
