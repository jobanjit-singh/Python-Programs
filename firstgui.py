from tkinter import *
root = Tk()#object of tkinder for gui
root.geometry("600x500")#startup size in width and height
root.minsize(200,100)#minimum size of window resize
#root.maxsize(1280,720)
label = Label(text="This is my first GUI in Python")
label2 = Label(text="This is my first GUI in Python second label")
label.pack()#To pack label in gui 
label2.pack()
root.mainloop()