# import tkinter
# root=tkinter.Tk()
# l1=tkinter.Label(root,text="Red Sun",bg="red",fg="white").pack(fill="x",pady=10)
# l1=tkinter.Label(root,text="Green Grass",bg="green",fg="black").pack(fill="x",ipadx=10)
# l1=tkinter.Label(root,text="Blue Sky",bg="blue",fg="white").pack(fill="x",pady=10)
# root.mainloop()
# ////////////////////////////////////////////////////////////
# import tkinter
# w=tkinter.Tk()
# w.title("GUI")
# t1=tkinter.Frame(w).pack()
# b1=tkinter.Frame(w).pack(side="bottom")
# bt1=tkinter.Button(t1,text="button1",fg="red").pack()
# bt1=tkinter.Button(t1,text="button2",fg="green").pack()
# bt1=tkinter.Button(b1,text="button3",fg="purple").pack()
# bt1=tkinter.Button(b1,text="button4",fg="orange").pack()
# w.mainloop()
# //////////////////////////////////////////////////////////
# import tkinter
# w=tkinter.Tk()
# w.title("GUI")
# l1=tkinter.Label(text="Username").grid(row=0)
# tkinter.Entry(w).grid(row=0,column=1)
# p=tkinter.Label(text="password").grid(row=1)
# tkinter.Entry(w).grid(row=1,column=1)
# tkinter.Checkbutton(w,text="Keep me Logged In").grid(column=1)
# w.mainloop()
# //////////////////////////////////////////////////////////////////////////
# import tkinter
# w=tkinter.Tk()
# w.title("Welcome to LikeGeeks app")
# ibl=tkinter.Label(text="Hello",font=("Arial Bold",50)).grid(column=0,row=0)
# w.mainloop()
# ////////////////////////////////////////////////////////
import tkinter
w=tkinter.Tk()
c=tkinter.Canvas(bg="grey",height="250",width="300")
ca=10,50,240,210
arc=c.create_arc(ca,start=0,extent=150,fill="red")
c.pack()
w.mainloop()
