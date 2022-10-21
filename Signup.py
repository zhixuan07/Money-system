from tkinter import *
from PIL import ImageTk, Image  # pip install pillow
from PIL.ImageTk import PhotoImage
import tkinter.messagebox
from tkinter import ttk
import tkinter.messagebox
import sqlite3
import os

class SignupWin(Frame):
    def __init__(self, window,controller):
        Frame.__init__(self, window)
        self.hide_button = None
        
        #self.state('zoomed')  # Maximizing the page
        self.resizable(0, 0)  # Delete the restore button
        #=================================
        self.Email = StringVar()
        self.Password =StringVar()
        self.Cpass = StringVar()
        self.Sign = StringVar()


        #============ Insert Data ============
        def addData():
            con = sqlite3.connect('money.db')

            if not self.Email.get() or not self.Password.get() :
                tkinter.messagebox.showerror("Sqlite Connector", "Enter Correct Details")
            elif self.Password.get() != self.Cpass.get() and self.Cpass.get() != self.Password.get():
                tkinter.messagebox.showerror("Please confirm your password")
            else:

                cursor = con.cursor()
                cursor.execute("INSERT INTO account (Email,Password) VALUES(?,?)",(self.Email.get(), self.Password.get(), ))
                con.commit()
                con.close()
                show()


        # ===========new page===========
        def show():
            window.destroy()
            os.system("python SecurityQuestion.py")

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
                                 font=('yu gothic ui', 13, 'bold'), textvariable=self.Email)
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
        self.sign_button = Image.open('images/12.jpeg')
        photo = ImageTk.PhotoImage(self.sign_button)
        self.sign_button_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.sign_button_label.image = photo
        self.sign_button_label.place(x=345, y=475)
        self.sign = Button(self.sign_button_label, text='Sign Up', font=('yu gothic ui', 10),
                            width=10, bd=0,bg='#DFDFDF', cursor='hand2', activebackground='#D1D0CE',
                           fg='#000000',command=addData)
        self.sign.place(relx=0.1, rely=0.4)
        #==================

def page():
    window = Tk()
    SignupWin(window)
    window.mainloop()





if __name__ == '__main__':
    page()