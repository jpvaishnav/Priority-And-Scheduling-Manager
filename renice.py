from tkinter import*
import random
import time
import tkinter as tk
from tkinter import ttk
import subprocess
from subprocess import call


import tkinter as tk
from tkinter import ttk
from tkinter import *
import subprocess
import os

'''
def re_nice(pr,id):
	subprocess.call(["sudo","renice","-n",str(pr),"-p",str(id)])
'''




def execute():
	pr = int(priority.get())
	ID = int(comman_var.get())
	print("executing with priority = ",pr)
	print("executing process id: = ",ID)
#process = subprocess.call(["sudo","renice","-n",str(pr),"-p",str(ID)])
def getprior():
	return
root = tk.Tk()
root.title("Priority Changing")
root.geometry('550x300') 
frame = tk.Frame(root)
frame.pack()
w2 = Label(frame, text='\nEnter Process ID to be changed: ')
w2.pack()

comman_var=tk.StringVar()
command_entry = tk.Entry(frame,textvariable = comman_var)#font=('calibre',10,'normal')
command_entry.pack()

line_ = Label(frame, text="_"*100)
line_.pack()
w = Label(frame, text='\n Priority : (highest = -20 , lowest = 19)')
w.pack()

priority =DoubleVar()
slidebar = Scale(frame,cursor = 'hand1',sliderlength=15,length = 200,variable=priority,from_=-20, to=19, orient=HORIZONTAL,activebackground='Blue',command = '')
slidebar.pack()
slogan = tk.Button(frame,
                   text="Change priority",cursor = 'hand1',
                   command=execute)
slogan.pack()
line_1 = Label(frame, text="_"*100)
line_1.pack()
root.mainloop()
