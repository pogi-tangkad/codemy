#!/usr/bin/env python3

import os
import sqlite3

def connect_db():
    # Connect to a database named 'customer.db' and/or create the database if it doesn't exist already
    conn = sqlite3.connect('customer.db')
    # Create a cursor to move through database
    c = conn.cursor()
    # Create a table and keys if it doesn't already exist
    c.execute("""CREATE TABLE IF NOT EXISTS customers (
    first_name TEXT,
    last_name TEXT,
    email TEXT DEFAULT 'no email given'
    )""")
    return conn, c

def close_db(conn):
    # Commit the executed commands (maybe not needed? possibly best practice like 'close')
    conn.commit()
    # Close the connection to database (best practice to do so explicitly)
    conn.close()

# Query the DB and show all results in nice table
def show_all():
    os.system('clear')
    conn, c = connect_db()
    # Run the query and build table
    c.execute("SELECT rowid,* FROM customers ORDER BY last_name,first_name")
    items = c.fetchall()
    print(f'\nID\tNAME\t\t\tEMAIL')
    print(f'-----\t------\t\t\t--------')
    for item in items:
        full_name = item[1] + ' ' + item[2]
        if len(full_name) <= 7:
            print(f'{item[0]}\t{full_name}\t\t\t{item[3]}')
        elif len(full_name) <= 14:
            print(f'{item[0]}\t{full_name}\t\t{item[3]}')
        else:
            print(f'{item[0]}\t{full_name}\t{item[3]}')
    close_db(conn)

# Add new record to the DB
def add_one(first, last, email='no email given'):
    conn, c = connect_db()
    c.execute("INSERT INTO customers VALUES(?,?,?)", (first, last, email))
    close_db(conn)

# Delete a single record by 'rowid'
def delete_one():
    show_all()
    conn, c = connect_db()
    id_q = input('\nChoose "ID" to delete:  ')
    c.execute("SELECT rowid FROM customers WHERE rowid=(?)", (id_q,))
    if c.fetchall():
        c.execute("DELETE FROM customers WHERE rowid=(?)", (id_q,))
        conn.commit()
        show_all()
    else:
        print(f'\n!ERROR!:  {id_q} is not a valid selection.')

    close_db(conn)