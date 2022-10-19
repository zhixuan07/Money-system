
from tkinter.ttk import * 
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox
import datetime
import matplotlib.pyplot as plt
from tkcalendar import DateEntry
from tkinter import filedialog
import pandas as pd
import csv
import os
import re
from tkinter.messagebox import askyesno


# Make a regular expression
# for validating an Email
#Regular Expression, is a sequence of characters that forms a search pattern. 
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

#label style
headlabelfont = ("Helvetica", 12,'bold')
labelfont = ("Helvetica", 12)
entryfont = ('Garamond', 12)

# main window
ws = Tk()
ws.title('Admin')
width= ws.winfo_screenwidth()
height= ws.winfo_screenheight()
ws.geometry("%dx%d" % (width, height))

ws.rowconfigure(0,weight=1)
ws.columnconfigure(0,weight=1)

# Define frame name
loginpage =tk.Frame(ws,bg='#D7F1EE')
homepage = tk.Frame(ws,bg='#D7F1EE')
studentpage = tk.Frame(ws,bg='#D7F1EE')
clubmemberpage = tk.Frame(ws,bg='#D7F1EE')
clubpage = tk.Frame(ws,bg='#D7F1EE')
eventpage = tk.Frame(ws,bg='#D7F1EE')
student_event_page =tk.Frame(ws,bg='#D7F1EE')
club_account_page =tk.Frame(ws,bg='#D7F1EE')

for frame in (loginpage,homepage,studentpage,clubpage,eventpage,clubmemberpage,student_event_page,club_account_page):
    frame.grid(row=0,column=0,sticky='nsew')


def show_frame(frame):
    frame.tkraise()


