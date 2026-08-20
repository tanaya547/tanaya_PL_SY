class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks
        self.grade = self.assign_grade()

    def assign_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "F"

    def display_details(self):
        print("Roll Number:", self.roll_number)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Grade:", self.grade)
        print("------------------------")


class College:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all_students(self):
        print("\n=====Student Details=====")

        for student in self.students:
            student.display_details()



college = College()

student1 = Student(101, "Tanaya", 95)
student2 = Student(102, "Rahul", 82)
student3 = Student(103, "Aisha", 68)
student4 = Student(104, "Rohan", 55)


college.add_student(student1)
college.add_student(student2)
college.add_student(student3)
college.add_student(student4)

college.display_all_students()



#OUTPUT
#=====Student Details=====
#Roll Number: 101
#Name: Tanaya
#Marks: 95
#Grade: A
#------------------------
#Roll Number: 102
#Name: Rahul
#Marks: 82
#Grade: B
#------------------------
#Roll Number: 103
#Name: Aisha
#Marks: 68
#Grade: C
#------------------------
#Roll Number: 104
#Name: Rohan
#Marks: 55
#Grade: F
#------------------------