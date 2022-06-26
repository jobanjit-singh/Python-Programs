a=eval(input("Enter the number: "))
fac=1
if a<=1:
    print(a,"factorial is",fac)
else:
    for i in range(1,a+1):
        fac=fac*i
    print(a,"factorial is",fac)