import pymysql
from tkinter import messagebox
import tkinter
from tkinter import *
from tkinter import ttk
def showdnavigate():
    t=tkinter.Tk()
    t.geometry('1000x1000')
    t.title('DAMS Navigate 5')
    t.config(bg='purple')
    
    xb=[]
    xc=[]
    xd=[]
    i=0
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='DAMS')
        cur=db.cursor()
        sql="select*from timetable"
        cur.execute(sql)
        data=cur.fetchall()
        
        for res in data:
            xb.append(str(res[0]))
            xc.append(res[1])
            xd.append(res[2])
            
            
            
            
        db.close()
        
    def first():
        global i
        i=0
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        
        
        
        e1.insert(0,xb[i])
        e2.insert(0,xc[i])
        e3.insert(0,xd[i])
        
        
        
    def next():
        global i
        i=i+1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        
        
        
        e1.insert(0,xb[i])
        e2.insert(0,xc[i])
        e3.insert(0,xd[i])
        
        
        
    def previous():
        global i
        i=i-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        
        
        
        e1.insert(0,xb[i])
        e2.insert(0,xc[i])
        e3.insert(0,xd[i])
        
        
        
    def last():
        global i
        i=len(xb)-1
        
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        
        
        
        e1.insert(0,xb[i])
        e2.insert(0,xc[i])
        e3.insert(0,xd[i])
        
        
        
        
    def chx():
        t.destroy()
        
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
        
        
        
        