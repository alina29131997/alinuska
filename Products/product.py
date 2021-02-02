
class Product:
    def __init__(self,name,manufacturer,dateOfIssue,amount,price):
        self.__name = name
        self.__manufacturer = manufacturer
        self.__dateOfIssue = int(dateOfIssue)
        self.__amount = int(amount)
        self.__price = int(price)

    def show(self):
        print("name:", self.__name,"\tproizvoditelj:", self.__manufacturer, "\tdatavqpuska:", self.__dateOfIssue, "\tkolichestvo:", self.__amount,"cena:", self.__price)       
    def getName(self):
        return self.__name
    def setName(self,name): 
        self.__name = name

    def getManufacturer(self):
        return self.__manufacturer
    def setManufacturer(self,manufacturer): 
        self.__manufacturer = manufacturer

    def getDateOfIssue(self):
        return self.__dateOfIssue
    def setDateOfIssue(self,dateOfIssue): 
        self.__dateOfIssue = dateOfIssue

    def getAmount(self):
        return self.__amount
    def setAmount(self,amount): 
        self.__amount = amount    

    def getPrice(self):
        return self.__price
    def setPrice(self,price): 
        self.__Price = price
