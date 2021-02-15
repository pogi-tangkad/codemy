#!/usr/bin/env python3

from tkinter import (Tk, Label, Frame, Button,
    Menu, PhotoImage, StringVar, Checkbutton,
    ttk, filedialog, Toplevel, Frame
)
import datetime
import platform
if platform.system() == 'Windows':
    import ctypes
    myappid = "This is the song that doesn't end" # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# Create the root window with title and size
root = Tk()
root.title('Combo Boxes')
root.geometry('700x400')
# Create window logo
win_icon = PhotoImage(file = "Rlogo.png")
root.iconphoto(False, win_icon)

# Define a menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Creat functions for Menu Items
def open_new_file():
    current_status.set('Opening New File')
    filetype_list = ['.png', '.gif']
    root.filename = filedialog.askopenfilename(
        initialdir='~',
        title='Open New File',
        filetypes=(('PNG File', '*.png'), ('All Files','*'))
    )
    if root.filename != '':
        image_preview_win = Toplevel()
        image_preview_win.title(root.filename)
        image_preview_win.geometry('400x400')
        def win_is_gone():
            current_status.set('Waiting')
            image_preview_win.destroy()
        for f_type in filetype_list:
            if f_type not in root.filename.lower():
                x = 1
            else:
                x = 0
                break
        if x == 1:
            current_status.set('New File Failed To Open')
            label_text = f'{root.filename}\nFile type not support by this program.'
            image_label = Label(image_preview_win, text=label_text)
        elif x == 0:
            current_status.set('New File Opened')
            new_img = PhotoImage(file=root.filename)
            my_img = new_img.zoom(2,2)
            image_label = Label(image_preview_win, image=my_img)
        image_label.pack(expand=True)
        image_preview_win.wm_protocol('WM_DELETE_WINDOW', win_is_gone)
        image_preview_win.mainloop()
    
def test1():
    print('test1')

def test2():
    print('test2')

# Create Menu Items
file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=open_new_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)
test_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Test', menu=test_menu)
test_menu.add_command(label='Test1', command=test1)
test_menu.add_separator()
test_menu.add_command(label='Test2', command=test2)

# Create Variables to use in program
current_status = StringVar()
current_status.set('Waiting')

# Create Functions to use in program


# Create Items to go in Grid


# Create a status bar to show 'current_status'
empty_label = Label(root, height=int(root.winfo_reqheight()/10))
empty_label.grid(row=99, column=0, columnspan=3)
my_status = Label(root, textvariable=current_status, bd=2, relief='sunken', anchor='e', width=9000)
my_status.grid(row=100, column=0, columnspan=20)




root.columnconfigure((0,1), weight=1)
root.rowconfigure(99, weight=1)


root.mainloop()
