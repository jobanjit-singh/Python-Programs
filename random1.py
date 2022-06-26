import random
a=eval(input("Enter the n value: "))
even=0
odd=0
for i in range(1,a+1):
    n=random.randint(1,500)
    print(n)
    if n%2==0:
        even+=1
    else:
        odd+=1
print(even,"is a even random number")
print(odd,"is a odd random number")