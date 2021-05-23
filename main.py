from tkinter import*
import random
import time
import tkinter as tk
from tkinter import ttk
import subprocess
from subprocess import call


def repeat():
    with open('ss.txt', 'w') as f:
        subprocess.call(["sudo","top","-n","1"],stdout=f)
#write the filename to be called for new window appearance
def call_rushil():
    call(["python", "new_process.py"])
def click_renice():
    call(["python", "renice.py"])
root = Tk()
root.title("Priority Manager")
root.minsize(width=1200,height=800)
root.geometry("1600x700+0+0")
def View():
    
    
    localtime=time.asctime(time.localtime(time.time()))
    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
    headingFrame1 = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
    headingFrame1.place(relx=0.25,rely=0.05,relwidth=0.5,relheight=0.08)
    headingLabel = Label(headingFrame1, font=( 'aria' ,30, 'bold' ),text="Priority Manager",fg="steel blue")
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    headingFrame2 = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
    headingFrame2.place(relx=0.25,rely=0.13,relwidth=0.5,relheight=0.05)
    headingLabel2 = Label(headingFrame2, font=( 'aria' ,15,'bold' ),text=localtime,fg="steel blue")
    headingLabel2.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='white')
    labelFrame.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.6)
    y = 0.25
    scrollbar = Scrollbar(labelFrame)
    scrollbar.pack(side=RIGHT, fill=Y)
    textbox = Text(labelFrame,font=( 'aria' ,10, 'bold' ),bg='white',fg="steel blue",height=100,width=100,padx=5,pady=5,relief=GROOVE,bd=3)
    textbox.pack()
    cnt=0

    ##yaha se top command ka output le rhe hain
    repeat()
    f=open('ss.txt','r')
    for l in f.readlines():
        if cnt<6:
            cnt+=1
            continue
        lst=(l.strip()).split(' ')
        content=""
        for ele in lst:
            if ele=='':
                continue
            if ele[0]=='':
                continue
            if ele[0]=='\\':
                continue
            else:
                content=content+ele+"\t"
        content=content+"\n"
        textbox.insert(tk.END,content)
        cnt+=1
        y+=0.05
    textbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=textbox.yview)
    f.close()
    addProcessBtn = Button(root,font=( 'aria' ,15,'bold' ),text="Perform Priority Setting Operations",bg = "light cyan", fg="black")
    addProcessBtn.place(relx=0.20,rely=0.82, relwidth=0.28,relheight=0.08)
    addProcessBtn.configure(command=click_checkinn)

    bt1 = Button(root,font=( 'aria' ,15,'bold' ),text="Change priority of current process",bg = "light cyan", fg="black")
    bt1.place(relx=0.60,rely=0.82, relwidth=0.28,relheight=0.08)
    bt1.configure(command=click_renice)
    
    quitBtn = Button(root,font=( 'aria' ,15,'bold' ), text="Exit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.01,rely=0.9, relwidth=0.18,relheight=0.08)
    status = Label(root,font=('aria', 10,'bold'),width = 16, text="Operating System Course Project\nJay Prakash & Rushil Sanghavi",bg='#f7f1e3', fg='black',bd=2,relief=SUNKEN)
    status.place(relx=0.8,rely=0.9, relwidth=0.18,relheight=0.08)
    root.after(1000, View)

View()
root.mainloop()
