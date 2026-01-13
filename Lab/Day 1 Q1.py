#Widely Used Built-in Functions & Lambda
# 1.Uses range() to generate numbers from 1 to 20
for i in range(1,21):
    print(i)
# 2. Uses filter() with a lambda to select only even numbers
num=range(1,21)
evennumbers=list(filter(lambda x:x%2==0,num))
print(evennumbers)

# 3. Uses map() with a lambda to square the filtered numbers
squared_filterednum=list(map(lambda x:x**2,evennumbers))
print(squared_filterednum)

# 4. Uses reduce() to calculate the sum of squared even numbers
from functools import reduce
sum_of_squares = reduce(lambda a, b: a + b, squared_filterednum)
print(sum_of_squares)

# 5. Uses enumerate() to print the index and value of the final result list
print("Index and Value of Squared Even Numbers:")
for index, value in enumerate(squared_filterednum):
    #print(f"Index {index}: {value}")
    print("Index",index,"value",value)