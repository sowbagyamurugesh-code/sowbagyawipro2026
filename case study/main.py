import json
import csv
import os
from abc import ABC, abstractmethod

# ================= BASE CLASS =================
class Person(ABC):
    def __init__(self, pid, name, dept):
        self.id = pid
        self.name = name
        self.department = dept

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def calculate_performance(self):
        pass


# ================= STUDENT =================
class Student(Person):
    def __init__(self, sid, name, dept, semester, marks):
        super().__init__(sid, name, dept)
        self.semester = semester
        self.marks = marks
        self.courses = []

    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)

        if avg >= 80:
            grade = "A"
        elif avg >= 60:
            grade = "B"
        else:
            grade = "C"

        return avg, grade

    def get_details(self):
        return {
            "id": self.id,
            "name": self.name,
            "department": self.department,
            "semester": self.semester,
            "marks": self.marks,
            "courses": self.courses
        }

    def __gt__(self, other):
        return self.calculate_performance()[0] > other.calculate_performance()[0]


# ================= FACULTY =================
class Faculty(Person):
    def __init__(self, fid, name, dept, salary):
        super().__init__(fid, name, dept)
        self.salary = salary

    def calculate_performance(self):
        return "Faculty Performance Calculated"

    def get_details(self):
        return {
            "id": self.id,
            "name": self.name,
            "department": self.department,
            "salary": self.salary
        }


# ================= COURSE =================
class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty


