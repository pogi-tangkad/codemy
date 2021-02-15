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
    filetype_list = ['.png', '.gif']
    root.filename = filedialog.askopenfilename(
        initialdir='C:/Users/Field/Desktop/python/py',
        title='Open New File',
        filetypes=(('PNG File', '*.png'), ('All Files','*'))
    )
    if root.filename != '':
        image_preview_win = Toplevel()
        image_preview_win.title(root.filename)
        image_preview_win.geometry('400x400')
        for f_type in filetype_list:
            if f_type not in root.filename.lower():
                x = 1
            else:
                x = 0
                break
        if x == 1:
            label_text = f'{root.filename}\nFile type not support by this program.'
            image_label = Label(image_preview_win, text=label_text)
        elif x == 0:
            new_img = PhotoImage(file=root.filename)
            my_img = new_img.zoom(2,2)
            image_label = Label(image_preview_win, image=my_img)
        image_label.pack(expand=True)
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

# Create Functions to use in program
def update_label(x,y,z):
    my_label['text'] = f'You have chosen:  {my_combo.get()}'

def hide_window():
    root.iconify()

# Create variables to use in program
options = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'
]
current_date = datetime.datetime.now()
current_weekday = current_date.strftime('%w')
my_label = Label(root)
option_var = StringVar()

# Create the Combo box selection
my_combo = ttk.Combobox(
    root,
    value=options,
    state='readonly',
    textvariable=option_var
)
my_combo.current(current_weekday)        # Uncomment to have a pre-selected value when program starts
my_combo.pack(pady=20)

my_label.pack(pady=20)

# Create trace for StringVar(option_var) after initial label pack to
# avoid displaying the Label(my_label) before an option was chosen.
option_var.trace_add('write', update_label)

# Create a button to test hiding the window ('iconify')
my_button = Button(root, text='Hide Window', command=hide_window)
my_button.pack(pady=50)

root.mainloop()