n=18
print("you have only 5 guess.")
for i in range(1,7):
    if i<=5:
        p=eval(input("Enter the guess number: "))
        if p>18:
            print("This is greater,Please enter less number\nTry Again")
        elif p<18:
            print("This is lesser,please enter greater number\n Try Again")
        else:
            print("you type correct number")
            break
    else:
        print("Game over.....")