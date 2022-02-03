from tkinter import *
def check():
    a = int(txt1.get())
    if a%2==0:
        lblresult.config(text="Number is Even")
    else:
        lblresult.config(text="Number is Odd")

form = Tk()
form.title("My Main Form")
frame = Frame(form, width=500, height= 400)
frame.pack()
form.resizable(width=False,height=False)
lblheading = Label(frame, text="Enter Value: ")
lblheading.place(x=10,y=10)

txt1=Entry(frame,width=30)
txt1.place(x=10,y=30)

btn1=Button(frame,text="Click", command=check)
btn1.place(x=10, y =60)

lblresult = Label(frame,text="Result")
lblresult.place(x=10,y=90)
form.mainloop()
