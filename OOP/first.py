class Student:
    role = "student"

    def profile(name, age, grade):
        print(name, "is", age, "years old")
        print(name, "is studying in", grade)


s1 = Student.profile("Thasnathan", 17, 12)
