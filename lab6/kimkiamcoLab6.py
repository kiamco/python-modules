#!/usr/bin/python3

from tkinter import * 
import sys
import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

root = Tk()

km_label = Label(root, text="kilometer")
km_label.pack()
# Code to add widgets will go here...
# L1 = Label(top, text="Kilometer")
# E1 = Entry( top, option )

root.mainloop()
