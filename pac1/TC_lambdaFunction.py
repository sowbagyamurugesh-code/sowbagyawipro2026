#lambda args:expressions
add=lambda a,b: a+b
print(add(3,4))

product=lambda a,b: a*b
print(product(3,4))

max_num=lambda x,y: x if x>y else y
print(max_num(3,4))


#map
# map(function,iterable)
num=[1,2,3,4,5,6,7,8,9,10]
result=map(lambda x:x*2,num)
print(list(result))