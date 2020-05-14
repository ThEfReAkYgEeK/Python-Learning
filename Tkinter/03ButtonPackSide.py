# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:49:23 2020

@author: Sureshkumar R
"""

import tkinter as tk

r=tk.Tk()

r.title('Window with exit window button')

button8=tk.Button(r,text="button8",width=25,command=r.destroy)
button8.pack(side=tk.TOP)

#button9=tk.Button(r,text="button9",width=25,command=r.destroy)
#button9.pack(expand=tk.LEFT)

#button10=tk.Button(r,text="button10",width=25,command=r.destroy)
#button10.pack(expand=tk.RIGHT)

#button11=tk.Button(r,text="button11",width=25,command=r.destroy)
#button11.pack(expand=tk.BOTTOM)

r.mainloop()