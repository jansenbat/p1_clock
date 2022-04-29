#python clock again, idk why it isn't working, maybe I just didn't configure the file properly man idk

from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Python Clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("courier new", 80), background = "black", foreground = "cyan")
label.pack(anchor='center')

time()

mainloop()