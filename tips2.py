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
        self.t2_frame = Frame(self.window, bg='#FFFFFF', width='1600', height='700')  # Color and the size of the frame
        self.t2_frame.place(x=150, y=150)  # Placement of the frame

        self.tips2_label = Label(self.t2_frame, text='Selected Tips:', bg='#FFFFFF', font=('yu gothic ui', 20, 'bold'),
                                  fg='#000000')
        self.tips2_label.place(x=16, y=10)

        self.t_frame = Frame(self.t2_frame, bg='#C2DFFF', width='1100', height='600')  # Color and the size of the frame
        self.t_frame.place(x=150, y=55)  # Placement of the frame







        # ===========Back button=================
        self.B_button = Image.open('images/12.jpg')
        photo = ImageTk.PhotoImage(self.B_button)
        self.B_button_label = Label(self.t2_frame, image=photo, bg='#FFFFFF')
        self.B_button_label.image = photo
        self.B_button_label.place(x=1355, y=575)
        self.B = Button(self.B_button_label, text='BACK', font=('yu gothic ui', 16, 'bold'),
                           width=10, bd=0,
                           bg='#DCDCDC', cursor='hand2', activebackground='#D1D0CE', fg='#000000')
        self.B.place(x=32, y=10)









def page():
    window = Tk()
    T1Win(window)
    window.mainloop()

if __name__ == '__main__':
    page()