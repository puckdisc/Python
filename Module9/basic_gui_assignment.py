import tkinter
"""
Basic GUI Assignment
Creates tkinter object to pick your favorite meal. Contains an exit button and actions when checked
"""


def mmmm():  # changes label when called
    label.config(text="mmmmmmmm")


m = tkinter.Tk()  # m is name of main window object
m.title("Favorite Meal")
label = tkinter.Label(m, text="Waiting...")
label.grid(row=5)

var1 = tkinter.IntVar()  # check boxes are defined for each meal
check = tkinter.Checkbutton(m, text="Breakfast", variable=var1, command=mmmm).grid(row=1)
var2 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Second Breakfast", variable=var2, command=mmmm).grid(row=2)
var3 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Lunch", variable=var3, command=mmmm).grid(row=3)
var4 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Dinner", variable=var4, command=mmmm).grid(row=4)

exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)  # exit button
exit_button.grid(row=6)
m.mainloop()
