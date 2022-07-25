# This is a Database for tracking the Merits that the Adventure Rangers have achieved.

# Here we import our dependencies
import tkinter as tk
from tkinter import *
import sqlite3

# Creating a GUI Window
window = Tk()
window.title("Adventure Ranger Merits")

# Create Database
conn = sqlite3.connect('Adventure_Ranger_Merits.db')

# Create Cursor
c_1 = conn.cursor()

# Create table
'''
c_1.execute("""CREATE TABLE merits (
        first_name text,
        last_name text,
        merit text,
        completed text
         )""")
'''


def save():
    # Connect to Database
    conn = sqlite3.connect('Adventure_Ranger_Merits.db')

    # Create Cursor
    c_1 = conn.cursor()

    record_id = r_delete_box.get()

    #
    c_1.execute("""UPDATE merits SET
        first_name = :first,
        last_name = :last,
        merit = :merit,
        completed = :completed

    WHERE oid = :oid""",
                {'first': f_name_update.get,
                 'last': l_name_update.get,
                 'merit': merit_update.get,
                 'completed': completed_update.get,
                 'oid': record_id
                 })

    # Commit Changes
    conn.commit()

    # Close Database
    conn.close()

    updater.destroy()


# Create Function to update a record
def update():
    global updater
    updater = Tk()
    updater.title('Update a Record')

    # Connect to Database
    conn = sqlite3.connect('Adventure_Ranger_Merits.db')

    # Connect to Cursor
    c_1 = conn.cursor()

    global record_id

    record_id = r_delete_box.get()
    # Delete a record
    c_1.execute("SELECT * FROM merits WHERE oid = " + record_id)
    records = c_1.fetchall()

    # Create Global Variables
    global f_name_update
    global l_name_update
    global merit_update
    global completed_update

    # Create Text Boxes
    f_name_update = Entry(updater, width=30)
    f_name_update.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_update = Entry(updater, width=30)
    l_name_update.grid(row=1, column=1, padx=20)

    merit_update = Entry(updater, width=30)
    merit_update.grid(row=2, column=1, padx=20)

    completed_update = Entry(updater, width=30)
    completed_update.grid(row=3, column=1, padx=20)

    # Loop through Records
    for record in records:
        f_name_update.insert(0, record[0])
        l_name_update.insert(0, record[1])
        merit_update.insert(0, record[2])
        completed_update.insert(0, record[3])

    # Create Text Box Labels
    f_name_update_label = Label(updater, text='First Name')
    f_name_label.grid(row=0, column=0, pady=(10, 0))

    l_name_update_label = Label(updater, text='Last Name')
    l_name_label.grid(row=1, column=0)

    merit_update_label = Label(updater, text='Merit')
    merit_label.grid(row=2, column=0)

    completed_update_label = Label(updater, text='Completed')
    completed_label.grid(row=3, column=0)

    # Create a button to save update to record
    save_btn = Button(updater, text="Save Update", command=save)
    save_btn.grid(row=4, column=0, pady=10, padx=10, ipadx=136)

    # Commit Changes
    conn.commit()

    # Close Database
    conn.close()

    updater.mainloop()


# Create Submit Function
def submit():
    # Connect to Database
    conn = sqlite3.connect('Adventure_Ranger_Merits.db')

    # Create Cursor
    c_1 = conn.cursor()

    # Insert Into Table
    c_1.execute("INSERT INTO merits VALUES (:f_name, :l_name, :merit, :completed)",
                {
                    'f_name': f_name.get(),
                    'l_name': l_name.get(),
                    'merit': merit.get(),
                    'completed': completed.get(),
                })

    # Commit Changes
    conn.commit()

    # Close Database
    conn.close()

    # Clear Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    merit.delete(0, END)
    completed.delete(0, END)


# Delete a Record from the Database
def r_delete():
    # Connect to Database
    conn = sqlite3.connect('Adventure_Ranger_Merits.db')

    # Connect to Cursor
    c_1 = conn.cursor()

    # Delete a record
    c_1.execute("DELETE from merits WHERE oid = " + r_delete_box.get())

    # Commit Changes
    conn.commit()

    # Close Database
    conn.close()


# Create Query Function
def query():
    # Connect to Database
    conn = sqlite3.connect('Adventure_Ranger_Merits.db')

    # Connect to Cursor
    c_1 = conn.cursor()

    # Query Database
    c_1.execute("SELECT *, oid FROM merits")
    records = c_1.fetchall()

    # Loop through Results
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(window, text=print_records)
    query_label.grid(row=10, column=0, columnspan=2)

    # Commit Changes
    conn.commit()

    # Close Database
    conn.close()


# Create Text Boxes
f_name = Entry(window, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(window, width=30)
l_name.grid(row=1, column=1, padx=20)

merit = Entry(window, width=30)
merit.grid(row=2, column=1, padx=20)

completed = Entry(window, width=30)
completed.grid(row=3, column=1, padx=20)

r_delete_box = Entry(window, width=30)
r_delete_box.grid(row=7, column=1, padx=20, pady=5)


# Create Text Box Labels
f_name_label = Label(window, text='First Name')
f_name_label.grid(row=0, column=0, pady=(10, 0))

l_name_label = Label(window, text='Last Name')
l_name_label.grid(row=1, column=0)

merit_label = Label(window, text='Merit')
merit_label.grid(row=2, column=0)

completed_label = Label(window, text='Completed')
completed_label.grid(row=3, column=0)

r_delete_label = Label(window, text='Select ID')
r_delete_label.grid(row=7, column=0, pady=5)


# Create Submit Button
submit_btn = Button(window, text='Add Record To Database', command=submit)
submit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(window, text="Show Records", command=query)
query_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create Delete Button
r_delete_btn = Button(window, text='Delete Record from Database', command=r_delete)
r_delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

# Create Update Button
update_btn = Button(window, text='Update Record from Database', command=update)
update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

# Commit Changes
conn.commit()

# Close Database
conn.close()


# This tells Python to run the Tkinter event loop.
window.mainloop()