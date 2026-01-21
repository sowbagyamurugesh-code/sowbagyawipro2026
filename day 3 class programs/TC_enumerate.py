name=['joe',"james"]
for index,value in enumerate(name):
    print(index,value)

from enum import Enum
class color(Enum):
    red=1
    green=2
    blue=3
print(color.red.value)
print(color.red.name)
print(color.green.value)
print(color.green.name)
print(color.blue.value)
print(color.blue.name)