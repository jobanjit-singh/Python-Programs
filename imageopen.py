from tkinter import *
root = Tk()
root.geometry("600x600")
photo = PhotoImage(file="edit.png")#store image into photo variable
label = Label(image=photo)#lable of image like text
label.pack()# pack image label into main screen

root.mainloop()