'''Create a class Car with fields: brand, model, and year.
Use setters to assign values. Create a method to print full car info.'''

class Car:
    def __init__(self):
        self.__brand=None
        self.__model=None
        self.__year=None

    def set_brand(self,brd):
        self.__brand=brd

    def set_model(self,mdl):
        self.__model=mdl

    def set_year(self,yrr):
        self.__year=yrr

    def display(self):
        print("-----Car Details-----")
        print(f"Car Brand : {self.__brand}")
        print(f"Car Model : {self.__model}")
        print(f"Year      : {self.__year}")

car1=Car()
car1.set_brand("Honda")
car1.set_model("H23")
car1.set_year(2022)
car1.display()

