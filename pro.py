s = "PROGRAM"
s2 = "OG"
s3 =""
for i  in s:
    if i not in s2:
        if i not in s3:
            s3 += i
print(s3)