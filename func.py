#program to make a simple calculator
def add(x,y):
    """For Addition"""
    return(x+y)
def subtract(x,y):
    """For Subtraction"""
    return(x-y) 
def multiply(x,y):
    """For Multiplication"""
    return(x*y)
def divide(x,y):
    """For Division"""
    return(x/y)
def modulus(x,y):
    """For Remainder"""
    return(x%y)
a=eval(input("Enter the 1st Number: "))
b=eval(input("Enter the 2nd Number: "))
print("Enter 1 for Addition")
print("Enter 2 for Subtraction")
print("Enter 3 for Multiplication")
print("Enter 4 for Division")
print("Enter 5 for Remainder")
ope = eval(input(":"))
if ope==1:
    print("Sum is:",add(a,b))
elif ope==2:
    print("Subtraction is:",subtract(a,b))
elif ope==3:
    print("Multiplication is:",multiply(a,b))
elif ope==4:
    print("Division is:",divide(a,b))
elif ope==5:
    print("Remainder is:",modulus(a,b))
else:
    print("Invalid Input...")
