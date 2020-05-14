# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:05:24 2020

@author: Sureshkumar R
"""

import tkinter as tk

r=tk.Tk()

r.title('Window with exit window button')

button1=tk.Button(r,text='Exit this window',width=25,command=r.destroy)
button1.pack()
button2=tk.Button(r,text='Exit this window',width=50)
button2.pack()
button3=tk.Button(r,text='Exit this window',command=r.destroy)
button3.pack()
button4=tk.Button(r)
button4.pack()

button5=tk.Button(r,text='ACTIVE BG RED',activebackground='red') #changing the colour of button whileclicking
button5.pack()

button6=tk.Button(r,text='ACTIVE FG GREEN',activeforeground='green') #changing thecolour of the text on the button while clicking
button6.pack()

button7=tk.Button(r,text='all colours',bg='yellow',fg='blue',activebackground='red',activeforeground='green')
button7.pack()

"""
photo1=tk.PhotoImage(file="animated-button-image-0201.gif")
photo2=tk.PhotoImage(file="Icon_10-512.png")
button8=tk.Button(r,image=photo2)
button8.pack()
button8.image = photo1
"""

r.mainloop()