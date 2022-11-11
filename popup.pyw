from tkinter import *
from password_generator import password
import json

win = Tk()
win.title("Key Generator")
win.geometry('250x75')
win.resizable(False, False)
def onClick():
    win.clipboard_clear()
    win.clipboard_append(password)
    with open("history.json", "w") as file:
        file.write(password)


button = Button(win, text="Copy Password", command=onClick, height=10, width=20, bg='pink', fg='red', font='Helvetica 18 bold') 
button.pack()

win.mainloop()