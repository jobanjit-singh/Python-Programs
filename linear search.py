a=[]
k=0
post=0
n=eval(input("Please enter the number of elements: "))
print("Enter elements : ")
for i in range(0,n):
    e=eval(input())
    a.append(e)
print("Entered List is:",a)
item=eval(input("Enter the element to be search: "))
for x in a:
    post+=1
    if x==item:
        k=1
        break
if k==1:
    print(item,"is found in list at position",post)
else:
    print(item,"is not found.")