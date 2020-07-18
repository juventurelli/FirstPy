class Computer:
    
    def __init__(self):
        self.__maxprice = 900    #private attribute

    def sell(self):
        print("Selling Price: {} ".format(self.__maxprice))

    def setMaxPrice(self,price):   ##Encapsulation
        self.__maxprice = price

c = Computer()
c.sell()

c.__maxprice = 1000
c.sell()              ## nao deixa mudar o valor


c.setMaxPrice(1000)   ## deixa mudar o valor
c.sell()