from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Welcome to Computer Dept")
window.geometry('300x300')

##combo = Combobox(window)
##combo['values']= (1, 2, 3, 4, 5, "SE", "TE", "BE")
##combo.current(5) #set the selected item
##combo.grid(column=0, row=0)

chk_state1 = BooleanVar()
chk_state1.set(True) #set check state
chk1 = Checkbutton(window, text='SE', var=chk_state1)
chk1.grid(column=0, row=0)

chk_state2 = BooleanVar()
chk_state2.set(False) #set check state
chk2 = Checkbutton(window, text='TE', var=chk_state2)
chk2.grid(column=0, row=1)

chk_state3 = BooleanVar()
chk_state3.set(False) #set check state
chk3 = Checkbutton(window, text='BE', var=chk_state3)
chk3.grid(column=0, row=2)

window.mainloop()
