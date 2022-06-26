def position(str,n):
        ch=str[n-1]
        return ch 
s=input("Enter the string: ")
num=eval(input("Enter the number to find character on that position: "))
if num>len(s):
    print("Error...Number is Greater than String Length")
elif num<=0:
    print("Invalid Input...")
else:
    print("Character at",num,"position is",position(s,num))