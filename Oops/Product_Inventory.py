'''Create a class Product with fields: productId, name, quantity, price.
Use setters to assign values. Add a method to calculate total value (quantity * price).'''

class Product:

    def __init__(self):
        self.__ProductId=None
        self.__Name=None
        self.__Quantity=None
        self.__Price=None

    def set_id(self,id):
        self.__ProductId=id

    def set_Name(self,name):
        self.__Name=name

    def set_Quantity(self, qty):
        self.__Quantity=qty

    def set_Price(self, prc):
        self.__Price=prc

    def total_value(self):
        return self.__Quantity * self.__Price

    def Display(self):
            print("----Product Details----")
            print(f"Product Id   : {self.__ProductId}")
            print(f"Product Name : {self.__Name}")
            print(f"Quantity     : {self.__Quantity}")
            print(f"Price        : {self.__Price}")
            print(f"Total Value  : {self.total_value()}")

product1=Product()
product1.set_id(101)
product1.set_Name("Malai Cake")
product1.set_Quantity(5)
product1.set_Price(300)
product1.Display()


    
    