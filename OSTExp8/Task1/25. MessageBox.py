from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Welcome to Computer Dept ")
window.geometry('350x200')
def clicked():
    #messagebox.showinfo('Message title', 'Message content')
    #messagebox.showwarning('Message title', 'Message content') #shows warning message
    #messagebox.showerror('Message title', 'Message content') #shows error message
    messagebox.askquestion('Message title','Message content')
    #messagebox.askyesno('Message title','Message content')
    #messagebox.askyesnocancel('Message title','Message content')
    #messagebox.askokcancel('Message title','Message content')
    #messagebox.askretrycancel('Message title','Message content')
btn = Button(window,text='Click here', command=clicked)
btn.grid(column=0,row=0)
window.mainloop()
