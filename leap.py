n=eval(input("Enter the year: "))
if n%400==0 and n%100==0:
    print(n,"is leap year")
elif n%4!=0 and n%100!=0:
    print(n,"is leap year")
else:
    print(n,"is not leap year")