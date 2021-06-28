import tkinter
from tkinter import *
from tkinter import messagebox

val=""
A = 0
operator=""

def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)

def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)

def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)

def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)

def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)

def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)

def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)

def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)

def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)

def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)

def btn_add_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_sub_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_mul_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btn_div_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def btn_equal_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "="
    val = val + "="
    data.set(val)

def C_pressed():
    global A
    global operator
    global val
    val = ""
    A=0
    operator=""
    data.set(val)


def result():
    global A
    global operator
    global val
    val2 = val
    if operator == "+":
        x=int((val2.split("+")[1]))
        c = A + x
        data.set(c)
        val=str(c)
    elif operator == "-":
        x=int((val2.split("-")[1]))
        c = A - x
        data.set(c)
        val=str(c)
    elif operator == "*":
        x=int((val2.split("*")[1]))
        c = A * x
        data.set(c)
        val=str(c)
    elif operator == "/":
        x=int((val2.split("/")[1]))
        if x==0:
            messagebox.showerror("Calculater Error","Dividing something by 0 is not possible")
            A==""
            val=""
            data.set(val)
        else:
            c=int(A/x)
            data.set(c)
            val=str(c)


base = tkinter.Tk()
base.geometry("250x400+300+300")
base.resizable(0,0)
base.title("DuB's Calculater")

data= StringVar()
lbl=Label(
    base,
    text="Label",
    anchor=SE,
    font=("Verdana",20),
    textvariable=data,
    background="#ffffff",
    fg="#000000",
)
lbl.pack(expand=True,fill="both",)

btnrow1=Frame(base,bg="#000000")
btnrow1.pack(expand=True,fill="both",)

btnrow2=Frame(base)
btnrow2.pack(expand=True,fill="both",)

btnrow3=Frame(base)
btnrow3.pack(expand=True,fill="both",)

btnrow4=Frame(base)
btnrow4.pack(expand=True,fill="both",)

btn1=Button(
    btnrow1,
    text = "1",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_1_isclicked,
)
btn1.pack(side=LEFT,expand=True,fill="both",)
btn2=Button(
    btnrow1,
    text = "2",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_2_isclicked,
)
btn2.pack(side=LEFT,expand=True,fill="both",)
btn3=Button(
    btnrow1,
    text = "3",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_3_isclicked,
)
btn3.pack(side=LEFT,expand=True,fill="both",)
btnadd=Button(
    btnrow1,
    text = "+",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_add_clicked,
)
btnadd.pack(side=LEFT,expand=True,fill="both",)
btn4=Button(
    btnrow2,
    text = "4",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_4_isclicked,
)
btn4.pack(side=LEFT,expand=True,fill="both",)
btn5=Button(
    btnrow2,
    text = "5",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_5_isclicked,
)
btn5.pack(side=LEFT,expand=True,fill="both",)
btn6=Button(
    btnrow2,
    text = "6",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_6_isclicked,
)
btn6.pack(side=LEFT,expand=True,fill="both",)
btnsub=Button(
    btnrow2,
    text = "-",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_sub_clicked,
)
btnsub.pack(side=LEFT,expand=True,fill="both",)
btn7=Button(
    btnrow3,
    text = "7",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_7_isclicked,
)
btn7.pack(side=LEFT,expand=True,fill="both",)
btn8=Button(
    btnrow3,
    text = "8",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_8_isclicked,
)
btn8.pack(side=LEFT,expand=True,fill="both",)
btn9=Button(
    btnrow3,
    text = "9",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_9_isclicked,
)
btn9.pack(side=LEFT,expand=True,fill="both",)
btnmul=Button(
    btnrow3,
    text = "*",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_mul_clicked,
)
btnmul.pack(side=LEFT,expand=True,fill="both",)
btnC=Button(
    btnrow4,
    text = "C",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = C_pressed,
)
btnC.pack(side=LEFT,expand=True,fill="both",)
btn0=Button(
    btnrow4,
    text = "0",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_0_isclicked,
)
btn0.pack(side=LEFT,expand=True,fill="both",)
btnequal=Button(
    btnrow4,
    text = "=",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command=result,
)
btnequal.pack(side=LEFT,expand=True,fill="both",)
btndiv=Button(
    btnrow4,
    text = "/",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_div_clicked,
    
)
btndiv.pack(side=LEFT,expand=True,fill="both",)


base.mainloop()