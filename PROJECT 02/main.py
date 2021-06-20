

def identify_grade(marks):
    if marks <= 100 and marks >= 0:
        if marks > 74:
            grade = "A"
        elif marks > 64:
            grade = "B"
        elif marks > 49:
            grade = "C"
        elif marks > 34:
            grade = "S"
        else:
            grade = "W"
    else:
        grade = "There is an Error on Your Input"
    return grade


class Student:
    def __init__(self):
        self.name = input("Enter the name : ")
        self.ict = int(input("Enter the ICT marks : "))
        self.python = int(input("Enter the Python marks : "))
        self.js = int(input("Enter the Javascript marks : "))

        self.total = self.ict+self.python+self.js
        self.average = self.total/3

        self.grade = []
        self.grade.append(identify_grade(self.ict))
        self.grade.append(identify_grade(self.python))
        self.grade.append(identify_grade(self.js))

        self.acount = 0
        self.bcount = 0
        self.ccount = 0
        self.scount = 0
        self.wcount = 0

        if "A" in self.grade:
            self.acount = self.grade.count("A")
        if "B" in self.grade:
            self.bcount = self.grade.count("B")
        if "C" in self.grade:
            self.ccount = self.grade.count("C")
        if "S" in self.grade:
            self.scount = self.grade.count("S")
        if "W" in self.grade:
            self.wcount = self.grade.count("W")


i = 0
student = []
student.extend(range(0, 5))
while i < 5:
    student[i] = Student()
    print(" ")
    print("Name", " | ", "ICT", " | ", "PYTHON", " | ", "JAVSCRIPT", " | ", "TOTAL", " | ", "AVERAGE",
          " | ", "A", " | ", "B", " | ", "C", " | ", "S", " | ", "W")
    print(" ")
    print(student[i].name, " | ", student[i].ict, " | ", student[i].python, " | ", student[i].js, " | ", student[i].total, " | ", student[i].average,
          " | ", student[i].acount, " | ", student[i].bcount, " | ", student[i].ccount, " | ", student[i].scount, " | ", student[i].wcount)

    i = i+1

temporay_student = student
print(" ")
print("****************************************************************COMPLETED********************************************************** ")
print("Name", " | ", "ICT", " | ", "PYTHON", " | ", "JAVSCRIPT", " | ", "TOTAL", " | ", "AVERAGE",
          " | ", "A", " | ", "B", " | ", "C", " | ", "S", " | ", "W")
print(" ")
for student in temporay_student:
    print(" ")
    
    print(student.name, " | ", student.ict, " | ", student.python, " | ", student.js, " | ", student.total, " | ", student.average,
          " | ", student.acount, " | ", student.bcount, " | ", student.ccount, " | ", student.scount, " | ", student.wcount)
