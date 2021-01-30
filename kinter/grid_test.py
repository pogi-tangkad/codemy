#!/usr/bin/env python3

from tkinter import *

# Create the root window with title and size
root = Tk()
root.title('Hello World')
root.geometry('700x400')
"""
**
__
"""
my_label = Label(root, text='Yo girl', font=('Utopia', 32))
my_label.grid(row=0, column=0, columnspan=2)
"""
__
_*
"""
my_label2 = Label(root, text='How you doin')
my_label2.grid(row=1, column=1, sticky=E)
"""
__
*_
"""
my_label3 = Label(root, text='Let me ask')
my_label3.grid(row=1, column=0)




root.mainloop()
