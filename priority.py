import tkinter as tk
from tkinter import ttk
from tkinter import *
import subprocess
import shlex
import os
# shlex.split("/bin/prog -i data.txt -o \"more data.txt\"")
def for_all_user():
    uid = os.getuid()
    nice = int(priority.get())
    print("changing priority for all the processes (current user) ... \n priority = ",nice)
    os.system('ls -l')
    os.system("sudo renice -n "+str(nice)+" -u "+str(uid))
# priority = 0
def execute():
    
    #print(int(priority.get()))
    nice = int(priority.get())
    print("executing with priority = ",nice)
    print(comman_var.get())
    process = subprocess.Popen(['sudo', 'nice', "-n "+str(nice)]+shlex.split(str(comman_var.get())), 
                           stdout=subprocess.PIPE,
                           universal_newlines=True)

    while True:
        output = process.stdout.readline()
        print(output.strip())
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output 
            for output in process.stdout.readlines():
                print(output.strip())
            break
def real_execute():
    
    #print(int(priority.get()))
    nice = int(priority2.get())
    print(comman_var.get())
    print("executing as a real-time process with priority = ",nice)
    commandlist=[]
    if(drop_var.get()[0]=='F'):
        commandlist=['sudo', 'chrt','-a', '-f',str(nice)]
    if(drop_var.get()[0]=='R'):
        commandlist=['sudo', 'chrt','-a', '-r',str(nice)]
    if(drop_var.get()[0]=='B'):
        print("In this scheduling policy, only priority = 0 is allowed . \n")
        commandlist=['sudo', 'chrt', '-b','0']
    if(drop_var.get()[0]=='I'):
        print("In this scheduling policy, only priority = 0 is allowed . \n")
        commandlist=['sudo', 'chrt', '-i','0']
    if(drop_var.get()[0]=='O'):
        print("In this scheduling policy, only priority = 0 is allowed . \n")
        commandlist=['sudo', 'chrt', '-o','0']
    process = subprocess.Popen(commandlist+shlex.split(str(comman_var.get())), 
                           stdout=subprocess.PIPE,
                           universal_newlines=True)

    while True:
        output = process.stdout.readline()
        print(output.strip())
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output 
            for output in process.stdout.readlines():
                print(output.strip())
            break
def getprior(v):
    #priority = int(v)
    v =1
    #print(v,str(v),str(int(v)))

root = tk.Tk()
root.title("Prioriy setting for upcoming process")
root.geometry('550x600') 
frame = tk.Frame(root)
frame.pack()
w2 = Label(frame, text='\nCommand to be executed: ')
w2.pack()

comman_var=tk.StringVar()
command_entry = tk.Entry(frame,textvariable = comman_var)#font=('calibre',10,'normal')
command_entry.pack()

line_ = Label(frame, text="_"*100)
line_.pack()
w = Label(frame, text='\n(1) Priority : (highest = -20 , lowest = 19)')
w.pack()
priority =DoubleVar()#;Variable=prioriy 

slidebar = Scale(frame,cursor = 'hand1',sliderlength=15,length = 200,variable=priority,from_=-20, to=19, orient=HORIZONTAL,activebackground='Blue',command = getprior)
slidebar.pack()
# inputtxt = Text(frame, height = 10,
#                 width = 25,
#                 bg = "light yellow")
# inputtxt.pack()


# button = tk.Button(frame, 
#                    text="cancel",cursor = 'hand1',
#                    fg="red",
#                    command=quit)
# button.pack(side=tk.LEFT)


slogan = tk.Button(frame,
                   text="normal-process execute",cursor = 'hand1',
                   command=execute)
slogan.pack()
line_1 = Label(frame, text="_"*100)
line_1.pack()
button2 = tk.Button(frame, 
                   text="(2) For All Process\n(current user)",cursor = 'hand1',
                   fg="red",
                   command=for_all_user)
button2.pack()
line_2 = Label(frame, text="_"*100)
line_2.pack()
real_time = Label(frame,text="\n(3)To set/create real-time process : ")
real_time.pack()
drop_var=tk.StringVar()
policy_chosen = ttk.Combobox(frame, width = 27, 
                            textvariable = drop_var)
  
# Adding combobox drop down list
policy_chosen['values'] = (' FIFO', 
                          ' Round-Robin',
                          'Batch','Idle','Other')
policy_chosen.current(4)

policy_chosen.pack()

w3 = Label(frame, text='\nreal-time Priority : (highest = 99 , lowest = 1)')
w3.pack()
priority =DoubleVar()#;Variable=prioriy 

priority2 = DoubleVar()
slidebar2 = Scale(frame,cursor = 'hand1',sliderlength=15,length = 200,variable=priority2,from_=1, to=99, orient=HORIZONTAL,activebackground='Blue')
slidebar2.pack()
slogan2 = tk.Button(frame,
                   text=" execute",cursor = 'hand1',
                   command=real_execute)
slogan2.pack()
line_3 = Label(frame, text=str("_"*100)+"\n\t\tprogrammed by Rushil & Jay , IIT Jodhpur.\n\tReport bugs & Issues to : sanghavi.1@iitj.ac.in")
line_3.pack()
root.mainloop()
