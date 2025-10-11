from tkinter import *

window = Tk()

window.title("my toplevel window") # ✅ use parentheses, don’t assign

window.geometry('500x500')

top = Toplevel()

top.title("my toplevel window") # ✅ same fix here

top.geometry("300x300")

window.mainloop()