import matplotlib.pyplot as plt
yviews=[534,258,689,401,724,689,350]
fviews=[536,258,681,301,724,689,360]
days = range(1,8)
plt.plot(days,yviews,color="red",marker="o",label = "Youtube Views")
plt.plot(days,fviews,color="green",marker="o",label="Facebook views")
plt.xlabel("Days")
plt.ylabel("Views")
plt.legend()
plt.grid(True)
plt.title("the Graph of views")
plt.savefig('/home/jobanjit/mat.pdf')
plt.show()