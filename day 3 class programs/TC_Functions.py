def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print(add(20,10))
print(sub(20,10))
print(mul(20,10))
print(div(20,10))

def hello(greeting="hello",name="world"):
    print(greeting,name)
hello()
hello("hlo",'name')


#unnamed params
def print_param(*params):
    print(params)
print_param("hello")
print_param(1,2,3,4)


#named params
def print_param1(**params):
    print(params)
print_param1(x=1,y=2,z=3)

