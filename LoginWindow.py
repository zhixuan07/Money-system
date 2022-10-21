from tkinter import *
from PIL import ImageTk, Image  # pip install pillow
from PIL.ImageTk import PhotoImage
import tkinter.messagebox
from tkinter import ttk
import tkinter.messagebox
import sqlite3

class LoginForm(Frame):
    def __init__(self, window,controller):
        self.hide_button = None
        Frame.__init__(self, window)
        self.Login= Frame(self,bg="#FFFFFF",width='1000',height='1000')
        self.Login.pack()
          # Delete the restore button
        #=================================
        self.Username=StringVar()
        self.password=StringVar()

        def New():
            User = self.Username.get()
            password = self.password.get()
            # Identify password and username
            if (User == str("Lemanta") and (password == str("abc4567"))):
                self.newWindow = Toplevel(self)
                self.app=Homepage(self.newWindow)
            # Reject function when above information are wrong
            else:
                tkinter.messagebox.askretrycancel("Booking system", "You have entered an invalid user name or password")
                self.Username.set("")
                self.password.set("")


        # ================= Background Image =================
        #self.bg_frame = Image.open('images/backlog.png')
        #photo: PhotoImage = ImageTk.PhotoImage(self.bg_frame)
        #self.bg_panel = Label(self, image=photo)
        #self.bg_panel.image = photo
        #self.bg_panel.pack(fill='both', expand='yes')
        # ================= Login Frame =================
        self.lgn_frame = Frame(self.Login, bg='#2B1B17', width='950', height=600)  # Color and the size of the frame
        self.lgn_frame.place(x=500, y=130)  # Placement of the frame

        self.txt = 'WELCOME'
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, 'bold'), bg='#2B1B17', fg='#43C6DB')
        self.heading.place(x=300, y=40, width=300, height=30)

        # ================= Left Side Image =================
        self.side_image = Image.open('images/log1.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=150, y=200)


        # ================= Sign In Image =================
        self.sign_in_image = Image.open('images/image-removebg-preview.jpeg')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#2B1B17')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=650, y=80)

        self.sign_in_label = Label(self.lgn_frame, text='Sign In', bg='#2B1B17', fg='#43C6DB',
                                   font=('yu gothic ui', 17, 'bold'))
        self.sign_in_label.place(x=676, y=200)

        # ================= Username =================
        self.username_label = Label(self.lgn_frame, text='Username', bg='#2B1B17', font=('yu gothic ui', 13, 'bold'),
                                    fg='#43C6DB')
        self.username_label.place(x=576, y=250)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#2B1B17', fg='#43C6DB',
                                    font=('yu gothic ui', 13, 'bold'),textvariable=self.Username)
        self.username_entry.place(x=606, y=285, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.username_line.place(x=576, y=309)

        # ================= Username Icon =================
        self.username_icon = Image.open('images/usernameIcon.jpeg')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#2B1B17')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=576, y=282)

        # ================= Password =================
        self.password_label = Label(self.lgn_frame, text='Password', bg='#2B1B17', font=('yu gothic ui', 13, 'bold'),
                                    fg='#43C6DB')
        self.password_label.place(x=576, y=340)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#2B1B17', fg='#43C6DB',
                                    font=('yu gothic ui', 13, 'bold'),textvariable=self.password, show='*')
        self.password_entry.place(x=606, y=375, width=270)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.password_line.place(x=576, y=399)

        # ================= Password Icon =================
        self.password_icon = Image.open('images/PasswordIcon.jpeg')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#2B1B17')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=576, y=372)

        # ================= Login Button =================
        self.lgn_button = Image.open('images/LogButton.jpeg')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#2B1B17')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=571, y=412)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=('yu gothic ui', 13, 'bold'), command=New, width=25, bd=0,
                            bg='#0080b3', cursor='hand2', activebackground='#0080b3', fg='white')
        self.login.place(x=20, y=10)

        # ================= Show/Hide Password =================
        self.show_image = Image.open('images/showpassword.jpeg')
        self.photo1 = ImageTk.PhotoImage(self.show_image)
        self.show_button = Button(self.lgn_frame, image=self.photo1, bg='white', activebackground='white',
                                  cursor='hand2', bd=0, command=self.show)
        self.show_button.image = self.photo1
        self.show_button.place(x=850, y=380)

        self.hide_image = Image.open('images/hidepassword.jpeg')
        self.photo = ImageTk.PhotoImage(self.hide_image)

        # ===========Register=================
        self.txt ='Dont have and account?'
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 12, 'italic'), bg='#2B1B17', fg='#43C6DB')
        self.heading.place(x=500, y=525, width=300, height=20)
        self.register = Button(text='REGISTER', font=('yu gothic ui', 10, 'bold'), width=10, bd=0,
                            bg='#2B1B17', cursor='hand2', activebackground='#43C6DB', fg='white')
        self.register.place(x=1240, y=652)

        # For creating login system

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.photo, bg='white', activebackground='white',
                                  cursor='hand2', bd=0, command=self.hide)
        self.hide_button.image = self.photo
        self.hide_button.place(x=850, y=380)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.photo1, bg='white', activebackground='white',
                                  cursor='hand2', bd=0, command=self.show)
        self.show_button.image = self.photo1
        self.show_button.place(x=850, y=380)
        self.password_entry.config(show='*')
