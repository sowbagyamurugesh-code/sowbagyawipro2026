#Iterators & Generators
# 1. Create a custom iterator class that iterates over numbers from 1 to N
class count:
    def __init__(self,n):
        self.n=n
        self.current=1
    def __iter__(self):
        return self
    def __next__(self):
        value=self.current
        if self.current<=self.n:
            self.current+=1
            return value
        else:
            raise StopIteration
for value in count(5):
    print(value)

# 2. Create a generator function that yields the first N Fibonacci numbers
def fibonacci(num):
    a, b = 0, 1
    count = 0

    while count < num:
        yield a
        a, b = b, a + b
        count += 1
num=5
for i in fibonacci(num):
    print(i)


# 3. Demonstrate the difference between using the iterator and generator by printing values using a for loop
#iterator
class EvenIterator:
    def __init__(self, N):
        self.N = N
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.N:
            val = self.current
            self.current += 2
            return val
        else:
            raise StopIteration


for nu in EvenIterator(10):
    print(nu)

#generator
def count(number):
    for i in range(10,number+1):
        yield i
for valu in count(20):
    print(valu)
