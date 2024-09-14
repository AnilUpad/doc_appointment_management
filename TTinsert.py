import pymysql
from tkinter import messagebox
import tkinter 
from tkinter import *
from tkinter import ttk
def showinsert():
    t = tkinter.Tk()


    def insertdata():
        if len(e1.get())==0:
            messagebox.showinfo('hi','please insert data')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='DAMS')
            cur=db.cursor()
            xb=int(e1.get())
            xc=e2.get()
            xd=e3.get()
            
            
            sql="insert into timetable values(%d,'%s','%s')"%(xb,xc,xd)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hi','insert data')
            db.close()
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            
    
    a = Label(t,text='TimeTable',font=('arial',15),fg='red',bg='cyan')
    a.place(x=350,y=20)
    
    b = Label(t,text='Doctorid',fg='red',bg='yellow')
    b.place(x=50,y=120)
    e1 = Entry(t,width=30)
    e1.place(x=200,y=120)
    
    c = Label(t,text='starttime',fg='red',bg='yellow')
    c.place(x=50,y=160)
    e2 = Entry(t,width=30)
    e2.place(x=200,y=160)
    
    d = Label(t,text='endtime',fg='red',bg='yellow')
    d.place(x=50,y=200)
    e3 = Entry(t,width=30)
    e3.place(x=200,y=200)
    
    btn = Button(t,text='insert',fg='red',bg='yellow',command=insertdata)
    btn.place(x=150,y=320)
    
    t.geometry('700x700')
    t.config(bg='purple')
    
    t.mainloop()


