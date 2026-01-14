class student:
    name="Sowbagya"
    age=22
s=student()  # s is object.creating object from the class student
print(s.name)
print(s.age)

#using constructor
class employee:
    def __init__(self,name,age,department):
        self.name=name
        self.age=age
        self.department=department
e=employee("john",22,"Software Engineer")
print(e.name)
print(e.age)
print(e.department)
print(e.name,e.age,e.department)