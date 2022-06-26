import matplotlib.pyplot as plt
yviews=[534,258,689,401,724,689,350]
fviews=[536,258,681,301,724,689,360]
days = range(1,8)
plt.bar([a-0.25 for a in days],yviews,color="red",label="youtube Views",width=0.2)
plt.bar([a+0.25 for a in days],fviews,color="green",label="youtube Views",width=0.2)
plt.xlabel("Days")
plt.ylabel("Views")
plt.title("the graph of views")
plt.legend(loc = "upper right")
plt.grid(True)
plt.show()