import matplotlib.pyplot as plt
import seaborn as sns
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 27000, 30000, 28000, 32000, 31000]
plt.plot(months,sales,marker='o',linestyle='--',color='red')
plt.title("monthly sales")
plt.xlabel("months")
plt.ylabel("sales")
plt.grid(True)
plt.show()


sns.barplot(x=months,y=sales)
plt.title("monthly sales")
plt.xlabel("months")
plt.ylabel("sales")
plt.grid(axis="y")
plt.show()