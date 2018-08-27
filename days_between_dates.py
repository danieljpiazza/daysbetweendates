from datetime import datetime, date

import tkinter as tk
from tkinter import ttk, Label, Entry, PhotoImage

from tkcalendar import DateEntry

root = tk.Tk()                              # Base Tkinter window.
root.wm_title("")                           # Window title.
root.resizable(width=False, height=False)   # Disable window resize.
root.geometry("+200+25")                    # Initial window position.

# Perform date math on user input and return the difference in days.
def date_math():
    date1 = cal1.get_date()
    date2 = cal2.get_date()
    difference = date2 - date1
    
    # Value of difference should always be positive.
    if difference.days < 0:
        difference *= -1

    # Store read-only difference.days value in another variable.
    final_difference = difference.days

    # Add one day if the user checked "Include End Date".
    global check_var
    if check_var.get() == 1:
        final_difference += 1

    output_entry.configure(state="normal")

    # Clear the output field and insert the difference in days.
    # Check for final_difference == 1 for grammar purposes.
    output_entry.delete(0, "end")
    if final_difference == 1:
        output_entry.insert(0, str(final_difference) + " Day")
    else:
        output_entry.insert(0, str(final_difference) + " Days")

    output_entry.configure(state="readonly")

def clear():
    # Build current date object.
    current_date = date(now.year, now.month, now.day)

    # Set DateEntry objects to the current date.
    cal1.set_date(current_date)  
    cal2.set_date(current_date) 

    # Clear the output_entry field.
    output_entry.configure(state="normal")
    output_entry.delete(0, "end")
    output_entry.configure(state="readonly")

# Get current datetime object.
now = datetime.now()

# Calendar #1 GUI elements.
ttk.Label(root, text="First Date").grid(row=0, column=0, sticky="W", padx=5, pady=5)

cal1 = DateEntry(root, selectmode="day", locale="en_US", year=now.year, month=now.month, day=now.day)
cal1.grid(row=0, column=1, sticky="E", padx=5, pady=5)

# Calendar #2 GUI elements.
ttk.Label(root, text="Second Date").grid(row=1, column=0, sticky="W", padx=5, pady=5)

cal2 = DateEntry(root, selectmode="day", locale="en_US", year=now.year, month=now.month, day=now.day)
cal2.grid(row=1, column=1, sticky="E", padx=5, pady=5)

# Output GUI elements.
ttk.Button(root, text="Calculate", command=date_math).grid(row=2, column=0, sticky="W", padx=5, pady=5)

output_entry = Entry(root, width=15, justify="center", state="readonly")
output_entry.grid(row=2, column=1, sticky="E", padx=5, pady=5)

# Clear button for output field.
ttk.Button(root, text="Reset", command=clear).grid(row=3, column=0, sticky="W", padx=5, pady=5)

# Checkbox to determine if date math should include end date in calculations.
# Lambda function, called on checkbox status change, calls date_math() with updated logic.
# Only calls date_math() on status change if there is a value in the output_entry field.
check_var = tk.IntVar()
check_end_date = tk.Checkbutton(root, text="Include End Date",
    variable=check_var, command=lambda: output_entry.get() and date_math())
check_end_date.grid(row=3, column=1, padx=5, pady=5)

# Call the main loop.
root.mainloop()
