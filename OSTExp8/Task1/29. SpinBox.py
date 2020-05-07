from tkinter import *
window = Tk()
window.title("Welcome to Computer Dept ")
window.geometry('350x200')

var =IntVar()
var.set(36)
spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
#spin = Spinbox(window, from_=0, to=100, width=5)
#spin = Spinbox(window, values=(3, 8, 11), width=5)

spin.grid(column=0,row=0)
window.mainloop()
