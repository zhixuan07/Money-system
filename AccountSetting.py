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
entryfont=("yu gothic ui",12)
btnfont=('yu gothic ui',12)
headfont=('yu gothic ui',14,'bold')




class AccountPage:
    def __init__(self,window):
        self.hide_button = None
        self = window
        self.width= window.winfo_screenwidth()
        self.height= window.winfo_screenheight()
        self.geometry("%dx%d" % (self.width, self.height))
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)

        def overview(path):
            window.destroy()
            os.system(path)

        def QuestionPage():
            self = Toplevel()
            self.app = SecurityQuestion(self)

        #======== Define Frame=======
        self.navbar_frame= Frame(window,bg='#ffffff',width=self.width,height='50')
        self.navbar_frame.place(x=0,y=10)
        self.accountcard_frame=Frame(window,bg='#ffffff',width='500',height='600')
        self.accountcard_frame.place(x=500,y=150)
        
        #======Nav bar======
        self.overview_label = Label(self.navbar_frame,bg='#FFFFFF',text='Overview',font=("yu gothic ui",16),fg='#11DD7B',cursor="hand2")
        self.overview_label.place(x=450,y=11)
        self.overview_label.bind("<Button-1>",lambda e:overview('python ResetPassword.py'))
        self.transaction_label = Label(self.navbar_frame,bg='#FFFFFF',text='Transaction',font=("yu gothic ui",16),fg='#11DD7B',cursor="hand2")
        self.transaction_label.place(x=650,y=11)
        self.transaction_label.bind("<Button-1>",lambda e:overview('python SelectSQ.py'))
        self.accountsetting_label = Label(self.navbar_frame,bg='#FFFFFF',text='Account Setting',font=("yu gothic ui",16),fg='#11DD7B',cursor="hand2")
        self.accountsetting_label.place(x=850,y=11)
        self.overview_label = Label(self.navbar_frame,bg='#FFFFFF',text='Tips',font=("yu gothic ui",16),fg='#11DD7B',cursor="hand2")
        self.overview_label.place(x=1090,y=11)

        #===== Account card=====
        #=====Name Entry======
        self.label_img =Image.open('images/27.jpg')
        img = ImageTk.PhotoImage(self.label_img)
        self.name_label =Label(self.accountcard_frame,text='Name',font=labelfont,bg='#ffffff')
        self.name_label.place(x=60,y=100)
        self.name_entry_label = Label(self.accountcard_frame,image=img,bg='#ffffff')
        self.name_entry_label.image=img
        self.name_entry_label.place(relx=0.5,rely=0.165)
        self.name_entry = Entry(self.accountcard_frame,width=19,bg='#D9D9D9',font= entryfont,highlightthickness=0, relief=FLAT)
        self.name_entry.place(relx=0.51,rely=0.18)

        #=====Email label and entry======
        self.email_label =Label(self.accountcard_frame,text='Email',font=labelfont,bg='#ffffff')
        self.email_label.place(x=60,y=200)
        self.email_entry_label = Label(self.accountcard_frame,image=img,bg='#ffffff')
        self.email_entry_label.image=img
        self.email_entry_label.place(relx=0.5,rely=0.33)
        self.email_entry = Entry(self.accountcard_frame,width=19,bg='#D9D9D9',font= entryfont,highlightthickness=0, relief=FLAT)
        self.email_entry.place(relx=0.51,rely=0.345)

        #=====Gender label and entry=====
        self.gender_label =Label(self.accountcard_frame,text='Gender',font=labelfont,bg='#ffffff')
        self.gender_label.place(x=60,y=300)
        self.gender_entry_label = Label(self.accountcard_frame,image=img,bg='#ffffff')
        self.gender_entry_label.image=img
        self.gender_entry_label.place(relx=0.5,rely=0.5)
        self.gender_entry = Entry(self.accountcard_frame,width=19,bg='#D9D9D9',font= entryfont,highlightthickness=0, relief=FLAT)
        self.gender_entry.place(relx=0.51,rely=0.515)

        #=====Password label and entry===
        self.password_label =Label(self.accountcard_frame,text='Password',font=labelfont,bg='#ffffff')
        self.password_label.place(x=60,y=400)
        self.password_entry_label = Label(self.accountcard_frame,image=img,bg='#ffffff')
        self.password_entry_label.image=img
        self.password_entry_label.place(relx=0.5,rely=0.67)
        self.password_entry = Entry(self.accountcard_frame,width=19,bg='#D9D9D9',font= entryfont,highlightthickness=0, relief=FLAT)
        self.password_entry.place(relx=0.51,rely=0.685)

        #======Button=======
        self.save_btn_img = Image.open('images/31.jpg')
        save_btn_img = ImageTk.PhotoImage(self.save_btn_img)
        self.save_btn_label = Label(self.accountcard_frame,image=save_btn_img,bg='#ffffff',cursor='hand2')
        self.save_btn_label.image = save_btn_img
        self.save_btn_label.place(relx=0.2,rely=0.8)
        self.save_label = Label(self.accountcard_frame,text='Save',bg='#D9D9D9',font=btnfont,cursor='hand2')
        self.save_label.place(relx=0.3,rely=0.81)

        self.reset_btn_img = Image.open('images/resetpassword.jpg')
        reset_btn_img = ImageTk.PhotoImage(self.reset_btn_img)
        self.reset_btn_img = Label(self.accountcard_frame,image=reset_btn_img,bg='#FFFFFF')
        self.reset_btn_img.image = reset_btn_img
        self.reset_btn_img.place(relx=0.56,rely=0.8)
        self.reset_label = Label(self.accountcard_frame,text='Reset Password',font=btnfont,bg='#D9D9D9',cursor='hand2')
        self.reset_label.place(relx=0.63,rely=0.81)
        self.reset_label.bind("<Button-1>",lambda e:QuestionPage())
        

