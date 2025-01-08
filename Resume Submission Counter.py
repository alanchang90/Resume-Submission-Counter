import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Create the main window
root = tk.Tk()
root.title("Resume Submission Counter")

# Initialize the counter and default date
counter = 0
selected_date = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))

# Update the counter display
def update_label():
    counter_label.config(text=f"Count: {counter}\nDate: {selected_date.get()}")

# Button functions
def increase():
    global counter
    counter += 1
    update_label()

def decrease():
    global counter
    if counter > 0:  # Prevent negative counts
        counter -= 1
    update_label()

def done():
    global counter
    counter = 0
    update_label()
    messagebox.showinfo("Good Luck", "Good luck today and go out and do some exercise!")

# Create widgets
# Date selection
date_label = tk.Label(root, text="Select Date (YYYY-MM-DD):", font=("Arial", 14))
date_label.pack(pady=5)

date_entry = tk.Entry(root, textvariable=selected_date, font=("Arial", 14))
date_entry.pack(pady=5)

# Counter label
counter_label = tk.Label(root, text=f"Count: {counter}\nDate: {selected_date.get()}", font=("Arial", 18))
counter_label.pack(pady=20)

# Buttons
increase_button = tk.Button(root, text="Increase (+)", font=("Arial", 14), command=increase)
increase_button.pack(pady=5)

decrease_button = tk.Button(root, text="Decrease (-)", font=("Arial", 14), command=decrease)
decrease_button.pack(pady=5)

done_button = tk.Button(root, text="Done", font=("Arial", 14), command=done)
done_button.pack(pady=5)

# Run the main loop
root.mainloop()
