class computer:

    def __init__(self):
        self.__maxprice = 1000
    def sell(self):
        print("the selling price is ",self.__maxprice)
    def setmaxprice(self,price):
        self.__maxprice = price
        
obj = computer()
obj.sell()

obj.__maxprice = 200
obj.sell()
obj.setmaxprice(200)
obj.sell()
