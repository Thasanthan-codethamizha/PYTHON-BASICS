class Light:
    def __init__(self):
        self.__maxprice = 10000
        print(self.__maxprice)

    def sell(self):
        print("Selling Price", self.__maxprice)

    def setMaxPrice(self, price):
        self.__maxprice = price


cfl = Light()
cfl.sell()


cfl.setMaxPrice(20000)
cfl.sell()

cfl.__maxprice = 30000
print(cfl.__maxprice)
