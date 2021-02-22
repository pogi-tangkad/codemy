from tkinter import Tk, Toplevel, Label, PhotoImage
import mainMenu

def new_window(file_name, filetype_list, current_status):
    image_preview_win = Toplevel()
    image_preview_win.title(file_name)
    image_preview_win.geometry('400x400')

    def win_is_gone():
        current_status.set('Waiting')
        image_preview_win.destroy()
    
    mainMenu.main_menu(image_preview_win,current_status)

    for f_type in filetype_list:
        if f_type not in file_name.lower():
            current_status.set('New File Failed To Open')
            label_text = f'{file_name}\nFile type not supported by this program.'
            image_label = Label(image_preview_win, text=label_text)
        else:
            current_status.set('New File Opened')
            new_img = PhotoImage(file=file_name)
            my_img = new_img.zoom(2,2)
            image_label = Label(image_preview_win, image=my_img)
            break

    image_label.pack(expand=True)
    image_preview_win.wm_protocol('WM_DELETE_WINDOW', win_is_gone)
    image_preview_win.mainloop()
