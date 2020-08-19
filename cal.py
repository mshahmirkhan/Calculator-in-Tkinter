from tkinter import *
root =Tk()
root.title("simple")

e=Entry(root,width=44,borderwidth=7)
e.grid(row=0,columnspan=5,padx=3,pady=4)

def Button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))
    return

def Button_add():
    first=e.get()
    global math
    math="add"
    global sum
    sum = int(first)
    e.delete(0,END)
    return

def Button_Sub():
    first=e.get()
    global math
    math="sub"
    global sum
    sum = int(first)
    e.delete(0,END)
    return

def Button_Mul():
    first=e.get()
    global math
    math="mul"
    global sum
    sum = int(first)
    e.delete(0,END)
    return

def Button_clear():
    e.delete(0,END)
    return

def Button_equal():
    secound=e.get()
    e.delete(0,END)

    if math=="add" :
        e.insert(0,sum+int(secound))

    elif math=="sub" :
        e.insert(0,sum-int(secound))

    elif math=="mul" :
        e.insert(0,sum*int(secound))
    else    :
        breakpoint()
    return

Button1=Button(root,text="1",padx=40,pady=20, command=lambda :Button_click(1))
Button2=Button(root,text="2",padx=40,pady=20, command=lambda :Button_click(2))
Button3=Button(root,text="3",padx=40,pady=20, command=lambda :Button_click(3))
Button4=Button(root,text="4",padx=40,pady=20, command=lambda :Button_click(4))
Button5=Button(root,text="5",padx=40,pady=20, command=lambda :Button_click(5))
Button6=Button(root,text="6",padx=40,pady=20, command=lambda :Button_click(6))
Button7=Button(root,text="7",padx=40,pady=20, command=lambda :Button_click(7))
Button8=Button(root,text="8",padx=40,pady=20, command=lambda :Button_click(8))
Button9=Button(root,text="9",padx=40,pady=20, command=lambda :Button_click(9))
Button0=Button(root,text="0",padx=40,pady=20, command=lambda :Button_click(0))


ButtonADD=Button(root,text="+",padx=40,pady=20, command=Button_add)
ButtonSUB=Button(root,text="-",padx=40,pady=20, command=Button_Sub)
ButtonMUL=Button(root,text="*",padx=40,pady=20, command=Button_Mul)
ButtonCLEAR=Button(root,text="CLEAR",padx=25,pady=20, command=Button_clear)
ButtonEQUAL=Button(root,text="=",padx=39,pady=20, command=Button_equal)

Button4.grid(row=2,column=0)
Button5.grid(row=2,column=1)
Button6.grid(row=2,column=2)

Button1.grid(row=1,column=0)
Button2.grid(row=1,column=1)
Button3.grid(row=1,column=2)

Button7.grid(row=3,column=0)
Button8.grid(row=3,column=1)
Button9.grid(row=3,column=2)

Button0.grid(row=4,column=0)
ButtonCLEAR.grid(row=4,column=1)
ButtonEQUAL.grid(row=4,column=2)
ButtonMUL.grid(row=5,column=2)

ButtonADD.grid(row=5,column=0)
ButtonSUB.grid(row=5,column=1)







root.mainloop()