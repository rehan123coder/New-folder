from tkinter import*
from tkinter import messagebox
Window=Tk()
def msg():
    messagebox.askokcancel("box","do you want to exit")
button1=Button(bg="green",fg="lightblue",text="click me",command=msg)
button1.pack()
Window.mainloop()