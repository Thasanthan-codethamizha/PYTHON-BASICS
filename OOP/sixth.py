import datetime

nowdatetime = datetime.datetime.now()
print(nowdatetime)


class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1+self.num2

    def substract(self):
        return self.num1-self.num2

    def multiply(self):
        return self.num1*self.num2

    def divide(self):
        return self.num1/self.num2


def inputsprinter(cal):
    for x in cal:
        print(x.num1, " ", x.num2)


f = open("input.txt", "a+")
f.write("=> {} \n".format(nowdatetime))

input_list = []
x = 0
while x < 2:
    print(" ")
    print("************************** CT CALCULATOR ******************************** ")
    print(" ")
    print("{} inputs \n".format(x))
    num1 = int(input("Enter the First Number : "))
    num2 = int(input("Enter the Second Number : "))

    cal = Calculator(num1, num2)
    f.write("{} {} \n".format(num1, num2))
    input_list.append(cal)
    total = cal.add()

    balance = cal.substract()
    multiply = cal.multiply()
    division = cal.divide()
    f.write(("Total : {},  Balance :  {}, Multipication is : {}, Division is : , {} \n").format(
        total, balance, multiply, division))
    x = x+1

print(" ")
f.write("{} inputs \n".format(x))

print(" ")
print("************************** THE END ******************************** ")

print(" ")
inputsprinter(input_list)
f.write(" \n")
f.close()
