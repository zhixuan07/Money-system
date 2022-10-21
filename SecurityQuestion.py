from tkinter import *
from PIL import ImageTk, Image  # pip install pillow
from PIL.ImageTk import PhotoImage
import tkinter.messagebox
from tkinter import ttk
import tkinter.messagebox
import sqlite3

class SQWin:
    def __init__(self, window):
        self.hide_button = None
        self = window
        self.geometry('900x718')
        # self.state('zoomed')  # Maximizing the page
        self.resizable(0, 0)  # Delete the restore button
        # =================================
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
        self.first_label = Label(self.lgn_frame, text='Question 1', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
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
        self.second_label = Label(self.lgn_frame, text='Question 2', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
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
        self.third_label = Label(self.lgn_frame, text='Question 3', bg='#FFFFFF', font=('yu gothic ui', 16, 'bold'),
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
        self.Next = Button(self.Next_button_label, text='Next', font=('yu gothic ui', 16, 'bold'),
                           width=10, bd=0,
                           bg='#DCDCDC', cursor='hand2', activebackground='#D1D0CE', fg='#000000')
        self.Next.place(x=32, y=10)

def page():
    window = Tk()
    SQWin(window)
    window.mainloop()

if __name__ == '__main__':
    page()