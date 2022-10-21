from tkinter import *
from PIL import ImageTk, Image  # pip install pillow
from PIL.ImageTk import PhotoImage
import tkinter.messagebox
from tkinter import ttk
import tkinter.messagebox
import sqlite3

class SelectSQWin(Frame):
    def __init__(self, window,controller):
        Frame.__init__(self, window)
        self.hide_button = None
        
        # self.state('zoomed')  # Maximizing the page
        self.resizable(0, 0)  # Delete the restore button
        # =================================
        SQuestion = StringVar()
        self.ans = StringVar()
        # ================= Sign up Frame =================
        self.lgn_frame = Frame(self, bg='#FFFFFF', width='900', height='718')  # Color and the size of the frame
        self.lgn_frame.place(x=0, y=0)  # Placement of the frame
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
        self.Next = Button(self.Next_button_label, text='Next', font=('yu gothic ui', 16, 'bold'),
                           width=10, bd=0,
                           bg='#DCDCDC', cursor='hand2', activebackground='#D1D0CE', fg='#000000')
        self.Next.place(x=32, y=10)

def page():
    window = Tk()
    SelectSQWin(window)
    window.mainloop()

if __name__ == '__main__':
    page()