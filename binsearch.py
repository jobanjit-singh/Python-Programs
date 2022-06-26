l=[]
n=eval(input("how many  elements you want on list "))
for i in range(1,n+1):
    x=eval(input("enter element "))
    l.append(x)
item=eval(input("enter element to searched "))
l.sort()
print("sorted list  is : ",l)
beg=1
end=n
mid=(beg+end )//2
while beg<=end and l[mid]!= item:
        if item>l[mid]:
            beg=mid+1
        if item<l[mid]:
            end=mid-1
        mid=(beg+end )//2
if l[mid]== item:
    print(item,"is found ",mid+1)
else:
    print(item,"not found ")
