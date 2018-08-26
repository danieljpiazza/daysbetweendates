import tkinter as tk
from tkinter import ttk, Label, Entry
from tkcalendar import DateEntry

# Tkinter window settings.
root = tk.Tk()
root.wm_title("Date Math")
root.resizable(width=False, height=False)
root.geometry("225x200+200+25")

# Perform date math on user input and return the difference in days.
def date_math():
    date1 = cal1.get_date()
    date2 = cal2.get_date()
    difference = date2 - date1
    
    # Value of difference should always be positive.
    if difference.days < 0:
        difference *= -1

    # Clear the output field and insert the difference in days.
    # Check for difference.days == 1 for grammar purposes.
    output_entry.delete(0, "end")
    if difference.days == 1:
        output_entry.insert(0, str(difference.days) + " Day")
    else:
        output_entry.insert(0, str(difference.days) + " Days")

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

# Call the main loop.
root.mainloop()
