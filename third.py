from tkinter import*
Window=Tk()
frame1=Frame(master=Window,width=100,height=100,bg="red")
frame1.pack(side=TOP)
frame2=Frame(master=Window,width=50,height=50,bg="yellow")
frame2.pack(side=LEFT)
frame3=Frame(master=Window,width=25,height=25,bg="blue")
frame3.pack(side=LEFT)
Window.mainloop()



