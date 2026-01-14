class PositiveSalary:
    def __get__(self, instance, owner):
        return instance._salary

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Salary must be a positive number")
        instance._salary = value


class Employee:
    salary = PositiveSalary()

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


# Demonstration
try:
    emp1 = Employee("Sowbagya", 50000)
    emp2 = Employee("Nithya", 60000)

    print("Employee 1:", emp1.name, emp1.salary)
    print("Employee 2:", emp2.name, emp2.salary)


    emp3 = Employee("Ravi", -30000)

except ValueError as e:
    print("Error:", e)
