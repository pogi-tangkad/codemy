#!/usr/bin/env python3

import sqlite3

# Connect to a database named 'customer.db' and/or create the database if it doesn't exist already
conn = sqlite3.connect('customer.db')

# Create a cursor to move through database
c = conn.cursor()

# Remove existing table to keep using same .py file
c.execute("DROP TABLE IF EXISTS customers")

# Create a table with a default value set for email
''' Data Types:
    NULL    - Does or does not exist
    INTEGER - Whole number
    REAL    - Decimal/Float
    TEXT    - Strings
    BLOB    - As is file (images, music)
'''
c.execute("""CREATE TABLE customers (
    first_name TEXT,
    last_name TEXT,
    email TEXT DEFAULT 'no email given'
    )""")

conn.commit()

# Create List of values to put into the Table via executemany
many_customers = [
    ('John', 'Elder', 'john@codemy.com'),
    ('Tim', 'Winky', 'twink@codemy.com'),
    ('Mary', 'Schmuckenhoffer', 'mary@codemy.com'),
    ('Darryl', 'Funbags', 'dbag@yabbadabba.com'),
    ('Betty', 'Elder', 'betty@someplace.com'),
    ('Paula', 'Poundstone', 'poundstone@retroencabulator.com'),
    ('Fuh', 'Kyu', 'kyu@yabbadabba.com')
    ]

c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)
conn.commit()

# Change the first_name of one of the entries matching a last_name value
c.execute(""" UPDATE customers SET first_name = 'Lin'
            WHERE last_name = 'Kyu'
    """)
conn.commit()

# Insert a single entry making sure to use the DEFAULT value for email
c.execute("INSERT INTO customers (first_name, last_name) VALUES ('Mark', 'Elberg')")
conn.commit()

# Delete a single entry using 'rowid'
c.execute("DELETE FROM customers WHERE rowid=2")
conn.commit()

# Query the database
#c.execute("SELECT first_name FROM customers")
#print(c.fetchall())

# A new execute-select needs to be implemented after a fetch
# to move the 'cursor' back to the beginning if needed
# Now adding a sort using multi-level 'ORDER BY'
c.execute("SELECT * FROM customers ORDER BY last_name,first_name")
#print(c.fetchone()[1])
#test_fetch = c.fetchmany(1)
#print(test_fetch)
#c.execute("SELECT * FROM customers WHERE last_name LIKE 'El%' ")
items = c.fetchall()
#first_names = []
print(f'\nNAME\t\t\tEMAIL')
print(f'------\t\t\t--------')
for item in items:
    full_name = item[0] + ' ' + item[1]
    if len(full_name) <= 7:
        print(f'{full_name}\t\t\t{item[2]}')
    elif len(full_name) <= 14:
        print(f'{full_name}\t\t{item[2]}')
    else:
        print(f'{full_name}\t{item[2]}')
#    first_names.append(item[0])
#print(first_names)





'''
I am assuming that the following 'commit' and 'close' are going to be necessary
when using sqlite3 within another program where the main program will still be
running after we are done with the database.
'''
# Commit the executed commands (maybe not needed? possibly best practice like 'close')
conn.commit()

# Close the connection to database (best practice to do so explicitly)
conn.close()