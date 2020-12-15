import tkinter as tk
from Topic_2_Connecting_to_Database import db_methods as dbm


m = tk.Tk()  # m is name of main window object
m.title("Database GUI")
database = "pythonsqlite.db"
conn = dbm.create_connection(database)


operate_text = tk.Label(m, text="Welcome to Database GUI.").grid(row=0, columnspan=4)
create_button = tk.Button(m, text="Create Database & Table", command=lambda: dbm.create_tables(database)).grid(row=1)
add_person_button = tk.Button(m, text="Add Person", command=lambda: add_person()).grid(row=2)
add_student_button = tk.Button(m, text="Add Student", command=lambda: add_student()).grid(row=3)
view_person_table_button = tk.Button(m, text="View Person Table", command=lambda: view_person_table(conn)).grid(row=4)
view_student_table_button = tk.Button(m, text="View Student Table", command=lambda: view_student_table(conn)).grid(row=5)




fname = tk.StringVar()
add_fname_input = tk.Entry(m, textvariable=fname).grid(row=1, column=3)
add_fname_label = tk.Label(m, text="First Name:", justify='right').grid(row=1, column=2)

lname = tk.StringVar()
add_lname_input = tk.Entry(m, textvariable=lname).grid(row=2, column=3)
add_lname_label = tk.Label(m, text="Last Name:", justify='right').grid(row=2, column=2)

major = tk.StringVar()
add_major_input = tk.Entry(m, textvariable=major).grid(row=3, column=3)
add_major_label = tk.Label(m, text="Major:", justify='right').grid(row=3, column=2)

start = tk.StringVar()
add_start_input = tk.Entry(m, textvariable=start).grid(row=4, column=3)
add_start_label = tk.Label(m, text="Start Date:", justify='right').grid(row=4, column=2)

exit_button = tk.Button(m, text='Exit', command=m.destroy)  # exit button
exit_button.grid(row=6)


def add_person():
    first = fname.get().replace(" ", "")
    if fname == '':
        raise ValueError('first name empty')
    last = lname.get().replace(" ", "")
    if lname == '':
        raise ValueError('last name empty')
    person = (str(first), str(last))
    dbm.create_person(conn, person)
    # print("{:} {:}".format(first, last))


def add_student():
    first = fname.get().replace(" ", "")
    if fname == '':
        raise ValueError('first name empty')
    last = lname.get().replace(" ", "")
    if lname == '':
        raise ValueError('last name empty')
    maj = major.get().rstrip()
    if maj == '':
        raise ValueError('major is empty')
    start_date = start.get().replace(" ", "")
    if start_date == '':
        raise ValueError('major is empty')
    person = (str(first), str(last))
    person_id = dbm.create_person(conn, person)
    student = (person_id, str(maj), str(start_date))
    dbm.create_student(conn, student)
    # print("{:} {:} {:} {:}".format(first, last, maj, start_date))


def view_person_table(conn):
    row = 6
    table = dbm.select_all_persons(conn)
    for a, *b in table:
        row += 1
        tk.Label(m, text=(a,b)).grid(row=row, columnspan=4)


def view_student_table(conn):
    row = 6
    table = dbm.select_all_students(conn)
    for a in table:
        row += 1
        tk.Label(m, text=(a)).grid(row=row, columnspan=4)






m.mainloop()

if __name__ == "__main__":
    pass
