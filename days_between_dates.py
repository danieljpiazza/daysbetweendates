import tkinter as tk
from tkinter import ttk, Label, Entry
from tkcalendar import DateEntry

# Tkinter window settings.
root = tk.Tk()
root.wm_title("Date Math")
root.resizable(width=False, height=False)
root.geometry("225x235+200+25")

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

    # Add one day if the user checked "Include End Date In Calculation".
    global check_var
    if check_var.get() == 1:
        final_difference += 1

    # Clear the output field and insert the difference in days.
    # Check for final_difference == 1 for grammar purposes.
    output_entry.delete(0, "end")
    if final_difference == 1:
        output_entry.insert(0, str(final_difference) + " Day")
    else:
        output_entry.insert(0, str(final_difference) + " Days")

# Calendar #1 GUI elements.
ttk.Label(root, text="Choose Date #1").pack(pady=(10, 0))

cal1 = DateEntry(root, selectmode="day", locale="en_US", year=2018, month=1, day=1)
cal1.pack()

# Calendar #2 GUI elements.
ttk.Label(root, text="Choose Date #2").pack(pady=(10, 0))

cal2 = DateEntry(root, selectmode="day", locale="en_US", year=2018, month=1, day=1)
cal2.pack()

# Output GUI elements.
ttk.Button(root, text="Display Difference", command=date_math).pack(pady=(10, 5))

output_entry = Entry(root, width=15, justify="center")
output_entry.pack()

# Clear button for output field.
ttk.Button(root, text="Clear Output",
    command=lambda: output_entry.delete(0, "end")).pack(pady=(11, 0))

# Checkbox to determine if date math should include end date in calculations.
check_var = tk.IntVar()
# Lambda function, called on checkbox status change, calls date_math() with updated logic.
# Only calls date_math() on status change if there is a value in the output_entry field.
check_end_date = tk.Checkbutton(root, text="Include End Date In Calculation", variable=check_var,
    command=lambda: output_entry.get() and date_math())
check_end_date.pack(pady=(10, 0))

# Call the main loop.
root.mainloop()
