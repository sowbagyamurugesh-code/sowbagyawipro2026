string="Hello World"
print(string)
print("at index 0:",string[0])
print("at index 1:",string[1])
print("at index -2:",string[-2])


str2="""this
 is
 Sowbagya"""
print(str2)
print("at index 0:",str2[0])
print("at index -5:",str2[-5])


#SLICING
print("SLICING")
a="welcome to python"
print(a[0:3])
print(a[3:])
print(a[:3])
print(a[:])
print(a[::-1])

text="training"
#concat
print("concat",a+text)
print("hii"*3)

print(text.upper())
print(a.replace("python","java"))
print("Length of the text:welcome to python:",len(a))

print("a" not in "sowbagya")
print("a" in "sowbagya")

#FORMAT
s1="I'm {0} and I'm {1} old".format("Sowbagya",23)
print(s1)

s2=a.split()
print(s2)


