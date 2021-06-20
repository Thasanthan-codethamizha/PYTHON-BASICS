class Student:
    role = "student"

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def profile(self):
        print(self.name, "is", self.age, "years old")
        print(self.name, "is studying in", self.grade)


s1 = Student("Thasanthan", 17, 12)

s1.profile()
