from tkinter import (Tk, Label, Frame, Button,
    Menu, PhotoImage, StringVar,
    ttk, filedialog, Toplevel
)

def main_menu(kinter_window, current_status):
    # Define a menu
    my_menu = Menu(kinter_window)
    kinter_window.config(menu=my_menu)

    # Creat functions for Menu Items
    def open_new_file():
        current_status.set('Opening New File')
        filetype_list = ['.png', '.gif']
        kinter_window.filename = filedialog.askopenfilename(
            initialdir='~',
            title='Open New File',
            filetypes=(('PNG File', '*.png'), ('All Files','*'))
        )
        if kinter_window.filename != '':
            image_preview_win = Toplevel()
            image_preview_win.title(kinter_window.filename)
            image_preview_win.geometry('400x400')
            def win_is_gone():
                current_status.set('Waiting')
                image_preview_win.destroy()
            for f_type in filetype_list:
                if f_type not in kinter_window.filename.lower():
                    x = 1
                else:
                    x = 0
                    break
            if x == 1:
                current_status.set('New File Failed To Open')
                label_text = f'{kinter_window.filename}\nFile type not support by this program.'
                image_label = Label(image_preview_win, text=label_text)
            elif x == 0:
                current_status.set('New File Opened')
                new_img = PhotoImage(file=kinter_window.filename)
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
    file_menu.add_command(label='Exit', command=kinter_window.destroy)
    test_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label='Test', menu=test_menu)
    test_menu.add_command(label='Test1', command=test1)
    test_menu.add_separator()
    test_menu.add_command(label='Test2', command=test2)


