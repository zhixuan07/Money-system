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
        self.width= self.winfo_screenwidth()
        self.height= self.winfo_screenheight()
        self.geometry("1530x1000")
        
        #Creating the sharing variables across classes
        self.shared_email={'signUp_email':StringVar(),'Login_email':StringVar()}
        
        # creating a frame and assigning it to container
        container = Frame(self, height='1000', width='1700')
        # specifying the region where the frame is packed in root
        container.place(x=0, y=0)

        # configuring the location of the container using grid
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (AccountPage,SecurityQuestion,ResetPass,LoginForm,SignupWin,SelectSQWin,Homepage,ResetWin,TransactionTable):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(LoginForm)

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
        Frame.__init__(self, window)
        self.Login= Frame(self,bg="#FFFFFF",width='1000',height='1000')
        self.Login.pack()
          # Delete the restore button
        #=================================
        
        self.login_password=StringVar()

    
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

      


        # ================= Login Frame =================
        self.lgn_frame = Frame(self, bg='#FFFFFF', width='1166', height='718')  # Color and the size of the frame
        self.lgn_frame.place(x=0, y=0)  # Placement of the frame

        self.frame1 = Frame(self, bg='#7FFFD4', width='583', height='718')
        self.frame1.place(x=0, y=0)

        # =============user icon===================
        self.username_icon = Image.open('images/user.jpeg')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#2B1B17')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=756, y=25)
        # ================= Username =================
        self.email_label = Label(self.lgn_frame, text='Email', bg='#FFFFFF', font=('yu gothic ui', 13, 'bold'),
                                 fg='#000000')
        self.email_label.place(x=656, y=275)
        self.email_icon = Image.open('images/UsernameBar.jpg')
        photo = ImageTk.PhotoImage(self.email_icon)
        self.email_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.email_icon_label.image = photo
        self.email_icon_label.place(x=695, y=300)
        self.email_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#FFFFFF', fg='#000000',
                                 font=('yu gothic ui', 13, 'bold'), textvariable=self.controller.shared_email['Login_email'])
        self.email_entry.place(x=706, y=305, width=270)

        # ================= Password =================
        self.pss_label = Label(self.lgn_frame, text='Password', bg='#FFFFFF', font=('yu gothic ui', 13, 'bold'),
                               fg='#000000')
        self.pss_label.place(x=656, y=355)
        self.pss_icon = Image.open('images/UsernameBar.jpg')
        photo = ImageTk.PhotoImage(self.email_icon)
        self.pss_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.pss_icon_label.image = photo
        self.pss_icon_label.place(x=695, y=390)
        self.pss_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#FFFFFF', fg='#000000',
                               font=('yu gothic ui', 13, 'bold'), textvariable=self.login_password)
        self.pss_entry.place(x=706, y=395, width=270)

        # ===========Forgot password=================
        self.forgot = Button(self.lgn_frame,text='Forgot Password?', font=('yu gothic ui', 16, 'bold'), width=20, bd=0,
                             bg='#FFFFFF', cursor='hand2', activebackground='#D1D0CE', fg='#728FCE')
        self.forgot.place(x=596, y=445)

        # ===========Login Button==========
        self.lgn_button = Image.open('images/3.jpg')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=670, y=550)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=('yu gothic ui', 13, 'bold'),
                            width=10, bd=0, command=lambda :login(self),
                            bg='#FFFFFF', cursor='hand2', activebackground='#D1D0CE', fg='#000000')
        self.login.place(x=23, y=10)
        # ==========Sign Up===================
        self.lgn_button = Image.open('images/3.jpg')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=870, y=550)
        self.login = Button(self.lgn_button_label, text='Sign Up', font=('yu gothic ui', 13, 'bold'),
                            width=10, bd=0, command=lambda: controller.show_frame(SignupWin),
                            bg='#FFFFFF', cursor='hand2', activebackground='#D1D0CE', fg='#000000')
        self.login.place(x=23, y=10)
    
