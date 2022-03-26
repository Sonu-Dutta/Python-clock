import string
from tkinter import *
from tkinter import font
from tkinter.ttk import *

from time import strftime

root= Tk()
root.title("Clock")

def time():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
label=Label(root, font=("bold",50), background="black",foreground="lightblue")
label.pack(anchor='center')
time()
mainloop()
