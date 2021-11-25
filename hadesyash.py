import math
from tkinter import*  

def func1():
    myWindow=Tk()
    myWindow['bg']="white"
    myWindow.title("Basic Calculator")
    myWindow.geometry('900x450')
    print("Your BASIC CALCULATOR GUI has opened in your taskbar")

    def findSum():
        a=int(No1.get())
        b=int(No2.get())
        c=a+b
        ans.delete(0,END)
        ans.insert(0,str(c))
        str1=str(a)+" and "+str(b)
       
    def findDifference():
        a=int(No1.get())
        b=int(No2.get())
        c=a-b
        ans.delete(0,END)
        ans.insert(0,str(c))
        str1=str(a)+" and "+str(b)

    def findProduct():
        a=int(No1.get())
        b=int(No2.get())
        c=a*b
        ans.delete(0,END)
        ans.insert(0,str(c))
        str1=str(a)+" and "+str(b)
        
    def finddivision():
        a=int(No1.get())
        b=int(No2.get())
        c=a/b
        ans.delete(0,END)
        ans.insert(0,str(c))
        str1=str(a)+" and "+str(b)

    Label(myWindow,text="Basic Operations", padx=100, pady=25, bg='red', fg='blue', bd=5, relief='raised', font='system').grid(row=0,column=1)

    Label(myWindow,text="Enter Your First Number", padx=50, pady=15, bg='white').grid(row=1,column=0)
    No1=Entry(myWindow,width=15)
    No1.grid(row=1,column=1)

    Label(myWindow,text="Enter Your Second Number", padx=42, pady=15, bg='white').grid(row=2,column=0)

    No2=Entry(myWindow,width=15)
    No2.grid(row=2,column=1)

    Label(myWindow,text="Here Is Your Answer", padx=65, pady=15, bg='white').grid(row=3,column=0)
    Label(myWindow,text="Which operation do you need to perform? Click on that.", padx=10, pady=15, bg='white', fg="blue").grid(row=5,column=0)
    ans=Entry(myWindow,width=15)
    ans.grid(row=3,column=1)


    Button(myWindow,text="Sum",padx=35,pady=13, command=findSum, bg='light green').grid(row=4,column=1)
    Button(myWindow,text="Difference",padx=20,pady=13, command=findDifference, bg='light green').grid(row=5,column=1)
    Button(myWindow,text="Product",padx=26,pady=13, command=findProduct, bg='light green').grid(row=6,column=1)
    Button(myWindow,text="Division",padx=26,pady=13, command=finddivision, bg='light green').grid(row=7,column=1)


    mainloop()
def func2():
    myWindow=Tk()
    myWindow['bg']="cyan"
    myWindow.title("Basic Calculator")
    myWindow.geometry('700x250')
    print("Your BASIC CALCULATOR GUI has opened in your taskbar")

    def squrt():
        a=int(No1.get())
        c=math.sqrt(a)
        ans.delete(0,END)
        ans.insert(0,str(c))
        str1=str(a)

    Label(myWindow,text="Square Root", padx=100, pady=25, bg='red', fg='blue', bd=5, relief='raised', font='system').grid(row=0,column=1)
    Label(myWindow,text="Enter Your Number", padx=50, pady=15, bg='white').grid(row=1,column=0)
    No1=Entry(myWindow,width=15)
    No1.grid(row=1,column=1)
    Label(myWindow,text="Here Is Your Answer", padx=48, pady=15, bg='white').grid(row=3,column=0)
    ans=Entry(myWindow,width=15)
    ans.grid(row=3,column=1)
    Button(myWindow,text="Sqaure Root",padx=26,pady=13, command=squrt, bg='light green').grid(row=7,column=1)
    mainloop()

myWindow=Tk()
myWindow['bg']="cyan"
myWindow.title("Calculator")
myWindow.geometry('530x177')
print("Your CALCULATOR GUI has opened in your taskbar")
Label(myWindow,text="Click on what math operation you want to perform:", padx=100, pady=25, bg='magenta', fg='blue', bd=5, relief='raised', font='system').grid(row=0,column=1)
Button(myWindow,text="Addition, Subtraction, Multiplpication, Division",padx=35,pady=13, command=func1, bg='light green').grid(row=4,column=1)
Button(myWindow,text="Square Root",padx=20,pady=13, command=func2, bg='light green').grid(row=5,column=1)
mainloop()
