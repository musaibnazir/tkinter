import tkinter as t
from tkinter import messagebox as msg
def myfunc():
    val = int(entry.get())
    if val >= 18:
        msg.showinfo('Result','Eligible')
    else:
        msg.showerror('Result','Not Eligible')


window = t.Tk()
window.title("My Application")

lbl = t.Label(window, text="Check Your Eligibility")
lbl.place(x=10, y = 10)
lbl = t.Label(window, text="Enter your Age: ")
lbl.place(x=10, y = 40)

entry = t.Entry(window,width = 20)
entry.place(x=10, y = 80)

btn = t.Button(window,text="ClickMe", command= myfunc)
btn.place(x=10,y=120)

window.mainloop()
