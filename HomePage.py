from tkinter import *
from PIL import ImageTk, Image  # pip install pillow
from PIL.ImageTk import PhotoImage
import tkinter.messagebox
from tkinter import ttk
import tkinter.messagebox
import sqlite3
import os

class HomepageWin(Frame):
    def __init__(self, window,controller):
        self.hide_button = None
        self = window
        self.geometry('900x718')
        self.state('zoomed')  # Maximizing the page
        self.resizable(0, 0)  # Delete the restore button
        # =================================
        # ================= Login Frame =================
        self.hp_frame = Frame(self, bg='#FFFFFF', width='1950', height='1400')  # Color and the size of the frame
        self.hp_frame.pack() # Placement of the frame

        self.frame1 = Frame(self, bg='#7FFFD4', width='2000', height='200')
        self.frame1.place(x=0, y=0)

def page():
    window = Tk()
    HomepageWin(window)
    window.mainloop()

if __name__ == '__main__':
    page()