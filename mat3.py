import matplotlib.pyplot as plt
yviews=[534,258,689,401,724,689,350]
bin= [100,200,300,400,500,600,700,800,900,1000]
plt.hist(yviews,bins=bin,color="red")
plt.xlabel("Views")
plt.ylabel("Days")
plt.title("the graph of views")
plt.xticks(bin)
plt.show()