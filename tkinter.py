from tkinter import *
root=Tk()
root.title("wELCOME TO ABHI'S WEB")
root.geometry("300x200")
lbl=Label(root,text="Are you a geek")
lbl.grid()
def clicked():
    lbl.configure(text="I just got clicked")
btn=Button(root,text="Click me",fg="black",bg="White",command=clicked())
btn.grid(column=1,row=0)
root.mainloop()

