from tkinter import filedialog
from os import path

#direc = filedialog.askdirectory()
file = filedialog.askopenfilenames(initialdir="C:/Users/shawn/Desktop/Assignments/OSTExp8", filetypes = (("PNG files","*.png"),("all files","*.*")))

print(file)
