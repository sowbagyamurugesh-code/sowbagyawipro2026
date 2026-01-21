import re
txt="pythonispowerfulpython"
#match  Beginning of string only
#Matches pattern only at the beginning of the string.
match_result=re.match("python",txt)

if match_result:
    print("match found")
else:
    print("no match found")




#search Anywhere in string
#Searches for pattern anywhere in the string.
search_result=re.search("powerful",txt)
print("search: ",search_result.group())
print("SEARCH: ",search_result.start())
print("SEARCH: ",search_result.end())

email="sowbagya@gmail.com"
if re.match(r"[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]",email):
    print("valid email")
else:
    print("invalid email")


#fullmatch
fullmatch_result=re.fullmatch(r"\d{10}","1234567890")
print("fullmatch: ",fullmatch_result.group())
if fullmatch_result:
    print("match found")
else:
    print("no match found")

#findall Returns a list of all matching substrings.
find_result=re.findall("python",txt)
print("findall: ",find_result)
count_findall=len(find_result)
print("count: ",count_findall)

print(re.findall(r"\d+","price is 50 , 10 , 20"))

for i in re.finditer(r"\d+","price is 50 , 10 , 20"):
    print(i.group(),i.start(),i.end())

print(re.search(r"\d+","Age is 25"))

print(re.search(r"^a.*c$","abngggnnc"))

m=re.search(r"\w+(?=@)","test@gmail.com")
print(m.group())



print(re.search("python","Python",re.I))

string="orange\napple\navocado"
print(re.findall(r"^a\w+",string,re.M))