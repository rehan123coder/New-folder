from tkinter import*
Window=Tk()
Window.title=("frame")
Window.geometry=("500x500")
boder_effects=[FLAT,SUNKEN,RAISED,GROOVE,RIDGE]
for r in boder_effects:
    frame=Frame(master=Window,relief=r, borderwidth=5)
    frame.pack(side=LEFT)
    label=Label(master=frame, text=r)
    label.pack()
