from email import message
from multiprocessing.forkserver import SIGNED_STRUCT
from pickle import FRAME
from tkinter.ttk import * 
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image  # pip install pillow
from PIL.ImageTk import PhotoImage
import tkinter.messagebox
from tkinter import ttk
import tkinter.messagebox as mb
import sqlite3
from tkinter.messagebox import askyesno
from tkcalendar import DateEntry
import os
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import pandas as pd
import numpy as np
import re
from forex_python.converter import CurrencyRates
import customtkinter
# Make a regular expression
# for validating an Email
#Regular Expression, is a sequence of characters that forms a search pattern. 
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'




labelfont=("yu gothic ui",14)
entryfont=("yu gothic ui",10)
btnfont=('yu gothic ui',12)
headfont=('yu gothic ui',14,'bold')

class windows(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Test Application")
        self.wm_title("Test Application")
        #self.width= self.winfo_screenwidth()
        #self.height= self.winfo_screenheight()
        
        self.geometry("1780x1000")
        #self.resizable(0,0)
        #Creating the sharing variables across classes
        self.shared_email={'signUp_email':StringVar(),'Login_email':StringVar(),'resetpass_email':StringVar()}

        # creating a frame and assigning it to container
        container = Frame(self, height='1000', width='1780')
        # specifying the region where the frame is packed in root
        container.place(x=0, y=0)

        # configuring the location of the container using grid
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (AccountPage,SecurityQuestion,ResetPass,LoginForm,SignupWin,AnswerSQWin,Homepage,ResetWin,TransactionTable,ValidEmail):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(SecurityQuestion)

    def show_frame(self, cont):
            frame = self.frames[cont]
            # raises the current frame to the top
            frame.tkraise()
            
    def saveChange(self):
        mb.showinfo('Success','WELL DONE')

    def changePassword(self):
        mb.showinfo('Success','WELL DONE')

class LoginForm(Frame):
    def __init__(self, window,controller):
        self.controller=controller
        self.hide_button = None       
        self.login_password=StringVar()
        self.show_pass=IntVar(value=0)
        def login(self):

            email = self.controller.shared_email['Login_email'].get()
            self.password = self.login_password.get()

            conn = sqlite3.connect('money.db')
            cursor = conn.cursor()
            cursor.execute("SELECT Email,Password FROM account WHERE Email =? AND Password =?", (email,self.password))
            user_login_list = cursor.fetchall()

            if not email or not self.password:
                mb.showerror('Error','Please fill all the field')
    
            elif user_login_list:
                mb.showinfo('Success',"Successfully login. ")
                
                controller.show_frame(Homepage)   
            else:
                tkinter.messagebox.showerror("Error",'Invalid username and password')

       
        def show_pass(self):
            # ================= Login Frame =================
            if (self.show_pass.get()==1):
                self.pss_entry.config(show='*')
            else:
                self.pss_entry.config(show='')

        Frame.__init__(self, window)
        self.lgn_frame = Frame(self, bg='#FFFFFF', width='1780', height='1000')  # Color and the size of the frame
        self.lgn_frame.place(x=0, y=0)  # Placement of the frame
        self.lgn_frame.pack()

        self.frame1 = Frame(self, bg='#7FFFD4', width='700', height='1000')
        self.frame1.place(x=0, y=0)

        # =============user icon===================
        self.username_icon = Image.open('images/user.jpeg')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#2B1B17')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=950, y=175)
        # ================= Username =================
        self.email_label = Label(self.lgn_frame, text='Email', bg='#FFFFFF', font=('yu gothic ui', 13, 'bold'),
                                 fg='#000000')
        self.email_label.place(x=900, y=425)
        self.email_icon = Image.open('images/UsernameBar.jpg')
        photo = ImageTk.PhotoImage(self.email_icon)
        self.email_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.email_icon_label.image = photo
        self.email_icon_label.place(x=905, y=450)
        self.email_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#FFFFFF', fg='#000000',
                                 font=('yu gothic ui', 13, 'bold'), textvariable=self.controller.shared_email['Login_email'])
        self.email_entry.place(x=912, y=457, width=270)

        # ================= Password =================
        self.pss_label = Label(self.lgn_frame, text='Password', bg='#FFFFFF', font=('yu gothic ui', 13, 'bold'),
                               fg='#000000')
        self.pss_label.place(x=900, y=505)
        self.pss_icon = Image.open('images/UsernameBar.jpg')
        photo = ImageTk.PhotoImage(self.email_icon)
        self.pss_icon_label = Label(self.lgn_frame,image=photo,bg='#FFFFFF')
        self.pss_icon_label.image = photo
        self.pss_icon_label.place(x=905, y=540)
        self.pss_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#FFFFFF', fg='#000000',
                               font=('yu gothic ui', 13, 'bold'), textvariable=self.login_password,show='*')
        self.pss_entry.place(x=912, y=547, width=270)
        
        self.eye_icon = Image.open('images/eye.jpeg')
        eye = ImageTk.PhotoImage(self.eye_icon)
        self.show_pass_label = Checkbutton(self.lgn_frame,image = eye,onvalue=1,offvalue=0,variable=self.show_pass, bg='#FFFFFF')
        self.show_pass_label.image = eye
        self.show_pass_label.place(x=1200,y=545)
        self.show_pass_label.bind('<Button-1>',lambda e: show_pass(self))
        # ===========Forgot password=================
        self.forgot = customtkinter.CTkButton(self.lgn_frame,text='Forgot Password?', width=100,
                    fg_color='#FFFFFF', hover_color="#D9D9D9" ,cursor='hand2',command=lambda :self.controller.show_frame(ValidEmail),)
        self.forgot.place(x=890, y=595)

        # ===========Login Button==========
        
      
        self.login = customtkinter.CTkButton(self.lgn_frame, text='Login',text_font=('yu gothic ui',13),
                            width=100,height=40, border_width=1, command=lambda :login(self),
                            fg_color='#FFFFFF', hover_color='#F2F2F2' ,cursor='hand2')
        self.login.place(relx=0.52, rely=0.7)
        # ==========Sign Up===================
        
        self.login = customtkinter.CTkButton(self.lgn_frame, text='Sign Up', text_font=('yu gothic ui', 13),
                            width=100,height=40, border_width=1, command=lambda: controller.show_frame(SignupWin),
                            fg_color='#FFFFFF',hover_color='#F2F2F2', cursor='hand2' )
        self.login.place(relx=0.64,rely=0.7)
    
class SignupWin(Frame):
    
    def __init__(self, window,controller):
        Frame.__init__(self, window)
        self.hide_button = None
        self.controller = controller
       
        #=================================
        #self.Sign_Email = StringVar()
        self.Name =StringVar()
        self.Password =StringVar()
        self.Cpass = StringVar()
        self.Sign = StringVar()
       


        #============ Insert Data ============
        def addData(self):
            con = sqlite3.connect('money.db')
            self.email = self.controller.shared_email['signUp_email'].get()

            if not self.Name.get() or not self.email or not self.Password.get() :
                mb.showerror("Error", "Enter All Details")
            elif self.Password.get() != self.Cpass.get() and self.Cpass.get() != self.Password.get():
                mb.showerror("Please confirm your password")
            elif not re.fullmatch(regex, self.email) :
                mb.showerror('Error','Invalid email format')
            else:

                cursor = con.cursor()
                cursor.execute("INSERT INTO account (Name,Email,Password) VALUES(?,?,?)",(self.Name.get(),self.email, self.Password.get(), ))
                con.commit()
                mb.showinfo('Success','Sign Up successfully')
                # bring user to answer security question
                controller.show_frame(SecurityQuestion)
         
        

       


        # ================= Sign up Frame =================
        self.lgn_frame = Frame(self, bg='#FFFFFF', width='2200', height='1000')  # Color and the size of the frame
        self.lgn_frame.pack()  # Placement of the frame
        #============== Title ===========================
        self.password_label = Label(self.lgn_frame, text='Sign Up Here', bg='#FFFFFF', font=('yu gothic ui', 28, 'bold'),
                                    fg='#000000')
        self.password_label.place(x=745, y=75)

        #===============Name====================
        self.name_label = Label(self.lgn_frame, text='Name', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
                                 fg='#000000')
        self.name_label.place(x=700, y=175)
        self.name_icon = Image.open('images/UsernameBar.jpg')
        photo = ImageTk.PhotoImage(self.name_icon)
        self.name_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.name_icon_label.image = photo
        self.name_icon_label.place(x=700, y=215)
        self.name_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#FFFFFF', fg='#000000',
                                 font=('yu gothic ui', 13, 'bold'), textvariable=self.Name)
        self.name_entry.place(x=705, y=225, width=270)
        #========== Email =================
        self.email_label = Label(self.lgn_frame, text='Email', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
                                 fg='#000000')
        self.email_label.place(x=700, y=275)
        self.email_icon = Image.open('images/UsernameBar.jpg')
        photo = ImageTk.PhotoImage(self.email_icon)
        self.email_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.email_icon_label.image = photo
        self.email_icon_label.place(x=700, y=315)
        self.email_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#FFFFFF', fg='#000000',
                                 font=('yu gothic ui', 13, 'bold'), textvariable=self.controller.shared_email['signUp_email'])
        self.email_entry.place(x=705, y=325, width=270)
        #============ Password ===========
        self.pass_label = Label(self.lgn_frame, text='Password', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
                                 fg='#000000')
        self.pass_label.place(x=700, y=375)
        self.pass_icon = Image.open('images/UsernameBar.jpg')
        photo = ImageTk.PhotoImage(self.email_icon)
        self.pass_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.pass_icon_label.image = photo
        self.pass_icon_label.place(x=700, y=415)
        self.pass_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#FFFFFF', fg='#000000',
                                 font=('yu gothic ui', 13, 'bold'), textvariable=self.Password,show='*')
        self.pass_entry.place(x=705, y=425, width=270)

        #========== Confirm password ===============
        self.cpass_label = Label(self.lgn_frame, text='Confirm-Password', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
                                fg='#000000')
        self.cpass_label.place(x=700, y=475)
        self.cpass_icon = Image.open('images/UsernameBar.jpg')
        photo = ImageTk.PhotoImage(self.email_icon)
        self.cpass_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.cpass_icon_label.image = photo
        self.cpass_icon_label.place(x=700, y=515)
        self.cpass_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#FFFFFF', fg='#000000',
                                font=('yu gothic ui', 13, 'bold'), textvariable=self.Cpass,show='*')
        self.cpass_entry.place(x=705, y=525, width=270)

        #===========Sign up button=================
       
       
        self.sign = customtkinter.CTkButton(self.lgn_frame, text='Sign Up', text_font=('yu gothic ui',10),
                           border_width=1, width=150,height=30, fg_color='#FFFFFF',hover_color='#F2F2F2',command=lambda:addData(self))
        self.sign.place(x=770, y=625)
        
