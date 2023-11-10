from tkinter import*
w=Tk()
w.config(background="black")
w.geometry('300x300')
l1=Label(w,text='num1')
e1=Entry(w,width=20)
l2=Label(w,text='num2')
e2=Entry(w,width=20)
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
e1.grid(row=0,column=1,padx=10)
e2.grid(row=1,column=1,padx=10)
def add():
    r=(int(e1.get()))+(int(e2.get()))
    e3.delete(0,END)
    e3.insert(END,r)
def sub():
    r=(int(e1.get()))-(int(e2.get()))
    e3.delete(0,END)
    e3.insert(END,r)
def mul():
    r=(int(e1.get()))*(int(e2.get()))
    e3.delete(0,END)
    e3.insert(END,r)
def div():
    r=(int(e1.get()))/(int(e2.get()))
    e3.delete(0,END)
    e3.insert(END,r)
b1=Button(w,text='ADD',command=add).grid(row=3,column=0) 
b2=Button(w,text='SUB',command=sub).grid(row=3,column=1) 
b3=Button(w,text='MUL',command=mul).grid(row=3,column=2) 
b4=Button(w,text='DIV',command=div).grid(row=3,column=3)

e3=Entry(w,width=20).grid()
w.mainloop()    


    