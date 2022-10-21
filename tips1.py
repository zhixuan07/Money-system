from tkinter import *
from PIL import ImageTk, Image  # pip install pillow
from PIL.ImageTk import PhotoImage
import tkinter.messagebox
from tkinter import ttk
import tkinter.messagebox
import sqlite3
import os

class T1Win:
    def __init__(self, window):
        self.hide_button = None
        self.window = window
        self.window.geometry('900x718')
        self.window.state('zoomed')  # Maximizing the page
        self.window.resizable(0, 0)  # Delete the restore button

        self.width = window.winfo_screenwidth()
        self.height = window.winfo_screenheight()
        self.window.geometry("%dx%d" % (self.width, self.height))
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)

        self.Tips = StringVar()
        self.tips = StringVar()

        # ================== Functions ==================

        # ================= Nav Frame ================
        self.navbar_frame = Frame(window, bg='#ffffff', width=self.width, height='65')
        self.navbar_frame.place(x=0, y=5)

        # ======Nav bar======
        self.overview_label = Label(self.navbar_frame, bg='#FFFFFF', text='Overview', font=("yu gothic ui", 18),
                                    fg='#11DD7B', cursor="hand2")
        self.overview_label.place(x=450, y=11)
        self.overview_label.bind("<Button-1>", lambda e: overview('python ResetPassword.py'))
        self.transaction_label = Label(self.navbar_frame, bg='#FFFFFF', text='Transaction', font=("yu gothic ui", 18),
                                       fg='#11DD7B', cursor="hand2")
        self.transaction_label.place(x=750, y=11)
        self.transaction_label.bind("<Button-1>", lambda e: overview('python SelectSQ.py'))
        self.accountsetting_label = Label(self.navbar_frame, bg='#FFFFFF', text='Account Setting',
                                          font=("yu gothic ui", 18), fg='#11DD7B', cursor="hand2")
        self.accountsetting_label.place(x=1050, y=11)
        self.overview_label = Label(self.navbar_frame, bg='#FFFFFF', text='Tips', font=("yu gothic ui", 18),
                                    fg='#11DD7B', cursor="hand2")
        self.overview_label.place(x=1390, y=11)

        #===================================
        self.t1_frame = Frame(self.window, bg='#FFFFFF', width='1150', height='700')  # Color and the size of the frame
        self.t1_frame.place(x=150, y=150)  # Placement of the frame

        self.tips1_label = Label(self.t1_frame, text='Select your Tips:', bg='#FFFFFF', font=('yu gothic ui', 20, 'bold'),
                                  fg='#000000')
        self.tips1_label.place(x=16, y=10)

        self.Stips_label = Label(self.t1_frame,text='Choose Here',bg='#FFFFFF',font=('yu gothic ui',16,'bold'),fg='#000000')
        self.Stips_label.place(x=200,y=150)


        self.cbotips = ttk.Combobox(self.t1_frame, font=('arial', 12, 'bold'), width=70, state='readonly',
                                  textvariable=self.Tips)
        self.cbotips['values'] = ('1', '2', '3')
        self.cbotips.current(0)
        self.cbotips.place(x=220, y=190)

        #=========Button======
        # =========HomePage Button======
        self.H_button = Image.open('images/12.jpg')
        photo = ImageTk.PhotoImage(self.H_button)
        self.H_button_label = Label(self.t1_frame, image=photo, bg='#FFFFFF')
        self.H_button_label.image = photo
        self.H_button_label.place(x=905, y=55)
        self.H = Button(self.H_button_label, text='Homepage', font=('yu gothic ui', 16, 'bold'),
                        width=10, bd=0,
                        bg='#DCDCDC', cursor='hand2', activebackground='#D1D0CE', fg='#000000')
        self.H.place(x=32, y=10)
        # ===========Next button=================
        self.Ok_button = Image.open('images/12.jpg')
        photo = ImageTk.PhotoImage(self.Ok_button)
        self.Ok_button_label = Label(self.t1_frame, image=photo, bg='#FFFFFF')
        self.Ok_button_label.image = photo
        self.Ok_button_label.place(x=905, y=575)
        self.Ok = Button(self.Ok_button_label, text='OK', font=('yu gothic ui', 16, 'bold'),
                           width=10, bd=0,
                           bg='#DCDCDC', cursor='hand2', activebackground='#D1D0CE', fg='#000000')
        self.Ok.place(x=32, y=10)









def page():
    window = Tk()
    T1Win(window)
    window.mainloop()

if __name__ == '__main__':
    page()