#=======================================================================================================================
class Homepage(Frame):
    def __init__(self, window,controller):
        self.hide_button = None
        Frame.__init__(self, window)

        def New1():
                self.newWindow = Toplevel(self)
                self.app=ConnectorDB(self.newWindow)


        # ================= Background Image =================
        #self.bg_frame = Image.open('images/backlog.png')
        #photo: PhotoImage = ImageTk.PhotoImage(self.bg_frame)
        #self.bg_panel = Label(self, image=photo)
        #self.bg_panel.image = photo
        #self.bg_panel.pack(fill='both', expand='yes')
        # ================= homepage Frame =================
        self.lgn_frame = Frame(self, bg='#555854', width='990', height=750)  # Color and the size of the frame
        self.lgn_frame.place(x=465, y=150)  # Placement of the frame

        self.txt = 'HOMEPAGE'
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, 'bold'), bg='#555854', fg='#43C6DB')
        self.heading.place(x=300, y=40, width=300, height=30)

        # ================= Booking Button =================
        self.lgn_button = Image.open('images/button2.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#555854')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=320, y=90)

        self.booking = Button(self.lgn_button_label, text='Booking', font=('yu gothic ui', 13, 'bold'),command=New1, width=15, bd=0,
                            bg='#F09304', cursor='hand2', activebackground='#555854', fg='white')
        self.booking.place(x=50, y=5)

        # ================= Update Button =================
        self.bgn_button = Image.open('images/button2.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.bgn_button_label = Label(self.lgn_frame, image=photo, bg='#555854')
        self.bgn_button_label.image = photo
        self.bgn_button_label.place(x=320, y=180)

        self.update = Button(self.bgn_button_label, text='Update', font=('yu gothic ui', 13, 'bold'), width=15, bd=0,
                            bg='#F09304', cursor='hand2', activebackground='#555854', fg='white')
        self.update.place(x=50, y=5)
        # ================= Update Button =================
        self.agn_button = Image.open('images/button2.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.agn_button_label = Label(self.lgn_frame, image=photo, bg='#555854')
        self.agn_button_label.image = photo
        self.agn_button_label.place(x=320, y=270)

        self.acc = Button(self.agn_button_label, text='Account', font=('yu gothic ui', 13, 'bold'), width=15, bd=0,
                            bg='#F09304', cursor='hand2', activebackground='#555854', fg='white')
        self.acc.place(x=50, y=5)
        # ================= Admin Button =================
        self.ign_button = Image.open('images/button2.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.ign_button_label = Label(self.lgn_frame, image=photo, bg='#555854')
        self.ign_button_label.image = photo
        self.ign_button_label.place(x=320, y=360)

        self.acc = Button(self.ign_button_label, text='Admin', font=('yu gothic ui', 13, 'bold'), width=15, bd=0,
                            bg='#F09304', cursor='hand2', activebackground='#555854', fg='white')
        self.acc.place(x=50, y=5)
#============================================================================================================================================
class ConnectorDB:
    def connect():
        con = sqlite3.connect("classroombooking.db")
        cursor = con.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS book (id TEXT PRIMARY KEY, username text,"
            " password integer, unknown text, name text, gmail text)")
        con.commit()
        con.close()

    def __init__(self,root):
        self.root = root
        titlespace = " "
        self.root.title(102 * titlespace + "Sqlite Connector")
        self.root.geometry("1166x718")
        self.root.resizable(width=False, height=False)

        
                

        MainFrame = Frame(self.root, bd=10,width =770, height=1166, relief =RIDGE, bg='cadet blue')
        MainFrame.grid()

        TitleFrame=Frame(MainFrame, bd=7, width=770, height=800, relief=RIDGE)
        TitleFrame.grid(row=0 , column=0)
        TopFrame3=Frame(MainFrame, bd=5, width=770, height=800, relief=RIDGE)
        TopFrame3.grid(row=1 , column=0)

        LeftFrame=Frame(TopFrame3, bd=5, width=770, height=400, padx=2, bg="cadet blue", relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1=Frame(LeftFrame, bd=5, width=600, height=180, padx=2,pady=4, relief=RIDGE)
        LeftFrame1.pack(side=TOP,padx=0,pady=0)

        RightFrame1=Frame(TopFrame3, bd=5, width=100, height=400, padx=2, bg="cadet blue", relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a=Frame(RightFrame1, bd=5, width=90, height=300, padx=2,pady=2, relief=RIDGE)
        RightFrame1a.pack(side=TOP)

        #========function========================
        BMonth=StringVar()
        NoStudent=StringVar()
        Bclasss=StringVar()
        BSTIME=StringVar()
        BETIME=StringVar()
        BReason=StringVar()

        #======================================
        def iExit():
            iExit=tkinter.messagebox.askyesno("Sqlite Connector","Confirm The Info Selected and Input Are Correct?")
            if iExit>0:
                root.destroy()
                return


        def addData():
            if BMonth.get()==""or NoStudent.get()=="" or Bclasss.get()=="" or BSTIME.get()=="" or BETIME.get()=="" or BReason.get()=="":
                tkinter.messagebox.showerror("Sqlite Connector","Enter Correct Details")
            con = sqlite3.connect('classroombooking.db')
            cursor = con.cursor()
            cursor.execute("INSERT INTO Booking (BMonth,NoOfStudent,BClass,BStime,BEtime,BookingReason) VALUES(?,?,?,?,?,?)",
                           (BMonth.get(),NoStudent.get(),Bclasss.get(),BSTIME.get(),BETIME.get(),BReason.get()))
            con.commit()
            con.close()


        #============Insert Column label========================================================================
        self.lbltitle=Label(TitleFrame, font=('arial',40,'bold'),text="Booking",bd=7)
        self.lbltitle.grid(row=0,column=0,padx=132)
        #===================================================================

        self.lblMonth=Label(LeftFrame1, font=('arial',12,'bold'),text="Month",bd=7)
        self.lblMonth.grid(row=0,column=0, sticky=W, padx=5)
        #======combo box(listbox)===============================================================
        self.cboMonth=ttk.Combobox(LeftFrame1, font=('arial',12,'bold'), width=42, state='readonly',textvariable=BMonth)
        self.cboMonth['values']=(' ','January','February','March','April','May','June','July','August','September',
                                 'October','November','December')
        self.cboMonth.current(0)
        self.cboMonth.grid(row=0,column=1, sticky=W, padx=5)

        self.lblNoStudent=Label(LeftFrame1, font=('arial',12,'bold'),text="Number of Student",bd=7)
        self.lblNoStudent.grid(row=1,column=0, sticky=W, padx=5)
        self.entNoStudent=Entry(LeftFrame1, font=('arial',12,'bold'),bd=5, width=44, justify='left',textvariable=NoStudent)
        self.entNoStudent.grid(row=1,column=1, sticky=W, padx=5)

        self.lblClass= Label(LeftFrame1, font=('arial', 12, 'bold'), text="Class", bd=7)
        self.lblClass.grid(row=2, column=0, sticky=W, padx=5)
        # ======combo box(listbox)======================================================================
        self.cboClass = ttk.Combobox(LeftFrame1, font=('arial', 12, 'bold'), width=42, state='readonly',textvariable=Bclasss)
        self.cboClass['values'] = (
        ' ', 'A101', 'A102', 'A103', 'AI LAB')
        self.cboClass.current(0)
        self.cboClass.grid(row=2, column=1, sticky=W, padx=5)


        self.lblS = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Starting_Time", bd=7)
        self.lblS.grid(row=3, column=0, sticky=W, padx=5)
        # ======combo box(listbox)===============================================================
        self.cboS = ttk.Combobox(LeftFrame1, font=('arial', 12, 'bold'), width=42, state='readonly',textvariable=BSTIME)
        self.cboS['values'] = (
            ' ', '08.00', '09.00', '10.00', '11.00','12.00','13.00','14.00')
        self.cboS.current(0)
        self.cboS.grid(row=3, column=1, sticky=W, padx=5)

        self.lblE = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Ending_Time", bd=7)
        self.lblE.grid(row=4, column=0, sticky=W, padx=5)
        # ======combo box(listbox)===============================================================
        self.cboE = ttk.Combobox(LeftFrame1, font=('arial', 12, 'bold'), width=42, state='readonly',textvariable=BETIME)
        self.cboE['values'] = (
            ' ', '08.00', '09.00', '10.00', '11.00','12.00','13.00','14.00','15.00','16.00')
        self.cboE.current(0)
        self.cboE.grid(row=4, column=1, sticky=W, padx=5)

        self.lblS = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Booking Reason", bd=7)
        self.lblS.grid(row=5, column=0, sticky=W, padx=5)
        # ======combo box(listbox)===============================================================
        self.cboS = ttk.Combobox(LeftFrame1, font=('arial', 12, 'bold'), width=42, state='readonly',textvariable=BReason)
        self.cboS['values'] = (
            ' ', 'Normal Booking', 'Replacement', 'Events', 'Online Lecturer')
        self.cboS.current(0)
        self.cboS.grid(row=5, column=1, sticky=W, padx=5)

        #====Button==========================================
        self.btnAddNew=Button(RightFrame1a,font=('arial',16,'bold'),text="Enter",bd=4,pady=1,padx=24,width=8,height=2
                              ,command=addData).grid(row=1,column=0,padx=1)
        self.btnNext = Button(RightFrame1a, font=('arial', 16, 'bold'), command=New2, text="Next", bd=4, pady=1, padx=24,
                              width=8,
                              height=2).grid(row=2, column=0, padx=1)





def page():
    window = Tk()
    LoginForm(window)
    window.mainloop()





if __name__ == '__main__':
    page()