# ================= SYSTEM =================
class UniversitySystem:
    def __init__(self):
        self.students = {}
        self.faculty = {}
        self.courses = {}
        self.load_students()

    # ---------- Load Students ----------
    def load_students(self):
        if os.path.exists("students.json"):
            with open("students.json", "r") as f:
                data = json.load(f)
                for s in data:
                    stu = Student(s["id"], s["name"], s["department"],
                                  s["semester"], s["marks"])
                    stu.courses = s.get("courses", [])
                    self.students[s["id"]] = stu

    # ---------- Save Students ----------
    def save_students(self):
        data = [s.get_details() for s in self.students.values()]
        with open("students.json", "w") as f:
            json.dump(data, f, indent=4)

    # ---------- Add Student ----------
    def add_student(self):
        try:
            sid = input("Student ID: ").strip()
            if not sid:
                raise ValueError("ID cannot be empty")
            if sid in self.students:
                raise ValueError("Student ID already exists")

            name = input("Name: ").strip()
            dept = input("Department: ").strip()
            semester = int(input("Semester (1-8): "))

            if semester < 1 or semester > 8:
                raise ValueError("Semester must be between 1 and 8")

            marks = list(map(int, input("Enter 5 subject marks: ").split()))
            if len(marks) != 5:
                raise ValueError("Exactly 5 marks required")

            for m in marks:
                if m < 0 or m > 100:
                    raise ValueError("Marks must be between 0 and 100")

            student = Student(sid, name, dept, semester, marks)
            self.students[sid] = student
            self.save_students()

            print("\nStudent Created Successfully")
            print("--------------------------------")
            print(f"Student ID  : {sid}")
            print(f"Name        : {name}")
            print(f"Department  : {dept}")
            print(f"Semester    : {semester}")
            print(f"Marks       : {marks}")

        except Exception as e:
            print("\nError:", e)

    # ---------- Add Faculty ----------
    def add_faculty(self):
        try:
            fid = input("Faculty ID: ").strip()
            if fid in self.faculty:
                raise ValueError("Faculty ID already exists")

            name = input("Name: ").strip()
            dept = input("Department: ").strip()
            salary = float(input("Salary: "))

            if salary <= 0:
                raise ValueError("Salary must be positive")

            faculty = Faculty(fid, name, dept, salary)
            self.faculty[fid] = faculty

            print("\nFaculty Created Successfully")
            print("--------------------------------")
            print(f"Faculty ID  : {fid}")
            print(f"Name        : {name}")
            print(f"Department  : {dept}")
            print(f"Salary      : {salary}")

        except Exception as e:
            print("\nError:", e)

    # ---------- Add Course ----------
    def add_course(self):
        try:
            code = input("Course Code: ").strip()
            name = input("Course Name: ").strip()
            credits = int(input("Credits: "))
            fid = input("Faculty ID: ").strip()

            if fid not in self.faculty:
                raise ValueError("Faculty not found")

            course = Course(code, name, credits, self.faculty[fid])
            self.courses[code] = course

            print("\nCourse Added Successfully")
            print("--------------------------------")
            print(f"Course Code : {code}")
            print(f"Course Name : {name}")
            print(f"Credits     : {credits}")
            print(f"Faculty     : {self.faculty[fid].name}")

        except Exception as e:
            print("\nError:", e)

    # ---------- Enroll Student ----------
    def enroll_student(self):
        try:
            sid = input("Student ID: ").strip()
            code = input("Course Code: ").strip()

            if sid not in self.students:
                raise ValueError("Student not found")
            if code not in self.courses:
                raise ValueError("Course not found")

            if code in self.students[sid].courses:
                raise ValueError("Student already enrolled")

            self.students[sid].courses.append(code)
            self.save_students()

            print("\nEnrollment Successful")
            print("--------------------------------")
            print(f"Student ID   : {sid}")
            print(f"Student Name : {self.students[sid].name}")
            print(f"Course Code  : {code}")
            print(f"Course Name  : {self.courses[code].name}")

        except Exception as e:
            print("\nError:", e)

    # ---------- Student Performance ----------
    def student_performance(self):
        try:
            sid = input("Student ID: ").strip()
            if sid not in self.students:
                raise ValueError("Student not found")

            student = self.students[sid]
            avg, grade = student.calculate_performance()

            print("\nStudent Performance Report")
            print("--------------------------------")
            print(f"Student ID   : {sid}")
            print(f"Name         : {student.name}")
            print(f"Marks        : {student.marks}")
            print(f"Average      : {round(avg,2)}")
            print(f"Grade        : {grade}")

        except Exception as e:
            print("\nError:", e)

    # ---------- Compare Students ----------
    def compare_students(self):
        try:
            s1 = input("First Student ID: ").strip()
            s2 = input("Second Student ID: ").strip()

            if s1 not in self.students or s2 not in self.students:
                raise ValueError("Student not found")

            print("\nStudent Comparison Report")
            print("--------------------------------")
            print(f"Student 1 : {self.students[s1].name}")
            print(f"Student 2 : {self.students[s2].name}")
            print(f"Higher Performer : {self.students[s1].name if self.students[s1] > self.students[s2] else self.students[s2].name}")

        except Exception as e:
            print("\nError:", e)

    # ---------- Generate Reports ----------
    def generate_reports(self):
        try:
            with open("students_report.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Name", "Department", "Average", "Grade"])

                for s in self.students.values():
                    avg, grade = s.calculate_performance()
                    writer.writerow([s.id, s.name, s.department, round(avg, 2), grade])

            print("\nReports Generated Successfully")
            print("--------------------------------")
            print("Student Data File : students.json")
            print("CSV Report File   : students_report.csv")

        except Exception as e:
            print("\nError:", e)


# ================= MENU =================
def menu():
    print("\n1 → Add Student")
    print("2 → Add Faculty")
    print("3 → Add Course")
    print("4 → Enroll Student to Course")
    print("5 → Calculate Student Performance")
    print("6 → Compare Two Students")
    print("7 → Generate Reports")
    print("8 → Exit")


def main():
    uni = UniversitySystem()

    while True:
        menu()
        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            uni.add_student()
        elif choice == "2":
            uni.add_faculty()
        elif choice == "3":
            uni.add_course()
        elif choice == "4":
            uni.enroll_student()
        elif choice == "5":
            uni.student_performance()
        elif choice == "6":
            uni.compare_students()
        elif choice == "7":
            uni.generate_reports()
        elif choice == "8":
            print("\nThank you for using Smart University Management System")
            break
        else:
            print("\nInvalid choice! Please enter 1-8.")


if __name__ == "__main__":
    main()