class SignupWin(Frame):
    
    def __init__(self, window,controller):
        Frame.__init__(self, window)
        self.hide_button = None
        self.controller = controller
       
        #=================================
        #self.Sign_Email = StringVar()
        self.Password =StringVar()
        self.Cpass = StringVar()
        self.Sign = StringVar()
       


        #============ Insert Data ============
        def addData(self):
            con = sqlite3.connect('money.db')
            self.email = self.controller.shared_email['signUp_email'].get()

            if not self.email or not self.Password.get() :
                mb.showerror("Sqlite Connector", "Enter Correct Details")
            elif self.Password.get() != self.Cpass.get() and self.Cpass.get() != self.Password.get():
                mb.showerror("Please confirm your password")
            else:

                cursor = con.cursor()
                cursor.execute("INSERT INTO account (Email,Password) VALUES(?,?)",(self.email, self.Password.get(), ))
                con.commit()
                mb.showinfo('Success','Sign Up successfully')
                controller.show_frame(SecurityQuestion)
         
        

        #======combine function==========
        def combine_funcs(*funcs):

            # this function will call the passed functions
            # with the arguments that are passed to the functions
            def inner_combined_func(*args, **kwargs):
                for f in funcs:
                    # Calling functions with arguments, if any
                    f(*args, **kwargs)

            # returning the reference of inner_combined_func
            # this reference will have the called result of all
            # the functions that are passed to the combined_funcs
            return inner_combined_func





        # ================= Sign up Frame =================
        self.lgn_frame = Frame(self, bg='#FFFFFF', width='900', height='718')  # Color and the size of the frame
        self.lgn_frame.pack()  # Placement of the frame
        #============== Title ===========================
        self.password_label = Label(self.lgn_frame, text='Sign Up Here', bg='#FFFFFF', font=('yu gothic ui', 28, 'bold'),
                                    fg='#000000')
        self.password_label.place(x=345, y=75)

        #========== Email =================
        self.email_label = Label(self.lgn_frame, text='Email', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
                                 fg='#000000')
        self.email_label.place(x=300, y=175)
        self.email_icon = Image.open('images/UsernameBar.jpg')
        photo = ImageTk.PhotoImage(self.email_icon)
        self.email_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.email_icon_label.image = photo
        self.email_icon_label.place(x=300, y=215)
        self.email_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#FFFFFF', fg='#000000',
                                 font=('yu gothic ui', 13, 'bold'), textvariable=self.controller.shared_email['signUp_email'])
        self.email_entry.place(x=305, y=225, width=270)
        #============ Password ===========
        self.pass_label = Label(self.lgn_frame, text='Password', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
                                 fg='#000000')
        self.pass_label.place(x=300, y=275)
        self.pass_icon = Image.open('images/UsernameBar.jpg')
        photo = ImageTk.PhotoImage(self.email_icon)
        self.pass_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.pass_icon_label.image = photo
        self.pass_icon_label.place(x=300, y=315)
        self.pass_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#FFFFFF', fg='#000000',
                                 font=('yu gothic ui', 13, 'bold'), textvariable=self.Password)
        self.pass_entry.place(x=305, y=325, width=270)

        #========== Confirm password ===============
        self.cpass_label = Label(self.lgn_frame, text='Confirm-Password', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
                                fg='#000000')
        self.cpass_label.place(x=300, y=375)
        self.cpass_icon = Image.open('images/UsernameBar.jpg')
        photo = ImageTk.PhotoImage(self.email_icon)
        self.cpass_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.cpass_icon_label.image = photo
        self.cpass_icon_label.place(x=300, y=405)
        self.cpass_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#FFFFFF', fg='#000000',
                                font=('yu gothic ui', 13, 'bold'), textvariable=self.Cpass)
        self.cpass_entry.place(x=305, y=415, width=270)

        #===========Sign up button=================
        self.sign_button = Image.open('images/12.jpg')
        photo = ImageTk.PhotoImage(self.sign_button)
        self.sign_button_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.sign_button_label.image = photo
        self.sign_button_label.place(x=345, y=475)
        self.sign = Button(self.sign_button_label, text='Sign Up', font=('yu gothic ui', 10),
                            width=10, bd=0,bg='#DFDFDF', cursor='hand2', activebackground='#D1D0CE',
                           fg='#000000',command=lambda:addData(self))
        self.sign.place(relx=0.1, rely=0.4)
        
