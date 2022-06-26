def fibbo(n):
    if n<=1:
        return 1
    else:
        return (fibbo(n-1)+fibbo(n-2))
n=eval(input("Enter the value of n: "))
if n<=0:
    print("Invalid Input..")
else:
    for i in range(0,n):
        print(fibbo(i),end=' ')