from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["company_db"]
collection = db["employees"]
print("Connected to MongoDB successfully!")

# 1. Insert a new employee document
new_employee = {
    "name": "Sowbagya",
    "department": "IT",
    "salary": 60000
}
collection.insert_one(new_employee)
print("New employee inserted successfully!")

# 2. Find all employees in IT department
print("\nEmployees in IT Department:")
it_employees = collection.find({"department": "IT"})
for emp in it_employees:
    print(emp)

# 3. Update salary of an employee with given name
employee_name = "Sowbagya"
new_salary = 75000
collection.update_one(
    {"name": employee_name},
    {"$set": {"salary": new_salary}}
)
print(f"\nSalary updated successfully for {employee_name}!")
