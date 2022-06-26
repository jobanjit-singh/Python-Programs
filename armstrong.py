a=eval(input("Enter the number: "))
s=0
k=a
while(a>0):
    n=a%10
    s=s+n**3
    a=a//10
if s==k:
    print(k,"is armstrong number")
else:
    print(k,"is not armstrong number")