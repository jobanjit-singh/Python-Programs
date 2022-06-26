n=eval(input("Enter the n value: "))
a=1
b=1
if n<=0:
    print("Invalid Input")
elif n==1:
    print(a,end=' ')
elif n==2:
    print(a,end=' ')
    print(b,end=' ')
else:
    print(a,end=' ')
    print(b,end=' ')
    for i in range(3,n+1):
        c=a+b
        print(c,end=' ')
        a=b
        b=c