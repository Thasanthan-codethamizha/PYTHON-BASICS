
def add(num):
    total = 0
    for n in num:
        total = total + n
    print("TOTAL IS : ", total)


x = 0
num = []
while x < 3:
    x = int(input("Enter number : "))
    num.append(x)
    x = x+1
add(num)
