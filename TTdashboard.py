import pymysql
import tkinter
from tkinter import *
from TTinsert import *
from TTfind import *
from TTupdate import *
from TTdelete import *

t = tkinter.Tk()
t.geometry('700x700')  

d = Canvas(t, height=700, width=700, bg="purple")
d.place(x=0, y=0)

ctn = Button(t, text='Insert', command=showinsert, fg='red', bg='yellow')
ctn.place(x=50, y=50)

ctn1 = Button(t, text='Find', command=showfind, fg='red', bg='yellow')
ctn1.place(x=50, y=100)

ctn2 = Button(t, text='Update', command=showupdate, fg='red', bg='yellow')
ctn2.place(x=50, y=150)

ctn3 = Button(t, text='Delete', command=showdelete, fg='red', bg='yellow')
ctn3.place(x=50, y=200)


t.mainloop()
