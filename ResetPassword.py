from tkinter import *
from PIL import ImageTk, Image  # pip install pillow
from PIL.ImageTk import PhotoImage
import tkinter.messagebox
from tkinter import ttk
import tkinter.messagebox
import sqlite3

class ResetWin(Frame):
    def __init__(self, window,controller):
        Frame.__init__(self, window)
        self.hide_button = None
        # self.state('zoomed')  # Maximizing the page
        self.resizable(0, 0)  # Delete the restore button
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

def page():
    window = Tk()
    ResetWin(window)
    window.mainloop()

if __name__ == '__main__':
    page()