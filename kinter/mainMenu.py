from tkinter import Menu, filedialog
import newWindow

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
        if kinter_window.filename not in [(), '']:
            newWindow.new_window(kinter_window.filename, filetype_list, current_status)
        else:
            current_status.set('Waiting')
        
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


