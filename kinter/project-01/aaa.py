#!/usr/bin/env python3

from tkinter import Tk, Label, PhotoImage, StringVar
import mainMenu
import platform
if platform.system() == 'Windows':
    import ctypes
    myappid = "This is the song that doesn't end" # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# Create the root window with title and size
root = Tk()
root.title('Template Window')
root.geometry('700x400')
# Create window logo
win_icon = PhotoImage(file = "Rlogo.png")
root.iconphoto(False, win_icon)

# Create Status Bar variable(current_status)
current_status = StringVar()
current_status.set('Waiting')

# Create Menus from Module(mainMenu.py)
mainMenu.main_menu(root, current_status)

# Create Variables to use in program


# Create Functions to use in program


# Create Items to go in Grid


# Create a Visible Status Bar to show 'current_status'
"""
I really need to figure out how to make the modules into classes and be able
to call and manipulate from the main program.  I also want to make the status
bar its own thing like the menu and window modules.
I don't like having these interlacing modules.
"""
empty_label = Label(root, height=int(root.winfo_reqheight()/10))
empty_label.grid(row=99, column=0, columnspan=3)
my_status = Label(root, textvariable=current_status, bd=2, relief='sunken', anchor='e', width=9000)
my_status.grid(row=100, column=0, columnspan=20)
# Force an empty grid to fill and keep the status bar at the bottom of the window
root.columnconfigure((0,1), weight=1)
root.rowconfigure(99, weight=1)



root.mainloop()
