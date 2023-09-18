from datetime import datetime
from tkinter import *
import tkinter as tk  
from tkcalendar import Calendar
from tkinter import messagebox
from PIL import ImageTk
from tkinter import ttk  
import mysql.connector
import random
import string

mydb = mysql.connector.connect(host='localhost', user='root', password='',database='epiz_32083127_traffic')
cur =  mydb.cursor()
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#Functions
def on_username_enter(event):
    if(username.get() == 'Name'):
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

def get_selected_date():
    year = str(year_picker.get())
    month = month_picker.get()
    mon = str(months.index(month)+1)
    day = str(day_picker.get())
    date = year+"-"+mon+"-"+day
    date_label.config(text=f"Selected Date: {date}")

def get_psd():
    # Define the characters you want to include in the mixture
    characters = string.ascii_letters + string.digits  # includes letters (both cases) and digits
    # Set the length of the random mixture
    mixture_length = 10  # Change this to your desired length
    # Generate the random mixture
    random_mixture = ''.join(random.choice(characters) for _ in range(mixture_length))
    print(random_mixture)
    return random_mixture

def insert_data():
    uname = username.get()
    uemail = useremail.get()
    nplate = numberplate.get()
    uphone = userphone.get()
    uaddress = useraddress.get()
    ublood = userbloodgroup.get()
    year = str(year_picker.get())
    month = month_picker.get()
    mon = str(months.index(month)+1)
    day = str(day_picker.get())
    date = year+"-"+mon+"-"+day
    psd = get_psd()
    # date_label.config(text=f"Selected Date: {date}")

    s = "INSERT INTO users (name, email,password, numberplate, phone, dob, bloodgroup, address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (uname, uemail,psd, nplate, uphone, date, ublood, uaddress) 

    try:
        cur.execute(s, values)
        mydb.commit()
        print("Data inserted successfully!")
        messagebox.showinfo("Alert", "Sign Up Successfull !")
        username.delete(0, END)
        userbloodgroup.delete(0, END)
        userphone.delete(0, END)
        numberplate.delete(0, END)
        useremail.delete(0, END)
        useraddress.delete(0, END)
        year_picker.set(current_year)
        month_picker.set('January')
        day_picker.set('1')


    except Exception as e:
        mydb.rollback()  # Rollback the transaction if there's an error
        print(f"Error inserting data: {str(e)}")
        messagebox.showinfo("Alert", "Sign Up Un Successfull !")

#GUI
root=Tk()
root.geometry('1179x627+35+10')
root.resizable(0,0)
root.title('Sign Up - ADMIN')
bgImage = ImageTk.PhotoImage(file='bg/laptop_bg_try.png')
bglabel = Label(root, image=bgImage)
bglabel.place(x=0, y=0)
heading = Label(root, text='Sign Up By ADMIN', font=('Microsoft Yahei UI Light', 23,'bold'), bg='white', fg='dark orange')
heading.place(x=220, y=90)

userlabel = Label(root, text='Name', font=('Microsoft Yahei UI Light', 13,'bold'),bg='orange', fg='white')
userlabel.place(x=100, y=200)
username = Entry(root, width=30, font=('Microsoft Yahei UI Light', 11,'bold'),bd=0, fg='dark orange')
username.place(x=100, y=240)
username.insert(0, 'Name')
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
current_year = datetime.now().year 

years = [str(year) for year in range(current_year - 65, current_year + 1)]
year_picker = ttk.Combobox(root, values=years)
year_picker.set(current_year)
year_picker.place(x=500, y=320)
# year_picker.bind("<<ComboboxSelected>>", on_userbloodgroup_enter)

month_picker = ttk.Combobox(root, values=months)
month_picker.set('January')
month_picker.place(x=650, y=320)
# month_picker.bind("<<ComboboxSelected>>", on_userbloodgroup_enter)

days = [str(day) for day in range(1, 33)]
day_picker = ttk.Combobox(root, values=days)
day_picker.set('1')
day_picker.place(x=800, y=320)
# day_picker.bind("<<ComboboxSelected>>", on_userbloodgroup_enter)


# Button to get the selected date
get_date_button = tk.Button(root, text="Select This Date", command=get_selected_date)
get_date_button.place(x=500, y=360)
# Label to display the selected date
date_label = tk.Label(root, text="No Date Chosen Yet")
date_label.place(x=600, y=360)

# Button to insert the data
insert_button = tk.Button(root, text="Sign UP", command=insert_data)
insert_button.place(x=500, y=400)

root.mainloop()