import tkinter as tk
from tkinter import ttk, Label
from tkcalendar import Calendar

# Tkinter window settings.
root = tk.Tk()
root.wm_title("Date Difference")
root.resizable(width=False, height=False)
root.geometry("+200+25")

# Declare global variables and initialize them to None.
date1 = date2 = None

# Perform date math on user input and return the difference in days.
# Inform the user if either date is not selected.
def date_math():
    if date1 == None or date2 == None:
        output_label.config(text="Please Select Both Dates")
        return False

    difference = date2 - date1
    
    # Make sure difference has a positive value.
    if difference.days < 0:
        difference *= -1

    output_label.config(text="Days Between Dates: " + str(difference.days))

# Calendar #1 input button pressed.
def input_cal1():
    global date1
    date1 = cal1.selection_get()
    d1.config(text=str(date1))

# Calendar #2 input button pressed.
def input_cal2():
    global date2
    date2 = cal2.selection_get()  
    d2.config(text=str(date2))

# Clear all fields and set date variables to None.
def clear():
    global date1, date2
    date1 = date2 = None
    d1.config(text="No Date Selected")
    d2.config(text="No Date Selected")
    output_label.config(text="Please Select Two Dates")

# Calendar #1 GUI elements.
cal1 = Calendar(root, selectmode='day', locale='en_US', year=2018, month=1, day=1)
cal1.pack()

ttk.Button(root, text="Input First Date", command=input_cal1).pack(pady=(10, 0))

d1 = Label(root, text="No Date Selected")
d1.pack()

# Calendar #2 GUI elements.
cal2 = Calendar(root, selectmode='day', locale='en_US', year=2018, month=1, day=1)
cal2.pack(pady=(10, 0))

ttk.Button(root, text="Input Second Date", command=input_cal2).pack(pady=(10, 0))

d2 = Label(root, text="No Date Selected")
d2.pack()

# Output GUI elements.
ttk.Button(root, text="Display Difference", command=date_math).pack(pady=(10, 0))

output_label = Label(root, text="Please Select Two Dates")
output_label.pack()

# Button to clear all displayed values and set date variables to None.
ttk.Button(root, text="Clear All", command=clear).pack(pady=(10, 10))

# Call the main loop.
root.mainloop()
