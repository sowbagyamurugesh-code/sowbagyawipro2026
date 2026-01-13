#List, Dictionary & Set Comprehensions
data = [1, 2, 3, 4, 5, 6, 2, 4]
# 1. Create a list comprehension to store squares of all numbers
squares_list = [x**2 for x in data]
print("Squares List:", squares_list)

# 2. 2. Create a set comprehension to store only unique even numbers
unique_even_set = {x for x in data if x % 2 == 0}
print("Unique Even Set:", unique_even_set)

# 3. Create a dictionary comprehension where the key is the number and the value is its cube
cube_dict = {x: x**3 for x in data}
print("Number-Cube Dictionary:", cube_dict)
