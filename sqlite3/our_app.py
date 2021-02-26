#!/usr/bin/env python3

import our_db

# Print nice looking table
our_db.show_all()

# Get new record entry from user
while True:
    q = input('\n\nDo you want to add a new entry?  ')
    if q.lower() in ['n', 'no']:
        break
    elif q.lower() in ['y', 'yes']:
        first = input('\nFirst Name:  ')
        last = input('Last Name:  ')
        email = input('Email Address:  ')
        our_db.add_one(first, last, email)

# Ask user to delete entry
while True:
    q = input('\n\nDo you want to delete an entry?  ')
    if q.lower() in ['n', 'no']:
        break
    elif q.lower() in ['y', 'yes']:
        our_db.delete_one()