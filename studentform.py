from tkinter import *
root = Tk()
def detail():#function of detail showing in vs code
    print(student.get())
    print(fathername.get())
    print(mothername.get())
    print(ageof.get())
root.title("Student's Detail Form..✍")
root.geometry("300x150")
user = Label(root,text="Student Name: ")
Father = Label(root,text="Father's Name: ")
mother = Label(root,text="Mother's Name: ")
age = Label(root,text="Age :")
user.grid(row=0)
Father.grid(row=1)
mother.grid(row=2)
age.grid(row=3)

student = StringVar()
fathername= StringVar()
mothername = StringVar()
ageof = IntVar()

studentvalue = Entry(root,textvariable=student)
fathernamevalue = Entry(root,textvariable=fathername)
mothernamevalue = Entry(root,textvariable=mothername)
agevalue = Entry(root,textvariable=ageof)

studentvalue.grid(row=0,column=1)
fathernamevalue.grid(row=1,column=1)
mothernamevalue.grid(row=2,column=1)
agevalue.grid(row=3,column=1)

button = Button(root,text = "Submit",command=detail)
button.grid(row=4)

root.mainloop()