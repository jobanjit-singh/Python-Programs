a=eval(input("Enter the a value: "))
b=eval(input("Enter the b value: "))
for i in range(a,b+1):
    k=i 
    s=0
    while(i>0):
        n=i%10
        s=s+n**3
        i=i//10
    if k==s:
        print(k,"is armstrong")
