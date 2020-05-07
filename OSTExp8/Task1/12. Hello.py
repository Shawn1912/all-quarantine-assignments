##from tkinter import *
##
##def clicked():
##    lbl.configure(text="Button was clicked!")
##
##window = Tk()
##window.title("Welcome to Comp Dept")
##window.geometry('800x300')
##
##lbl = Label(window, text=" Hello, I am Shawn", font=("Arial Bold", 50))
##btn = Button(window, text="Click Here", font=("Arial Bold", 30), bg="orange", fg="red", command = clicked)
##
##lbl.grid(column=0, row=0)
##btn.grid(column=1,row=0)
##
##window.mainloop()

from tkinter import *
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)
window = Tk()
window.title("Welcome to Computer Dept")
window.geometry('300x300')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
txt = Entry(window,width=10)
txt.focus()	 #set focus (no need to click)
txt.grid(column=1, row=0)
txt1 = Entry(window,width=10, state='disabled')
txt1.grid(column=3, row=0) 
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()