class SelectSQWin(Frame):
    def __init__(self, window,controller):
        self.controller=controller
        Frame.__init__(self, window)
        self.hide_button = None
        
        # self.state('zoomed')  # Maximizing the page
        
        # =================================
        SQuestion = StringVar()
        self.ans = StringVar()
        # ================= Sign up Frame =================
        self.lgn_frame = Frame(self, bg='#FFFFFF', width='900', height='718')  # Color and the size of the frame
        self.lgn_frame.pack()  # Placement of the frame
        # ============== Title ===========================
        self.SQ_label = Label(self.lgn_frame, text='Select Security Question', bg='#FFFFFF',
                                    font=('yu gothic ui', 32, 'bold'),
                                    fg='#000000')
        self.SQ_label.place(x=215, y=55)
        # ========== Select Question =================
        self.SQ_label = Label(self.lgn_frame, text='Choose here', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
                                 fg='#000000')
        self.SQ_label.place(x=200, y=175)
        self.cboSQ = ttk.Combobox(self.lgn_frame, font=('arial', 12, 'bold'), width=42, state='readonly',
                                  textvariable=SQuestion)
        self.cboSQ['values'] = ('1', '2', '3')
        self.cboSQ.current(0)
        self.cboSQ.place(x=240,y=210)

        #========== Answer ===========
        self.ans_icon = Image.open('images/14.jpg')
        photo = ImageTk.PhotoImage(self.ans_icon)
        self.ans_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.ans_icon_label.image = photo
        self.ans_icon_label.place(x=230, y=300)
        self.ans_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#FFFFFF', fg='#000000',
                                    font=('yu gothic ui', 13, 'bold'), textvariable=self.ans)
        self.ans_entry.place(x=235, y=325, width=430)

        # ===========Next button=================
        self.Next_button = Image.open('images/12.jpg')
        photo = ImageTk.PhotoImage(self.Next_button)
        self.Next_button_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.Next_button_label.image = photo
        self.Next_button_label.place(x=345, y=525)
        self.Next = Button(self.Next_button_label, text='Finish', font=('yu gothic ui', 16, 'bold'),
                           width=10, bd=0,
                           bg='#DCDCDC', cursor='hand2', activebackground='#D1D0CE', fg='#000000')
        self.Next.place(x=32, y=10)

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
        self.lgn_frame = Frame(self, bg='#FFFFFF', width='900', height='718')  # Color and the size of the frame
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

        # ================= Frame 1 =================
        self.a_frame = Frame(self, bg='#FFFFFF', width='450', height='650')  # Color and the size of the frame
        self.a_frame.place(x=100, y=230)  # Placement of the frame

        # ================= Frame 2 =================
        self.b_frame = Frame(self, bg='#FFFFFF', width='450', height='650')  # Color and the size of the frame
        self.b_frame.place(x=700, y=230)  # Placement of the frame

        # ================ Frame 3 =================
        self.c_frame = Frame(self, bg='#FFFFFF', width='450', height='650')  # Color and the size of the frame
        self.c_frame.place(x=1300, y=230)  # Placement of the frame

        # ============ Add Transaction ====================
        self.agn_button = Image.open('images/addb.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self, image=photo, bg='#11DD7B')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=30, y=125)
        

        self.acc = Button(self.agn_button_label, text='Add Transaction', font=('yu gothic ui', 13, 'bold'), width=15, bd=0,
                          bg='#11DD7B', cursor='hand2', activebackground='#11DD7B', fg='white',command= lambda:open_add(self))
        self.acc.place(x=50, y=5)

        #===============================
        self.Income_label = Label(self.a_frame, text='Income', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
                                 fg='#000000')
        self.Income_label.place(x=16, y=10)

        self.Expenses_label = Label(self.b_frame, text='Expenses', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
                                  fg='#000000')
        self.Expenses_label.place(x=16, y=10)

        self.Savings_label = Label(self.c_frame, text='Savings', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
                                  fg='#000000')
        self.Savings_label.place(x=16, y=10)
        #==============================
        self.agn_button = Image.open('images/16.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.a_frame, image=photo, bg='#FFFFFF')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=0, y=305)
        self.acc = Button(self.agn_button_label, text='Home', font=('yu gothic ui', 13, 'bold'), width=15,
                          bd=0,
                          bg='#FFFFFF', cursor='hand2', activebackground='#DCDCDC', fg='#000000')
        self.acc.place(x=70, y=8)
        self.ac = Button(self.agn_button_label, text='-100MYR', font=('yu gothic ui', 13, 'bold'), width=10,
                         bd=0,
                         bg='#FFFFFF', cursor='hand2', activebackground='#FFFFFF', fg='#C11B17')
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
        self.agn_button_label = Label(self.a_frame, image=photo, bg='#000000')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=20, y=375)

        self.agn_button = Image.open('images/16.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.a_frame, image=photo, bg='#FFFFFF')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=0, y=418)
        self.acc = Button(self.agn_button_label, text='Home', font=('yu gothic ui', 13, 'bold'), width=15,
                          bd=0,
                          bg='#FFFFFF', cursor='hand2', activebackground='#DCDCDC', fg='#000000')
        self.acc.place(x=70, y=8)
        self.ac = Button(self.agn_button_label, text='-100MYR', font=('yu gothic ui', 13, 'bold'), width=10,
                          bd=0,
                          bg='#FFFFFF', cursor='hand2', activebackground='#FFFFFF', fg='#C11B17')
        self.ac.place(x=330, y=8)

        self.agn_button = Image.open('images/4.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.a_frame, image=photo, bg='#000000')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=20, y=431)

        #======B frame detail========
        # ==============================
        self.agn_button = Image.open('images/16.jpg')
        photo = ImageTk.PhotoImage(self.agn_button)
        self.agn_button_label = Label(self.b_frame, image=photo, bg='#FFFFFF')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=0, y=305)
        self.acc = Button(self.agn_button_label, text='Home', font=('yu gothic ui', 13, 'bold'), width=15,
                          bd=0,
                          bg='#FFFFFF', cursor='hand2', activebackground='#DCDCDC', fg='#000000')
        self.acc.place(x=70, y=8)
        self.ac = Button(self.agn_button_label, text='-100MYR', font=('yu gothic ui', 13, 'bold'), width=10,
                         bd=0,
                         bg='#FFFFFF', cursor='hand2', activebackground='#FFFFFF', fg='#C11B17')
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
        self.acc = Button(self.agn_button_label, text='Home', font=('yu gothic ui', 13, 'bold'), width=15,
                          bd=0,
                          bg='#FFFFFF', cursor='hand2', activebackground='#DCDCDC', fg='#000000')
        self.acc.place(x=70, y=8)
        self.ac = Button(self.agn_button_label, text='-100MYR', font=('yu gothic ui', 13, 'bold'), width=10,
                         bd=0,
                         bg='#FFFFFF', cursor='hand2', activebackground='#FFFFFF', fg='#C11B17')
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
        self.acc = Button(self.agn_button_label, text='Home', font=('yu gothic ui', 13, 'bold'), width=15,
                          bd=0,
                          bg='#FFFFFF', cursor='hand2', activebackground='#DCDCDC', fg='#000000')
        self.acc.place(x=70, y=8)
        self.ac = Button(self.agn_button_label, text='-100MYR', font=('yu gothic ui', 13, 'bold'), width=10,
                         bd=0,
                         bg='#FFFFFF', cursor='hand2', activebackground='#FFFFFF', fg='#C11B17')
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
        self.acc = Button(self.agn_button_label, text='Home', font=('yu gothic ui', 13, 'bold'), width=15,
                          bd=0,
                          bg='#FFFFFF', cursor='hand2', activebackground='#DCDCDC', fg='#000000')
        self.acc.place(x=70, y=8)
        self.ac = Button(self.agn_button_label, text='-100MYR', font=('yu gothic ui', 13, 'bold'), width=10,
                         bd=0,
                         bg='#FFFFFF', cursor='hand2', activebackground='#FFFFFF', fg='#C11B17')
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
        self.acc = Button(self.agn_button_label, text='Home', font=('yu gothic ui', 13, 'bold'), width=15,
                          bd=0,
                          bg='#FFFFFF', cursor='hand2', activebackground='#DCDCDC', fg='#000000')
        self.acc.place(x=70, y=8)
        self.ac = Button(self.agn_button_label, text='-100MYR', font=('yu gothic ui', 13, 'bold'), width=10,
                         bd=0,
                         bg='#FFFFFF', cursor='hand2', activebackground='#FFFFFF', fg='#C11B17')
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
        self.acc = Button(self.agn_button_label, text='Home', font=('yu gothic ui', 13, 'bold'), width=15,
                          bd=0,
                          bg='#FFFFFF', cursor='hand2', activebackground='#DCDCDC', fg='#000000')
        self.acc.place(x=70, y=8)
        self.ac = Button(self.agn_button_label, text='-100MYR', font=('yu gothic ui', 13, 'bold'), width=10,
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
        self.acc = Button(self.agn_button_label, text='Home', font=('yu gothic ui', 13, 'bold'), width=15,
                          bd=0,
                          bg='#FFFFFF', cursor='hand2', activebackground='#DCDCDC', fg='#000000')
        self.acc.place(x=70, y=8)
        self.ac = Button(self.agn_button_label, text='-100MYR', font=('yu gothic ui', 13, 'bold'), width=10,
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
        

        def display_profile(self):
            
                email = self.email_strvar
                conn = sqlite3.connect('money.db')
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM account WHERE Email LIKE ?',(self.controller.shared_email['Login_email'].get(), ))
                data = cursor.fetchall()
                print(data)
                email.set(data[0][0]),self.password_strvar.set(data[0][1]),self.name_strvar.set(data[0][2]),self.gender_strvar.set(data[0][3])
        
        #======== Define Frame=======
       
        self.navbar_frame= Frame(self,bg='#ffffff',width=self.width,height='50')
        self.navbar_frame.pack()
        self.accountcard_frame=Frame(self,bg='#ffffff',width='500',height='600')
        self.accountcard_frame.pack(pady=50)
        
        #======Nav bar======
        self.overview_label = Label(self.navbar_frame,bg='#FFFFFF',text='Overview',font=("yu gothic ui",16),fg='#11DD7B',cursor="hand2")
        self.overview_label.place(x=450,y=11)
        self.overview_label.bind("<Button-1>",lambda e:controller.show_frame(Homepage))
        self.transaction_label = Label(self.navbar_frame,bg='#FFFFFF',text='Transaction',font=("yu gothic ui",16),fg='#11DD7B',cursor="hand2")
        self.transaction_label.place(x=650,y=11)
        self.transaction_label.bind("<Button-1>",lambda e:controller.show_frame(TransactionTable))
        self.accountsetting_label = Label(self.navbar_frame,bg='#FFFFFF',text='Account Setting',font=("yu gothic ui",16),fg='#11DD7B',cursor="hand2")
        self.accountsetting_label.place(x=850,y=11)
        
        self.tips_label = Label(self.navbar_frame,bg='#FFFFFF',text='Tips',font=("yu gothic ui",16),fg='#11DD7B',cursor="hand2")
        self.tips_label.place(x=1090,y=11)
        self.tips_label.bind("<Button-1>")

    
        #===== Account card=====
        #=====Name Entry======
        Button(self.accountcard_frame,text='show',width=10,command= lambda:display_profile(self)).place(x=60,y=60)
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

        #=====Password label and entry===
        self.password_label =Label(self.accountcard_frame,text='Password',font=labelfont,bg='#ffffff')
        self.password_label.place(x=60,y=400)
        self.password_entry_label = Label(self.accountcard_frame,image=img,bg='#ffffff')
        self.password_entry_label.image=img
        self.password_entry_label.place(relx=0.5,rely=0.67)
        self.password_entry = Entry(self.accountcard_frame,width=19,bg='#D9D9D9',font= entryfont,highlightthickness=0, relief=FLAT,textvariable=self.password_strvar)
        self.password_entry.place(relx=0.51,rely=0.685)

        #======Button=======
        self.save_btn_img = Image.open('images/31.jpg')
        save_btn_img = ImageTk.PhotoImage(self.save_btn_img)
        self.save_btn_label = Label(self.accountcard_frame,image=save_btn_img,bg='#ffffff',cursor='hand2')
        self.save_btn_label.image = save_btn_img
        self.save_btn_label.place(relx=0.2,rely=0.8)
        self.save_label = Label(self.accountcard_frame,text='Save',bg='#D9D9D9',font=btnfont,cursor='hand2')
        self.save_label.place(relx=0.3,rely=0.81)
        self.save_label.bind('<Button-1>',lambda e:controller.saveChange())

        self.reset_btn_img = Image.open('images/resetpassword.jpg')
        reset_btn_img = ImageTk.PhotoImage(self.reset_btn_img)
        self.reset_btn_img = Label(self.accountcard_frame,image=reset_btn_img,bg='#FFFFFF')
        self.reset_btn_img.image = reset_btn_img
        self.reset_btn_img.place(relx=0.56,rely=0.8)
        self.reset_label = Label(self.accountcard_frame,text='Reset Password',font=btnfont,bg='#D9D9D9',cursor='hand2')
        self.reset_label.place(relx=0.63,rely=0.81)
        self.reset_label.bind("<Button-1>",lambda e:controller.show_frame(SecurityQuestion))
        
class SecurityQuestion(Frame):
    def __init__(self, window,controller):
        Frame.__init__(self, window)
        self.controller=controller
       

        def add_question(self):
            
            email = self.controller.shared_email['Login_email'].get()
            conn = sqlite3.connect('money.db')
            cursor = conn.cursor()
            if not self.first.get() or not self.second.get() or not self.third.get():
                mb.showerror('Error','Please answer all the questions')
            else:
                cursor.execute("INSERT INTO Security_Question(Email,Questions,Answer) VALUES(?,?,?)",(email,'What do you live?',self.first.get()))
                conn.commit()
                mb.showinfo('Success','Commit Success!')
                controller.show_frame(LoginForm)

        self.Question =Frame(self,bg='#FFFFFF',width='900',height='800')
        self.Question.pack(pady=50)
        
        
        self.first = StringVar()
        self.second = StringVar()
        self.third = StringVar()
        self.Next = StringVar()
        # ================= Sign up Frame =================
        self.lgn_frame = Frame(self, bg='#FFFFFF', width='900', height='718')  # Color and the size of the frame
        self.lgn_frame.place(x=0, y=0)  # Placement of the frame
        # ============== Title ===========================
        self.SQ_label = Label(self.lgn_frame, text='Set Security Question', bg='#FFFFFF',
                                    font=('yu gothic ui', 32, 'bold'),
                                    fg='#000000')
        self.SQ_label.place(x=255, y=55)
        # ========== 1st Question =================
        self.first_label = Label(self.lgn_frame, text='Where do you live?', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
                                 fg='#000000')
        self.first_label.place(x=300, y=175)
        self.first_icon = Image.open('images/UsernameBar.jpg')
        photo = ImageTk.PhotoImage(self.first_icon)
        self.first_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.first_icon_label.image = photo
        self.first_icon_label.place(x=300, y=215)
        self.first_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#FFFFFF', fg='#000000',
                                 font=('yu gothic ui', 13, 'bold'), textvariable=self.first)
        self.first_entry.place(x=305, y=225, width=270)

        # ========== 2nd Question =================
        self.second_label = Label(self.lgn_frame, text='What is your primary school?', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
                                 fg='#000000')
        self.second_label.place(x=300, y=275)
        self.second_icon = Image.open('images/UsernameBar.jpg')
        photo = ImageTk.PhotoImage(self.first_icon)
        self.second_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.second_icon_label.image = photo
        self.second_icon_label.place(x=300, y=315)
        self.second_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#FFFFFF', fg='#000000',
                                 font=('yu gothic ui', 13, 'bold'), textvariable=self.second)
        self.second_entry.place(x=305, y=325, width=270)

        # ========== 3rd Question =================
        self.third_label = Label(self.lgn_frame, text='What is your father name?', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
                                  fg='#000000')
        self.third_label.place(x=300, y=375)
        self.third_icon = Image.open('images/UsernameBar.jpg')
        photo = ImageTk.PhotoImage(self.first_icon)
        self.third_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.third_icon_label.image = photo
        self.third_icon_label.place(x=300, y=415)
        self.third_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#FFFFFF', fg='#000000',
                                  font=('yu gothic ui', 13, 'bold'), textvariable=self.third)
        self.third_entry.place(x=305, y=425, width=270)

        # ===========Next button=================
        self.Next_button = Image.open('images/12.jpg')
        photo = ImageTk.PhotoImage(self.Next_button)
        self.Next_button_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.Next_button_label.image = photo
        self.Next_button_label.place(x=345, y=525)
        self.Next = Button(self.Next_button_label, text='Finish', font=('yu gothic ui', 16, 'bold'),
                           width=10, bd=0,
                           bg='#DCDCDC', cursor='hand2', activebackground='#D1D0CE', fg='#000000',command= lambda :add_question(self))
        self.Next.place(x=32, y=10)

class ResetPass(Frame):
    def __init__(self,ResetWindow,controller) :
        Frame.__init__(self, ResetWindow)
        self.controller=controller
        #open Top level window
        def open(self):
            window = AddTransaction(self)
            window.grab_set()

        self.Reset =Frame(self,bg='#FFFFFF',width='900',height='800')
        self.Reset.pack(pady=40)

        self.head_label = Label(self.Reset,text='Reset Password',font=headfont,bg='#FFFFFF')
        self.head_label.place(relx=0.42,rely=0.2)

        self.pass_label = Label(self.Reset,text='Password',bg='#FFFFFF',font=labelfont)
        self.pass_label.place(relx=0.35,rely=0.3)
        self.pass_box = Image.open('images/32.jpg')
        pass_box_img = ImageTk.PhotoImage(self.pass_box)
        self.pass_box = Label(self.Reset,image=pass_box_img,bg='#FFFFFF')
        self.pass_box.image=pass_box_img
        self.pass_box.place(relx=0.35,rely=0.35)
        self.pass_entry = Entry(self.Reset,width=29,bg='#FFFFFF',font= entryfont,highlightthickness=0, relief=FLAT)
        self.pass_entry.place(relx=0.36,rely=0.36)

        self.repass_label =Label(self.Reset,text='Confirm Password',bg='#FFFFFF',font=labelfont)
        self.repass_label.place(relx=0.35,rely=0.4)
        self.repass_box = Image.open('images/32.jpg')
        self.repass_box = Label(self.Reset,image=pass_box_img,bg='#FFFFFF')
        self.repass_box.image=pass_box_img
        self.repass_box.place(relx=0.35,rely=0.45)
        self.repass_entry = Entry(self.Reset,width=29,bg='#FFFFFF',font= entryfont,highlightthickness=0, relief=FLAT)
        self.repass_entry.place(relx=0.36,rely=0.46)

        self.resetbtn_img =Image.open('images/31.jpg')
        resetbtn = ImageTk.PhotoImage(self.resetbtn_img)
        self.resetbtn = Label(self.Reset,image=resetbtn,bg='#FFFFFF')
        self.resetbtn.image = resetbtn
        self.resetbtn.place(relx=0.43,rely=0.58)
        self.reset_label = Label(self.Reset,text='Reset',bg='#D9D9D9',cursor='hand2',font=btnfont)
        self.reset_label.place(relx=0.48,rely=0.59)
        self.reset_label.bind('<Button-1>',lambda e: controller.show_frame(SecurityQuestion))

class AddTransaction(Toplevel):
    def __init__(self,window,controller):
        Toplevel.__init__(self,window)
        self.geometry('1000x500')
        category_list =['Food&Drink','Cars','Home','Shopping']
        currency_list = ['MYR','USD','CAD','EUR','SG','CNH','JPY','GBP','CHF','AUD']

        self.controller= controller
        self.resizable(0,0)

        def add(self):
            email = self.controller.shared_email['Login_email'].get()
            
            self.category = self.category.get()
            self.note = self.note.get()
            self.amount = self.amount.get()
            self.currency = self.currency.get()
            self.date = self.date.get_date()

            conn = sqlite3.connect('money.db')
            cursor = conn.cursor()
            
            if not self.category or not self.amount or not self.currency :
                mb.showerror('Error','Please fill in the blank!')
            elif self.amount <= 0:
                mb.showerror('Error','The amount cannot less than zero!')
            else:
                cursor.execute('INSERT INTO Transaction_record (Email,Category,Date,Note,Amount,Currency) VALUES(?,?,?,?,?,?)',(email,self.category,self.date,self.note,self.amount,self.currency))
                conn.commit()
                mb.showinfo('Success','Commit success')

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

        
        currency = Combobox(self.Add,width=5,values=currency_list,state='readonly',textvariable=self.currency)
        currency.place(relx=0.74,rely=0.125)

   
        self.add_btn = Button(self.Add,bg='#11DD7B',fg='#FFFFFF',width=15,cursor='hand2',command=lambda:add(self),text='Add Transaction',bd=0,font=('yu gothic ui',10,'bold'))
        self.add_btn.place(relx=0.667,rely=0.255)

class TransactionTable(Frame):       
    def __init__(self,window,controller) :
        Frame.__init__(self,window)
        self.controller = controller 

        
        def display_record(self):
            email = self.controller.shared_email['Login_email'].get()
            self.tree.delete(*self.tree.get_children())
            conn = sqlite3.connect('money.db')
            cursor =conn.cursor()
            cursor.execute('SELECT * FROM Transaction_record WHERE Email =?',(email,))
            data =cursor.fetchall()
            for record in data:
                self.tree.insert('',END,values=record)
        
        self.table_frame =Frame(self,bg='#FFFFFF',width='1520',height='800')
        self.table_frame.pack()

        self.navbar_frame = Frame(self, bg='#ffffff', width='1500', height='65')
        self.navbar_frame.place(x=0, y=5)

        # ======Nav bar======
        self.overview_label = Label(self.navbar_frame, bg='#FFFFFF', text='Overview', font=("yu gothic ui", 14),
                                    fg='#11DD7B', cursor="hand2")
        self.overview_label.place(x=450, y=11)
        self.overview_label.bind("<Button-1>",lambda e: controller.show_frame(Homepage))

        self.transaction_label = Label(self.navbar_frame, bg='#FFFFFF', text='Transaction', font=("yu gothic ui", 14),
                                       fg='#11DD7B', cursor="hand2")
        self.transaction_label.place(x=750, y=11)
        self.transaction_label.bind("<Button-1>",lambda e: controller.show_frame(TransactionTable))

        self.accountsetting_label = Label(self.navbar_frame, bg='#FFFFFF', text='Account Setting',
                                          font=("yu gothic ui", 14), fg='#11DD7B', cursor="hand2")
        self.accountsetting_label.place(x=1050, y=11)
        self.accountsetting_label.bind('<Button-1>',lambda e: controller.show_frame(AccountPage))

        self.tips_label = Label(self.navbar_frame, bg='#FFFFFF', text='Tips', font=("yu gothic ui", 14),
                                    fg='#11DD7B', cursor="hand2")
        self.tips_label.place(x=1390, y=11)

        self.show = Button(self.table_frame,width=10,text='Show',font=labelfont,command=lambda:display_record(self))
        self.show.place(x=200,y=60)

        self.tree = Treeview(self.table_frame, height=100, selectmode=BROWSE,
                                columns=('Category', 'Date', "Note","Amount", "Currency" ))
        X_scroller = Scrollbar(self.tree, orient=HORIZONTAL, command=self.tree.xview)
        Y_scroller = Scrollbar(self.tree, orient=VERTICAL, command=self.tree.yview)
        X_scroller.pack(side=BOTTOM, fill=X)
        Y_scroller.pack(side=RIGHT, fill=Y)
        self.tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
        self.tree.heading('Category', text='Category', anchor=CENTER)
        self.tree.heading('Date', text='Date', anchor=CENTER)
        self.tree.heading('Note', text='Note', anchor=CENTER)
        self.tree.heading('Amount', text='Amount', anchor=CENTER)
        self.tree.heading('Currency', text='Currency', anchor=CENTER)


        self.tree.column('#0', width=10, stretch=NO,anchor=CENTER)
        self.tree.column('#1', width=70, stretch=NO,anchor=CENTER)
        self.tree.column('#2', width=100, stretch=NO,anchor=CENTER)
        self.tree.column('#3', width=150, stretch=NO,anchor=CENTER)
        self.tree.column('#4', width=80, stretch=NO,anchor=CENTER)
        self.tree.column('#5', width=80, stretch=NO,anchor=CENTER)

       
        self.tree.place(y=120, relwidth=1, relheight=0.9, relx=0)
       
    
def page():
    app =windows()
    app.mainloop()
    
    

if __name__ == '__main__':
    page()