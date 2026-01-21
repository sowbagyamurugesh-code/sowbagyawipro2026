student={
    "name":"joe",
    "age":20,
    "course":"python"
}

print(student)
print(student["name"])
print(student.get("age"))
print(student.get("course"))
print(student.keys())
print(student.values())
print(student.items())

student.pop("age")
print(student)
student.popitem()
print(student)
student["mrak"]=90
student["age"]=30
print(student)

for key in student:
    print(key,student[key])

if 'name' in student:
    print("key exixts")

# nested dict
emp={
    101:{"name":"joe","salary":5000},
    102:{"name":"james","salary":1000},
}
print(emp)
print(emp.keys())
print(emp.values())
print(emp.items())
print(emp[101])
print(emp[102])

print(emp[101]["name"])
print(emp[102]["name"])

