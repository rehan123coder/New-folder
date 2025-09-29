from tkinter import*
from tkinter import messagebox
Window=Tk()
label1=Label(text="i am at (0,0)",bg="red")
label1.place(x=0, y=0)
label2=Label(text="i am at (75,75)",bg="red")
label2.place(x=75, y=75)
def clickme(event):
    print("the button was clicked")
def msg():
    messagebox.showwarning("box","do you want to delete")
button1=Button(bg="green",fg="lightblue",text="click me")
Window.bind("<Button-1>", clickme)
button1.pack()
button2=Button(bg="green",fg="lightblue",text="click me",command=msg)
button2.pack()
Window.mainloop()