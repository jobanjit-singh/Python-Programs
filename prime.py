import math
c=0
a=eval(input("Enter the number: "))
if a<=1:
    print(a,"is not prime number")
else:
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            c=1
            break
    if c==0:
        print(a,"is Prime number")
    else:
        print(a,"is not prime number")
