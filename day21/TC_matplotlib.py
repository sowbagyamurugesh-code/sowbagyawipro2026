import matplotlib.pyplot as plt
plt.plot([1,2,3],[4,5,6])
plt.show()


x=[1,2,3,4]
y=[10,20,25,30]
plt.plot(x,y, marker='o',linestyle='--')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Line Chart")
plt.grid(True)
plt.show()

names=["a","b","c","d","e","f"]
scores=[70,50,80,90,78,98]
plt.bar(names,scores)
plt.title("bar chart")
plt.xlabel("names")
plt.ylabel("scores")
plt.show()

plt.barh(names,scores)
plt.title("horizontal bar chart")
plt.xlabel("names")
plt.ylabel("scores")
plt.show()

#histogram
plt.hist(scores,bins=5)
plt.title("histogram chart")
plt.xlabel("scores")
plt.show()

#scatter plot
plt.scatter(x,y)
plt.title("scatter chart")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

labels=["chrome","firefox","edge"]
size=[60,25,15]

plt.pie(size,labels=labels,autopct='%1.1f%%')
plt.title("pie chart")
plt.show()