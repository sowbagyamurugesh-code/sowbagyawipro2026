t1=(1,2,3,4,5,5,1)
t2="apple","orange","mango"
print(t1[0])
print(t2[1])

print(t2[1:])

#tuple methods

#count
print(t1)
print(t1.count(1))


#index
print(t1.index(2))

# Swapping
a=1
b=2
print("before swapping",a,b)
a,b=b,a
print("after swapping",a,b)


data=10,20,30
x,y,z=data
print(x,y,z)
print("before swapping",x,y,z)
x,y,z=z,y,x
print("after swapping",x,y,z)

