from tkinter import *
from tkinter import font

def add():
    t3.delete(0, 'end')
    num1=int(t1.get())
    num2=int(t2.get())
    result=num1+num2
    t3.insert(END, str(result))
    
def sub():		#add event as parameter if using bind function
    t3.delete(0, 'end')
    num1=int(t1.get())
    num2=int(t2.get())
    result=num1-num2
    t3.insert(END, str(result))
     
def multiply():
    t3.delete(0, 'end')
    num1=int(t1.get())
    num2=int(t2.get())
    result=num1*num2
    t3.insert(END, str(result))
def divide():
     t3.delete(0, 'end')
     num1=int(t1.get())
     num2=int(t2.get())
     result=num1/num2
     t3.insert(END, str(result))
win=Tk()
#mywin=MyWindow(window)
win.title('Calculator')
win.geometry("400x300+10+10")
win.configure(bg='DeepSkyBlue3')

"""init"""
myfont=font.Font(family='Helvetica', size=10, weight='bold')
lbl1=Label(win, text='First number')
lbl1.configure(bg='DeepSkyBlue3', font=myfont)
lbl2=Label(win, text='Second number')
lbl2.configure(bg='DeepSkyBlue3', font=myfont)
lbl3=Label(win, text='Result')
lbl3.configure(bg='DeepSkyBlue3', font=myfont)

t1=Entry(bd=3)
t2=Entry(bd=3)
t3=Entry(bd=5)


b1=Button(win, text='Add', command=add, font=myfont)
b2=Button(win, text='Subtract', command=sub, font=myfont)
##b2.bind('<Button-1>', sub)	#sub takes event as argument
b3=Button(win, text='Multiply', command=multiply, font=myfont)
b4=Button(win, text='Divide', command=divide, font=myfont)

b1.configure(bg='gold')
b2.configure(bg='gold')
b3.configure(bg='gold')
b4.configure(bg='gold')

lbl1.place(x=100, y=50)
t1.place(x=200, y=50)

lbl2.place(x=80, y=100)
t2.place(x=200, y=100)

b1.place(x=50, y=150)
b2.place(x=120, y=150)
b3.place(x=220, y=150)
b4.place(x=320, y=150)


lbl3.place(x=130, y=200)
t3.place(x=200, y=200)

win.mainloop()
	
