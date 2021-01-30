#!/usr/bin/env python3

from tkinter import Tk, Label, Entry, Button
from random import randint

# Create the root window with title and size
root = Tk()
root.title('Hello World')
root.geometry('1000x800')

# Create a label for the root screen
my_label = Label(root, text='Hello World', fg = 'white', bg = 'black', font = ('Z003', 32), height = 5, width = 20)
my_label.pack(pady=20)
my_label2 = Label(root, text='Second thing', relief = 'ridge', font = ('Z003', 50), state = 'disabled')
my_label2.pack(pady=70)

"""
Create function for button:  Label is created outside but only packed inside.
This got a little out of hand with global declarations, but I managed to clean it up quite a bit.
No more counter or global pad_val
The big issue was trying to declare and pack in the same line (pythonic style).  This prevented
the Label from having the attributes necessary to use 'pack.forget()'.
"""
def clicked(x):
    pad_val = randint(5,x)
    if my_label3.winfo_exists():
        my_label3.pack_forget()
    my_label3.pack(pady=pad_val)
    
# Create Label that will appear after button is clicked
my_label3 = Label(root, text = 'You clicked the button!')

# Create Buttons (with goofy random padding value to test lambda)
# loc_val is really not needed, but I am testing passing a variable.
loc_val = 50
my_button = Button(root, text = 'Click Me!', command = lambda: clicked(loc_val))
my_button.pack(pady = 30)

# Create an entry widget
e = Entry(root, width = 200, font = ("Z003", 32))
e.pack(pady = 10)



root.mainloop()
