# starter code


# import tkinter
# win = tkinter.Tk()

# from tkinter import *
# win = Tk()
from tkinter import ttk
import tkinter as tk
import mysql.connector
win = tk.Tk()
win.title("first gui window")


# ttk.Label(win,text = "enter your name ").pack() pack can also use
# ttk.Label(win,text = "enter your name ").grid(row=0,column=0)

name_label = ttk.Label(win,text = "enter your name ")
name_label.grid(row=0,column=0,sticky = tk.W)

age_lable = ttk.Label(win,text = "enter your age :-")
age_lable.grid(row=1,column=0,sticky=tk.W)

email = ttk.Label(win,text ="enter your email :-")
email.grid(row=2,column=0,sticky=tk.W)

gender_label = ttk.Label(win,text ="select your gender :-")
gender_label.grid(row=3,column=0,sticky=tk.W)

# entry box

name_var = tk.StringVar()
name_entry_box = ttk.Entry(win,width=16,textvariable = name_var)
name_entry_box.grid(row = 0,column = 1)
name_entry_box.focus()

age_var = tk.StringVar()
age_entry_box = ttk.Entry(win,width=16,textvariable = age_var)
age_entry_box.grid(row=1,column = 1)

email_var = tk.StringVar()
email_entry_box = ttk.Entry(win,width=16,foreground = "Red",textvariable = email_var)
email_entry_box.grid(row = 2,column = 1)

# combo box 

gender_var = tk.StringVar()
first_combo = ttk.Combobox(win,width = 16,textvariable = gender_var,state = "readonly")
first_combo["values"] = ("male","female")
first_combo.current(0)
first_combo.grid(row = 3,column = 1)

# radio button how to add radio button
usertype = tk.StringVar()
radio_btn = ttk.Radiobutton(win,text = "student" ,value = "student",variable = usertype)
radio_btn.grid(row = 4,column = 0)

radio_btn = ttk.Radiobutton(win,text = "teacher",value = "teacher",variable = usertype)
radio_btn.grid(row=4,column = 1)

# check button
condition_var = tk.IntVar()
check_btn = ttk.Checkbutton(win,text = "check for latest update ",variable = condition_var)
check_btn.grid(row = 6,column = 0)
# create button

def action():
    username = name_var.get()
    age = age_var.get()
    email = email_var.get()
    user_gender = gender_var.get()
    teacher_or_student = usertype.get()

    if condition_var.get() == 0:
        checked = ("please check the check button")
    else:
    #     checked = ("you have successfully check the check button")
    # print(f"Your name is {username} age is {age} email id is {email}")
    # print(f"your gender is {user_gender} and your are {teacher_or_student}")
    # print(checked)
        conn= mysql.connector.connect(host="localhost",username="root",password="password@123",database="test")
        my_cursor=conn.cursor(buffered=True)
        my_cursor.execute("SHOW TABLES")
        my_cursor.execute("CREATE TABLE IF NOT EXISTS user_data (name VARCHAR(255), age INT,email VARCHAR(255),gender VARCHAR(255),usertype VARCHAR(255))")
            #my_cursor.execute("insert into user_information values(%s,%s,%s,%s,%s)",(name_var.get(),age_var.get(),email_var.get(),gender_var.get(),usertype.get()))
        my_cursor.execute("insert into user_information values(%s,%s,%s,%s,%s)",(name_var.get(),age_var.get(),email_var.get(),gender_var.get(),usertype.get()))
        #print("table already exist")
        #print(my_cursor)
        #my_cursor.execute("CREATE TABLE user_data (name VARCHAR(255), age INT(),email VARCHAR(255),gender VARCHAR(255),usertype VARCHAR(255))")
        #my_cursor.execute("insert into user_data values(%s,%s,%s,%s,%s)",(name_var.get(),age_var.get(),email_var.get(),gender_var.get(),usertype.get()))
        conn.commit()
        conn.close()
        all_detail = (f"Your name is {username}\n Age is {age} \n Email id is {email} \n your gender is {user_gender} \n and your are {teacher_or_student}")
        new_lable =ttk.Label(win,text = all_detail,)
        new_lable.grid(row = 8,column = 0,sticky = tk.W)

submit_button = ttk.Button(win,text = "submit",command = action)
submit_button.grid(row=7,column = 1)


win.mainloop()

# widget ---> label,button,radio button


