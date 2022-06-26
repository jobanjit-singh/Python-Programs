n=eval(input("Enter the number: "))
original=str(n)
reverse=""
while(n>0):
    an=str(n%10)
    reverse=reverse+an
    n=n//10
print("reverse number is:",reverse)
