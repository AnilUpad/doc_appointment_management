import pymysql
from tkinter import messagebox
import tkinter 
from tkinter import *
from tkinter import ttk
def showupdate():
    t = tkinter.Tk()
    t.geometry('700x700')
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='DAMS')
        cur=db.cursor()
        xb=int(e1.get())
        xc=e2.get()
        xd=e3.get()
        xf=e4.get()
        xg=e5.get()
        sql="UPDATE Doctor SET doctorname='%s',specilization='%s',email='%s',phone='%s' WHERE doctorid='%d'" % (xc,xd,xf,xg,xb)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','update')
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e4.insert(0,data[3])
        
        db.close()
    
    a = Label(t,text='Doctor',font=('arial',15),fg='red',bg='cyan')
    a.place(x=350,y=20)
    
    b = Label(t,text='doctorid',fg='red',bg='yellow')
    b.place(x=50,y=120)
    e1 = Entry(t,width=30)
    e1.place(x=200,y=120)
    
    c = Label(t,text='doctorname',fg='red',bg='yellow')
    c.place(x=50,y=160)
    e2 = Entry(t,width=30)
    e2.place(x=200,y=160)
    
    d = Label(t,text='specilization',fg='red',bg='yellow')
    d.place(x=50,y=200)
    e3 = Entry(t,width=30)
    e3.place(x=200,y=200)
    
    f = Label(t,text='email',fg='red',bg='yellow')
    f.place(x=50,y=240)
    e4 = Entry(t,width=30)
    e4.place(x=200,y=240)
    
    g = Label(t,text='phone',fg='red',bg='yellow')
    g.place(x=50,y=280)
    e5 = Entry(t,width=30)
    e5.place(x=200,y=280)
    
    btn = Button(t,text='update',fg='red',bg='yellow',command=updatedata)
    btn.place(x=150,y=360)
    
    t.mainloop()
