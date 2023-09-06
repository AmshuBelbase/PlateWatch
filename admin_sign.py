from datetime import datetime
from tkinter import *
import tkinter as tk  
from tkcalendar import Calendar
from PIL import ImageTk
from tkinter import ttk  

#Functions
def on_username_enter(event):
    if(username.get() == 'Username'):
        username.delete(0, END)

def on_useraddress_enter(event):
    if(useraddress.get() == 'Address'):
        useraddress.delete(0, END)

def on_useremail_enter(event):
    if(useremail.get() == 'Email'):
        useremail.delete(0, END)
        
def on_numberplate_enter(event):
    if(numberplate.get() == 'Number Plate'):
        numberplate.delete(0, END)

def on_userphone_enter(event):
    if(userphone.get() == 'Phone Number'):
        userphone.delete(0, END)

def on_userbloodgroup_enter(event):
    if(userbloodgroup.get() == 'Blood Group'):
        userbloodgroup.delete(0, END)

def update_calendar_year(event): 
    selected_year = year_picker.get() 
    cal = Calendar(root, year=int(selected_year), month=1, day=1, date_pattern="yyyy-mm-dd")  
    # cal = Calendar(root, year=current_year, month=1, day=1, date_pattern="yyyy-mm-dd") 
    cal.place(x=500, y=320)

def get_selected_date():
    selected_date = cal.get_date()
    date_label.config(text=f"Selected Date: {selected_date}")



#GUI
root=Tk()
root.geometry('1179x627+35+10')
root.resizable(0,0)
root.title('Sign Up - ADMIN')
bgImage = ImageTk.PhotoImage(file='bg/laptop_bg_try.png')
bglabel = Label(root, image=bgImage)
bglabel.place(x=0, y=0)
heading = Label(root, text='Sign Up - ADMIN', font=('Microsoft Yahei UI Light', 23,'bold'), bg='white', fg='dark orange')
heading.place(x=220, y=90)

userlabel = Label(root, text='User Name', font=('Microsoft Yahei UI Light', 13,'bold'),bg='orange', fg='white')
userlabel.place(x=100, y=200)
username = Entry(root, width=30, font=('Microsoft Yahei UI Light', 11,'bold'),bd=0, fg='dark orange')
username.place(x=100, y=240)
username.insert(0, 'Username')
username.bind('<FocusIn>', on_username_enter)

emaillabel = Label(root, text='Email', font=('Microsoft Yahei UI Light', 13,'bold'),bg='orange', fg='white')
emaillabel.place(x=100, y=280)
useremail = Entry(root, width=30, font=('Microsoft Yahei UI Light', 11,'bold'),bd=0, fg='dark orange')
useremail.place(x=100, y=320)
useremail.insert(0, 'Email')
useremail.bind('<FocusIn>', on_useremail_enter)

platelabel = Label(root, text='Number Plate', font=('Microsoft Yahei UI Light', 13,'bold'),bg='orange', fg='white')
platelabel.place(x=100, y=360)
numberplate = Entry(root, width=30, font=('Microsoft Yahei UI Light', 11,'bold'),bd=0, fg='dark orange')
numberplate.place(x=100, y=400)
numberplate.insert(0, 'Number Plate')
numberplate.bind('<FocusIn>', on_numberplate_enter)

phonelabel = Label(root, text='Phone Number', font=('Microsoft Yahei UI Light', 13,'bold'),bg='orange', fg='white')
phonelabel.place(x=100, y=440)
userphone = Entry(root, width=30, font=('Microsoft Yahei UI Light', 11,'bold'),bd=0, fg='dark orange')
userphone.place(x=100, y=480)
userphone.insert(0, 'Phone Number')
userphone.bind('<FocusIn>', on_userphone_enter)

addresslabel = Label(root, text='Address', font=('Microsoft Yahei UI Light', 13,'bold'),bg='orange', fg='white')
addresslabel.place(x=100, y=520)
useraddress = Entry(root, width=30, font=('Microsoft Yahei UI Light', 11,'bold'),bd=0, fg='dark orange')
useraddress.place(x=100, y=560)
useraddress.insert(0, 'Address')
useraddress.bind('<FocusIn>', on_useraddress_enter)

bloodgrouplabel = Label(root, text='Blood Group', font=('Microsoft Yahei UI Light', 13,'bold'),bg='orange', fg='white')
bloodgrouplabel.place(x=500, y=200)
userbloodgroup = Entry(root, width=30, font=('Microsoft Yahei UI Light', 11,'bold'),bd=0, fg='dark orange')
userbloodgroup.place(x=500, y=240)
userbloodgroup.insert(0, 'Blood Group')
userbloodgroup.bind('<FocusIn>', on_userbloodgroup_enter)

doblabel = Label(root, text='Date of Birth', font=('Microsoft Yahei UI Light', 13,'bold'),bg='orange', fg='white')
doblabel.place(x=500, y=280) 
# Create a Calendar widget
current_year = datetime.now().year - 25

cal = Calendar(root, year=2000, month=1, day=1, date_pattern="yyyy-mm-dd")
cal.destroy()
# Button to get the selected date
get_date_button = tk.Button(root, text="Select This Date", command=get_selected_date)
get_date_button.place(x=500, y=510)
# Label to display the selected date
date_label = tk.Label(root, text="No Date Chosen Yet")
date_label.place(x=500, y=550)

years = [str(year) for year in range(current_year - 65, current_year + 1)]
year_picker = ttk.Combobox(root, values=years)
year_picker.set(current_year)
year_picker.pack()
year_picker.bind("<<ComboboxSelected>>", update_calendar_year)



root.mainloop()