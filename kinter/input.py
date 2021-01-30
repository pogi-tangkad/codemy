#!/usr/bin/env python3

# I have no idea how to setup an Icon in the GNOME3 IDE / CentOS 8

from tkinter import Tk, Label, Button, Entry, PhotoImage
# from tkinter.ttk import *
from random import randint
#from PIL import ImageTk, Image
#filen = r'~/codemy/kinter/Rlogo.png'
#img = Image.open(filen)
#img.save('~/codemy/kinter/Rlogo.ico',format = 'ICO', sizes=[(32,32)])

# Create the root window with title and size
root = Tk()
root.title('Input Tester')
root.geometry('1000x800')
'''
# The following works but it is clunky
img = PhotoImage(file='/home/pogi/codemy/kinter/Rlogo.png')
root.call('wm', 'iconphoto', root._w, img)

# The following does not work (intended for windows)
# could use an OS determining if statement to use
root.iconphoto(True, '@/home/pogi/codemy/kinter/Rlogo.png')
root.iconbitmap('Rlogo.ico')
'''
win_icon = PhotoImage(file = "Rlogo.png")
root.iconphoto(False, win_icon)


# Create a label for the root screen
my_label = Label(root, text='Input Name', font = ('Z003', 30))
my_label.pack(pady=40)

#Create a function for the button/entry box
def clicked():
    if my_label2.winfo_exists():
        my_label2.pack_forget()
    if e.get() == '':
        my_label2['text'] = 'You forgot to type something, silly goat'
    else:
        my_label2['text'] = 'Hello, ' + e.get()
    my_label2.pack(pady=10)
    e.delete(0, 'end')

# Clear function to get rid of the hello
def clear():
    my_label2.pack_forget()

# Add Images
my_image = PhotoImage(file = "taycan.png")
image_label = Label(image = my_image)
image_label.pack()

# Create an Entry widget
e = Entry(root, width = 20, font = ('', 15))
e.pack(pady = 10)

# Create label for use in multiple functions
my_label2 = Label(root, font = ('Z003', 32))

# Create a button to use the Entry box
my_button = Button(root, text = 'Click Me!', command = clicked)
my_button.pack(pady=5)

my_button = Button(root, text = 'clear', command = clear)
my_button.pack(pady=5)







root.mainloop()
