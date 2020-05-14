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

button5=tk.Button(r,text="button5",width=25,command=r.destroy)
button5.pack(expand=tk.NO)

button6=tk.Button(r,text="button6",width=25,command=r.destroy)
button6.pack(expand=tk.YES)

button7=tk.Button(r,text="button7",width=25,command=r.destroy)
button7.pack(expand=tk.NO)

button8=tk.Button(r,text="button8",width=25,command=r.destroy)
button8.pack(side=tk.TOP)

#button9=tk.Button(r,text="button9",width=25,command=r.destroy)
#button9.pack(expand=tk.LEFT)

#button10=tk.Button(r,text="button10",width=25,command=r.destroy)
#button10.pack(expand=tk.RIGHT)

#button11=tk.Button(r,text="button11",width=25,command=r.destroy)
#button11.pack(expand=tk.BOTTOM)

r.mainloop()