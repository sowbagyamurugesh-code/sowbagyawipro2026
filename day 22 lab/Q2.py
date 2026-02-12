import pandas as pd
import numpy as np
# 1. Load the CSV into a Pandas DataFrame
data=pd.read_csv("sales.csv")
df=pd.DataFrame(data)
print("Original Data:")
print(df)
# 2. Add a new column "Total" (Quantity * Price)
df['Total']=df["Quantity"]*df["Price"]
print("\nData with Total column:")
print(df)

# 3. Using NumPy calculate total sales, average daily sales, std deviation
daily_sales=df["Total"].to_numpy()

total_sales = np.sum(daily_sales)
average_sales = np.mean(daily_sales)
std_sales = np.std(daily_sales)
print("Total Sales:", total_sales)
print("Average Daily Sales:", average_sales)
print("Standard Deviation of Daily Sales:", std_sales)

# 4. Find best-selling product based on total quantity sold
best_product = df.groupby("Product")["Quantity"].sum().idxmax()
print("Best Selling Product:", best_product)