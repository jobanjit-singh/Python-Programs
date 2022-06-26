list=[]
n=eval(input("Please enter the number of Elements: "))
for i in range(0,n):
    ele=eval(input())
    list.append(ele)
for j in range(0,n-1):
    for k in range(0,n-j-1):
        if list[k]>list[k+1]:
            temp = list[k]
            list[k]=list[k+1]
            list[k+1]=temp
item=eval(input("Enter the number to Search: "))
beg=0
end=n-1
mid=beg+end//2
while beg<=end and list[mid]!=item:
    if item<list[mid]:
        end=mid-1
    elif item>list[mid]:
        beg=mid+1
    mid=beg+end//2
if list[mid]==item:
    print("Sorted List is: ",list)
    print(item,"is present in list at",mid+1,"position.")
else:
    print("Sorted List is: ",list)
    print(item,"is not present in list.")