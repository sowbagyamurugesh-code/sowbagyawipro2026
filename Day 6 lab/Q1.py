import re
from string import digits

#1. Uses re.match() to check whether a string starts with a valid employee ID in the format EMP followed by 3 digits (e.g., EMP123)
emp_id="EMP123"
if re.match(r"[A-Z]+\d{3}",emp_id):
    print("valid emp ip and the id is: ",emp_id)
else:
    print("invalid emp ip and the id is: ",emp_id)


#2. Uses re.search() to find the first occurrence of a valid email address in a given text
text="this is my mail id sowbagya@gmail.com"
search_result=re.search(r"\w+@\w+\.\w+",text)
if search_result:
    print("Email Found:", search_result.group())
else:
    print("No email found")

#3. Demonstrates the use of meta-characters (., *, +, ?) and special sequences (\d, \w, \s) in the patterns
sample_text = "Python programming"

# .  any single character
print("Dot (.) match:", re.search(r"P.t", sample_text).group())

# * zero or more occurrences
print("Star (*) match:", re.search(r"Py.*g", sample_text).group())

# + one or more occurrences
print("Plus (+) match:", re.search(r"o+", sample_text).group())

# ? zero or one occurrence
print("Question (?) match:", re.search(r"progra?m", sample_text).group())


#4. Prints matched groups using capturing parentheses
data = "User123 logged in at 10 AM"
digits=re.findall(r"\d+",data)
words=re.findall(r"\w+",data)
spaces=re.findall(r"\s",data)
print("Digits:",digits)
print("Words:",words)
print("Spaces:",len(spaces))