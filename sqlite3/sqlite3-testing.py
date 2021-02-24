#!/usr/bin/env python3

import sqlite3

# Connect to a database named 'customer.db' and/or create the database if it doesn't exist already
conn = sqlite3.connect('customer.db')

# Create a cursor to move through database
c = conn.cursor()

# Create a table
''' Data Types:
    NULL    - Does or does not exist
    INTEGER - Whole number
    REAL    - Decimal/Float
    TEXT    - Strings
    BLOB    - As is file (images, music)
'''
c.execute("""CREATE TABLE customers (
    first_name text,
    last_name text,
    email text
    )""")

# Create List of values to put into the Table
many_customers = [
    ('John', 'Elder', 'john@codemy.com'),
    ('Tim', 'Wonky', 'twonk@codemy.com'),
    ('Mary', 'Schmuckenhoffer', 'mary@codemy.com')
    ]

c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# Query the database
c.execute("SELECT first_name FROM customers")
print(c.fetchall())

# A new execute-select needs to be implemented after a fetch
# to move the 'cursor' back to the beginning if needed
c.execute("SELECT * FROM customers")
#print(c.fetchone()[1])
#test_fetch = c.fetchmany(1)
#print(test_fetch)
items = c.fetchall()
#first_names = []
print(f'NAME\t\t\tEMAIL')
print(f'------\t\t\t--------')
for item in items:
    full_name = item[0] + ' ' + item[1]
    if len(full_name) <= 12:
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