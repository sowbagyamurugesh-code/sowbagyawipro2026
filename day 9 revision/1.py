# 1. range, xrange (Python 3 uses range only)
print("RANGE FUNCTION:")
for i in range(5):
    print(i)

# 2. enumerate()
names = ["Alice", "Bob", "Charlie"]
print("ENUMERATE FUNCTION:")
for index, name in enumerate(names):
    print(index, name)

# 3. iter()
print("\nITER FUNCTION:")
nums = [10, 20, 30]
it = iter(nums)
print(next(it))
print(next(it))
print(next(it))

# 4. map()
print("\nMAP FUNCTION:")
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, numbers))
print(squared)

# 5. filter()
print("\nFILTER FUNCTION:")
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# 6. reduce()
from functools import reduce

print("\nREDUCE FUNCTION:")
total = reduce(lambda a, b: a + b, numbers)
print(total)


# 7. lambda functions
print("\nLAMBDA FUNCTION:")
multiply = lambda a, b: a * b
print(multiply(3, 4))

# 8. List Comprehension
print("\nLIST COMPREHENSION:")
squares = [x*x for x in range(5)]
print(squares)

# 9. Dictionary Comprehension
print("\nDICTIONARY COMPREHENSION:")
square_dict = {x: x*x for x in range(5)}
print(square_dict)

# 10. Set Comprehension
print("\nSET COMPREHENSION:")
unique_squares = {x*x for x in range(5)}
print(unique_squares)

# 11. Iterators
print("\nITERATOR:")

class Counter:
    def __init__(self, max_val):
        self.max_val = max_val
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max_val:
            self.current += 1
            return self.current
        else:
            raise StopIteration

for num in Counter(5):
    print(num)

# 12. Generators
print("\nGENERATOR FUNCTION:")

def count_up_to(n):
    for i in range(1, n + 1):
        yield i

for num in count_up_to(5):
    print(num)


# 13. Descriptors

print("\nDESCRIPTORS:")

class AgeDescriptor:
    def __get__(self, instance, owner):
        return instance._age

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        instance._age = value


class Person:
    age = AgeDescriptor()

    def __init__(self, age):
        self.age = age


p = Person(25)
print(p.age)


# 14. Decorators

print("\nDECORATORS:")

def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()


#15. Regular expression
import re
print("REGULAR EXPRESSION")
# 1. re.match() – Match at beginning of string
print("\nre.match():")
text = "Python Programming"
match = re.match(r"Python", text)
print(match.group() if match else "No match")

# 2. re.search() – Search anywhere in string
print("\nre.search():")
search = re.search(r"Programming", text)
print(search.group() if search else "Not found")

# 3. re.findall() – Find all occurrences
print("\nre.findall():")
sentence = "My number is 9876543210 and office number is 9123456780"
numbers = re.findall(r"\d{10}", sentence)
print(numbers)

# re.finditer() – Iterator of match objects
print("\nre.finditer():")
for match in re.finditer(r"\d+", sentence):
    print(match.group(), "at position", match.start())

# re.sub() – Replace patterns
print("\nre.sub():")
masked = re.sub(r"\d", "X", sentence)
print(masked)