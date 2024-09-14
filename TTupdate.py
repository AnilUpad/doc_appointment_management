import pymysql
from tkinter import messagebox
import tkinter 
from tkinter import *
from tkinter import ttk
def showupdate():
    t = tkinter.Tk()


    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='DAMS')
        cur=db.cursor()
        xb=int(e1.get())
        xc=e2.get()
        xd=e3.get()
        sql="UPDATE timetable SET starttime='%s', endtime='%s' WHERE doctorid='%d'" % (xc, xd, xb)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','update')
        e2.delete(0,100)
        e2.delete(0,100)
        
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        db.close()
    
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
    
    btn = Button(t,text='update',fg='red',bg='yellow',command=updatedata)
    btn.place(x=150,y=320)
    
    t.geometry('700x700')
    t.config(bg='purple')
    
    t.mainloop()
