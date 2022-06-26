def occur(str,c):
    num = str.count(c)
    return num
n=input("Enter the string: ")
f=input("Enter character to find occurrence in string: ")
print("Character occur in string",occur(n,f),"time")