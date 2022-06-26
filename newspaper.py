from cProfile import label
from textwrap import fill
from tkinter import *
from turtle import left
root = Tk()
root.geometry("1280x720")
root.title('The Breaking News')
f1 = Frame(root,borderwidth=6)
l= Label(f1,text="This is breaking news",font="rockwell 19 bold",padx=3,background="red",foreground="white")
l.pack()
f1.pack(side=TOP,anchor='nw')
f2= Frame(root ,borderwidth=7)
photo = PhotoImage(file = "edit.png")
l2 = Label(f2,image=photo)
l2.pack()
f2.pack(side="left",anchor='nw')
f3 = Frame(root,borderwidth=7)
l3 = Label(f3,padx=15,text="This news is about the edit application which is in process and which is developed by the jit code",pady=20)
l3.pack()
f3.pack(side=BOTTOM,anchor='se')
root.mainloop()