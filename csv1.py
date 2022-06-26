import csv
ls =[]
f = open("attendees1.csv")
csv_r = csv.reader(f)
for row in csv_r:
    ls.append(row[2])
f.close()
f1 = open("attendees2.csv")
csv_read = csv.reader(f1)
ls2 =[]
for i in csv_read:
    ls2.append(i[2])
# print(ls)
# print()
# print(ls2)
f1.close()
diff = set(ls2).difference(set(ls))
print(diff)