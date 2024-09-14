import pymysql
from tkinter import messagebox
import tkinter
from tkinter import *
from tkinter import ttk
def showdnavigate():
    t=tkinter.Tk()
    t.geometry('1000x1000')
    t.title('DAMS Navigate 4')
    t.config(bg='purple')
    
    xb=[]
    xc=[]
    xd=[]
    xf=[]
    xg=[]
    xh=[]
    xi=[]
    xj=[]
    i=0
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='DAMS')
        cur=db.cursor()
        sql="select*from patients"
        cur.execute(sql)
        data=cur.fetchall()
        
        for res in data:
            xb.append(str(res[0]))
            xc.append(res[1])
            xd.append(res[2])
            xf.append(res[3])
            xg.append(res[4])
            xh.append(res[5])
            xi.append(res[5])
            xj.append(res[5])
            
            
        db.close()
        
    def first():
        global i
        i=0
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        e8.delete(0,100)
        
        e1.insert(0,xb[i])
        e2.insert(0,xc[i])
        e3.insert(0,xd[i])
        e4.insert(0,xf[i])
        e5.insert(0,xg[i])
        e6.insert(0,xh[i])
        e7.insert(0,xi[i])
        e8.insert(0,xj[i])
        
    def next():
        global i
        i=i+1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        e8.delete(0,100)
        
        e1.insert(0,xb[i])
        e2.insert(0,xc[i])
        e3.insert(0,xd[i])
        e4.insert(0,xf[i])
        e5.insert(0,xg[i])
        e6.insert(0,xh[i])
        e7.insert(0,xi[i])
        e8.insert(0,xj[i])
        
    def previous():
        global i
        i=i-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        e8.delete(0,100)
        
        e1.insert(0,xb[i])
        e2.insert(0,xc[i])
        e3.insert(0,xd[i])
        e4.insert(0,xf[i])
        e5.insert(0,xg[i])
        e6.insert(0,xh[i])
        e7.insert(0,xi[i])
        e8.insert(0,xj[i])
        
    def last():
        global i
        i=len(xb)-1
        
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        e8.delete(0,100)
        
        
        e1.insert(0,xb[i])
        e2.insert(0,xc[i])
        e3.insert(0,xd[i])
        e4.insert(0,xf[i])
        e5.insert(0,xg[i])
        e6.insert(0,xh[i])
        e7.insert(0,xi[i])
        e8.insert(0,xj[i])
        
        
    def chx():
        t.destroy()
        
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


    
    b1 = Button(t, text='First', command=first)
    b1.place(x=200, y=450)
   
    b2 = Button(t, text='Next', command=next)
    b2.place(x=250, y=450)
   
    b3 = Button(t, text='Last', command=last)
    b3.place(x=300, y=450)
   
    b4 = Button(t, text='Previous', command=previous)
    b4.place(x=350, y=450)
     
    filldata()
    
    t.mainloop()
     
showdnavigate()
        
        
        
        