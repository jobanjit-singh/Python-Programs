import matplotlib.pyplot as plt
x = [2,6,8,10]
y = [3,5,7,9]
plt.plot(x, y, '-.')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.savefig("line-graph.pdf")