# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 21:28:35 2020

@author: Sureshkumar R
"""

import tkinter
import tkinter.messagebox

def hello():
    tkinter.messagebox.showinfo("Hello Window","Hello")

m=tkinter.Tk()

m.title("Hello Button")

openhellowindowbutton=tkinter.Button(m,text="Open Hello Window",command=hello)
exitbutton=tkinter.Button(m,text="Exit",command=m.destroy)

openhellowindowbutton.pack()
exitbutton.pack()

m.mainloop()