import matplotlib.pyplot as pt
l = [37,50,60,68,35,70,55,89,90,45]
pt.hist(l,bins=[0,40,60,80,100],color='green')
pt.title("Student Grade")
pt.xticks([0,40,60,80,100])
pt.show()