# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:49:23 2020

@author: Sureshkumar R
"""

import tkinter as tk

r=tk.Tk()

r.title('Window with exit window button')

button5=tk.Button(r,text="button5",width=25,command=r.destroy)
button5.pack(expand=tk.NO)

button6=tk.Button(r,text="button6",width=25,command=r.destroy)
button6.pack(expand=tk.YES)

button7=tk.Button(r,text="button7",width=25,command=r.destroy)
button7.pack(expand=tk.NO)

r.mainloop()