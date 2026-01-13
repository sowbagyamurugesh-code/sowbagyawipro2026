from unittest import case

n=5
if n%2 == 0:
    print("even number")
else:
    print("odd number")

score=85
if score>90:
    print("Grade A")
elif score>=80 and score<=90:
    print("Grade B")
else:
    print("Grade C")

# for loop
list=[55,33,77,11,99]
for i in list:
    print(i)

for numbers in range(1,11):
    print(numbers)

# while loop
j=0
while j<=8:
    print(j)
    j=j+1

# switch statement (match)
day=3
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")

# break statement
a=1
while a<=7:
    print(a)
    a=a+1
    if a==5:
        break