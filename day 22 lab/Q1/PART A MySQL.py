# MySQL
import mysql.connector
host = "localhost"
user = "root"
password = "root"
database = "company_db"
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = conn.cursor()
print("Connected to the database successfully!")
# 1. Fetch employees whose salary is greater than 50,000
print("\nEmployees with salary > 50000:")

query1 = "SELECT * FROM employees WHERE salary > 50000"
cursor.execute(query1)

result = cursor.fetchall()

for row in result:
    print(row)

# 2. Insert a new employee record
query2 = "INSERT INTO employees (id, name, department, salary) VALUES (%s, %s, %s, %s)"
new_employee = (106, "Sowbagya", "IT", 60000)
cursor.execute(query2, new_employee)
conn.commit()
print("\nNew employee inserted successfully!")

# 3. Update salary of a specific employee by 10%

emp_id = 105
query3 = "UPDATE employees SET salary = salary + (salary * 0.10) WHERE id = %s"
cursor.execute(query3, (emp_id,))
conn.commit()

print("\nSalary updated by 10% successfully!")

# Close connection
cursor.close()
conn.close()
print("\nDatabase connection closed.")
