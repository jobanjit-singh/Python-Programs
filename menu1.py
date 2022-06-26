from tkinter import *
root = Tk()
root.geometry("500x300")
root.title("Menus..")
def myfunc():
    print("Helloo Menus...")

mainmenu = Menu(root)

filemenu = Menu(mainmenu)
filemenu.add_command(label="Open", command=myfunc)
filemenu.add_command(label="New", command=myfunc)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)
root.config(mainmenu)
mainmenu.add_cascade(label="File", menu=filemenu)

root.mainloop()