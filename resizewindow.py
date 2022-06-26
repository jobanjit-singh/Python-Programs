from tkinter import *
root = Tk()
def resizer():
    height1=e1entry
    width1=e2entry
    root.geometry(f"{e2entry.get()}x{e1entry.get()}") 
root.title("Resizer")
l1=Label(root,text="Height:")
l2=Label(root,text="Width:")
l3=Label(root,text="Window Resizer")
l3.grid(row=0,column=1)
l1.grid(row=1,column=0)
l2.grid(row=2,column=0)
b1 = Button(root,text="Resize",command=resizer)
b1.grid(row=3,column=1)
e1entry = StringVar()
e2entry = StringVar()
e1 = Entry(root,textvariable=e1entry)
e2 = Entry(root,textvariable=e2entry)
e1.grid(row=1,column=1)
e2.grid(row=2,column=1)
root.mainloop()
