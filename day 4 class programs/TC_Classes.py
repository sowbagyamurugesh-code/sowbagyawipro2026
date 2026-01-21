class Student:
    def display_details(self):
        print("Student Details:")
        print("Name:", self.name)
        print("roll no:",self.roll_no)

s1=Student()
s1.name="sow"
s1.roll_no=100

s1.display_details()


class std:
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
    def display_details(self):
        print("Student Details:")
        print("Name:", self.name)
        print("roll no:",self.roll_no)
s2=std("resh",22)
s2.display_details()