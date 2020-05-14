# -*- coding: utf-8 -*-
"""
Created on Sat May  2 12:48:30 2020

@author: Sureshkumar R
"""

class Human:
    def __init__(self,gender="notprovided",age="0"):
        self.gender=gender
        self.age=age
    def printgender(self):
        print(self.gender)
    def printage(self):
        print(self.age)
    def work(self,occupation="notgiven"):
        if(occupation=="engineer"):
            print("working as an engineer")
        elif(occupation=="fashiondesigner"):
            print("working as an fashiondesigner")
        elif(occupation=="notgiven"):
            print("occupation not given")

if (__name__=="__main__"):
    suresh=Human("male","25")
    suresh.work("engineer")
    suresh.printgender()
    suresh.printage()
    yazhini=Human("famale","18")
    yazhini.work("fashiondesigner")    
    yazhini.printgender()
    yazhini.printage()
    namenotgiven=Human()
    namenotgiven.work("fashiondesigner")    
    namenotgiven.printgender()
    namenotgiven.printage()