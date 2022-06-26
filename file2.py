# f = open("num.txt","w")
# for i in range(1,21):
#     f.write(str(i)+' ')
# f.close()
f =open("num.txt")
s = f.readline().split()
count =0
for i in s:
    if i!=" ":
        # print(i)
        count+=1
print(s)
print(count)
f.close()