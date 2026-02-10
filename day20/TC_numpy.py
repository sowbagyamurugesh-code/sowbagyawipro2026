import numpy as np
import pandas as pd

array1=np.array([10,20,30,60])
print("array:",array1)
print("sum:",np.sum(array1))
print("mean:",np.mean(array1))
print("median:",np.median(array1))
print("max:",np.max(array1))
print("min:",np.min(array1))
print("multiply by 2:",array1*2)
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
for i in arr:
    print("sum:",sum(i))


#pandas
data = {
    "Name": ["Sowbagya", "Reshmi", "Abinaya"],
    "Age": [21, 22, 35],
    "Department": ["Data Science", "CSE", "CSE"]
}
df = pd.DataFrame(data)
#print(df)
print(df["Name"])
print(df[df["Age"]>30])
print(df["Department"])
df["Salary"]=[50000,600000,700000]
print(df)