import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar 
from datetime import datetime

def create_calendar(year):
    cal = Calendar(root, year=year, month=1, day=1, date_pattern="yyyy-mm-dd") 
    cal.pack()

def update_calendar_year(event):
    selected_year = int(year_picker.get())
    cal.destroy()
    create_calendar(selected_year)


root = tk.Tk()
root.title("Date Picker")

# Create a Combobox for year selection
current_year = datetime.now().year
years = [str(year) for year in range(current_year - 25, current_year + 1)]
year_picker = ttk.Combobox(root, values=years)
year_picker.set(current_year)
year_picker.pack()

year_picker.bind("<<ComboboxSelected>>", update_calendar_year)

create_calendar(current_year)  # Initial calendar creation

root.mainloop()