class AccountSetting:
    def __init__(self,window):
       

        def overview(path):
            window.destroy()
            os.system(path)

        #======== Define Frame=======
        self.navbar_frame= Frame(self,bg='#ffffff',width=self.width,height='50')
        self.navbar_frame.place(x=0,y=10)
        self.accountcard_frame=Frame(self,bg='#ffffff',width='500',height='600')
        self.accountcard_frame.place(x=500,y=150)
        
        #======Nav bar======
        self.overview_label = Label(self.navbar_frame,bg='#FFFFFF',text='Overview',font=("yu gothic ui",16),fg='#11DD7B',cursor="hand2")
        self.overview_label.place(x=450,y=11)
        self.overview_label.bind("<Button-1>",lambda e:overview('python ResetPassword.py'))
        self.transaction_label = Label(self.navbar_frame,bg='#FFFFFF',text='Transaction',font=("yu gothic ui",16),fg='#11DD7B',cursor="hand2")
        self.transaction_label.place(x=650,y=11)
        self.transaction_label.bind("<Button-1>",lambda e:overview('python SelectSQ.py'))
        self.accountsetting_label = Label(self.navbar_frame,bg='#FFFFFF',text='Account Setting',font=("yu gothic ui",16),fg='#11DD7B',cursor="hand2")
        self.accountsetting_label.place(x=850,y=11)
        self.overview_label = Label(self.navbar_frame,bg='#FFFFFF',text='Tips',font=("yu gothic ui",16),fg='#11DD7B',cursor="hand2")
        self.overview_label.place(x=1090,y=11)

        #===== Account card=====
        #=====Name Entry======
        self.label_img =Image.open('images/27.jpg')
        img = ImageTk.PhotoImage(self.label_img)
        self.name_label =Label(self.accountcard_frame,text='Name',font=labelfont,bg='#ffffff')
        self.name_label.place(x=60,y=100)
        self.name_entry_label = Label(self.accountcard_frame,image=img,bg='#ffffff')
        self.name_entry_label.image=img
        self.name_entry_label.place(relx=0.5,rely=0.165)
        self.name_entry = Entry(self.accountcard_frame,width=19,bg='#D9D9D9',font= entryfont,highlightthickness=0, relief=FLAT)
        self.name_entry.place(relx=0.51,rely=0.18)

        #=====Email label and entry======
        self.email_label =Label(self.accountcard_frame,text='Email',font=labelfont,bg='#ffffff')
        self.email_label.place(x=60,y=200)
        self.email_entry_label = Label(self.accountcard_frame,image=img,bg='#ffffff')
        self.email_entry_label.image=img
        self.email_entry_label.place(relx=0.5,rely=0.33)
        self.email_entry = Entry(self.accountcard_frame,width=19,bg='#D9D9D9',font= entryfont,highlightthickness=0, relief=FLAT)
        self.email_entry.place(relx=0.51,rely=0.345)

        #=====Gender label and entry=====
        self.gender_label =Label(self.accountcard_frame,text='Gender',font=labelfont,bg='#ffffff')
        self.gender_label.place(x=60,y=300)
        self.gender_entry_label = Label(self.accountcard_frame,image=img,bg='#ffffff')
        self.gender_entry_label.image=img
        self.gender_entry_label.place(relx=0.5,rely=0.5)
        self.gender_entry = Entry(self.accountcard_frame,width=19,bg='#D9D9D9',font= entryfont,highlightthickness=0, relief=FLAT)
        self.gender_entry.place(relx=0.51,rely=0.515)

        #=====Password label and entry===
        self.password_label =Label(self.accountcard_frame,text='Password',font=labelfont,bg='#ffffff')
        self.password_label.place(x=60,y=400)
        self.password_entry_label = Label(self.accountcard_frame,image=img,bg='#ffffff')
        self.password_entry_label.image=img
        self.password_entry_label.place(relx=0.5,rely=0.67)
        self.password_entry = Entry(self.accountcard_frame,width=19,bg='#D9D9D9',font= entryfont,highlightthickness=0, relief=FLAT)
        self.password_entry.place(relx=0.51,rely=0.685)

        #======Button=======
        self.save_btn_img = Image.open('images/31.jpg')
        save_btn_img = ImageTk.PhotoImage(self.save_btn_img)
        self.save_btn_label = Label(self.accountcard_frame,image=save_btn_img,bg='#ffffff',cursor='hand2')
        self.save_btn_label.image = save_btn_img
        self.save_btn_label.place(relx=0.2,rely=0.8)
        self.save_label = Label(self.accountcard_frame,text='Save',bg='#D9D9D9',font=btnfont,cursor='hand2')
        self.save_label.place(relx=0.3,rely=0.81)

        self.reset_btn_img = Image.open('images/resetpassword.jpg')
        reset_btn_img = ImageTk.PhotoImage(self.reset_btn_img)
        self.reset_btn_img = Label(self.accountcard_frame,image=reset_btn_img,bg='#FFFFFF',cursor='hand2')
        self.reset_btn_img.image = reset_btn_img
        self.reset_btn_img.place(relx=0.56,rely=0.8)
        self.reset_label = Label(self.accountcard_frame,text='Reset Password',font=btnfont,bg='#D9D9D9',cursor='hand2')
        self.reset_label.place(relx=0.63,rely=0.81)

