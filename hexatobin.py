def hexatobin(hnum):
    bnum=''
    for i in hnum:
        if i in ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']:
            if i=='0':
                bnum+='0000'
            if i=='1':
                bnum+='0001'
            if i=='2':
                bnum+='0010'
            if i=='3':
                bnum+='0011'
            if i=='4':
                bnum+='0100'
            if i=='5':
                bnum+='0101'
            if i=='6':
                bnum+='0110'
            if i=='7':
                bnum+='0111'
            if i=='8':
                bnum+='1000'
            if i=='9':
                bnum+='1001'
            if i=='A':
                bnum+='1010'
            if i=='B':
                bnum+='1011'
            if i=='C':
                bnum+='1100'
            if i=='D':
                bnum+='1101'
            if i=='E':
                bnum+='1110'
            if i=='F':
                bnum+='1111'
        else:
            return 'N'
            break
    return bnum
n=input("Enter Hexadecimal Number: ")
flag=hexatobin(n)
if flag!='N':
    print("Binary Number of",n,"is",flag)
else:
    print("Invalid Input..")    