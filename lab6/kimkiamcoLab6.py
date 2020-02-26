#!/usr/bin/python3

from tkinter import * 
import sys
import os


class Converter:

    def __init__(self,input):
        self.km = input
        self.converted = 0

    def convert(self):
        if(self.km != None):
            self.converted = float(self.km) * 0.621371 #m per km
        return self.converted


root = Tk()

def on_click():
    miles = "{0:.2f}".format(round(Converter(km_entry.get()).convert(),2))
    mile_label = Label(root, text=f'{miles} miles')
    mile_label.grid(row=1, column=1)
    return miles

def quit():
    root.destroy()
    

def only_numbers(char):
    return char.isdigit()


validation = root.register(only_numbers)
km_label = Label(root, text="kilometer")
km_entry = Entry(root,validate="key", validatecommand=(validation, '%S'))

convert_btn = Button(root, text="Convert", command=on_click)
quit_btn = Button(root, text="Quit", command=quit)


km_label.grid(row=0, column=0)
km_entry.grid(row=0,column=1)
convert_btn.grid(row=1, ipadx=10, ipady=10)
quit_btn.grid(row=2, column=0,ipadx=19.3,ipady=10)



root.mainloop()