class SecurityQuestion:
    def __init__(self,window):
       
        
        self = window
        self.geometry('900x800')
        self.Question =Frame(window,bg='#FFFFFF',width='900',height='800')
        self.Question.place(x=0,y=0)
        
        def ResetPage():
            self.Resetwindow = Toplevel(self.Questionwindow)
            self.app = ResetPass(self.Resetwindow)
        # Label
        self.select_label = Label(self.Question,bg='#FFFFFF',text='Select Security Question',font=labelfont)
        self.select_label.place(relx=0.44,rely=0.3)
        # Combo box
        self.question_box = Combobox(self.Question,state='readonly',width=60)
        self.question_box.place(relx=0.33,rely=0.35)
        #Answer box
        self.answer_box_img = Image.open('images/33.jpg')
        img = ImageTk.PhotoImage(self.answer_box_img)
        self.answer_box = Label(self.Question,image=img,bg='#FFFFFF')
        self.answer_box.image= img
        self.answer_box.place(relx=0.4,rely=0.4)
        self.answer_enrty = Entry(self.Question,width=19,bg='#D9D9D9',font= entryfont,highlightthickness=0, relief=FLAT)
        self.answer_enrty.place(relx=0.41,rely=0.41)

        self.proceed_btn_img = Image.open('images/31.jpg')
        proceed_btn = ImageTk.PhotoImage(self.proceed_btn_img)
        self.proceed_btn_img =Label(self.Question,image=proceed_btn,bg='#FFFFFF')
        self.proceed_btn_img.image = proceed_btn
        self.proceed_btn_img.place(relx=0.47,rely=0.5)
        self.proceed_label = Label(self.Question,text='Proceed',font=btnfont,cursor='hand2',bg="#D9D9D9")
        self.proceed_label.place(relx=0.514,rely=0.51)
        self.proceed_label.bind('<Button-1>',lambda e:ResetPage())

