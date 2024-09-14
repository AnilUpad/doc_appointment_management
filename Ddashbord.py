import pymysql
import tkinter
from tkinter import *
from Dinsert import *
from Ddelete import *
from Dupadte import *
from Dfind import *
t=tkinter.Tk()
t.geometry('700x700')
d=Canvas(t,height=800,width=800,bg="purple")
d.place(x=0,y=0)

ctn=Button(t,text='Insert',command=showinsert,background="#FFD700", foreground="#2E2E2E", font=("Helvetica", 12, "bold"))
ctn.place(x=50,y=50)

ctn1=Button(t,text='Delete',command=showdelete,background="#FFD700", foreground="#2E2E2E", font=("Helvetica", 12, "bold"))
ctn1.place(x=50,y=100)

ctn2=Button(t,text='update',command=showfind,background="#FFD700", foreground="#2E2E2E", font=("Helvetica", 12, "bold"))
ctn2.place(x=50,y=150)

ctn3=Button(t,text='find', command=showupdate,background="#FFD700", foreground="#2E2E2E", font=("Helvetica", 12, "bold"))
ctn3.place(x=50,y=200)


ctn4.place(x=50,y=250)






t.mainloop()