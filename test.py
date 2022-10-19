
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

class windows(Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Test Application")
        self.width= self.winfo_screenwidth()
        self.height= self.winfo_screenheight()
        self.geometry("%dx%d" % (self.width, self.height))
       

        # creating a frame and assigning it to container
        container = tk.Frame(self, height='1000', width='500',bg="#FFFFFF")
        # specifying the region where the frame is packed in root
        container.place(x=0,y=0)

        # configuring the location of the container using grid
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (MainPage, SidePage, CompletionScreen):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(MainPage)

    def show_frame(self, cont):
            frame = self.frames[cont]
            # raises the current frame to the top
            frame.tkraise()

class MainPage(Frame):
    def __init__(self, window, controller):
        Frame.__init__(self, window)
        label = tk.Label(self, text="Main Page",bg="#ffffff")
        label.place(x=10,y=100)

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        switch_window_button = tk.Button(
            self,
            text="Go to the Side Page",
            command=lambda: controller.show_frame(SidePage),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


class SidePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is the Side Page")
        label.pack(padx=100, pady=10)

        switch_window_button = tk.Button(
            self,
            text="Go to the Completion Screen",
            command=lambda: controller.show_frame(CompletionScreen),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


class CompletionScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Completion Screen, we did it!")
        label.pack(padx=10, pady=10)
        switch_window_button = ttk.Button(
            self, text="Return to menu", command=lambda: controller.show_frame(MainPage)
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

if __name__ == "__main__":
    testObj = windows()
    testObj.mainloop()        