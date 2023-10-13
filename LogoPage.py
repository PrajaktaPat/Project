from tkinter import ttk
import tkinter as tk
#from tkinter import *
import tkinter.font as tkFont
import mysql.connector
from PIL import ImageTk, Image
win = tk.Tk()
win.title("")
win['background']='white'
win.geometry("800x600")
#widget_object = ttk.Progressbar(container, **options)

image1= Image.open("Accurate Softwares.jpg")
resize_img=image1.resize((800, 300))

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(resize_img)
#image1.resize((50, 50))

# Create a Label Widget to display the text or Image
label = ttk.Label(image = img)
label.place(x = 1,y = 2)

name_label= tk.Label(win,text = "IAS",font='Times 20 bold')
name_label.place(x=350,y=310)
name_label.cget('background')

version_label = ttk.Label(win,text = "version 9.0 Gold",font='Times 10',background='white')
version_label.place(x=320,y=340)

license_label = ttk.Label(win,text = "This Product Licensed To:",font='Times 15',background='white')
license_label .place(x=280,y=360)

Top_label = ttk.Label(win,text = "TOP GEAR TRANSMISSION",font='Times 20 underline',background='white')
Top_label.place(x=250,y=380)

Year = ttk.Label(win,text = "Year Of Finance",font='Times 15 bold',background='white')
Year.place(x=150,y=425)

Year_of_finance = tk.StringVar()
first_combo = ttk.Combobox(win,width = 16,textvariable = Year_of_finance,state = "readonly",background='white')
first_combo["values"] = ("2023","2024")
first_combo.current(0)
first_combo.place(x=280,y=420)


Year_finance = tk.StringVar()
second_combo = ttk.Combobox(win,width = 16,textvariable = Year_finance,state = "readonly",background='white')
second_combo["values"] = ("2024","2025")
second_combo.current(0)
second_combo.place(x=450,y=420)

def action():
    pass



exit_button = ttk.Button(win,text = "Exit",command = action)
exit_button.place(x=400,y=480)

Bottom_label = ttk.Label(win,text = "All rights reserved to Accurate Softwares Kolhapur",font='Times 10 bold',background='white')
Bottom_label.place(x=550,y=550)

Bottom_label1 = ttk.Label(win,text = "Accurate Softwares Kolhapur",font='Times 18 bold',background='white')
Bottom_label1.place(x=10,y=570)

progress = ttk.Progressbar(win, orient = 'horizontal', 
              length = 400, mode = 'determinate') 
  
# Function responsible for the updation 
# of the progress bar value 
def bar(): 
    import time 
    progress['value'] = 10
    win.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 40
    win.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 50
    win.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 60
    win.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 80
    win.update_idletasks() 
    time.sleep(1) 
    progress['value'] = 100
  
progress.place(x=180,y=455)

submit_button = ttk.Button(win,text = "Submit",command = bar)
submit_button.place(x=250,y=480)
# This button will initialize 
# the progress bar 

  

win.mainloop()