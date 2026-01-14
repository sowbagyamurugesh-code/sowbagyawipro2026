#generator. keyword is yield
def num():
    yield 1
    yield 2
    yield 3
    yield 4
gen=num()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


def count(n):
    for i in range(10,n+1):
        yield i
for val in count(20):
    print(val)