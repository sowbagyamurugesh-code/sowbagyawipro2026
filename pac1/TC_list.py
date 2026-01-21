numbers=[10,20,30,40,50]
names=["Sowbagya","Vikram","Reshmi","Rathna"]
mixed=[1,"python",False,2.8]
numbers[4]=60
print(numbers)
print(names)
print(mixed)

for i in numbers:
    print(i)

if 20 in numbers:
    print("number found")

matrix=[[1,2,3],[4,5,6]]
print(matrix[1][2])

#LIST METHODS
#REVERSE
names.reverse()
print(names)

# APPEND
names.append("harini")
print(names)

#EXTEND

names.extend(["joe","james"])
print(names)
#remove
names.remove("joe")
print(names)

#insert
names.insert(0,"joe")
print(names)