class AnswerSQWin(Frame):
    def __init__(self, window,controller):
        self.controller=controller
        Frame.__init__(self, window)
        self.hide_button = None

        # self.state('zoomed')  # Maximizing the page
        def valid_answer(self):
            conn = sqlite3.connect('money.db')
            cursor = conn.cursor()
            if self.controller.shared_email['resetpass_email'].get():
                cursor.execute('SELECT * FROM Security_Question WHERE Email =? AND Questions=? AND Answer= ?',(self.controller.shared_email['resetpass_email'].get(),self.SQuestion.get(),self.ans.get()))
                data = cursor.fetchall()
                print(data)
                if data:
                    mb.showinfo('Success','Answered Correctly')
                    self.controller.show_frame(ResetPass)
                else:
                    mb.showerror('Error','Please try again')    
            elif self.controller.shared_email['Login_email'].get():
                cursor.execute('SELECT * FROM Security_Question WHERE Email =? AND Questions=? AND Answer= ?',(self.controller.shared_email['Login_email'].get(),self.SQuestion.get(),self.ans.get()))
                data = cursor.fetchall()
                print(data)
                if data:
                    mb.showinfo('Success','Answered Correctly')
                    self.controller.show_frame(ResetPass)
                else:
                    mb.showerror('Error','Please try again')

        # =================================
        self.SQuestion = StringVar()
        self.ans = StringVar()
        #======================================
       
        # ================= Sign up Frame =================
        self.lgn_frame = Frame(self, bg='#FFFFFF', width='2300', height='1000')  # Color and the size of the frame
        self.lgn_frame.pack()  # Placement of the frame
        # ============== Title ===========================
        self.SQ_label = Label(self.lgn_frame, text='Select Security Question', bg='#FFFFFF',
                                    font=('yu gothic ui', 32, 'bold'),
                                    fg='#000000')
        self.SQ_label.place(x=715, y=55)
        # ========== Select Question =================
        self.SQ_label = Label(self.lgn_frame, text='Choose here', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
                                 fg='#000000')
        self.SQ_label.place(x=700, y=175)
        self.cboSQ = ttk.Combobox(self.lgn_frame, font=('arial', 12, 'bold'), width=42, state='readonly',
                                  textvariable=self.SQuestion)
        self.cboSQ['values'] = ('Where do you live?', 'What is your primary school?', 'What is your father name?')
        self.cboSQ.current(0)
        self.cboSQ.place(x=740,y=210)

        #========== Answer ===========
        self.ans_icon = Image.open('images/14.jpg')
        photo = ImageTk.PhotoImage(self.ans_icon)
        self.ans_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.ans_icon_label.image = photo
        self.ans_icon_label.place(x=770, y=300)
        self.ans_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#FFFFFF', fg='#000000',
                                    font=('yu gothic ui', 13, 'bold'), textvariable=self.ans)
        self.ans_entry.place(x=775, y=325, width=430)

        # ===========Next button=================
        self.Next_button = Image.open('images/12.jpg')
        photo = ImageTk.PhotoImage(self.Next_button)
        self.Next_button_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.Next_button_label.image = photo
        self.Next_button_label.place(x=1045, y=525)
        
        self.Next = Button(self.Next_button_label, text='Finish', font=('yu gothic ui', 14, 'bold'),
                           width=6, bd=0,
                           bg='#DCDCDC', cursor='hand2', activebackground='#D1D0CE', fg='#000000' ,command=lambda :valid_answer(self))
        self.Next.place(x=18, y=5)

class ResetWin(Frame):
    def __init__(self, window,controller):
        self.controller=controller
        Frame.__init__(self, window)
        self.hide_button = None
        # self.state('zoomed')  # Maximizing the page
        
        # =================================
        self.Password = StringVar()
        self.Cpass = StringVar()
        self.Proceed = StringVar()
        # ================= Reset Frame =================
        self.lgn_frame = Frame(self, bg='#FFFFFF', width='1900', height='1000')  # Color and the size of the frame
        self.lgn_frame.pack()  # Placement of the frame
        # ============== Title ===========================
        self.SQ_label = Label(self.lgn_frame, text='Reset Password', bg='#FFFFFF',
                                    font=('yu gothic ui', 26, 'bold'),
                                    fg='#000000')
        self.SQ_label.place(x=325, y=55)
        # ========== 1st Question =================
        self.Password_label = Label(self.lgn_frame, text='Password', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
                                 fg='#000000')
        self.Password_label.place(x=300, y=175)
        self.Password_icon = Image.open('images/UsernameBar.jpg')
        photo = ImageTk.PhotoImage(self.Password_icon)
        self.Password_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.Password_icon_label.image = photo
        self.Password_icon_label.place(x=300, y=215)
        self.Password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#FFFFFF', fg='#000000',
                                 font=('yu gothic ui', 13, 'bold'), textvariable=self.Password)
        self.Password_entry.place(x=305, y=225, width=270)

        # ========== Confirm Password Question =================
        self.Cpass_label = Label(self.lgn_frame, text='Confirm-Password', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
                                 fg='#000000')
        self.Cpass_label.place(x=300, y=275)
        self.Cpass_icon = Image.open('images/UsernameBar.jpg')
        photo = ImageTk.PhotoImage(self.Cpass_icon)
        self.Cpass_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.Cpass_icon_label.image = photo
        self.Cpass_icon_label.place(x=300, y=315)
        self.Cpass_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#FFFFFF', fg='#000000',
                                 font=('yu gothic ui', 13, 'bold'), textvariable=self.Cpass)
        self.Cpass_entry.place(x=305, y=325, width=270)

        # =========== Proceed button=================
        self.Proceed_button = Image.open('images/12.jpg')
        photo = ImageTk.PhotoImage(self.Proceed_button)
        self.Proceed_button_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.Proceed_button_label.image = photo
        self.Proceed_button_label.place(x=345, y=425)
        self.Proceed = Button(self.Proceed_button_label, text='Proceed', font=('yu gothic ui', 14, 'bold'),
                           width=10, bd=0,
                           bg='#DCDCDC', cursor='hand2', activebackground='#D1D0CE', fg='#000000')
        self.Proceed.place(x=38, y=16)

