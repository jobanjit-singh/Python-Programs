from tkinter import *
def printval():
    Label(root,text="Form Submitted",font="rockwell 19 bold",pady=10).grid(row=7,column=2)
root = Tk()
root.geometry("400x400") 
root.title("Registration Form")
Label(root,text="Registration Form",font="rockwell 19 bold",pady=10).grid(row=0,column=2)
Label(root,text='Name',font="rockwell 10 bold").grid(row=1,column=1)
Label(root,text='Rollno',font="rockwell 10 bold").grid(row=2,column=1)
Label(root,text='Branch',font="rockwell 10 bold").grid(row=3,column=1)
Label(root,text='Department',font="rockwell 10 bold").grid(row=4,column=1)

namevalue=StringVar()
rollnovalue=StringVar()
branchvalue=StringVar()
departvalue=StringVar()
studentcheck=IntVar()

namepack=Entry(root,textvariable=namevalue)
rollpack=Entry(root,textvariable=rollnovalue)
branchpack=Entry(root,textvariable=branchvalue)
departpack = Entry(root,textvariable=departvalue)
namepack.grid(row=1,column=2)
rollpack.grid(row=2,column=2)
branchpack.grid(row=3,column=2)
departpack.grid(row=4,column=2)

studentpack = Checkbutton(root,text="Check If you are Student..",pady=10,variable=studentcheck)
studentpack.grid(row=5,column=2)

Button(root,text="Submit Your Form",command=printval).grid(row=6,column=2)

root.mainloop()
