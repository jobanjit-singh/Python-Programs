import math
a=eval(input("Enter the a value: "))
b=eval(input("Enter the b value: "))
print("Prime numbers between",a,"and",b,"is:-")
for i in range(a,b+1):
    c=0
    for n in range(2,int(math.sqrt(i))+1):
        if i%n==0:
            c=1
            break
    if c==0:
        if i>1:
            print(i,"is prime")