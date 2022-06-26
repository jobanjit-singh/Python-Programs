import matplotlib.pyplot as plt
labe = ['youtube','insta','linkedin','tiktok']
view = [200,600,300,100]
co = ['green','red','blue','white']
ex = [0,0,0,0.1]
plt.pie(view,labels=labe,explode=ex,autopct='%1.1f%%')
plt.show()