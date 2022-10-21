from tkinter import *
from PIL import ImageTk, Image  # pip install pillow
from PIL.ImageTk import PhotoImage
import tkinter.messagebox
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
import sqlite3
import os
import re


class LoginForm:
    def __init__(self, window):
        self.hide_button = None
        self = window
        self.geometry('1166x718')
        #self.state('zoomed')  # Maximizing the page
        self.resizable(0, 0)  # Delete the restore button
        self.UsernameStr=StringVar()
        self.passwordStr=StringVar()

        def check():
            self.Username = self.UsernameStr.get()
            self.password = self.passwordStr.get()
            conn = sqlite3.connect('money.db')
            cursor = conn.cursor()
            cursor.execute("SELECT Email,Password FROM account WHERE Email =? AND Password =?", (self.Username,self.password))
            user_login_list = cursor.fetchall()
            if user_login_list:
                window.destroy()
                tkinter.messagebox.showinfo("Successfully login. ")
                os.system('python HomePage.py')
            else:
                tkinter.messagebox.showinfo("Error")

      


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
                                 font=('yu gothic ui', 13, 'bold'), textvariable=self.UsernameStr)
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
                               font=('yu gothic ui', 13, 'bold'), textvariable=self.passwordStr)
        self.pss_entry.place(x=706, y=395, width=270)

        # ===========Forgot password=================
        self.forgot = Button(text='Forgot Password?', font=('yu gothic ui', 16, 'bold'), width=20, bd=0,
                             bg='#FFFFFF', cursor='hand2', activebackground='#D1D0CE', fg='#728FCE')
        self.forgot.place(x=596, y=445)

        # ===========Login Button==========
        self.lgn_button = Image.open('images/3.jpg')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=670, y=550)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=('yu gothic ui', 13, 'bold'),
                            width=10, bd=0, command=check,
                            bg='#FFFFFF', cursor='hand2', activebackground='#D1D0CE', fg='#000000')
        self.login.place(x=23, y=10)
        # ==========Sign Up===================
        self.lgn_button = Image.open('images/3.jpg')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=870, y=550)
        self.login = Button(self.lgn_button_label, text='Sign Up', font=('yu gothic ui', 13, 'bold'),
                            width=10, bd=0, command=check,
                            bg='#FFFFFF', cursor='hand2', activebackground='#D1D0CE', fg='#000000')
        self.login.place(x=23, y=10)
        #=================================



        def check():
            self.Username = self.UsernameStr.get()
            self.password = self.passwordStr.get()
            conn = sqlite3.connect('money.db')
            cursor = conn.cursor()
            cursor.execute("SELECT Email,Password FROM account WHERE Email =? AND Password =?", (self.Username,self.password))
            user_login_list = cursor.fetchall()
            if user_login_list:
                window.destroy()
                tkinter.messagebox.showinfo("Successfully login. ")
                os.system('python HomePage.py')
            else:
                tkinter.messagebox.showinfo("Error")



       







def page():
    window = Tk()
    LoginForm(window)
    window.mainloop()





if __name__ == '__main__':
    page()

