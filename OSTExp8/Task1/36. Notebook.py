from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Welcome to Computer Dept ")
window.geometry("600x400")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='First Tab')
tab_control.add(tab2, text='Second Tab')

lbl1 = Label(tab1, text= 'Welcome to Tab1', padx = 100, pady = 10)
lbl1.grid(column=0, row=0)

lbl2 = Label(tab2, text= 'welcome to Tab2')
lbl2.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')

window.mainloop()
