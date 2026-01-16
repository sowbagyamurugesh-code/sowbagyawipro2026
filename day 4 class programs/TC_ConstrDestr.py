class employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(" constructor is called")
    def __del__(self):
        print(" destructor is called")
employee("abc",22)
