class Animal:

    def __init__(self, type):
        self.type = type
        print("Animal", self.type, "is Ready")

    def whoisThis(self):
        print("Animal", self.type)

    def canwalk(self):
        print(self.type, "Walk slower")


class Dog(Animal):
    def __init__(self, name):
        self.name = name
        self.age = 18
        super().__init__("DOG")
        print(self.name, " is Ready")

    def whoisThis(self):
        print(self.name, self.age)

    def canwalk(self):
        print("Walk faster")


jimmy = Dog("JIMMY")

jimmy.whoisThis()