#Login function 
def login():
            uname = usernameStr.get()
            pwd = passwordStr.get()
            user = user_strvar.get()
            
            conn =sqlite3.connect('club_management.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM admin WHERE username =? AND password =?",[uname,pwd])

            admin_login_list =cursor.fetchall()

            cursor = conn.cursor()
            cursor.execute("SELECT * FROM club_account WHERE account_username =? AND account_password =?",[uname,pwd])
            club_login_list =cursor.fetchall()

       
            if admin_login_list and user =='Admin':
                messagebox.showinfo('Login status','Success')
                show_frame(homepage)
            elif club_login_list and user =='Club President' and uname=='IEC':
                messagebox.showinfo('Login status','Success') 
                ws.destroy()
                os.system('python Invest.py')
            elif club_login_list and user =='Club President' and uname=='IT':
                messagebox.showinfo('Login status','Success') 
                ws.destroy()
                os.system('python IT.py')    
            else:
                messagebox.showerror('Login status','Invalid username and password')   

def show_login_password():
    if(check_password.get()==1):
        passwd.config(show='')
    else:
        passwd.config(show='*')

#Log out
def logout():
    show_frame(loginpage)
    
    messagebox.showinfo('Success','You have log out!')

#=============================================================================Login page===================================================================================================================
#Database
conn = sqlite3.connect('club_management.db')
cursor = conn.cursor()
#Define string variable        
usernameStr =tk.StringVar()
passwordStr=tk.StringVar()
check_password=IntVar(value=0)
user_strvar =tk.StringVar(loginpage,'Admin') 
img_logo =Image.open('logo_inti.png')
img_logo = img_logo.resize((400,50))
img_logo = ImageTk.PhotoImage(img_logo)

#Label , Enrty 
Label(loginpage,bg='#9BCEEC').place(x=0,y=0,relwidth=1,relheight=0.1)
Label(loginpage,image=img_logo,bg='#9BCEEC').place(x=0,y=15)
Label(loginpage,text='STUDENT CLUB MANAGEMENT SYSTEM',font=("Helvetica", 12, 'bold'),bg='#D7F1EE').place(relx=0.4,rely=0.15)
Label(loginpage,text='OF INTI INTERNATIONAL COLLEGE PENANG',font=("Helvetica", 12, 'bold'),bg='#D7F1EE').place(relx=0.4,rely=0.20)

Label(loginpage,text='Username',bg='#D7F1EE',font=labelfont).place(relx=0.4,rely=0.25)
username = Entry(loginpage,width=100,textvariable=usernameStr)
username.place(relx=0.4,rely=0.3,relwidth=0.1)

Label(loginpage,text="Password",bg='#D7F1EE',font=labelfont).place(relx=0.4,rely=0.35)
passwd = Entry(loginpage,width=100,textvariable=passwordStr,show='*')
passwd.place(relx=0.4,rely=0.4,relwidth=0.1)

Checkbutton(loginpage,text='Show Password',variable=check_password,onvalue=1,offvalue=0,command=show_login_password,bg='#D7F1EE').place(relx=0.4,rely=0.45)
Radiobutton(loginpage,text='Admin',value='Admin',variable=user_strvar,bg='#D7F1EE',state=NORMAL).place(relx=0.4,rely=0.5) 
Radiobutton(loginpage,text='Club President',value='Club President',variable=user_strvar,bg='#D7F1EE',state=NORMAL).place(relx=0.5,rely=0.5) 
Button(loginpage,text='Login',command=login,width=10).place(relx=0.42,rely=0.55,relwidth=0.1)     

#=========================================================================Admin home page==============================================================================================
Label(homepage,bg='#9BCEEC').place(x=0,y=0,relwidth=1,relheight=0.1)
Label(homepage,image=img_logo,bg='#9BCEEC').place(x=0,y=15)
Button(homepage,text='Log out',command=logout,width=10,bg='lightgrey').place(x=1200,y=20)
Label(homepage, text="Welcome Admin",font=labelfont,bg='#D7F1EE').place(relx=0.45,rely=0.2)
Button(homepage,text='Student Profiles ',command=lambda:show_frame(studentpage),width=30,bg='#FFFFFF',font=labelfont).place(relx=0.4,rely=0.25)
Button(homepage,text='Club Profiles',command=lambda:show_frame(clubpage),width=30,bg='#FFFFFF',font=labelfont).place(relx=0.4,rely=0.3)
Button(homepage,text='Club Members ',command=lambda:show_frame(clubmemberpage),width=30,bg='#FFFFFF',font=labelfont).place(relx=0.4,rely=0.35)
Button(homepage,text='Completed  Event',command=lambda:show_frame(eventpage),width=30,bg='#FFFFFF',font=labelfont).place(relx=0.4,rely=0.4)
Button(homepage,text='Club accounts',command=lambda:show_frame(club_account_page),width=30,bg='#FFFFFF',font=labelfont).place(relx=0.4,rely=0.45)


#============================================================Student profile page=====================================================================================================

conn.execute(
"CREATE TABLE IF NOT EXISTS student ( STUDENT_ID TEXT PRIMARY KEY , NAME TEXT, EMAIL TEXT, PHONE_NO TEXT, GENDER TEXT, DOB TEXT, PROGRAMME TEXT,  IMAGE BLOB) WITHOUT ROWID;"
)


# convert the image to binary
def convert(filename):
    with open(filename,'rb') as file:
           image =file.read()
    return image

#Clear the current entry fields    
def reset_student_fields():
    
    for i in ['id_strvar','name_strvar', 'email_strvar', 'contact_strvar', 'gender_strvar', 'stream_strvar']:
        exec(f"{i}.set('')")
    dob.set_date(datetime.datetime.now().date())
    try:
        convert(filename)
        b2.config(image='')
    except NameError:
        pass    
  
#Display  and reset the table after CRUD 
def display_student_records():
    
    tree.delete(*tree.get_children())
    curr = conn.execute('SELECT * FROM student')
    data = curr.fetchall()
    for records in data:
        tree.insert('', END, values=records)
 
# Add student inforamtion 
def add_student_record():
   
        id = id_strvar.get().upper()
        name = name_strvar.get().upper()
        email = email_strvar.get().lower()
        contact = contact_strvar.get()
        gender = gender_strvar.get()
        DOB = dob.get_date()
        stream = stream_strvar.get().upper()
        
        student_id_data = conn.execute('SELECT STUDENT_ID FROM student')
        id_list = [x for x, in student_id_data]
        
        # To check whether the Image has upload or not

    
    
        try:
            img = convert(filename)
            
        except NameError:   
            messagebox.showerror('Error','Please insert profile image')            
            # Data validation 
        if not id or not name or not email or not contact or not gender or not DOB or not stream:
                messagebox.showerror('Error!', "Please fill all the missing fields!!")
        elif len(id) !=9:
                messagebox.showerror('Error','The Student ID is incorrect format')   
        elif len(contact) <10 or len(contact) > 11 :
                messagebox.showerror('Error','The length of contact must be 10 or 11 numbers!')    
        elif contact.isdecimal() == False:
                messagebox.showerror('Error','The phone number must be integer')
        elif not re.fullmatch(regex, email) :
                messagebox.showerror('Error','Invalid email')
                    
        elif id  in id_list:
                messagebox.showerror('Error','The student ID already in database')   

            
        else:
                    #Insert the data to database    
                    conn.execute(
                                'INSERT INTO student (STUDENT_ID,NAME, EMAIL, PHONE_NO, GENDER, DOB, PROGRAMME,IMAGE) VALUES (?,?,?,?,?,?,?,?)', (id,name, email, contact, gender, DOB, stream,img)
                                )
                    conn.commit()
                    messagebox.showinfo('Record added', f"Record of {name} was successfully added")
                    
                    reset_student_fields()
                    display_student_records()
        

#Remove the student record     
def remove_student_record():
    #Select from the table 
   if not tree.selection():
        messagebox.showerror('Error!', 'Please select a record from the table')
   else:
     answer = askyesno(title='confirmation',
            message='Are you sure that you want to delete')
     if answer:
       current_item = tree.focus()
       values = tree.item(current_item)
       tree.delete(current_item)
       conn.execute('DELETE FROM student WHERE STUDENT_ID=?' , (id_strvar.get(),))
       conn.commit()
       messagebox.showinfo('Done', 'The record you wanted deleted was successfully deleted.')
       reset_student_fields()


def view_student_record(e):

   global id_strvar,name_strvar, email_strvar, contact_strvar, gender_strvar, dob, stream_strvar,club_strvar
   current_item = tree.focus()
   values = tree.item(current_item)
   selection = values["values"]

   date = datetime.date(int(selection[5][:4]), int(selection[5][5:7]), int(selection[5][8:]))
   id_strvar.set(selection[0]);name_strvar.set(selection[1]); email_strvar.set(selection[2])
   contact_strvar.set(selection[3]); gender_strvar.set(selection[4])
   dob.set_date(date); stream_strvar.set(selection[6])
   
 

#Update student record
def update_student():

   
    
    id = id_strvar.get().upper()
    name = name_strvar.get().upper()
    email = email_strvar.get().lower()
    contact = contact_strvar.get()
    gender = gender_strvar.get()
    DOB = dob.get_date()
    stream = stream_strvar.get().upper()

    conn=sqlite3.connect('club_management.db')
    cursor = conn.cursor()
    if not tree.selection():
        messagebox.showerror('Please select a record from the table')
    else:
        try:
            img = convert(filename)
            cursor.execute('UPDATE student SET IMAGE =? WHERE STUDENT_ID =?',(img,id_strvar.get().upper()))
            conn.commit()
            b2.config(image='')
    
        except NameError:
            pass
            
        if not id or not name or not email or not contact or not gender or not DOB or not stream:
                messagebox.showerror('Error!', "Please fill all the missing fields!!")
        elif len(id) !=9:
                messagebox.showerror('Error','The Student ID is incorrect format')   
        elif len(contact) <10 or len(contact) > 11 :
                messagebox.showerror('Error','The length of contact must be 10 or 11 numbers!')    
        elif contact.isdecimal() == False:
                messagebox.showerror('Error','The phone number must be integer')
        elif not re.fullmatch(regex, email) :
                messagebox.showerror('Error','Invalid email')
        else:            

            
                cursor.execute('''UPDATE student SET NAME = ?, EMAIL= ?, PHONE_NO =?, GENDER = ?,DOB = ?, PROGRAMME =? WHERE STUDENT_ID = ?''',(name_strvar.get().upper(),email_strvar.get(),contact_strvar.get(),gender_strvar.get(),dob.get_date(),stream_strvar.get().upper(),id_strvar.get().upper())
                            )
                            
                conn.commit()
                reset_student_fields()
                messagebox.showinfo("Success",'The record have been updated!')
    
#search function
def search():
    
    conn=sqlite3.connect('club_management.db')
    cursor = conn.cursor()
    

    values1 = search_by_strvar.get()
    values2 = search_strvar.get()

    if values1 == 'NAME':
        
        cursor.execute('SELECT * FROM student WHERE NAME LIKE ? ' ,(values2,))
        data = cursor.fetchall()

        if len(data)!=0:
              tree.delete(*tree.get_children())
              for records in data:
                  tree.insert('', END, values=records)
              conn.commit()
        else:
            messagebox.showerror('Error','The record is not found!')     

    elif values1=='STUDENT_ID':  

        cursor.execute('SELECT * FROM student WHERE STUDENT_ID LIKE ?',(values2,))
        data = cursor.fetchall()
        
        if len(data)!=0:
              tree.delete(*tree.get_children())
              for records in data:
                  tree.insert('', END, values=records)
              conn.commit()
        else:
            messagebox.showerror('Error','The record is not found!')  

    
    
    elif values1=='PROGRAMME':  

        cursor.execute('SELECT * FROM student WHERE PROGRAMME LIKE ?',(values2,))
        data = cursor.fetchall()
        
        if len(data)!=0:
              tree.delete(*tree.get_children())
              for records in data:
                  tree.insert('', END, values=records)
              conn.commit()
        else:
            messagebox.showerror('Error','The record is not found!')  

    else:
        values2 ==''
        messagebox.showerror('Error','Please fill up the field')
        

# Upload and display the image on the field     
def upload_file():
    global img
    global filename
    global b2
    f_types = [('Jpg Files', '*.jpg'),('Jpeg Files','.*jpeg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img=Image.open(filename)
    img_resized=img.resize((100,100)) # new width & height
    img=ImageTk.PhotoImage(img_resized)
    b2 =Label(student_left_frame,image=img) 
    b2.place(relx=0.2,rely=0.8)    


def download_student_image():
    if not tree.selection():
        messagebox.showerror('Error','Please select a record from table')
    else:    
       
        conn = sqlite3.connect('club_management.db')
        curr = conn.execute('SELECT IMAGE FROM student WHERE STUDENT_ID=?',(id_strvar.get(),))
        result =curr.fetchall()
   
        for i in result: 
            try:
               for j in i:
                img=j[0]
            except TypeError:
                messagebox.showerror('Error','The file is not found')
                break
            img=i[0]
            file_name = filedialog.asksaveasfilename(initialdir=os.getcwd(),defaultextension=".png",title='Save Image',filetypes=(('PNG File','*.png'),('JPG File','*.jpg'),('JPEG File','*jpeg'),('All Files','*.*')))    
            writeTofile(img,file_name)
            messagebox.showinfo('Success','The image has been exported to '+ os.path.basename(file_name) +' successfully.')  





# Creating the background and foreground color variables
lf_bg = '#C2E3DE' # bg color for the left_frame
cf_bg = '#9BCEEC' # bg color for the center_frame

# Creating the StringVar or IntVar variables
id_strvar =StringVar()    
name_strvar = StringVar()
email_strvar = StringVar()
contact_strvar = StringVar()
gender_strvar = StringVar()
stream_strvar = StringVar()
club_strvar = StringVar()
search_strvar = StringVar()
search_by_strvar =StringVar()
file_strvar = StringVar()
img_strvar =StringVar()

program_list = ['BMCUH','BCTCU','BCSCU','CIT','DEC','DEEI','DIB','DMEN','DCS','DITN','DMC']

# Placing the components in the main window
Label(studentpage, text="CLUB MANAGEMENT SYSTEM", font=headlabelfont, bg=cf_bg,height=10).pack(side=TOP, fill=X)
student_left_frame = Frame(studentpage, bg=lf_bg,highlightbackground='black',highlightthickness=1)
student_left_frame.place(x=0, y=30, relheight=1, relwidth=0.2)
student_center_frame = Frame(studentpage, bg=lf_bg,highlightbackground='black',highlightthickness=1)
student_center_frame.place(relx=0.2, y=30, relheight=1, relwidth=0.2)
student_right_frame = Frame(studentpage, bg="Gray35")
student_right_frame.place(relx=0.4, y=30, relheight=1, relwidth=0.6)


#Placing the component in the top frame
Button(studentpage,command=lambda:show_frame(homepage),text='Home',width=10).place(x=60,y=4)
Button(studentpage, text='Refresh',command=display_student_records,width=10).place(x=160,y=4)


 # Placing components in the left frame
Label(student_left_frame, text="Student's Information", font=headlabelfont, bg=lf_bg).place(relx=0.1, rely=0.01) 
Label(student_left_frame, text="Student ID", font=labelfont, bg=lf_bg).place(relx=0.1, rely=0.05)
Label(student_left_frame, text="Student Name", font=labelfont, bg=lf_bg).place(relx=0.1, rely=0.14)
Label(student_left_frame, text="Contact Number", font=labelfont, bg=lf_bg).place(relx=0.1, rely=0.24)
Label(student_left_frame, text="Email Address", font=labelfont, bg=lf_bg).place(relx=0.1, rely=0.34)
Label(student_left_frame, text="Gender", font=labelfont, bg=lf_bg).place(relx=0.1, rely=0.44)
Label(student_left_frame, text="Date of Birth (DOB)", font=labelfont, bg=lf_bg).place(relx=0.11, rely=0.54)
Label(student_left_frame, text="Programme", font=labelfont, bg=lf_bg).place(relx=0.1, rely=0.64)
Label(student_left_frame,text='Upload profile picture',font=labelfont,bg=lf_bg).place(relx=0.1,rely=0.74)

Entry(student_left_frame, width=19, textvariable= id_strvar, font=entryfont).place(relx=0.1, rely=0.1)
Entry(student_left_frame, width=19, textvariable=name_strvar, font=entryfont).place(relx=0.1, rely=0.2)
Entry(student_left_frame, width=19, textvariable=contact_strvar, font=entryfont).place(relx=0.1, rely=0.3)
Entry(student_left_frame, width=19, textvariable=email_strvar, font=entryfont).place(relx=0.1, rely=0.4)
OptionMenu(student_left_frame, gender_strvar, 'Male', "Female").place(relx=0.1, rely=0.5, relwidth=0.5)
dob = DateEntry(student_left_frame, font=("Arial", 12), width=15)
dob.place(relx=0.1, rely=0.6)
stream=Combobox(student_left_frame, width=19, textvariable=stream_strvar, state='readonly',values=program_list).place(relx=0.1, rely=0.7)
b1 = tk.Button(student_left_frame, text='Upload Image', 
   width=10,command = lambda:upload_file())
b1.place(relx=0.63,rely=0.8)

# Placing components in the center frame 
Label(student_center_frame,text='Search By',font=labelfont,bg=lf_bg).place(relx=0.1, rely=0.01)
search_combo=Combobox(student_center_frame,state='readonly',textvariable=search_by_strvar)
search_combo['values']=('NAME','STUDENT_ID','PROGRAMME')
search_combo.current(0)
search_combo.place(relx=0.1,rely=0.05)
Button(student_center_frame,text='Search',width=10,command=search).place(relx=0.67,rely=0.1)
Entry(student_center_frame,width=19,textvariable=search_strvar).place(relx=0.1,rely=0.1)
Button(student_center_frame, text='Download Image', font=labelfont, command=download_student_image, width=19).place(relx=0.1, rely=0.2)
Button(student_center_frame, text='Delete Student', font=labelfont, command=remove_student_record, width=19).place(relx=0.1, rely=0.25)
Button(student_center_frame, text='Reset Fields', font=labelfont, command=reset_student_fields, width=19).place(relx=0.1, rely=0.3)
Button(student_center_frame, text='Update Student', font=labelfont,command=update_student, width=19).place(relx=0.1, rely=0.35)
Button(student_center_frame, text=' Add Student', font=labelfont, command=add_student_record, width=19).place(relx=0.1, rely=0.4)


# Placing components in the right frame
Label(student_right_frame, text='Students Profile Record', font=headlabelfont, bg='DarkGreen', fg='LightCyan').pack(side=TOP, fill=X)
tree = Treeview(student_right_frame, height=100, selectmode=BROWSE,
                        columns=('Student ID', "Name", "Email Address", "Contact Number", "Gender", "Date of Birth", "Programme"   ))
X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)
X_scroller.pack(side=BOTTOM, fill=X)
Y_scroller.pack(side=RIGHT, fill=Y)
tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
tree.heading('Student ID', text='ID', anchor=CENTER)
tree.heading('Name', text='Name', anchor=CENTER)
tree.heading('Email Address', text='Email Address', anchor=CENTER)
tree.heading('Contact Number', text='Phone No', anchor=CENTER)
tree.heading('Gender', text='Gender', anchor=CENTER)
tree.heading('Date of Birth', text='DOB', anchor=CENTER)
tree.heading('Programme', text='Programme', anchor=CENTER)


tree.column('#0', width=10, stretch=NO,anchor=CENTER)
tree.column('#1', width=70, stretch=NO,anchor=CENTER)
tree.column('#2', width=100, stretch=NO,anchor=CENTER)
tree.column('#3', width=150, stretch=NO,anchor=CENTER)
tree.column('#4', width=80, stretch=NO,anchor=CENTER)
tree.column('#5', width=80, stretch=NO,anchor=CENTER)
tree.column('#6', width=80, stretch=NO,anchor=CENTER)
tree.column('#7',width=80,stretch=NO,anchor=CENTER)


tree.place(y=30, relwidth=1, relheight=0.9, relx=0)
display_student_records()


#=========================================================================Club member list============================================================================================== 
conn.execute(
"""CREATE TABLE IF NOT EXISTS club_member ( STUDENT_ID TEXT , STUDENT_NAME TEXT, CLUB TEXT,ROLE TEXT)
                                              WITHOUT ROWID;"""
)

    
    

def reset_member_fields():
   
   for i in ['search_by_club_strvar', 'search_by_role_strvar','search_program']:
       exec(f"{i}.set('')")
   

def display_member_records():
    
    tree4.delete(*tree4.get_children())
    curr = conn.execute('''SELECT c.STUDENT_ID , c.STUDENT_NAME,c.CLUB, c.ROLE, s.PROGRAMME
                            FROM club_member c, student s
                            WHERE c.STUDENT_ID = s.STUDENT_ID''')
    data = curr.fetchall()
    for records in data:
        tree4.insert('', END, values=records)
    club_data = cursor.execute('SELECT CLUB_NAME FROM club')
    club_list = [x for x, in club_data]
    

    club =  Combobox(member_center_frame,state='readonly',textvariable = search_by_club_strvar, value= club_list)
    club.place(relx=0.1,rely=0.25)

def search_member():
    
    conn=sqlite3.connect('club_management.db')
    cursor = conn.cursor()
    club =search_by_club_strvar.get()
    role = search_by_role_strvar.get()
    program =search_program.get()
    if club != '' and role == '' and program== "":
        cursor.execute('''SELECT c.STUDENT_ID , c.STUDENT_NAME,c.CLUB,c.ROLE, s.PROGRAMME
                            FROM club_member c, student s
                            WHERE c.STUDENT_ID = s.STUDENT_ID AND c.CLUB =? ''',( search_by_club_strvar.get(),))
        data = cursor.fetchall()
        
        if len(data)!=0:
              tree4.delete(*tree4.get_children())
              for records in data:
                  tree4.insert('', END, values=records)
              conn.commit()
        else:
            messagebox.showerror('Error','The record is not found!')  

    elif role != '' and club == '' and program == "":
        data= cursor.execute('''SELECT c.STUDENT_ID , c.STUDENT_NAME,c.CLUB,c.ROLE, s.PROGRAMME
                            FROM club_member c, student s
                            WHERE c.STUDENT_ID = s.STUDENT_ID AND c.ROLE =? ''',( search_by_role_strvar.get(),))
        data = data.fetchall()
        
        if len(data)!=0:
              tree4.delete(*tree4.get_children())
              for records in data:
                  tree4.insert('', END, values=records)
              conn.commit()
        else:
            messagebox.showerror('Error','The record is not found! ')

    elif program != '' and role == '' and club == '':
        program = cursor.execute('''SELECT c.STUDENT_ID , c.STUDENT_NAME,c.CLUB,c.ROLE, s.PROGRAMME
                            FROM club_member c, student s
                            WHERE c.STUDENT_ID = s.STUDENT_ID AND s.PROGRAMME =? ''',( search_program.get(),))
        data = program.fetchall()
        
        if len(data)!=0:
              tree4.delete(*tree4.get_children())
              for records in data:
                  tree4.insert('', END, values=records)
              
        else:
            messagebox.showerror('Error','The record is not found! ')              
    else:
        messagebox.showerror('Error','Please select one field only')

        
def create_member_csv():
    conn=sqlite3.connect('club_management.db')
    curr=conn.execute('''SELECT c.STUDENT_ID , c.STUDENT_NAME,c.CLUB, c.ROLE, s.PROGRAMME
                            FROM club_member c, student s
                            WHERE c.STUDENT_ID = s.STUDENT_ID''')
    result = curr.fetchall()
    
    filename = filedialog.asksaveasfilename(initialdir=os.getcwd(),defaultextension=".csv",title='Save csv',filetypes=(('CSV File','*.csv'),('All Files','*.*')))
    with open(filename,'a') as f:
         w =csv.writer(f,delimiter=',')
         for i in result:
            w.writerow(i)
    messagebox.showinfo('Success','The file has been exported to'+os.path.basename(filename)+'successfully.')        

programme_data = cursor.execute('SELECT programme_id FROM programme')
programme_list = [x for x in programme_data]


role_list=['MEMBER','COMMITTEE']


# Creating the StringVar or IntVar variables

search_by_club_strvar =StringVar()
search_by_role_strvar =StringVar()
search_program = StringVar()
program_list = ['BMCUH','BCTCU','BCSCU','CIT','DEC','DEEI','DIB','DMEN','DCS','DITN','DMC']
# Placing the components in the main window
Label(clubmemberpage, text="CLUB MANAGEMENT SYSTEM", font=headlabelfont, bg=cf_bg,height=10).pack(side=TOP, fill=X)
member_center_frame = Frame(clubmemberpage, bg=lf_bg,highlightbackground='black',highlightthickness=1)
member_center_frame.place(x=0, y=30, relheight=1, relwidth=0.4)
member_right_frame = Frame(clubmemberpage, bg="Gray35")
member_right_frame.place(relx=0.4, y=30, relheight=1, relwidth=0.6)

#Placing the component in the top frame
Button(clubmemberpage,command=lambda:show_frame(homepage),text='Home',width=10,font=labelfont).place(x=60,y=4)
Button(clubmemberpage, text='Refresh',command=display_member_records,width=10,font=labelfont).place(x=160,y=4)

# Placing components in the center frame 

Label(member_center_frame,text='Search by role',font=labelfont, bg=lf_bg).place(relx=0.1,rely=0.1)
role = Combobox(member_center_frame,state='readonly',textvariable = search_by_role_strvar, value= role_list)
role.place(relx=0.1,rely=0.15)
Label(member_center_frame,text='Search by club',font=labelfont, bg=lf_bg).place(relx=0.1,rely=0.2)

Label(member_center_frame,text='Search by program',font=labelfont, bg=lf_bg).place(relx=0.1,rely=0.3)
program =  Combobox(member_center_frame,state='readonly',textvariable = search_program , value= program_list )
program.place(relx=0.1,rely=0.35)

Button(member_center_frame,text='Search',font=labelfont,width=15,command=search_member).place(relx=0.1,rely=0.4)
Button(member_center_frame, text='Reset', font=labelfont,command=reset_member_fields, width=15).place(relx=0.1, rely=0.45)
Button(member_center_frame, text='Export ', font=labelfont,command=create_member_csv, width=15).place(relx=0.1, rely=0.5)





# Placing components in the right frame
Label(member_right_frame, text='Club member Records', font=headlabelfont, bg='DarkGreen', fg='LightCyan').pack(side=TOP, fill=X)
tree4 = Treeview(member_right_frame, height=100, selectmode=BROWSE,
                        columns=('Student ID', "Student Name","Club",'Role','Programme' ))

X_scroller = Scrollbar(tree4, orient=HORIZONTAL, command=tree.xview)
Y_scroller = Scrollbar(tree4, orient=VERTICAL, command=tree.yview)
X_scroller.pack(side=BOTTOM, fill=X)
Y_scroller.pack(side=RIGHT, fill=Y)
tree4.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
tree4.heading('Student ID', text='Student ID', anchor=CENTER)
tree4.heading('Student Name', text='Student Name', anchor=CENTER)
tree4.heading('Club', text='Club', anchor=CENTER)
tree4.heading('Role', text='Role', anchor=CENTER)
tree4.heading('Programme', text='Programme', anchor=CENTER)

tree4.column('#0', width=10, stretch=NO,anchor=CENTER)
tree4.column('#1', width=70, stretch=NO,anchor=CENTER)
tree4.column('#2', width=100, stretch=NO,anchor=CENTER)
tree4.column('#3', width=80, stretch=NO,anchor=CENTER)
tree4.column('#4', width=60, stretch=NO,anchor=CENTER)
tree4.column('#5', width=60, stretch=NO,anchor=CENTER)

tree4.place(y=30, relwidth=1, relheight=0.9, relx=0)
display_member_records()



#============================================================================Club Profile page========================================================================================
cursor.execute(
"CREATE TABLE IF NOT EXISTS club (CLUB_ID INTEGER PRIMARY KEY AUTOINCREMENT, CLUB_NAME TEXT , CLUB_PRESIDENT TEXT, CLUB_DESCRIPTION TEXT, CLUB_USERNAME TEXT,CLUB_CONTACT TEXT,ADVISOR TEXT, FILE BLOB) "
)
# Reset Entry Fields
def reset_club_fields():
  
   for i in ['club_name_strvar', 'club_president_strvar','club_description_strvar', 'club_contact_strvar','club_id_strvar','advisor_strvar','club_email_strvar']:
       exec(f"{i}.set('')")

#Dipslay the data to the table
def display_club_records():
   
    tree2.delete(*tree2.get_children())
    curr = conn.execute('SELECT * FROM club')
    data = curr.fetchall()
    for records in data:
        tree2.insert('', END, values=records)
    club_data = cursor.execute('SELECT CLUB_NAME FROM club')
    club_list = [x for x, in club_data]       
    Combobox(club_center_frame, state='readonly', textvariable=search_club,value=club_list).place(relx=0.1,rely=0.1)

# Add the club
def add_club_record():
    

    club_name = club_name_strvar.get().upper()
    club_description = club_description_strvar.get()
    club_contact = club_contact_strvar.get()
    club_president =club_president_strvar.get().upper()
    club_email = club_email_strvar.get().lower()
    advisor = advisor_strvar.get()
    club_data=conn.execute('SELECT CLUB_NAME FROM club')
    club_name_current_list = [x for x,in club_data]

    student_name_data = conn.execute('SELECT NAME FROM student')
    name_list = [x for x, in student_name_data]
    
    

    # Data validation
    if not club_name or  not club_contact or not club_description or not club_president or not club_email or not advisor :
        messagebox.showerror('Error!', "Please fill all the missing fields!!")
    elif club_name in club_name_current_list:
            messagebox.showerror('Error!','The club name have exists!')
       
    elif len(club_contact) < 10 or len(club_contact) > 11:
        messagebox.showerror('Error','The length of of contact number is incorrect!')    
    elif club_contact.isnumeric()==  False:
        messagebox.showerror('Error','The phone number must be integer!')
    elif club_president not in name_list:
        messagebox.showerror('Error','The president do not exist in college')    
    elif not re.fullmatch(regex, club_email) :
        messagebox.showerror('Error','Invalid email')    

    else:

            conn.execute(
            'INSERT INTO club (CLUB_NAME, CLUB_DESCRIPTION,CLUB_EMAIL,CLUB_CONTACT,CLUB_PRESIDENT,ADVISOR) VALUES (?,?,?,?,?,?)', (club_name, club_description,club_email,club_contact,club_president,advisor)
            )
            conn.commit()
            messagebox.showinfo('Record added', f"Record of {club_name} was successfully added")
            reset_club_fields()
            display_club_records()
     
            
            
# Remove the club
def remove_club_record():

   if not tree2.selection():
       messagebox.showerror('Error!', 'Please select a record from the table')
   else:
    # Select the one row of the table
       answer = askyesno(title='confirmation',
            message='Are you sure that you want to delete')
       if answer:
        current_item = tree2.focus()
        values = tree2.item(current_item)
        selection = values["values"]
        tree2.delete(current_item)
        conn.execute('DELETE FROM club WHERE CLUB_ID=%d' % selection[0])
        conn.commit()
        messagebox.showinfo('Done', 'The record you wanted deleted was successfully deleted.')
        display_club_records()
        reset_club_fields()

def view_club_record(e):

   #Auto fill in the data into entry fields after selecting the row 
   current_item = tree2.focus()
   values = tree2.item(current_item)
   selection = values["values"]

   club_id_strvar.set(selection[0]);club_name_strvar.set(selection[1]); club_description_strvar.set(selection[2]); club_email_strvar.set(selection[3])
   club_president_strvar.set(selection[4]); club_contact_strvar.set(selection[5])
   advisor_strvar.set(selection[6])

# Update the club record
def update_club_record():
 
    club_contact = club_contact_strvar.get()
    
    if not tree2.selection():
        messagebox.showerror('Error','Please select a record from the table')
    elif not club_name_strvar.get() or  not club_contact_strvar.get() or not club_description_strvar.get() or not club_president_strvar.get() or not club_email_strvar.get() or not advisor_strvar.get():
        messagebox.showerror('Error!', "Please fill all the missing fields!!")

    elif len(club_contact_strvar.get()) < 10 or len(club_contact_strvar.get()) > 11:
        messagebox.showerror('Error','The length of of contact number is incorrect!')  

    elif club_contact.isnumeric()==  False:
        messagebox.showerror('Error','The phone number must be integer!')

    else:    
        conn=sqlite3.connect('club_management.db')
        cursor = conn.cursor()
    
        cursor.execute('''UPDATE club SET CLUB_NAME=?,CLUB_DESCRIPTION=? ,CLUB_EMAIL=?,CLUB_PRESIDENT=?,CLUB_CONTACT=?,ADVISOR =? WHERE CLUB_ID = ?'''
                    ,(club_name_strvar.get(),club_description_strvar.get(),club_email_strvar.get(),club_president_strvar.get(),club_contact_strvar.get(),advisor_strvar.get(),club_id_strvar.get()))                          
                    
                                                
        conn.commit()
        
        reset_club_fields()
        
        messagebox.showinfo("Success",'The record have been updated!')
# Search the club by keyword
def search_club_record():
    if search_club.get()=='':
        messagebox.showerror('Error','Please select club')
    else:   
        cursor.execute('SELECT * FROM club WHERE CLUB_NAME =?',(search_club.get(),))  
        data = cursor.fetchall()

        if len(data)!=0:
            tree2.delete(*tree2.get_children())
            for records in data:
                tree2.insert('',END,values=records)
            conn.commit()
                  
        else:
            messagebox.showerror('Error','The record is not found! ')        

# Dwonload the file
def download_club_file():

    #Select from the table 
   if not tree2.selection():
        messagebox.showerror('Error!', 'Please select a record from the table')
   else:
       
      
       conn = sqlite3.connect('club_management.db')
       curr= conn.execute('SELECT FILE FROM club WHERE CLUB_ID=?' , (club_id_strvar.get(),))
       result =curr.fetchall()
   
       for i in result: 
            try:
               for j in i:
                file=j[0]
            except TypeError:
                messagebox.showerror('Error','The file is not found !')
                break
            file=i[0]
            file_name = filedialog.asksaveasfilename(initialdir=os.getcwd(),defaultextension=".pdf",title='Save File',filetypes=(('PDF File','*.pdf'),('All Files','*.*')))    
            writeTofile(file,file_name)
            messagebox.showinfo('Success','The file has been exported to ' + os.path.basename(file_name)+ ' successfully.')  
 
# Show graph
def show_member_graph():
    cursor.execute('''SELECT cm.CLUB ,COUNT(cm.STUDENT_NAME) as 'Number of Member'
                        FROM club_member cm
                        GROUP BY cm.CLUB ''')
    member= cursor.fetchall()
    df = pd.DataFrame(member,columns=['Club Name','Number of Member'])
    df.plot(kind='bar',x='Club Name', y='Number of Member')
    plt.xticks(rotation=30, horizontalalignment="center")
    plt.title('Total Member in each Club',fontsize=10)
    plt.xlabel('Club Name')
    plt.ylabel('Number of Member')
    plt.show()

# Creating the StringVar or IntVar variables
club_name_strvar = StringVar()
club_president_strvar =StringVar()
club_contact_strvar = StringVar()
club_description_strvar = StringVar()
club_email_strvar =StringVar()
member_strvar = StringVar()
club_id_strvar =StringVar()
advisor_strvar = StringVar()
search_club = StringVar()
download_zip =StringVar()

# Placing the components in the main window
Label(clubpage,text="CLUB MANAGEMENT SYSTEM", font=headlabelfont, bg=cf_bg,height=10).pack(side=TOP, fill=X)
club_left_frame = tk.Frame(clubpage,bg=lf_bg,highlightbackground='black',highlightthickness=1)
club_left_frame.place(x=0, y=30, relheight=1, relwidth=0.2)
club_center_frame = tk.Frame(clubpage, bg=lf_bg,highlightbackground='black',highlightthickness=1)
club_center_frame.place(relx=0.2, y=30, relheight=1, relwidth=0.2)
club_right_frame = tk.Frame(clubpage, bg="Gray35")
club_right_frame.place(relx=0.4, y=30, relheight=1, relwidth=0.6)
Button(clubpage,command=lambda:show_frame(homepage),text='Home',width=10).place(x=60,y=5)
Button(clubpage, text='Refresh',command=display_club_records,width=10).place(x=160,y=5)

# Placing components in the left frame
Label(club_left_frame,text="Club's Information",font=headlabelfont,bg=lf_bg).place(relx=0.1,rely=0.01)
Label(club_left_frame,text='Club ID',font=labelfont,bg=lf_bg).place(relx=0.1,rely=0.05)
Label(club_left_frame, text="Club Name", font=labelfont, bg=lf_bg).place(relx=0.1, rely=0.15)
Label(club_left_frame, text="Club Description", font=labelfont, bg=lf_bg).place(relx=0.1, rely=0.25)
Label(club_left_frame, text="Email Address", font=labelfont, bg=lf_bg).place(relx=0.1, rely=0.35)
Label(club_left_frame, text="President", font=labelfont, bg=lf_bg).place(relx=0.1, rely=0.45)
Label(club_left_frame, text="President Contact", font=labelfont, bg=lf_bg).place(relx=0.1, rely=0.55)
Label(club_left_frame,text='Main Advisor',font=labelfont,bg=lf_bg).place(relx=0.1,rely=0.65)
Entry(club_left_frame, width=19, textvariable=club_id_strvar, font=entryfont).place(relx=0.1, rely=0.1)
Entry(club_left_frame, width=19, textvariable=club_name_strvar, font=entryfont).place(relx=0.1, rely=0.2)
Entry(club_left_frame, width=19, textvariable=club_description_strvar, font=entryfont).place(relx=0.1, rely=0.3)
Entry(club_left_frame, width=19, textvariable=club_email_strvar, font=entryfont).place(relx=0.1, rely=0.4)
Entry(club_left_frame, width=19, textvariable=club_president_strvar, font=entryfont).place(relx=0.1, rely=0.5)
Entry(club_left_frame, width=19, textvariable=club_contact_strvar, font=entryfont).place(relx=0.1, rely=0.6)
Entry(club_left_frame, width=19,textvariable=advisor_strvar ,font=entryfont).place(relx=0.1, rely=0.7)




# Placing components in the center frame
Label(club_center_frame,text='Search club',font=labelfont, bg=lf_bg ).place(relx=0.1,rely=0.05)

Button(club_center_frame, text='Search',font=labelfont, command=search_club_record,width=19).place(relx=0.1,rely=0.15)
Button(club_center_frame, text='Download File', font=labelfont, command=download_club_file, width=19).place(relx=0.1, rely=0.3)
Button(club_center_frame, text='Add Club', font=labelfont, command=add_club_record, width=19).place(relx=0.1, rely=0.4)
Button(club_center_frame, text='Update Club', font=labelfont, command=update_club_record, width=19).place(relx=0.1, rely=0.45)
Button(club_center_frame, text='Delete Club', font=labelfont, command=remove_club_record, width=19).place(relx=0.1, rely=0.5)
Button(club_center_frame, text='Reset Fields', font=labelfont, command=reset_club_fields, width=19).place(relx=0.1, rely=0.55)
Button(club_center_frame, text='Compare size of all clubs', font=labelfont, command=show_member_graph, width=25).place(relx=0.1, rely=0.6)



# Placing components in the right frame
Label(club_right_frame, text='Club Profile Record', font=headlabelfont, bg='DarkGreen', fg='LightCyan').pack(side=TOP, fill=X)
tree2 = Treeview(club_right_frame, height=100, selectmode=BROWSE,   
                   columns=('Club_ID', "Club_Name", "Club_Description",'Club_email', "President","President_Contact", "Main Advisor"))
X_scroller = Scrollbar(tree2, orient=HORIZONTAL, command=tree2.xview)
Y_scroller = Scrollbar(tree2, orient=VERTICAL, command=tree2.yview)
X_scroller.pack(side=BOTTOM, fill=X)
Y_scroller.pack(side=RIGHT, fill=Y)
tree2.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
tree2.heading('Club_ID', text='ID', anchor=CENTER)
tree2.heading('Club_Name', text='Name', anchor=CENTER)
tree2.heading('Club_Description', text='Description', anchor=CENTER)
tree2.heading('Club_email', text='Email', anchor=CENTER)
tree2.heading('President',text='President',anchor=CENTER)
tree2.heading('President_Contact', text='Phone No', anchor=CENTER)

tree2.heading('Main Advisor', text='Main Advisor', anchor=CENTER)

tree2.column('#0', width=0, stretch=NO)
tree2.column('#1', width=40, stretch=NO)
tree2.column('#2', width=140, stretch=NO)
tree2.column('#3', width=200, stretch=NO)
tree2.column('#4', width=80, stretch=NO)
tree2.column('#5', width=80, stretch=NO)
tree2.column('#6', width=80, stretch=NO)
tree2.column('#7', width=80, stretch=NO)


tree2.place(y=30, relwidth=1, relheight=0.9, relx=0)
display_club_records()


#================================================================================Event Page==============================================================================================
cursor.execute(
"CREATE TABLE IF NOT EXISTS club_event (EVENT_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, EVENT_NAME TEXT, EVENT_DESCRIPTION TEXT,NO_PARTICIPANTS TEXT, NO_GUEST TEXT , START_DATE TEXT, END_DATE TEXT,EVENT_TYPE TEXT,EVENT_RATING INTEGER, CLUB_NAME TEXT,EVENT_PROPOSAL BLOB)"
)

rating = cursor.execute('SELECT* FROM rating')
rating_list = [x for x in rating]

#Write the file to binary data
def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    

# Open and select file     
def open_file():
    global filepath
    global pdf_file
    file_type= [('PDF Files', '*.pdf')]
    filepath = filedialog.askopenfilename(filetype=file_type)
    pdf_file=Label(event_center_frame,text=filepath)
    pdf_file.place(relx=0.1,rely=0.7)
    if filepath is None:
        pass

# Convert data file to binary     
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData
#Reset entry fields
def reset_event_fields():

   for i in ['search_by_organizer','search_by_event_type','search_by_rating','download_id_strvar']:
       exec(f"{i}.set('')")
 
#Display the data in table
def display_club_event_records():
    tree3.delete(*tree3.get_children())
    curr = conn.execute('SELECT * FROM club_event')
    data = curr.fetchall()
    for records in data:
        tree3.insert('', END, values=records)
    club_data = cursor.execute('SELECT CLUB_NAME FROM club')
    club_list = [x for x,in club_data]   
    organizer = Combobox(event_center_frame,state='readonly',textvariable=search_by_organizer,value=club_list)
    organizer.place(relx=0.1,rely=0.15)   

# Search by keyword
def search_event():

    conn=sqlite3.connect('club_management.db')
    cursor = conn.cursor()

    organizer =search_by_organizer.get()
    type =search_by_event_type.get()
    rating = search_by_rating.get()
  
    
    if organizer!= '' and type =='' and rating == '':
        cursor.execute('SELECT * FROM club_event WHERE CLUB_NAME LIKE ? ',(search_by_organizer.get(),))
        data = cursor.fetchall()
    
        if len(data)!=0:
              tree3.delete(*tree3.get_children())
              for records in data:
                  tree3.insert('', END, values=records)
              conn.commit()
        else:
            messagebox.showerror('Error','The record is not found! ')   

    elif type !='' and organizer =='' and rating =='':
        cursor.execute('SELECT * FROM club_event WHERE EVENT_TYPE = ? ',(search_by_event_type.get(),))
        data = cursor.fetchall()
        
        if len(data)!=0:
              tree3.delete(*tree3.get_children())
              for records in data:
                  tree3.insert('', END, values=records)
              conn.commit()
        else:
            messagebox.showerror('Error','The record is not found! ')           

    elif rating != '' and organizer == '' and type == '':
        cursor.execute('SELECT * FROM club_event WHERE EVENT_RATING = ? ',(search_by_rating.get(),))
        data = cursor.fetchall()
        print(rating_list)
        
        if len(data)!=0:
              tree3.delete(*tree3.get_children())
              for records in data:
                  tree3.insert('', END, values=records)
              conn.commit()
        else:
            messagebox.showerror('Error','The record is not found! ')            
    
    else:
        messagebox.showerror('Error','Please select one field only ')

#Downlaod file by selecting the row of table
def download_event_file():

    if not tree3.selection():
        messagebox.showerror('Error','Please select a record from table')
    else:    
        current_item = tree3.focus()
        values = tree3.item(current_item)
        selection = values["values"]
        conn = sqlite3.connect('club_management.db')
        curr = conn.execute('SELECT EVENT_PROPOSAL FROM club_event WHERE EVENT_ID=%d' % selection[0])
        result =curr.fetchall()
   
        for i in result: 
            try:
               for j in i:
                pdf=j[0]
            except TypeError:
                messagebox.showerror('Error','The file is not found!')
                break
            pdf=i[0]
            file_name = filedialog.asksaveasfilename(initialdir=os.getcwd(),defaultextension=".pdf",title='Save PDF',filetypes=(('PDF File','*.pdf'),('All Files','*.*')))    
            writeTofile(pdf,file_name)
            messagebox.showinfo('Success','The file has been exported to '+ os.path.basename(file_name) +' successfully.')  
    
     
def create_event_csv():
    conn=sqlite3.connect('club_management.db')
    curr=conn.execute(''' SELECT * FROM club_event''')
    result = curr.fetchall()
    
    filename = filedialog.asksaveasfilename(initialdir=os.getcwd(),defaultextension=".csv",title='Save csv',filetypes=(('CSV File','*.csv'),('All Files','*.*')))
    with open(filename,'a') as f:
         w =csv.writer(f,delimiter=',')
         for i in result:
            w.writerow(i)
    messagebox.showinfo('Success','The file has been exported to'+os.path.basename(filename)+'successfully.')      
    

search_by_event = tk.StringVar()
search_by_organizer = tk.StringVar()
search_by_event_type =tk.StringVar()
search_by_rating =tk.StringVar()
download_id_strvar =StringVar()

Label(eventpage,text="Organized Event Records", font=headlabelfont, bg=cf_bg,height=10).pack(side=TOP, fill=X)

event_center_frame = tk.Frame(eventpage, bg=lf_bg,highlightbackground='black',highlightthickness=1)
event_center_frame.place(x=0, y=30, relheight=1, relwidth=0.4)
event_right_frame = tk.Frame(eventpage, bg=lf_bg)
event_right_frame.place(relx=0.4, y=30, relheight=1, relwidth=0.6)
Button(eventpage,command=lambda:show_frame(homepage),text='Home',width=10).place(x=60,y=5)
Button(eventpage, text='Refresh',command=display_club_event_records,width=10).place(x=160,y=5)



# Placing components in the center frame
Label(event_center_frame,text='Search by club',font=labelfont, bg=lf_bg).place(relx=0.1,rely=0.1)
Label(event_center_frame,text='Search by type of event',font=labelfont, bg=lf_bg).place(relx=0.1,rely=0.2)
event_type = Combobox(event_center_frame,state='readonly',textvariable=search_by_event_type)
event_type['values'] = ('Activity','Workshop','Seminar','Competition')
event_type.place(relx=0.1,rely=0.25)
Label(event_center_frame,text='Search by rating',font=labelfont, bg=lf_bg).place(relx=0.1,rely=0.3)
rating =  Combobox(event_center_frame,state='readonly',textvariable=search_by_rating,value=rating_list)

rating.place(relx=0.1,rely=0.35)

Button(event_center_frame, text='Search', font=labelfont, command=search_event, width=19).place(relx=0.1, rely=0.4)
Button(event_center_frame, text='Reset Fields', font=labelfont, command=reset_event_fields, width=19).place(relx=0.1, rely=0.65)
Button(event_center_frame, text='Download File', font=labelfont, command=download_event_file, width=19).place(relx=0.1, rely=0.6)
Button(event_center_frame, text='Export', font=labelfont, command= create_event_csv, width=19).place(relx=0.1, rely=0.7)

# Placing components in the right frame
Label(event_right_frame, text='Club Event Records', font=headlabelfont, bg='DarkGreen', fg='LightCyan').pack(side=TOP, fill=X)
tree3 = Treeview(event_right_frame, height=100, selectmode=BROWSE,
                   columns=('Event_ID', "Event_Name", "Event_Description","Organized By", "Number_of_participants", 'Guest',"Start Date", "End Date","Event Type","Event Rating"))
X_scroller = Scrollbar(tree3, orient=HORIZONTAL, command=tree3.xview)
Y_scroller = Scrollbar(tree3, orient=VERTICAL, command=tree3.yview)
X_scroller.pack(side=BOTTOM, fill=X)
Y_scroller.pack(side=RIGHT, fill=Y)
tree3.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
tree3.heading('Event_ID', text='Event_ID', anchor=CENTER)
tree3.heading('Event_Name', text='Event_Name', anchor=CENTER)
tree3.heading('Event_Description', text='Event_Description', anchor=CENTER)
tree3.heading('Organized By', text='Organized By', anchor=CENTER)
tree3.heading('Number_of_participants',text='Number_of_participants',anchor=CENTER)
tree3.heading('Guest',text='Guest',anchor=CENTER)
tree3.heading('Start Date', text='Start Date', anchor=CENTER)
tree3.heading('End Date', text='End Date', anchor=CENTER)
tree3.heading('Event Type', text='Event Type', anchor=CENTER)
tree3.heading('Event Rating', text='Event Rating',anchor=CENTER)

tree3.column('#0', width=0, stretch=NO,anchor=CENTER)
tree3.column('#1', width=50, stretch=NO,anchor=CENTER)
tree3.column('#2', width=100, stretch=NO,anchor=CENTER)
tree3.column('#3', width=100, stretch=NO,anchor=CENTER)
tree3.column('#4', width=80, stretch=NO,anchor=CENTER)
tree3.column('#5', width=80, stretch=NO,anchor=CENTER)
tree3.column('#6', width=80, stretch=NO,anchor=CENTER)
tree3.column('#7', width=80, stretch=NO,anchor=CENTER)
tree3.column('#8', width=100, stretch=NO,anchor=CENTER)
tree3.column('#9', width=40, stretch=NO, anchor=CENTER)

tree3.place(y=30, relwidth=1, relheight=0.9, relx=0)
display_club_event_records()


#========================================================================Student_event_record page=====================================================================================

#============================================================================CLUB ACCOUNT==================================================================================================================
cursor.execute('CREATE TABLE IF NOT EXISTS club_account(account_id INTEGER PRIMARY KEY AUTOINCREMENT ,club_name TEXT,account_user TEXT,account_username TEXT, account_password TEXT) WITHOUT ROWID;') 
#Reset entry fields
def reset_account_fields():
   
   for i in ['account_id','club_account','account_user','account_username','account_password','confirm_account_password']:
       exec(f"{i}.set('')")
   
   

#Auto fill the data to entry fields
def view_account_record(e):
    current_item = tree6.focus()
    values = tree6.item(current_item)
    selection = values['values']
    account_id.set(selection[0]);club_account.set(selection[1]);account_user.set(selection[2])
    account_username.set(selection[3])


# Display the data in table 
def display_account_records():
    global event_list
    tree6.delete(*tree6.get_children())
    curr = conn.execute('SELECT * FROM club_account')
    data = curr.fetchall()
    for records in data:
        tree6.insert('', END, values=records)
    club_data = cursor.execute('SELECT CLUB_NAME FROM club')
    club_list = [x for x ,in club_data]   
    Combobox(account_left_frame,state='readonly',value = club_list,textvariable=club_account).place(relx=0.1,rely=0.2)   
    Combobox(account_center_frame,state='readonly',textvariable= search_account_club,value=club_list).place(relx=0.1,rely=0.1)
# Add account   
def add_account():
    conn = sqlite3.connect('club_management.db')
   

    club = club_account.get()
    user = account_user.get()
    username = account_username.get().upper()
    password1 =account_password.get()
    password2 =confirm_account_password.get()

    club_name = conn.execute('SELECT club_name FROM club_account')
    club_list = [x for x in club_name ]
    #Data validated
    if not club or not user or not username or not password1 or not password2:
        messagebox.showerror('Error','Please fill all the fields')
    elif password1 != password2 and password2!= password1:
        messagebox.showerror('Error',"The password is incorrect")
    elif club in club_list:
        messagebox.showerror('Error','The club account already exist')
    else:
        conn.execute('INSERT INTO club_account(club_name, account_user, account_username, account_password) VALUES (?,?,?,?)',(club,user,username,password1))
        conn.commit()
        messagebox.showinfo('Success',f'The {username} account have successfully created')
        reset_account_fields()
        display_account_records()

def remove_account():
    
   if not tree6.selection():
        messagebox.showerror('Error!', 'Please select a record from the table')
    
   else:
      answer = askyesno(title='confirmation',
            message='Are you sure that you want to delete')
      if answer:
        current_item = tree6.focus()
        values = tree6.item(current_item)
        selection = values["values"]
        tree6.delete(current_item)  
        conn.execute('DELETE FROM club_account WHERE account_id=%d ' % selection[0])
        conn.commit()
        messagebox.showinfo('Done', 'The record you wanted deleted was successfully deleted.')
        reset_account_fields()

def update_account():

    conn=sqlite3.connect('club_management.db')
    cursor =conn.cursor()
    id= account_id.get()
    club = club_account.get()
    user = account_user.get()
    username = account_username.get().upper()
    password1 =account_password.get()
    password2 =confirm_account_password.get()

    current_item = tree6.focus()
    tree6.item(current_item,text='',values =(id,club,user,username,password1,password2))

   
    if not tree6.selection():
        messagebox.showerror('Error','Please select a record from the table')
    elif not club or not user or not username or not password1 or not password2:
        messagebox.showerror('Error',"Please fill all the fields")
    elif  password1 != password2 and password2!= password1:
        messagebox.showerror('Error',"The password is incorrect")
    else:
        conn=sqlite3.connect('club_management.db')
        cursor =conn.cursor()
        cursor.execute('''UPDATE club_account SET club_name =?, account_user =?, account_username =?, account_password=? WHERE account_id =?'''
                        ,(club_account.get(),account_user.get(),account_username.get(),account_password.get(),account_id.get()))
        conn.commit()
        messagebox.showinfo('Done', 'The account was successfully updated.')
        reset_account_fields()


def search_account():
    if search_account_club.get()=="":
        messagebox.showerror('Error','Please select the club')
    else:
        cursor.execute('SELECT * FROM club_account WHERE club_name =?',(search_account_club.get(),))  
        data = cursor.fetchall()

        if len(data)!=0:
            tree6.delete(*tree6.get_children())
            for records in data:
                tree6.insert('',END,values=records)
            conn.commit()
                  
        else:
            messagebox.showerror('Error','The record is not found! ')       

def show_account_password():
    if(check_account_password.get()==1):
        password.config(show='')
        confirm_password.config(show='')
    else:
        password.config(show='*')
        confirm_password.config(show='*')

# Creating the background and foreground color variables

# Creating the StringVar or IntVar variables
account_id =StringVar()
club_account = StringVar()
account_user = StringVar()
account_username = StringVar()
account_password = StringVar()
confirm_account_password = StringVar()
search_account_club =StringVar()
check_account_password =IntVar(value=0)
username_list=['IT','IEC']

# Placing the components in the main window
Label(club_account_page, text="CLUB MANAGEMENT SYSTEM", font=headlabelfont, bg=cf_bg,height=10).pack(side=TOP, fill=X)
account_left_frame = Frame(club_account_page, bg=lf_bg,highlightbackground='black',highlightthickness=1)
account_left_frame.place(x=0, y=30, relheight=1, relwidth=0.2)
account_center_frame = Frame(club_account_page, bg=lf_bg,highlightbackground='black',highlightthickness=1)
account_center_frame.place(relx=0.2, y=30, relheight=1, relwidth=0.2)
account_right_frame = Frame(club_account_page, bg="Gray35")
account_right_frame.place(relx=0.4, y=30, relheight=1, relwidth=0.6)

#Placing the component in the top frame
Button(club_account_page,command=lambda:show_frame(homepage),text='Home',width=10).place(x=60,y=4)
Button(club_account_page, text='Refresh',command=display_account_records,width=10).place(x=160,y=4)


 # Placing components in the left frame
Label(account_left_frame,text='Account Information',font=headlabelfont, bg=lf_bg).place(relx=0.1,rely=0.0)
Label(account_left_frame,text='Account ID',font=labelfont, bg=lf_bg).place(relx=0.1,rely=0.05)
Entry(account_left_frame,width=19,textvariable=account_id).place(relx=0.1,rely=0.1)
Label(account_left_frame,text='Club Name',font=labelfont, bg=lf_bg).place(relx=0.1,rely=0.15)

Label(account_left_frame,text='Account User',font=labelfont, bg=lf_bg).place(relx=0.1,rely=0.25)
Entry(account_left_frame,width=19, font = entryfont,textvariable=account_user).place(relx=0.1,rely=0.3)
Label(account_left_frame,text='Account Username',font=labelfont, bg=lf_bg).place(relx=0.1,rely=0.35)
Combobox(account_left_frame,width=19, state='readonly',textvariable=account_username,values=username_list).place(relx=0.1,rely=0.4)
Label(account_left_frame,text='Account Password',font=labelfont, bg=lf_bg).place(relx=0.1,rely=0.45)
password=Entry(account_left_frame,width=19, font = entryfont,show='*',textvariable=account_password)
password.place(relx=0.1,rely=0.5)
Label(account_left_frame,text='Confirm Account Password',font=labelfont, bg=lf_bg).place(relx=0.1,rely=0.55)
confirm_password=Entry(account_left_frame,width=19, font = entryfont,show='*',textvariable=confirm_account_password)
confirm_password.place(relx=0.1,rely=0.6)
Checkbutton(account_left_frame,text='Show Password',variable=check_account_password,onvalue=1,offvalue=0,command=show_account_password,bg=lf_bg).place(relx=0.1,rely=0.65)

# Placing components in the center frame 
Label(account_center_frame,text='Search Account',font=labelfont, bg=lf_bg).place(relx=0.1,rely=0.05)

Button(account_center_frame,text='Search',font=labelfont,command=search_account,width=19).place(relx=0.1,rely=0.15)
Button(account_center_frame, text='Add Club Account', font=labelfont, command=add_account, width=19).place(relx=0.1, rely=0.45)
Button(account_center_frame, text='Update Club Account', font=labelfont, command=update_account, width=19).place(relx=0.1, rely=0.5)
Button(account_center_frame, text='Delete Club Account', font=labelfont, command=remove_account, width=19).place(relx=0.1, rely=0.55)
Button(account_center_frame, text='Reset Fields', font=labelfont, command=reset_account_fields, width=19).place(relx=0.1, rely=0.6)



# Placing components in the right frame
Label(account_right_frame, text='Club account Records', font=headlabelfont, bg='DarkGreen', fg='LightCyan').pack(side=TOP, fill=X)
tree6 = Treeview(account_right_frame, height=100, selectmode=BROWSE,
                        columns=("Account ID","Club Name",'Account User', "Account Username"  ))
X_scroller = Scrollbar(tree6, orient=HORIZONTAL, command=tree.xview)
Y_scroller = Scrollbar(tree6, orient=VERTICAL, command=tree.yview)
X_scroller.pack(side=BOTTOM, fill=X)
Y_scroller.pack(side=RIGHT, fill=Y)
tree6.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
tree6.heading('Account ID', text='Account ID', anchor=CENTER)
tree6.heading('Club Name', text='Club Name', anchor=CENTER)
tree6.heading('Account User', text='Account User', anchor=CENTER)
tree6.heading('Account Username', text='Account Username', anchor=CENTER)

tree6.column('#0', width=10, stretch=NO,anchor=CENTER)
tree6.column('#1', width=70, stretch=NO,anchor=CENTER)
tree6.column('#2', width=100, stretch=NO,anchor=CENTER)
tree6.column('#3', width=60, stretch=NO,anchor=CENTER)
tree6.column('#4', width=60, stretch=NO,anchor=CENTER)


tree6.place(y=30, relwidth=1, relheight=0.9, relx=0)
display_account_records()


show_frame(loginpage)

tree.bind("<ButtonRelease-1>", view_student_record)
tree2.bind("<ButtonRelease-1>", view_club_record)
tree6.bind("<ButtonRelease-1>", view_account_record)



ws.update()
ws.mainloop()   