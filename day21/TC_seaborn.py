import seaborn as sns
import matplotlib.pyplot as plt
marks=[60,50,70,80,67,90]
sns.set_style("whitegrid")
sns.histplot(marks,bins=5)
plt.title("MARKS")
plt.show()