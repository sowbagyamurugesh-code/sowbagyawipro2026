import matplotlib.pyplot as plt
plt.subplot(1,2,1)
plt.plot([1,2,3],[4,5,6])
plt.title("line chart")
plt.subplot(1,2,2)
plt.bar(["a","b","c"],[4,5,6])
plt.title("bar chart")
plt.show()
plt.savefig("subplot.png")