from tkinter import *
root = Tk()
def print1():
    print(name.get())
root.geometry("500x700")
l1 = Label(root,text="Welcome",font="Rockwell 50 bold")
l1.grid(row=0,column=0)
name = StringVar()
e1 = Entry(root,textvariable=name)
e1.grid(row=1,column=1)
b1 = Button(root,text="Submit",command=print1)
b1.grid(row=2,column=1)
root.mainloop()