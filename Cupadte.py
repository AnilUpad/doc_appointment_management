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
        xe=e4.get()
        xf=e5.get()
        xg=e6.get()
        xi=e8.get()
        sql="UPDATE Clinicmaster SET Cname='%s',ownername='%s',address='%s',phone='%s',email='%s',regno='%s' WHERE clinicid='%d'" % (xc,xd,xe,xf,xg,xi,xb)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','update')
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e8.delete(0,100)
        
        
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        e6.insert(0,data[4])
        e8.insert(0,data[5])
        
        db.close()
    
    a = Label(t,text='Clinicmaster',font=('arial',15),fg='red',bg='cyan')
    a.place(x=350,y=20)
    
    b = Label(t,text='clinicid',fg='red',bg='yellow')
    b.place(x=50,y=120)
    e1 = Entry(t,width=30)
    e1.place(x=200,y=120)
    
    c = Label(t,text='Cname',fg='red',bg='yellow')
    c.place(x=50,y=160)
    e2 = Entry(t,width=30)
    e2.place(x=200,y=160)
    
    d = Label(t,text='Ownername',fg='red',bg='yellow')
    d.place(x=50,y=200)
    e3 = Entry(t,width=30)
    e3.place(x=200,y=200)
    
    e = Label(t,text='address',fg='red',bg='yellow')
    e.place(x=50,y=240)
    e4 = Entry(t,width=30)
    e4.place(x=200,y=240)
    
    f = Label(t,text='phone',fg='red',bg='yellow')
    f.place(x=50,y=280)
    e5 = Entry(t,width=30)
    e5.place(x=200,y=280)
    
    g = Label(t,text='email',fg='red',bg='yellow')
    g.place(x=50,y=320)
    e6 = Entry(t,width=30)
    e6.place(x=200,y=320)
    
    
    
    i = Label(t,text='regno',fg='red',bg='yellow')
    i.place(x=50,y=400)
    e8 = Entry(t,width=30)
    e8.place(x=200,y=400)
    
    btn = Button(t,text='update',fg='red',bg='yellow',command=updatedata)
    btn.place(x=150,y=450)
    
    t.geometry('700x700')
    t.config(bg='purple')
    
    t.mainloop()