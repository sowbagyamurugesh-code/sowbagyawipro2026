class box1:
    def __init__(self,value ):
        self.value=value
    def __add__(self,other):
        return box1(self.value+other.value)

    def __str__(self):
        return str(self.value)
b1=box1(10)
b2=box1(20)
b3=box1(30)
print(b1+b2+b3)