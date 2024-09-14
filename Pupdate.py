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
        xf=e4.get()
        xg=e5.get()
        xh=e6.get()
        xi=e7.get()
        xj=e8.get()
        sql="UPDATE patients SET patientsname='%s',address='%s',phone='%s',email='%s',doctorid='%s',problem='%s',remarks='%s' WHERE patientsid='%d'" % (xc,xd,xf,xg,xh,xi,xj,xb)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','update')
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        e8.delete(0,100)
        
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        e6.insert(0,data[4])
        e7.insert(0,data[5])
        e8.insert(0,data[6])
        
        db.close()
    
    a = Label(t,text='patients',font=('arial',15),fg='red',bg='cyan')
    a.place(x=350,y=20)
    
    b = Label(t,text='patientsid',fg='red',bg='yellow')
    b.place(x=50,y=120)
    e1 = Entry(t,width=30)
    e1.place(x=200,y=120)
    
    c = Label(t,text='patientsname',fg='red',bg='yellow')
    c.place(x=50,y=160)
    e2 = Entry(t,width=30)
    e2.place(x=200,y=160)
    
    d = Label(t,text='address',fg='red',bg='yellow')
    d.place(x=50,y=200)
    e3 = Entry(t,width=30)
    e3.place(x=200,y=200)
    
    f = Label(t,text='phone',fg='red',bg='yellow')
    f.place(x=50,y=240)
    e4 = Entry(t,width=30)
    e4.place(x=200,y=240)
    
    g = Label(t,text='email',fg='red',bg='yellow')
    g.place(x=50,y=280)
    e5 = Entry(t,width=30)
    e5.place(x=200,y=280)
    
    h = Label(t,text='doctorid',fg='red',bg='yellow')
    h.place(x=50,y=320)
    e6 = Entry(t,width=30)
    e6.place(x=200,y=320)
    
    i = Label(t,text='problem',fg='red',bg='yellow')
    i.place(x=50,y=360)
    e7 = Entry(t,width=30)
    e7.place(x=200,y=360)
    
    j = Label(t,text='remarks',fg='red',bg='yellow')
    j.place(x=50,y=400)
    e8 = Entry(t,width=30)
    e8.place(x=200,y=400)
    
    
    
    btn = Button(t,text='update',command=updatedata)
    btn.place(x=150,y=450)
    
    t.geometry('700x700')
    t.config(bg='purple')
    
    t.mainloop()
