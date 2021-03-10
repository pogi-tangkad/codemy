#!/usr/bin/env python3

import os
import our_db

# Print nice looking table
def nice_table():
    our_db.show_all()

# Get new record entry from user
def single_entry():
    os.system('clear')
    while True:
        q = input('\n\nDo you want to add a new entry?(y/n)  ')
        if q.lower() in ['n', 'no']:
            break
        elif q.lower() in ['y', 'yes']:
            first = input('\nFirst Name:  ')
            last = input('Last Name:  ')
            if (email := input('Email Address:  ')) != '':
                our_db.add_one(first, last, email)
            else:
                our_db.add_one(first, last)

# Ask user to delete entry
def single_delete():
    os.system('clear')
    while True:
        q = input('\n\nDo you want to delete an entry?(y/n)  ')
        if q.lower() in ['n', 'no']:
            break
        elif q.lower() in ['y', 'yes']:
            our_db.delete_one()

while True:
    os.system('clear')

    print("""
    CUSTOMER DATABASE APP
    ------------------------------
    What would you like to do

    1. Show Table
    2. Add single entry
    3. Delete single entry

    4. Quit App
    """)

    if (q := input(':  ')) in ['1', '2', '3', '4']:
        if q == '1':
            nice_table()
            input('\nPress "Enter" key to continue')
        elif q == '2':
            single_entry()
        elif q == '3':
            single_delete()
        elif q == '4':
            break
