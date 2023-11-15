from tkinter import*
w=Tk()
w.geometry("312x324")
w.resizable(0,0)
w.title("Calculator")
def btn_click(item):
    global expression
    expression=expression+str(item)
    input_text.set(expression)
def btn_clear():
    global expression
    expression=""
    input_text.set("")
def btn_equal():
    global expression
    result=str(eval(expression))  
    input_text.set(result)
    expression=""
    expression=""
    input_text=StringVar()
# input_frame=Frame(w,width=312,height=50,bd=0,highlightbackground="black",highlightcolor="black",highlightthickness=1)
# input_frame.grid(row=0,column=0,side=TOP)
# input_field=Entry(input_frame,font=('arial',18,'bold'),width=50,bg="#eee",bd=0,justify=RIGHT)
# input_field.grid(row=1,column=0)
# input_field.grid(row=1,column=0,pady=10)
btns_frame=Frame(w,width=312,height=272.5,bg="grey")
btns_frame.grid(row=2,column=0)
clear=Button(btns_frame,text="C",fg="black",width=32,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:btn_clear()).grid(row=0,column=0,columnspan=3,padx=1,pady=1)
divide=Button(btns_frame,text="/",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:btn_click("/")).grid(row=0,column=3,padx=1,pady=1)
seven=Button(btns_frame,text="7",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btn_click(7)).grid(row=1,column=0,padx=1,pady=1)
eight=Button(btns_frame,text="8",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btn_click(8)).grid(row=1,column=1,padx=1,pady=1)
nine=Button(btns_frame,text="9",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btn_click(9)).grid(row=1,column=2,padx=1,pady=1)
multiply=Button(btns_frame,text="*",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:btn_click("*")).grid(row=1,column=3,padx=1,pady=1)
four=Button(btns_frame,text="4",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btn_click(4)).grid(row=2,column=0,padx=1,pady=1)
five=Button(btns_frame,text="5",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btn_click(5)).grid(row=2,column=1,padx=1,pady=1)
six=Button(btns_frame,text="6",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btn_click(6)).grid(row=2,column=2,padx=1,pady=1)
minus=Button(btns_frame,text="-",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:btn_click("-")).grid(row=2,column=3,padx=1,pady=1)
one=Button(btns_frame,text="1",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btn_click(1)).grid(row=3,column=0,padx=1,pady=1)
two=Button(btns_frame,text="2",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btn_click(2)).grid(row=3,column=1,padx=1,pady=1)
three=Button(btns_frame,text="3",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btn_click(3)).grid(row=3,column=2,padx=1,pady=1)
plus=Button(btns_frame,text="+",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:btn_click("+")).grid(row=3,column=3,padx=1,pady=1)
zero=Button(btns_frame,text="0",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btn_click(0)).grid(row=4,column=2,columnspan=2,padx=1,pady=1)
point=Button(btns_frame,text=".",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:btn_click(".")).grid(row=4,column=2,padx=1,pady=1)
equals=Button(btns_frame,text="=",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btn_equal(6)).grid(row=4,column=3,padx=1,pady=1)
input_text=Entry(w,width=20).grid()
w.mainloop()








