# from random import randint
# f = open("rand.txt","w")
# for i in range(1,51):
#     x=randint(100,500)
#     f.write(str(x)+" ")
f = open("rand.txt")
s = f.readline().split()
even=odd=0
print(type(s))
for i in s:
    if int(i)%2==0:
        even+=1
    else:
        odd+=1
print("even",even,"odd",odd)
f.close()