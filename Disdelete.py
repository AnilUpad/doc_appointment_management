import pymysql
from tkinter import messagebox
import tkinter 
from tkinter import *
from tkinter import ttk
def showdelete():
    t = tkinter.Tk()


    def deletedata():
        if len(e1.get())==0:
            messagebox.showinfo('hi','pls filldata')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='DAMS')
            cur=db.cursor()
            xa=int(e1.get())
            sql="delete from Discharge where dischargeno=%d"%(xa)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hi','deleted')
            db.close()
            e1.delete(0,100)
    
    
    a = Label(t,text='Discharge',font=('arial',15),fg='red',bg='cyan')
    a.place(x=350,y=20)
    
    b = Label(t,text='dischargeno',fg='red',bg='yellow')
    b.place(x=50,y=120)
    e1 = Entry(t,width=30)
    e1.place(x=200,y=120)
    
    c = Label(t,text='appointmentno',fg='red',bg='yellow')
    c.place(x=50,y=160)
    e2 = Entry(t,width=30)
    e2.place(x=200,y=160)
    
    d = Label(t,text='patienstid',fg='red',bg='yellow')
    d.place(x=50,y=200)
    e3 = Entry(t,width=30)
    e3.place(x=200,y=200)
    
    
    g = Label(t,text='dateofdischarge',fg='red',bg='yellow')
    g.place(x=50,y=280)
    e5 = Entry(t,width=30)
    e5.place(x=200,y=280)
    
    h = Label(t,text='remarks',fg='red',bg='yellow')
    h.place(x=50,y=320)
    e6 = Entry(t,width=30)
    e6.place(x=200,y=320)
    
    btn = Button(t,text='delete',fg='red',bg='yellow',command=deletedata)
    btn.place(x=150,y=380)
    
    t.geometry('700x700')
    t.config(bg='purple')
    
    
    
    t.mainloop()