class ResetPass:
    def __init__(self,ResetWindow) :
        self.ResetWindow = ResetWindow
        self.ResetWindow.geometry('900x800')
        self.Reset =Frame(ResetWindow,bg='#FFFFFF',width='900',height='800')
        self.Reset.place(x=0,y=0)

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

        pass


class AddTransaction:
    def __init__(self,window):
        self =window
        self.geometry('1000x500')
        self.resizeable = 0
        self.Add = Frame(self,bg='#FFFFFF',height='500',width='1000')
        self.Add.place(x=0,y=0)

        self.category_label = Label(self.Add,text='Category',bg='#FFFFFF',font=labelfont)
        self.category_label.place(relx=0.05,rely=0.05)
        self.category_img = Image.open('images/category_box.jpg')
        category = ImageTk.PhotoImage(self.category_img)
        self.category_img = Label(self,image=category,bg='#FFFFFF')
        self.category_img.image = category
        self.category_img.place(relx=0.05,rely=0.12)

        self.date_label = Label(self.Add,text='Date',bg='#FFFFFF',font=labelfont)
        self.date_label.place(relx=0.2,rely=0.05)
        #self.date_img = Image.open('images/category_box.jpg')
        #date_img = ImageTk.PhotoImage(self.date_img)
        #self.date_img = Label(self,image=date_img,bg='#FFFFFF')
        #self.date_img.image = date_img
        #self.date_img.place(relx=0.2,rely=0.12)
        date=DateEntry(self.Add, font=("Arial", 12), width=12)
        date.place(relx=0.2,rely=0.12)

        self.note_label = Label(self.Add,text='Note (optional)',bg='#FFFFFF',font=labelfont)
        self.note_label.place(relx=0.37,rely=0.05)
        self.note_img = Image.open('images/note_box.jpg')
        note = ImageTk.PhotoImage(self.note_img)
        self.note_img = Label(self.Add,image=note,bg='#FFFFFF')
        self.note_img.image = note
        self.note_img.place(relx=0.37,rely=0.12)

        self.amount_label = Label(self.Add,text='Amount',bg='#FFFFFF',font=labelfont)
        self.amount_label.place(relx=0.55,rely=0.05)
        self.amount_img = Image.open('images/note_box.jpg')
        amount = ImageTk.PhotoImage(self.amount_img)
        self.amount_img = Label(self.Add,image=amount,bg='#FFFFFF')
        self.amount_img.image = amount
        self.amount_img.place(relx=0.55,rely=0.12)

        self.currency_label = Label(self.Add,text='Currency',bg='#FFFFFF',font=labelfont)
        self.currency_label.place(relx=0.72,rely=0.05)
        self.currency_img = Image.open('images/currency_box.png')
        currency = ImageTk.PhotoImage(self.currency_img)
        self.currency_img = Label(self.Add,image=currency,bg='#FFFFFF')
        self.currency_img.image = currency
        self.currency_img.place(relx=0.73,rely=0.12)

        self.add_img = Image.open('images/add_btn.png')
        add = ImageTk.PhotoImage(self.add_img)
        self.add_img = Label(self.Add,image=add,bg='#FFFFFF')
        self.add_img.image = add
        self.add_img.place(relx=0.66,rely=0.25)

        pass

def page():
    window = Tk()
    AccountPage(window)
    window.mainloop()
    
    

if __name__ == '__main__':
    page()