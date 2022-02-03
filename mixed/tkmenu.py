from tkinter import *

top = Tk()
top.title("MyMenu")

menubar =Menu(top)
file = Menu(menubar,tearoff=0)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save As")
file.add_command(label="Close")

file.add_separator()

file.add_command(label="Exit",command=top.quit)
menubar.add_cascade(label="File",menu=file)

edit = Menu(menubar,tearoff=0)
edit.add_command(label="Undo")
edit.add_separator()
edit.add_command(label="Appearences")
edit.add_command(label="Tools")

menubar.add_cascade(label="Edit",menu=edit)

top.config(menu=menubar)
top.mainloop()
