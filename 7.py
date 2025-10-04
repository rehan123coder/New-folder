from tkinter import*
from tkinter import messagebox
Window=Tk()
def msg():
    messagebox.showerror("box","there is an error found")
button1=Button(bg="green",fg="lightblue",text="click me",command=msg)
button1.pack()
Window.mainloop()