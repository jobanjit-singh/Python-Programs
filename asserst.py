def avg(marks):
    assert len(marks)!=0,"list is empty"
    return sum(marks)/len(marks)
li = [89,45,23]
# li =[]
print(avg(li))