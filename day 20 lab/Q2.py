import pandas as pd

data = {
    "Employee": ["John", "Alice", "Bob", "Eva", "Mark"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 60000, 55000, 65000, 62000]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# 1. Filter all employees from IT department
it_employees = df[df["Department"] == "IT"]
print("\nIT Department Employees:\n", it_employees)

# 2. Find average salary per department
avg_salary = df.groupby("Department")["Salary"].mean()
print("\nAverage Salary per Department:\n", avg_salary)

# 3. Add new column Salary_Adjusted (increase salary by 10%)
df["Salary_Adjusted"] = df["Salary"] * 1.10
print("\nDataFrame with Adjusted Salary:\n", df)
