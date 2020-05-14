# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:49:23 2020

@author: Sureshkumar R
"""

import tkinter as tk

r=tk.Tk()

r.title('Window with exit window button')

button1=tk.Button(r,text="button1",width=25,command=r.destroy)
button1.pack(fill=tk.NONE)

button2=tk.Button(r,text="button2",width=25,command=r.destroy)
button2.pack(fill=tk.X)

button3=tk.Button(r,text="button3",width=25,command=r.destroy)
button3.pack(fill=tk.Y)

button4=tk.Button(r,text="button4",width=25,command=r.destroy)
button4.pack(fill=tk.BOTH)

r.mainloop()