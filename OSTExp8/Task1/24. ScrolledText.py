from tkinter import *
from tkinter import scrolledtext
window = Tk()
window.title("Welcome to Computer Dept ")
window.geometry('350x200')
txt = scrolledtext.ScrolledText(window,width=40,height=10)
txt.insert(INSERT,'Shawn\nBatch B\nRoll no 31\nSE Comps\nDBIT\nPython\nJava\nC\nc++\nWebdev\nGamedev')

txt.grid(column=0,row=0)
window.mainloop()
