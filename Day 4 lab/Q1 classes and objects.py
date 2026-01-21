class Student:
    def display_details(self):
        print("Student Details:")
        print("Name:", self.name)
        print("roll no:",self.roll_no)
student1 = Student()
student1.name = "Sowbagya"
student1.roll_no = 101

student2 = Student()
student2.name = "Reshmi"
student2.roll_no = 102

student1.display_details()
student2.display_details()