import csv
# fields = ['name','rollno']
# rows = [['joban','118'],['himanshu','109'],['karam','122'],['gill','123']]
# f = open("detail.csv","w",newline='')
# csvwr = csv.writer(f)
# csvwr.writerow(fields)
# csvwr.writerows(rows)
f = open("detail.csv")
read = csv.reader(f)
next(read,None)
for i in read:
    print(i)