class Homepage(Frame):  
    def __init__(self, window,controller):
        Frame.__init__(self, window)
        self.controller=controller
        self.hide_button = None

       

        def open_add(self):
            window = AddTransaction(self,controller)
            window.grab_set()
        
        def reset(self):
            self.start_date_calender.delete(0,'end')
            self.end_date_calender.delete(0,'end')

        def show(self):

            self.start_date = self.start_date_calender.get_date()
            self.start_date_str = self.start_date.strftime("%Y-%m-%d")
            self.end_date = self.end_date_calender.get_date()
            self.end_date_str = self.end_date.strftime("%Y-%m-%d")
            conn = sqlite3.connect('money.db')
            cursor = conn.cursor()

            #============= Income chart =============#
            cursor.execute('''SELECT SUM(Amount)
                                FROM Income
                                WHERE Email=? AND Date BETWEEN ? AND ? AND Category='Salary'
                                 ''',(self.controller.shared_email['Login_email'].get(),self.start_date_str,self.end_date_str,))
            salary_data = cursor.fetchall()
          
            if len(salary_data) == 0:
                salary.set(0)
            else: 
                salary.set(salary_data[0])
            #====================================#
            cursor.execute('''SELECT SUM(Amount)
                                FROM Income
                                WHERE Email=? AND Date BETWEEN ? AND ? AND Category='Loan'
                                 ''',(self.controller.shared_email['Login_email'].get(),self.start_date_str,self.end_date_str,))
            loan_data = cursor.fetchall()
            if len(loan_data) == 0:
                loan.set(0)
            else: 
                loan.set(loan_data[0])
            #====================================#
            cursor.execute('''SELECT SUM(Amount)
                                FROM Income
                                WHERE Email=? AND Date BETWEEN ? AND ? AND Category='Investment'
                                 ''',(self.controller.shared_email['Login_email'].get(),self.start_date_str,self.end_date_str,))
            invest_data = cursor.fetchall()
            if len(invest_data) == 0:
                investment.set(0)
            else: 
                investment.set(invest_data[0])
            #====================================#
            cursor.execute('''SELECT Category ,SUM(Amount)
                                FROM Income
                                WHERE Email=? AND Date BETWEEN ? AND ?
                                GROUP BY Category 
                                 ''',(self.controller.shared_email['Login_email'].get(),self.start_date_str,self.end_date_str,))
            
            income_graph_data=cursor.fetchall()   
           
            df1 = pd.DataFrame(income_graph_data,columns=['Category','Amount'])
            
       
            fig = Figure(figsize=(3,3)) # create a figure object
            ax = fig.add_subplot(111) # add an Axes to the figure

            ax.pie(df1['Amount'], radius=1, labels=df1['Category'], colors=['wheat','salmon','greenyellow'],wedgeprops={'width':0.3}, 
                startangle=90,)
            

            chart1 = FigureCanvasTkAgg(fig,self.a_frame)
            chart1.get_tk_widget().place(relx=0.17,rely=0.01)
           
            #============= Expenses chart =============#
            cursor.execute('''SELECT SUM(Amount)
                                FROM Expenses
                                WHERE Email=? AND Date BETWEEN ? AND ? AND Category='Home'
                                 ''',(self.controller.shared_email['Login_email'].get(),self.start_date_str,self.end_date_str,))
            home_data = cursor.fetchall()
          
            if len(home_data) == 0:
                salary.set(0)
            else: 
                home.set(home_data[0])
            #====================================#
            cursor.execute('''SELECT SUM(Amount)
                                FROM Expenses
                                WHERE Email=? AND Date BETWEEN ? AND ? AND Category='Travel'
                                 ''',(self.controller.shared_email['Login_email'].get(),self.start_date_str,self.end_date_str,))
            travel_data = cursor.fetchall()
          
            if len(travel_data) == 0:
                travel.set(0)
            else: 
                travel.set(travel_data[0])
            #====================================#
            cursor.execute('''SELECT SUM(Amount)
                                FROM Expenses
                                WHERE Email=? AND Date BETWEEN ? AND ? AND Category='Shopping'
                                 ''',(self.controller.shared_email['Login_email'].get(),self.start_date_str,self.end_date_str,))
            shopping_data = cursor.fetchall()
          
            if len(shopping_data) == 0:
                shopping.set(0)
            else: 
                shopping.set(shopping_data[0])  
            #====================================#
            cursor.execute('''SELECT Category , SUM(Amount)
                            FROM Expenses
                            WHERE Email=? AND Date BETWEEN ? AND ?
                            GROUP BY Category
                            ''',(self.controller.shared_email['Login_email'].get(),self.start_date_str,self.end_date_str,))

            cursor.execute('''SELECT SUM(Amount)
                                FROM Expenses
                                WHERE Email=? AND Date BETWEEN ? AND ? AND Category='Food&Drink'
                                 ''',(self.controller.shared_email['Login_email'].get(),self.start_date_str,self.end_date_str,))
            food_data = cursor.fetchall()
          
            if len(food_data) == 0:
                food.set(0)
            else: 
                food.set(food_data[0])
            #=====================================#
            cursor.execute('''SELECT SUM(Amount)
                                FROM Expenses
                                WHERE Email=? AND Date BETWEEN ? AND ? AND Category='Transport'
                                 ''',(self.controller.shared_email['Login_email'].get(),self.start_date_str,self.end_date_str,))
            transport_data = cursor.fetchall()
          
            if len(transport_data) == 0:
                transport.set(0)
            else: 
                transport.set(transport_data[0])


            #=============== Saving chart =============#
            cursor.execute('''SELECT SUM(Amount)
                                FROM Saving
                                WHERE Email=? AND Date BETWEEN ? AND ? AND Category='Saving'
                                 ''',(self.controller.shared_email['Login_email'].get(),self.start_date_str,self.end_date_str,))
            saving_data = cursor.fetchall()
          
            if len(saving_data) == 0:
                saving.set(0)
            else: 
                saving.set(transport_data[0])


        def log_out(self):
            answer = askyesno(title='Confirmation',message='Are you sure want log out?')
            if answer:
                self.controller.show_frame(LoginForm)

        
          #=====Int variable
        salary=IntVar()
        loan = IntVar()
        investment = IntVar()
        home = IntVar()
        travel = IntVar()
        food = IntVar()
        shopping = IntVar()
        transport =IntVar()
        saving =IntVar()


        self.str_date=StringVar()
        self.end_date=StringVar()
       
        # ================= homepage Frame =================
        self.navbar_frame = Frame(self, bg='#ffffff', width='2500', height='65')
        self.navbar_frame.place(x=0, y=5)

        # ======Nav bar======
        self.overview_label = Label(self.navbar_frame, bg='#FFFFFF', text='Overview', font=("yu gothic ui", 18),
                                    fg='#11DD7B', cursor="hand2")
        self.overview_label.place(x=450, y=11)
        self.overview_label.bind("<Button-1>",lambda e: controller.show_frame(Homepage))

        self.transaction_label = Label(self.navbar_frame, bg='#FFFFFF', text='Transaction', font=("yu gothic ui", 18),
                                       fg='#11DD7B', cursor="hand2")
        self.transaction_label.place(x=750, y=11)
        self.transaction_label.bind("<Button-1>",lambda e: controller.show_frame(TransactionTable))

        self.accountsetting_label = Label(self.navbar_frame, bg='#FFFFFF', text='Account Setting',
                                          font=("yu gothic ui", 18), fg='#11DD7B', cursor="hand2")
        self.accountsetting_label.place(x=1050, y=11)
        self.accountsetting_label.bind('<Button-1>',lambda e: controller.show_frame(AccountPage))

        self.tips_label = Label(self.navbar_frame, bg='#FFFFFF', text='Tips', font=("yu gothic ui", 18),
                                    fg='#11DD7B', cursor="hand2")
        self.tips_label.place(x=1390, y=11)

        self.log_out_btn = Image.open('images/log_out.jpeg')
        lgn_btn = ImageTk.PhotoImage(self.log_out_btn)
        self.log_out_label = Label(self.navbar_frame, bg='#FFFFFF', image=lgn_btn ,cursor="hand2")
        self.log_out_label.image = lgn_btn
        self.log_out_label.place(x=100, y=11)
        self.log_out_label.bind('<Button-1>',lambda e:log_out(self))


        # ================= Frame 1 =================
        self.a_frame = Frame(self, bg='#FFFFFF', width='450', height='650')  # Color and the size of the frame
        self.a_frame.place(x=100, y=230)  # Placement of the frame

        # ================= Frame 2 =================
        self.b_frame = Frame(self, bg='#FFFFFF', width='450', height='650')  # Color and the size of the frame
        self.b_frame.place(x=700, y=230)  # Placement of the frame

        # ================ Frame 3 =================
        self.c_frame = Frame(self, bg='#FFFFFF', width='450', height='650')  # Color and the size of the frame
        self.c_frame.place(x=1300, y=230)  # Placement of the frame

      

        self.start_date_calender = DateEntry(self,width=10,font=("Arial", 12),textvariable=self.str_date)
        self.start_date_calender.place(x=700,y=126)


        self.end_date_calender= DateEntry(self,width=10,font=("Arial", 12),textvariable=self.end_date)
        self.end_date_calender.place(x=800,y=126)
        
        self.show = customtkinter.CTkButton(self,width=100,text='show',fg_color='#FFFFFF',hover_color='#F2F2F2',command=lambda:show(self))
        self.show.place(x=550,y=125)

        self.reset =customtkinter.CTkButton(self,width=100,text='Reset',fg_color='#FFFFFF',hover_color='#F2F2F2',command= lambda:reset(self))
        self.reset.place(x=400,y=125)
        
        
        self.add = customtkinter.CTkButton(self, text='Add Transaction', fg_color='#11DD7B',
                        hover_color='#FFFFFF', cursor='hand2', relief=FLAT,command= lambda:open_add(self))
        self.add.place(x=100, y=125)

        #===============================Card Title Label =====================
        self.Income_label = Label(self.a_frame, text='Income', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
                                 fg='#000000')
        self.Income_label.place(x=16, y=10)

        self.Expenses_label = Label(self.b_frame, text='Expenses', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
                                  fg='#000000')
        self.Expenses_label.place(x=16, y=10)

        self.Savings_label = Label(self.c_frame, text='Savings', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
                                  fg='#000000')
        self.Savings_label.place(x=16, y=10)
        #============================== Income Card =============================
        self.agn_button = Image.open('images/16.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.a_frame, image=photo, bg='#FFFFFF')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=0, y=305)
        self.acc = Label(self.agn_button_label, text='Salary', font=('yu gothic ui', 13, 'bold'), width=15,
                          bd=0,
                          bg='#FFFFFF', cursor='hand2', activebackground='#DCDCDC', fg='#000000')
        self.acc.place(x=70, y=8)
        self.ac = Label(self.agn_button_label,text='', font=('yu gothic ui', 13, 'bold'), width=10,textvariable=salary,
                         bd=0,
                         bg='#FFFFFF')
        self.ac.place(x=330, y=8)

        self.agn_button = Image.open('images/1.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.a_frame, image=photo, bg='#000000')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=20, y=320)

        self.agn_button = Image.open('images/16.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.a_frame, image=photo, bg='#FFFFFF')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=0, y=361)
        self.acc = Label(self.agn_button_label, text='Loan', font=('yu gothic ui', 13, 'bold'), width=15,
                          bd=0,
                          bg='#FFFFFF', cursor='hand2', activebackground='#DCDCDC', fg='#000000')
        self.acc.place(x=70, y=8)
        self.ac = Label(self.agn_button_label, text='', font=('yu gothic ui', 13, 'bold'), width=10,textvariable=loan,
                         bd=0,
                         bg='#FFFFFF')
        self.ac.place(x=330, y=8)

        self.agn_button = Image.open('images/2.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.a_frame, image=photo, bg='#000000')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=20, y=375)

        self.agn_button = Image.open('images/16.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.a_frame, image=photo, bg='#FFFFFF')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=0, y=418)
        self.acc = Label(self.agn_button_label, text='Invesment', font=('yu gothic ui', 13, 'bold'), width=15,
                          bd=0,
                          bg='#FFFFFF', cursor='hand2', activebackground='#DCDCDC', fg='#000000')
        self.acc.place(x=70, y=8)
        self.ac = Label(self.agn_button_label, text='', font=('yu gothic ui', 13, 'bold'), width=10,textvariable=investment,
                          bd=0,
                          bg='#FFFFFF')
        self.ac.place(x=330, y=8)

        self.agn_button = Image.open('images/4.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.a_frame, image=photo, bg='#000000')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=20, y=431)

        #======B frame detail========
        # ============================== Expenses Card =======================
        self.agn_button = Image.open('images/16.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.b_frame, image=photo, bg='#FFFFFF')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=0, y=305)
        self.acc = Label(self.agn_button_label, text='Home', font=('yu gothic ui', 13, 'bold'), width=15,
                          bd=0,
                          bg='#FFFFFF')
        self.acc.place(x=70, y=8)
        self.ac = Label(self.agn_button_label, text='',textvariable=home, font=('yu gothic ui', 13, 'bold'), width=10,
                         bd=0,
                         bg='#FFFFFF')
        self.ac.place(x=330, y=8)

        self.agn_button = Image.open('images/5.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.b_frame, image=photo, bg='#000000')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=20, y=320)

        self.agn_button = Image.open('images/16.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.b_frame, image=photo, bg='#FFFFFF')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=0, y=361)
        self.acc = Label(self.agn_button_label, text='Travel', font=('yu gothic ui', 13, 'bold'), width=15,
                          bd=0,
                          bg='#FFFFFF')
        self.acc.place(x=70, y=8)
        self.ac = Label(self.agn_button_label, text='',textvariable=travel, font=('yu gothic ui', 13, 'bold'), width=10,
                         bd=0,
                         bg='#FFFFFF')
        self.ac.place(x=330, y=8)

        self.agn_button = Image.open('images/6.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.b_frame, image=photo, bg='#000000')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=20, y=375)

        self.agn_button = Image.open('images/16.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.b_frame, image=photo, bg='#FFFFFF')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=0, y=418)
        self.acc = Label(self.agn_button_label, text='Shopping', font=('yu gothic ui', 13, 'bold'), width=15,
                          bd=0,
                          bg='#FFFFFF')
        self.acc.place(x=70, y=8)
        self.ac = Label(self.agn_button_label, text='',textvariable=shopping, font=('yu gothic ui', 13, 'bold'), width=10,
                         bd=0,
                         bg='#FFFFFF')
        self.ac.place(x=330, y=8)

        self.agn_button = Image.open('images/7.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.b_frame, image=photo, bg='#000000')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=20, y=431)

        self.agn_button = Image.open('images/16.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.b_frame, image=photo, bg='#FFFFFF')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=0, y=475)
        self.acc = Label(self.agn_button_label, text='Food & Beverage', font=('yu gothic ui', 13, 'bold'), width=15,
                          bd=0,
                          bg='#FFFFFF', cursor='hand2', activebackground='#DCDCDC', fg='#000000')
        self.acc.place(x=70, y=8)
        self.ac = Label(self.agn_button_label, text='',textvariable=food, font=('yu gothic ui', 13, 'bold'), width=10,
                         bd=0,
                         bg='#FFFFFF')
        self.ac.place(x=330, y=8)

        self.agn_button = Image.open('images/8.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.b_frame, image=photo, bg='#000000')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=20, y=488)

        self.agn_button = Image.open('images/16.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.b_frame, image=photo, bg='#FFFFFF')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=0, y=532)
        self.acc = Label(self.agn_button_label, text='Transport', font=('yu gothic ui', 13, 'bold'), width=15,
                          bd=0,
                          bg='#FFFFFF', cursor='hand2', activebackground='#DCDCDC', fg='#000000')
        self.acc.place(x=70, y=8)
        self.ac = Label(self.agn_button_label, text='',textvariable=transport, font=('yu gothic ui', 13, 'bold'), width=10,
                         bd=0,
                         bg='#FFFFFF')
        self.ac.place(x=330, y=8)

        self.agn_button = Image.open('images/9.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.b_frame, image=photo, bg='#000000')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=20, y=545)

        #=========C Frame==================
        self.agn_button = Image.open('images/16.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.c_frame, image=photo, bg='#FFFFFF')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=0, y=305)
        self.acc = Label(self.agn_button_label, text='Saving', font=('yu gothic ui', 13, 'bold'), width=15,
                          bd=0,
                          bg='#FFFFFF', cursor='hand2', activebackground='#DCDCDC', fg='#000000')
        self.acc.place(x=70, y=8)
        self.ac = Label(self.agn_button_label, text='',textvariable=saving, font=('yu gothic ui', 13, 'bold'), width=10,
                         bd=0,
                         bg='#FFFFFF', cursor='hand2', activebackground='#FFFFFF', fg='#C11B17')
        self.ac.place(x=330, y=8)

        self.agn_button = Image.open('images/1.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.c_frame, image=photo, bg='#000000')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=20, y=320)

        self.agn_button = Image.open('images/16.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.c_frame, image=photo, bg='#FFFFFF')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=0, y=361)
        self.acc = Button(self.agn_button_label, text='Home', font=('yu gothic ui', 13, 'bold'), width=15,
                          bd=0,
                          bg='#FFFFFF', cursor='hand2', activebackground='#DCDCDC', fg='#000000')
        self.acc.place(x=70, y=8)
        self.ac = Button(self.agn_button_label, text='-100MYR', font=('yu gothic ui', 13, 'bold'), width=10,
                         bd=0,
                         bg='#FFFFFF', cursor='hand2', activebackground='#FFFFFF', fg='#C11B17')
        self.ac.place(x=330, y=8)

        self.agn_button = Image.open('images/2.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.c_frame, image=photo, bg='#000000')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=20, y=375)

        self.agn_button = Image.open('images/16.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.c_frame, image=photo, bg='#FFFFFF')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=0, y=418)
        self.acc = Label(self.agn_button_label, text='Home', font=('yu gothic ui', 13, 'bold'), width=15,
                          bd=0,
                          bg='#FFFFFF', cursor='hand2', activebackground='#DCDCDC', fg='#000000')
        self.acc.place(x=70, y=8)
        self.ac = Label(self.agn_button_label, text='-100MYR', font=('yu gothic ui', 13, 'bold'), width=10,
                         bd=0,
                         bg='#FFFFFF', cursor='hand2', activebackground='#FFFFFF', fg='#C11B17')
        self.ac.place(x=330, y=8)

        self.agn_button = Image.open('images/4.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.c_frame, image=photo, bg='#000000')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=20, y=431)

class AccountPage(Frame):
    def __init__(self, window, controller):
        Frame.__init__(self, window)
        self.controller= controller
        self.width= self.winfo_screenwidth()
        
        self.name_strvar= StringVar()
        self.email_strvar= StringVar()
        self.gender_strvar= StringVar()
        self.password_strvar= StringVar()

        
        
        email = self.email_strvar
        conn = sqlite3.connect('money.db')
        cursor = conn.cursor()
        def display_profile(self):
            if self.controller.shared_email['Login_email'].get():
                cursor.execute('SELECT * FROM account WHERE Email LIKE ?',(self.controller.shared_email['Login_email'].get(), ))
                data = cursor.fetchall()
                
                email.set(data [0][0]),self.password_strvar.set(data[0][1]),self.name_strvar.set(data[0][2]),self.gender_strvar.set(data[0][3])
            
        #======== Define Frame=======

        self.accountcard_frame=Frame(self,bg='#ffffff',width='500',height='600')
        self.accountcard_frame.place(x=655,y=120)
        self.navbar_frame = Frame(self, bg='#ffffff', width='2500', height='65')
        self.navbar_frame.place(x=0, y=5)

        # ======Nav bar======
        self.overview_label = Label(self.navbar_frame, bg='#FFFFFF', text='Overview', font=("yu gothic ui", 18),
                                    fg='#11DD7B', cursor="hand2")
        self.overview_label.place(x=450, y=11)
        self.overview_label.bind("<Button-1>",lambda e: controller.show_frame(Homepage))

        self.transaction_label = Label(self.navbar_frame, bg='#FFFFFF', text='Transaction', font=("yu gothic ui", 18),
                                       fg='#11DD7B', cursor="hand2")
        self.transaction_label.place(x=750, y=11)
        self.transaction_label.bind("<Button-1>",lambda e: controller.show_frame(TransactionTable))

        self.accountsetting_label = Label(self.navbar_frame, bg='#FFFFFF', text='Account Setting',
                                          font=("yu gothic ui", 18), fg='#11DD7B', cursor="hand2")
        self.accountsetting_label.place(x=1050, y=11)
        self.accountsetting_label.bind('<Button-1>',lambda e: controller.show_frame(AccountPage))

        self.tips_label = Label(self.navbar_frame, bg='#FFFFFF', text='Tips', font=("yu gothic ui", 18),
                                    fg='#11DD7B', cursor="hand2")
        self.tips_label.place(x=1390, y=11)

        self.log_out_btn = Image.open('images/log_out.jpeg')
        lgn_btn = ImageTk.PhotoImage(self.log_out_btn)
        self.log_out_label = Label(self.navbar_frame, bg='#FFFFFF', image=lgn_btn ,cursor="hand2")
        self.log_out_label.image = lgn_btn
        self.log_out_label.place(x=100, y=11)
        self.log_out_label.bind('<Button-1>',lambda e:log_out(self))
    
        #===== Account card=====
        #=====Name Entry======
        display_btn =customtkinter.CTkButton(self.accountcard_frame,text='show',width=20,fg_color='#FFFFFF',hover_color='#F2F2F2',border_width=1,command= lambda:display_profile(self)).place(x=60,y=60)

        self.label_img =Image.open('images/27.jpg')
        img = ImageTk.PhotoImage(self.label_img)
        self.name_label =Label(self.accountcard_frame,text='Name',font=labelfont,bg='#ffffff')
        self.name_label.place(x=60,y=100)
        self.name_entry_label = Label(self.accountcard_frame,image=img,bg='#ffffff')
        self.name_entry_label.image=img
        self.name_entry_label.place(relx=0.5,rely=0.165)
        self.name_entry = Entry(self.accountcard_frame,width=19,bg='#D9D9D9',font= entryfont,highlightthickness=0, relief=FLAT,textvariable=self.name_strvar)
        self.name_entry.place(relx=0.51,rely=0.18)

        #=====Email label and entry======
        self.email_label =Label(self.accountcard_frame,text='Email',font=labelfont,bg='#ffffff')
        self.email_label.place(x=60,y=200)
        self.email_entry_label = Label(self.accountcard_frame,image=img,bg='#ffffff')
        self.email_entry_label.image=img
        self.email_entry_label.place(relx=0.5,rely=0.33)
        self.email_entry = Entry(self.accountcard_frame,width=19,bg='#D9D9D9',font= entryfont,highlightthickness=0, relief=FLAT,textvariable=self.email_strvar)
        self.email_entry.place(relx=0.51,rely=0.345)

        #=====Gender label and entry=====
        self.gender_label =Label(self.accountcard_frame,text='Gender',font=labelfont,bg='#ffffff')
        self.gender_label.place(x=60,y=300)
        self.gender_entry_label = Label(self.accountcard_frame,image=img,bg='#ffffff')
        self.gender_entry_label.image=img
        self.gender_entry_label.place(relx=0.5,rely=0.5)
        self.gender_entry = Entry(self.accountcard_frame,width=19,bg='#D9D9D9',font= entryfont,highlightthickness=0, relief=FLAT,textvariable=self.gender_strvar)
        self.gender_entry.place(relx=0.51,rely=0.515)

       

        #======Button=======
        
        self.save_label = customtkinter.CTkButton(self.accountcard_frame,text='Save',fg_color='#D9D9D9',hover_color='#FFFFFF'
                        ,width=100,height=40,text_font=btnfont,cursor='hand2',border_width=1)
        self.save_label.place(relx=0.3,rely=0.81)
        self.save_label.bind('<Button-1>',lambda e:controller.saveChange())

        
        self.reset_label = customtkinter.CTkButton(self.accountcard_frame,text='Reset Password',text_font=btnfont,fg_color='#D9D9D9',hover_color='#FFFFFF',
                                width=100,height=40,cursor='hand2',border_width=1)
        self.reset_label.place(relx=0.63,rely=0.81)
        self.reset_label.bind("<Button-1>",lambda e:controller.show_frame(SecurityQuestion))

class ValidEmail(Frame):
    def __init__(self, window,controller):
        Frame.__init__(self, window)
        self.controller=controller
        
        def valid_email(self):
            conn = sqlite3.connect('money.db')  
            cursor = conn.cursor()
            cursor.execute('SELECT Email  FROM account WHERE Email=?',(self.controller.shared_email['resetpass_email'].get(),))
            email_data = cursor.fetchall()
            print(email_data)

            if  email_data:
                self.controller.show_frame(AnswerSQWin)
            else:
                mb.showerror('Error','Invalid email')
                
    
        self.Valid =Frame(self,bg='#FFFFFF',width='2300',height='1000')
        self.Valid.pack(pady=0,padx=0)

        self.head_label = Label(self.Valid,text='Enter your email',font=headfont,bg='#FFFFFF')
        self.head_label.place(relx=0.28,rely=0.2)

        self.email_label = Label(self.Valid,text='Email',bg='#FFFFFF',font=labelfont)
        self.email_label.place(relx=0.32,rely=0.3)
        self.email_box = Image.open('images/32.jpg')
        email_box_img = ImageTk.PhotoImage(self.email_box)
        self.email_box = Label(self.Valid,image=email_box_img,bg='#FFFFFF')
        self.email_box.image=email_box_img
        self.email_box.place(relx=0.32,rely=0.35)

        self.email_entry = Entry(self.Valid,width=29,bg='#FFFFFF',font= entryfont,highlightthickness=0, relief=FLAT, textvariable=self.controller.shared_email['resetpass_email'])
        self.email_entry.place(relx=0.33,rely=0.36)

        
        self.nextbtn_img =Image.open('images/31.jpg')
        nextbtn = ImageTk.PhotoImage(self.nextbtn_img)
        self.nextbtn = Label(self.Valid,image=nextbtn,bg='#FFFFFF')
        self.nextbtn.image = nextbtn
        self.nextbtn.place(relx=0.35,rely=0.52)
        self.next_label = Label(self.Valid,text='Next',bg='#D9D9D9',cursor='hand2',font=btnfont)
        self.next_label.place(relx=0.37,rely=0.53)
        self.next_label.bind('<Button-1>',lambda e:valid_email(self))

class SecurityQuestion(Frame):
    def __init__(self, window,controller):
        Frame.__init__(self, window)
        self.controller=controller
       

        def add_question(self):
            
            email = self.controller.shared_email['signUp_email'].get()
            conn = sqlite3.connect('money.db')
            cursor = conn.cursor()
            if not self.first.get() or not self.second.get() or not self.third.get():
                mb.showerror('Error','Please answer all the questions')
            else:
                cursor.execute("INSERT INTO Security_Question(Email,Questions,Answer) VALUES(?,?,?)",(email,'What do you live?',self.first.get()))
                cursor.execute("INSERT INTO Security_Question(Email,Questions,Answer) VALUES(?,?,?)",(email,'What is your primary school',self.second.get()))
                cursor.execute("INSERT INTO Security_Question(Email,Questions,Answer) VALUES(?,?,?)",(email,'What is your father name?',self.third.get()))
                conn.commit()
                mb.showinfo('Success','Commit Success!')
                controller.show_frame(LoginForm)
                
        self.Question =Frame(self,bg='#FFFFFF',width='1780',height='1000')
        self.Question.pack(pady=50)
        
        
        self.first = StringVar()
        self.second = StringVar()
        self.third = StringVar()
        self.Next = StringVar()
        # ================= Sign up Frame =================
        self.lgn_frame = Frame(self, bg='#FFFFFF', width='1780', height='1000')  # Color and the size of the frame
        self.lgn_frame.place(x=0, y=0)  # Placement of the frame
        # ============== Title ===========================
        self.SQ_label = Label(self.lgn_frame, text='Set Security Question', bg='#FFFFFF',
                                    font=('yu gothic ui', 32, 'bold'),
                                    fg='#000000')
        self.SQ_label.place(x=655, y=55)
        # ========== 1st Question =================
        self.first_label = Label(self.lgn_frame, text='Where do you live?', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
                                 fg='#000000')
        self.first_label.place(x=700, y=175)
        self.first_icon = Image.open('images/UsernameBar.jpg')
        photo = ImageTk.PhotoImage(self.first_icon)
        self.first_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.first_icon_label.image = photo
        self.first_icon_label.place(x=700, y=215)
        self.first_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#FFFFFF', fg='#000000',
                                 font=('yu gothic ui', 13, 'bold'), textvariable=self.first)
        self.first_entry.place(x=705, y=225, width=270)

        # ========== 2nd Question =================
        self.second_label = Label(self.lgn_frame, text='What is your primary school?', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
                                 fg='#000000')
        self.second_label.place(x=700, y=275)
        self.second_icon = Image.open('images/UsernameBar.jpg')
        photo = ImageTk.PhotoImage(self.first_icon)
        self.second_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.second_icon_label.image = photo
        self.second_icon_label.place(x=700, y=315)
        self.second_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#FFFFFF', fg='#000000',
                                 font=('yu gothic ui', 13, 'bold'), textvariable=self.second)
        self.second_entry.place(x=705, y=325, width=270)

        # ========== 3rd Question =================
        self.third_label = Label(self.lgn_frame, text='What is your father name?', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
                                  fg='#000000')
        self.third_label.place(x=700, y=375)
        self.third_icon = Image.open('images/UsernameBar.jpg')
        photo = ImageTk.PhotoImage(self.first_icon)
        self.third_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.third_icon_label.image = photo
        self.third_icon_label.place(x=700, y=415)
        self.third_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#FFFFFF', fg='#000000',
                                  font=('yu gothic ui', 13, 'bold'), textvariable=self.third)
        self.third_entry.place(x=705, y=425, width=270)

        # ===========Next button=================
       
     
        self.Next = customtkinter.CTkButton(self.lgn_frame, text='Finish', text_font=('yu gothic ui', 14),
                           width=150,height=30,fg_color='#FFFFFF',hover_color='#F2F2F2', cursor='hand2',border_width=1,command= lambda :add_question(self))
        self.Next.place(x=780, y=500)

class ResetPass(Frame):
    def __init__(self,ResetWindow,controller) :
        Frame.__init__(self, ResetWindow)
        self.controller=controller
        #open Top level window
       
        def change(self):
            conn = sqlite3.connect('money.db')
            cursor = conn.cursor()
            cursor.execute('UPDATE account SET Password =? WHERE Email=?')

        self.Reset =Frame(self,bg='#FFFFFF',width='2300',height='1000')
        self.Reset.pack(pady=0,padx=0)

        self.head_label = Label(self.Reset,text='Reset Password',font=headfont,bg='#FFFFFF')
        self.head_label.place(relx=0.28,rely=0.2)

        self.pass_label = Label(self.Reset,text='Password',bg='#FFFFFF',font=labelfont)
        self.pass_label.place(relx=0.32,rely=0.3)
        self.pass_box = Image.open('images/32.jpg')
        pass_box_img = ImageTk.PhotoImage(self.pass_box)
        self.pass_box = Label(self.Reset,image=pass_box_img,bg='#FFFFFF')
        self.pass_box.image=pass_box_img
        self.pass_box.place(relx=0.32,rely=0.35)
        self.pass_entry = Entry(self.Reset,width=29,bg='#FFFFFF',font= entryfont,highlightthickness=0, relief=FLAT)
        self.pass_entry.place(relx=0.33,rely=0.36)

        self.repass_label =Label(self.Reset,text='Confirm Password',bg='#FFFFFF',font=labelfont)
        self.repass_label.place(relx=0.32,rely=0.4)
        self.repass_box = Image.open('images/32.jpg')
        self.repass_box = Label(self.Reset,image=pass_box_img,bg='#FFFFFF')
        self.repass_box.image=pass_box_img
        self.repass_box.place(relx=0.32,rely=0.45)
        self.repass_entry = Entry(self.Reset,width=29,bg='#FFFFFF',font= entryfont,highlightthickness=0, relief=FLAT)
        self.repass_entry.place(relx=0.33,rely=0.46)

        self.resetbtn_img =Image.open('images/31.jpg')
        resetbtn = ImageTk.PhotoImage(self.resetbtn_img)
        self.resetbtn = Label(self.Reset,image=resetbtn,bg='#FFFFFF')
        self.resetbtn.image = resetbtn
        self.resetbtn.place(relx=0.35,rely=0.52)
        self.reset_label = Label(self.Reset,text='Reset',bg='#D9D9D9',cursor='hand2',font=btnfont)
        self.reset_label.place(relx=0.37,rely=0.53)
        self.reset_label.bind('<Button-1>',lambda e: controller.show_frame(SecurityQuestion))

class AddTransaction(Toplevel):
    def __init__(self,window,controller):
        Toplevel.__init__(self,window)
        self.geometry('1000x500')
        category_list =['Food&Drink','Cars','Home','Travel','Shopping','Salary','Loan','Investment','Saving']
        currency_list = ['MYR','USD','CAD','EUR','SG','CNH','JPY','GBP','CHF','AUD']

        self.controller= controller
        self.resizable(0,0)

        def open_calculator(self):
            window = Calculator(self,controller)
            window.grab_set()


        def add(self):
            email = self.controller.shared_email['Login_email'].get()
            self.category = self.category.get()
            self.note = self.note.get()
            self.amount = self.amount.get()
            self.currency = self.currency.get()
            self.date = self.date.get_date()
            self.str_date = self.date.strftime("%Y-%m-%d")

            conn = sqlite3.connect('money.db')
            cursor = conn.cursor()
            cr = CurrencyRates()

            if not self.category or not self.amount or not self.currency :
                mb.showerror('Error','Please fill in the blank!')
            elif self.amount <= 0:
                mb.showerror('Error','The amount cannot less than zero!')
            elif self.category =='Salary' or self.category == 'Loan' or self.category == 'Investment':
                converted_amount = cr.convert(self.currency,'MYR',self.amount)
                decimal_amount = round(converted_amount,2)
                cursor.execute('INSERT INTO Income(Email,Category,Date,Note,Amount,Currency) VALUES(?,?,?,?,?,?)',(email,self.category,self.str_date,self.note,decimal_amount,'MYR'))
                conn.commit()
                mb.showinfo('Success','Commit success')
            elif self.category =='Food&Drink' or self.category == 'Travel' or self.category == 'Cars' or self.category == 'Shopping' or self.category == 'Home':
                converted_amount = cr.convert(self.currency,'MYR',self.amount)
                decimal_amount = round(converted_amount,2)
                cursor.execute('INSERT INTO Expenses(Email,Category,Date,Note,Amount,Currency) VALUES(?,?,?,?,?,?)',(email,self.category,self.str_date,self.note,decimal_amount,'MYR'))
                conn.commit()
                mb.showinfo('Success','Commit success') 
            elif self.category =='Saving' :
                converted_amount = cr.convert(self.currency,'MYR',self.amount)
                decimal_amount = round(converted_amount,2)
                cursor.execute('INSERT INTO Saving(Email,Category,Date,Note,Amount,Currency) VALUES(?,?,?,?,?,?)',(email,self.category,self.str_date,self.note,decimal_amount,'MYR'))
                conn.commit()
                mb.showinfo('Success','Commit success')
            else:
                mb.showerror('Error','Error')

        self.category =  StringVar()
        self.note = StringVar()
        self.amount = IntVar()
        self.currency = StringVar()
        

        self.Add = Frame(self,bg='#FFFFFF',height='500',width='1000')
        self.Add.place(x=0,y=0)

        self.category_label = Label(self.Add,text='Category',bg='#FFFFFF',font=labelfont)
        self.category_label.place(relx=0.05,rely=0.05)
        category = Combobox(self,width=12,values=category_list,state='readonly',textvariable=self.category)
        category.place(relx=0.05,rely=0.12)

        self.date_label = Label(self.Add,text='Date',bg='#FFFFFF',font=labelfont)
        self.date_label.place(relx=0.2,rely=0.05)
    
        self.date=DateEntry(self.Add, font=("Arial", 12), width=12)
        self.date.place(relx=0.2,rely=0.12)

        self.note_label = Label(self.Add,text='Note (optional)',bg='#FFFFFF',font=labelfont)
        self.note_label.place(relx=0.37,rely=0.05)
        self.note_img = Image.open('images/note_box.jpg')
        note = ImageTk.PhotoImage(self.note_img)
        self.note_img = Label(self.Add,image=note,bg='#FFFFFF')
        self.note_img.image = note
        self.note_img.place(relx=0.37,rely=0.12)
        note_entry = Entry(self,width=16,bg='#FFFFFF',font=entryfont,highlightthickness=0, relief=FLAT,textvariable=self.note)
        note_entry.place(relx=0.38,rely=0.125)

        self.amount_label = Label(self.Add,text='Amount',bg='#FFFFFF',font=labelfont)
        self.amount_label.place(relx=0.55,rely=0.05)
        self.amount_img = Image.open('images/note_box.jpg')
        amount = ImageTk.PhotoImage(self.amount_img)
        self.amount_img = Label(self.Add,image=amount,bg='#FFFFFF')
        self.amount_img.image = amount
        self.amount_img.place(relx=0.55,rely=0.12)
        amount_entry = Entry(self,width=17,bg='#FFFFFF',font=entryfont,highlightthickness=0, relief=FLAT,textvariable=self.amount)
        amount_entry.place(relx=0.56,rely=0.125)

        currency_label = Label(self.Add,text='Currency',bg='#FFFFFF',font=labelfont)
        currency_label.place(relx=0.73,rely=0.05)
        currency = Combobox(self.Add,width=5,values=currency_list,state='readonly',textvariable=self.currency)
        currency.place(relx=0.74,rely=0.125)

        self.add_btn = customtkinter.CTkButton(self.Add,text='Add transaction',fg_color='#11DD7B',hover_color='#FFFFFF',border_width=1
                                                ,width=15,cursor='hand2',command=lambda:add(self))
        self.add_btn.place(relx=0.667,rely=0.255)

        self.cal_btn = customtkinter.CTkButton(self.Add,text='Calculator',width=15,fg_color='#11DD7B',
                                                hover_color='#FFFFFF',command=lambda:open_calculator(self),border_width=1)
        self.cal_btn.place(relx=0.5,rely=0.255)

class TransactionTable(Frame):       
    def __init__(self,window,controller) :
        Frame.__init__(self,window)
        self.controller = controller 
        self.category = StringVar()
        category_list=['Salary','Loan','Investment','Home','Travel','Shopping','Food&Drink','Transport','Saving']
        
        def display_record(self):
            email = self.controller.shared_email['Login_email'].get()
            self.tree.delete(*self.tree.get_children())
            conn = sqlite3.connect('money.db')
            cursor =conn.cursor()
            cursor.execute('SELECT Transaction_ID,Category,Date,Note,Amount,Currency FROM Income WHERE Email =?',(email,))
            data =cursor.fetchall()
            for record in data:
                self.tree.insert('',END,values=record)
            cursor.execute('SELECT Transaction_ID,Category,Date,Note,Amount,Currency FROM Expenses WHERE Email =?',(email,))
            data =cursor.fetchall()
            for record in data:
                self.tree.insert('',END,values=record)
            
        def delete_record(self):
            conn = sqlite3.connect('money.db')
            cursor =conn.cursor()
            if not self.tree.selection():
                 mb.showerror('Error!', 'Please select a record from the table')
            else:
                # Select the one row of the table
                answer = askyesno(title='confirmation',
                        message='Are you sure that you want to delete')
                if answer:
                    current_item = self.tree.focus()
                    values = self.tree.item(current_item)
                    selection = values["values"]
                    self.tree.delete(current_item)
                    cursor.execute('DELETE FROM Income WHERE Transaction_ID=%s' % selection[0])
                    cursor.execute('DELETE FROM Expenses WHERE Transaction_ID=%s' % selection[0])
                    cursor.execute('DELETE FROM Saving WHERE Transaction_ID=%s' % selection[0])
                    conn.commit()
                    mb.showinfo('Done', 'The record you wanted deleted was successfully deleted.')
                    display_record(self)

        def search_by_category(self):
            conn =sqlite3.connect('money.db')
            cursor = conn.cursor()
            if self.category.get() == 'Salary' or self.category.get() == 'Loan' or self.category.get() == 'Investment':
                self.tree.delete(*self.tree.get_children())
                cursor.execute('SELECT Transaction_ID, Category,Date,Note,Amount,Currency FROM Income WHERE Email =? AND Category=?',(self.controller.shared_email['Login_email'].get(),self.category.get()))
                salary_data = cursor.fetchall()
                for record in salary_data:
                    self.tree.insert('',END,values=record)
                
            elif self.category.get() == 'Home' or self.category.get() == 'Travel' or self.category.get() == 'Shopping' or self.category.get() == 'Food&Drink' or self.category.get() == 'Transport' :
                self.tree.delete(*self.tree.get_children())
                cursor.execute('SELECT Transaction_ID, Category,Date,Note,Amount,Currency FROM Expenses WHERE Email =? AND Category=?',(self.controller.shared_email['Login_email'].get(),self.category.get()))
                salary_data = cursor.fetchall()
                for record in salary_data:
                    self.tree.insert('',END,values=record)
       
            elif self.category.get() == 'Saving':
                self.tree.delete(*self.tree.get_children())
                cursor.execute('SELECT Transaction_ID, Category,Date,Note,Amount,Currency FROM Saving WHERE Email =? AND Category+?',(self.controller.shared_email['Login_email'].get(),'Saving'))
                salary_data = cursor.fetchall()
                for record in salary_data:
                    self.tree.insert('',END,values=record)
            else:
                mb.showerror('Error','Please select one category')

        self.table_frame =Frame(self,bg='#FFFFFF',width='1760',height='800')
        self.table_frame.place(x=5,y=110)
        self.navbar_frame = Frame(self, bg='#ffffff', width='2500', height='65')
        self.navbar_frame.place(x=0, y=5)

        # ======Nav bar======
        self.overview_label = Label(self.navbar_frame, bg='#FFFFFF', text='Overview', font=("yu gothic ui", 18),
                                    fg='#11DD7B', cursor="hand2")
        self.overview_label.place(x=450, y=11)
        self.overview_label.bind("<Button-1>",lambda e: controller.show_frame(Homepage))

        self.transaction_label = Label(self.navbar_frame, bg='#FFFFFF', text='Transaction', font=("yu gothic ui", 18),
                                       fg='#11DD7B', cursor="hand2")
        self.transaction_label.place(x=750, y=11)
        self.transaction_label.bind("<Button-1>",lambda e: controller.show_frame(TransactionTable))

        self.accountsetting_label = Label(self.navbar_frame, bg='#FFFFFF', text='Account Setting',
                                          font=("yu gothic ui", 18), fg='#11DD7B', cursor="hand2")
        self.accountsetting_label.place(x=1050, y=11)
        self.accountsetting_label.bind('<Button-1>',lambda e: controller.show_frame(AccountPage))

        self.tips_label = Label(self.navbar_frame, bg='#FFFFFF', text='Tips', font=("yu gothic ui", 18),
                                    fg='#11DD7B', cursor="hand2")
        self.tips_label.place(x=1390, y=11)

        self.log_out_btn = Image.open('images/log_out.jpeg')
        lgn_btn = ImageTk.PhotoImage(self.log_out_btn)
        self.log_out_label = Label(self.navbar_frame, bg='#FFFFFF', image=lgn_btn ,cursor="hand2")
        self.log_out_label.image = lgn_btn
        self.log_out_label.place(x=100, y=11)
        self.log_out_label.bind('<Button-1>',lambda e:controller.log_out(self))

        self.show = customtkinter.CTkButton(self.table_frame,width=100,text='Show',fg_color='#FFFFFF',hover_color='#F2F2F2',border_width=1,command=lambda:display_record(self))
        self.show.place(x=200,y=60)

        self.delete_record= customtkinter.CTkButton(self.table_frame,width=100,text='Delete',fg_color='#FFFFFF',hover_color='#F2F2F2',border_width=1,command=lambda :delete_record(self))
        self.delete_record.place(x=350,y=60)

        self.search_category= customtkinter.CTkButton(self.table_frame,width=100,text='Search',fg_color='#FFFFFF',hover_color='#F2F2F2',border_width=1,command=lambda :search_by_category(self))
        self.search_category.place(x=490,y=60)

        self.category_list = Combobox(self.table_frame,width=10,textvariable=self.category,values=category_list,state='readonly')
        self.category_list.place(x=620,y=65)

        self.tree = Treeview(self.table_frame, height=100, selectmode=BROWSE,
                                columns=('Transaction_ID','Category', 'Date', "Note","Amount", "Currency" ))
        X_scroller = Scrollbar(self.tree, orient=HORIZONTAL, command=self.tree.xview)
        Y_scroller = Scrollbar(self.tree, orient=VERTICAL, command=self.tree.yview)
        X_scroller.pack(side=BOTTOM, fill=X)
        Y_scroller.pack(side=RIGHT, fill=Y)
        self.tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
        self.tree.heading('Transaction_ID', text='Transaction_ID', anchor=CENTER)
        self.tree.heading('Category', text='Category', anchor=CENTER)
        self.tree.heading('Date', text='Date', anchor=CENTER)
        self.tree.heading('Note', text='Note', anchor=CENTER)
        self.tree.heading('Amount', text='Amount', anchor=CENTER)
        self.tree.heading('Currency', text='Currency', anchor=CENTER)


        self.tree.column('#0', width=0, stretch=NO,anchor=CENTER)
        self.tree.column('#1', width=120, stretch=NO,anchor=CENTER)
        self.tree.column('#2', width=100, stretch=NO,anchor=CENTER)
        self.tree.column('#3', width=150, stretch=NO,anchor=CENTER)
        self.tree.column('#4', width=80, stretch=NO,anchor=CENTER)
        self.tree.column('#5', width=80, stretch=NO,anchor=CENTER)
        self.tree.column('#6', width=80, stretch=NO,anchor=CENTER)

       
        self.tree.place(y=120, relwidth=1, relheight=0.9, relx=0)
       
class Calculator(Toplevel):
    def __init__(self,window,controller):
        
        Toplevel.__init__(self,window)
        self.geometry('500x500')

        self.expression = ""
        # be used to store data in memory
        self.recall = ""
        # be used to store current data in memory
        self.current = ""
        # self.answer
        self.sum_up = ""
        # create string for text input
        self.text_input = tk.StringVar()
        # assign instance to master
      
        # set frame showing inputs and title
        top_frame = tk.Frame(self, width=500, height=20, bd=4, relief='flat', bg='#11DD7B')
        top_frame.pack(side=tk.TOP)
        # set frame showing all buttons
        bottom_frame = tk.Frame(self, width=650, height=470, bd=4, relief='flat', bg='#11DD7B')
        bottom_frame.pack(side=tk.BOTTOM)
        # name of calculator
        my_item = tk.Label(top_frame, text="Calculator", font=('arial', 14), fg='white', width=26, bg='#11DD7B')
        my_item.pack()
        # entry interface for inputs
        txt_display = tk.Entry(top_frame, font=('arial', 23), relief='flat', bg='#F2F2F2', fg='black',
                               textvariable=self.text_input, width=55, bd=4, justify='right', state='readonly')
        txt_display.pack()

        # row 0
        # clears self.expression
        self.btn_clear = customtkinter.CTkButton(bottom_frame,width=10, border_width=1, fg_color='#FFFFFF', bg_color='#F2F2F2', text="C", command=self.btn_clear_all)
        self.btn_clear.grid(row=0, column=4)
        # deletes last string input
        self.btn_del = customtkinter.CTkButton(bottom_frame, width=10,border_width=1, fg_color='#FFFFFF', bg_color='#F2F2F2', text="del", command=self.btn_clear1)
        self.btn_del.grid(row=0, column=5)
        # inputs a negative sign to the next entry
        self.btn_change_sign = customtkinter.CTkButton(bottom_frame, width=10,border_width=1, fg_color='#FFFFFF', bg_color='#F2F2F2', text=chr(177), command=self.change_signs)
        self.btn_change_sign.grid(row=0, column=6)
        # division
        self.btn_div = customtkinter.CTkButton(bottom_frame, width=10,border_width=1, fg_color='#FFFFFF', bg_color='#F2F2F2', text="/", command=lambda: self.btn_click('/'))
        self.btn_div.grid(row=0, column=7)
        # stores previous expression as an answer value
        self.btn_ans = customtkinter.CTkButton(bottom_frame, width=10,border_width=1, fg_color='#FFFFFF', bg_color='#F2F2F2', text="ans", command=self.answer)
        self.btn_ans.grid(row=0, column=8)

        # row 1
        # seven
        self.btn_7 = customtkinter.CTkButton(bottom_frame, width=10,border_width=1, fg_color='#FFFFFF', bg_color='#F2F2F2', text="7", command=lambda: self.btn_click(7))
        
        self.btn_7.grid(row=1, column=4)
        # eight
        self.btn_8 = customtkinter.CTkButton(bottom_frame, width=10,border_width=1, fg_color='#FFFFFF', bg_color='#F2F2F2', text="8", command=lambda: self.btn_click(8))
        
        self.btn_8.grid(row=1, column=5)
        # nine
        self.btn_9 = customtkinter.CTkButton(bottom_frame, width=10,border_width=1, fg_color='#FFFFFF', bg_color='#F2F2F2', text="9", command=lambda: self.btn_click(9))
        
        self.btn_9.grid(row=1, column=6)
        # multiplication
        self.btn_mult = customtkinter.CTkButton(bottom_frame,width=10, border_width=1, fg_color='#FFFFFF', bg_color='#F2F2F2', text="x", command=lambda: self.btn_click('*'))
        self.btn_mult.grid(row=1, column=7)
        # 'memory clear' button. Wipes self.recall to an empty string
        self.btn_MC = customtkinter.CTkButton(bottom_frame, width=10,border_width=1, fg_color='#FFFFFF', bg_color='#F2F2F2', text="MC", command=self.memory_clear)
        self.btn_MC.grid(row=1, column=8)

        # row 2
        # four
        self.btn_4 = customtkinter.CTkButton(bottom_frame,width=10,border_width=1, fg_color='#FFFFFF', bg_color='#F2F2F2', text="4", command=lambda: self.btn_click(4))
        
        self.btn_4.grid(row=2, column=4)
        # five
        self.btn_5 = customtkinter.CTkButton(bottom_frame, width=10,border_width=1, fg_color='#FFFFFF', bg_color='#F2F2F2', text="5", command=lambda: self.btn_click(5))
        
        self.btn_5.grid(row=2, column=5)
        # six
        self.btn_6 = customtkinter.CTkButton(bottom_frame,width=10,border_width=1, fg_color='#FFFFFF', bg_color='#F2F2F2', text="6", command=lambda: self.btn_click(6))
        
        self.btn_6.grid(row=2, column=6)
        # subtraction
        self.btnSub = customtkinter.CTkButton(bottom_frame, width=10,border_width=1, fg_color='#FFFFFF', bg_color='#F2F2F2', text="-", command=lambda: self.btn_click('-'))
        self.btnSub.grid(row=2, column=7)
        # outputs what is in self.recall
        self.btn_MR = customtkinter.CTkButton(bottom_frame, width=10,border_width=1, fg_color='#FFFFFF', bg_color='#F2F2F2', text="MR", command=self.memory_recall)
        self.btn_MR.grid(row=2, column=8)

        # row 3
        # one
        self.btn_1 = customtkinter.CTkButton(bottom_frame, width=10,border_width=1, fg_color='#FFFFFF', bg_color='#F2F2F2', text="1", command=lambda: self.btn_click(1))
        
        self.btn_1.grid(row=3, column=4)
        # two
        self.btn_2 = customtkinter.CTkButton(bottom_frame, width=10,border_width=1, fg_color='#FFFFFF', bg_color='#F2F2F2', text="2", command=lambda: self.btn_click(2))
        
        self.btn_2.grid(row=3, column=5)
        # three
        self.btn_3 = customtkinter.CTkButton(bottom_frame, width=10,border_width=1, fg_color='#FFFFFF', bg_color='#F2F2F2', text="3", command=lambda: self.btn_click(3))
        self.btn_3.grid(row=3, column=6)
        # addition
        self.btn_add = customtkinter.CTkButton(bottom_frame, width=10,border_width=1, fg_color='#FFFFFF', bg_color='#F2F2F2', text="+", command=lambda: self.btn_click('+'))
        self.btn_add.grid(row=3, column=7)
        # adds current self.expression to self.recall string
        self.btn_M_plus = customtkinter.CTkButton(bottom_frame, width=10,border_width=1, fg_color='#FFFFFF', bg_color='#F2F2F2', text="M+", command=self.memory_add)
        self.btn_M_plus.grid(row=3, column=8)

        # row 4
        # zero
        self.btn_0 = customtkinter.CTkButton(bottom_frame,width=10, border_width=1, fg_color='#FFFFFF', bg_color='#F2F2F2', text="0", command=lambda: self.btn_click(0))
        
        self.btn_0.grid(row=4, column=4, columnspan=2)
        # equals button
        self.btn_eq = customtkinter.CTkButton(bottom_frame,width=10, border_width=1, fg_color='#FFFFFF', bg_color='#F2F2F2', text="=", command=self.btn_equal)
    
        self.btn_eq.grid(row=4, column=6)
        # decimal to convert to float
        self.btn_dec = customtkinter.CTkButton(bottom_frame, width=10,border_width=1, fg_color='#FFFFFF', bg_color='#F2F2F2', text=".", command=lambda: self.btn_click('.'))
        self.btn_dec.grid(row=4, column=7)
        # subtracts current self.expression to self.recall string
        self.btn_M_sub = customtkinter.CTkButton(bottom_frame, width=10,border_width=1, fg_color='#FFFFFF', bg_color='#F2F2F2', text="M-", command=self.memory_minus)
        self.btn_M_sub.grid(row=4, column=8)

    # functions
    # allows button you click to be put into self.expression

    def btn_click(self, expression_val):
        if len(self.expression) >= 23:
            self.expression = self.expression
            self.text_input.set(self.expression)
        else:
            self.expression = self.expression + str(expression_val)
            self.text_input.set(self.expression)

    # validate number of dots

    def val_dot(self, expression_val):
        self.current = self.expression
        while "." in self.expression:
            self.text_input.set(self.current)
        self.btn_click('.')

    # clears last item in string

    def btn_clear1(self):
        self.expression = self.expression[:-1]
        self.text_input.set(self.expression)

    # adds in a negative sign

    def change_signs(self):
        self.expression = '-' + self.expression
        self.text_input.set(self.expression)

    # clears memory_recall

    def memory_clear(self):
        self.recall = ""

    # adds whatever is on the screen to self.recall

    def memory_add(self):
        self.recall = self.recall + '+' + self.expression

    # minus whatever is on the screen to self.recall

    def memory_minus(self):
        self.recall = self.recall + '-' + self.expression

    # uses whatever is stored in memory_recall

    def answer(self):
        self.answer = self.sum_up
        self.expression = self.expression + self.answer
        self.text_input.set(self.expression)

    # uses whatever is stored in memory_recall

    def memory_recall(self):
        if self.expression == "":
            self.text_input.set('0' + self.expression + self.recall)
        else:
            self.text_input.set(self.expression + self.recall)

    # clears self.expression

    def btn_clear_all(self):
        self.expression = ""
        self.text_input.set("")

    # converts self.expression into a mathematical expression and evaluates it

    def btn_equal(self):
        self.sum_up = str(eval(self.expression))
        self.text_input.set(self.sum_up)
        self.expression = self.sum_up




def page():
    app =windows()
    app.mainloop()
    
    

if __name__ == '__main__':
    page()