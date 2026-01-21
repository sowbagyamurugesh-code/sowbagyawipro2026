import json

data={
    "name":"sowbagya",
    "age":22,
    "department":"CSE"
}
with open("data.json","w") as file:
     json.dump(data,file,indent=4)