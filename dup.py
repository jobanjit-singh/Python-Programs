def check_duplicate(lst):
    if len(lst)==len(set(lst)):
        print("No,This List not contain Duplicate Value.")
    else:
        print("Yes,This List contain duplicate value.")
l=eval(input("Enter the number of elements: "))
print("Enter the elements: ")
lt=[]
for i in range(0,l):
    x=eval(input())
    lt.append(x)
check_duplicate(lt)