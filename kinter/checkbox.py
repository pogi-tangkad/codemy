#!/usr/bin/env python3

from tkinter import Tk, Label, Frame, Button, Menu, PhotoImage, StringVar, Checkbutton

# Create the root window with title and size
root = Tk()
root.title('Pizza Order')
root.geometry('700x400')
root.minsize(width=300, height=300)

# Create window logo
win_icon = PhotoImage(file = "Rlogo.png")
root.iconphoto(False, win_icon)

# Define a menu
my_menu = Menu(root)
root.config(menu=my_menu)
# Create Menu Items
file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='File', menu=file_menu)
#file_menu.add_command(label='New', command=fake_command)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)

# Create Toppings Lists for use in the program
# Use the default list or comment created list and uncomment section to ask for user input
toppings_list = ['Pepperoni', 'Cheese', 'Onion', 'Mushroom', 'Bacon']
# toppings_list = []
# toppings_enter = True
# while toppings_enter:
#     tops = input('Enter topping (blank to finish):  ')
#     if tops == '':
#         break
#     else:
#         toppings_list.append(tops)
toppings_grid_size = len(toppings_list)
toppings_var_list = []
toppings_check_list = []
toppings_label_list = []

# Create a Function for the Show Button that will.....
def show_toppings():
    # First check to see if the button has been pressed already and clear the previous displayed order
    if len(toppings_label_list) > 0:
        clear_toppings(False)
    # Create a list of labels for the Check Boxes and display their values to order along with the Clear Button
    x=0
    for top in toppings_list:
        my_label = Label(root, text=toppings_var_list[x].get())
        my_label.grid(row=toppings_grid_size+x+1, column=0, padx=20, sticky='w')
        toppings_label_list.append(my_label)
        x+=1
    clear_button.grid(row=toppings_grid_size+x+1, column=0, padx=20)

# Create a Function for the Clear Button that will remove the order list and the button itself
def clear_toppings(test):
    for l in toppings_label_list:
        l.grid_forget()
    if test:
        for top in toppings_check_list:
            top.deselect()
    clear_button.grid_forget()

# Create a list of StringVar to use for the Check Boxes
for top in toppings_list:
    top = StringVar()
    toppings_var_list.append(top)

# Create Check Boxes for each toppings using the variable list, deselect them, and store them in another list
x=0
for top in toppings_list:
    topping = Checkbutton(root,
        text=top,
        variable=toppings_var_list[x],
        onvalue=top,
        offvalue=f'No {top}')
    topping.deselect()
    topping.grid(row=x, column=0, padx=20, sticky='w')
    toppings_check_list.append(topping)
    x+=1


# Create Button to show the toppings to order or ignore for the pizza
show_button = Button(root, text='Select Toppings', command=show_toppings)
show_button.grid(row=x, column=0)

# Create a Button that will be used to clear the order, reset the Check Boxes, and clear itself.
clear_button = Button(root, text='Clear toppigns', command=lambda: clear_toppings(True))






root.mainloop()
