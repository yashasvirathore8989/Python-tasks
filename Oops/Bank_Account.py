'''Bank Account
Create a class BankAccount with fields: accountNumber, holderName, balance.
Use setters to assign values. Add a method to display balance.'''

class BankAccount:
    def __init__(self):
        self.__AccountNumber = None
        self.__HolderName = None
        self.__Balance = None

    def set_AccountNumber(self, AccNo):
        self.__AccountNumber=AccNo

    def set_HolderName(self, name):
        self.__HolderName=name

    def set_Balance(self, amount):
        self.__Balance=amount

    def Display_Balance(self):
        print("----Customer Details----")
        print(f"Account Number : {self.__AccountNumber}")
        print(f"Holder Name : {self.__HolderName}")
        print(f"Balance : {self.__Balance}")

customer1= BankAccount()
customer1.set_AccountNumber(989756478345)
customer1.set_HolderName("Ankit Vyas")
customer1.set_Balance(1000000)
customer1.Display_Balance()

book2=BankAccount()
book2.set_AccountNumber(987345672345)
book2.set_HolderName("Yashasvi Rathore")
book2.set_Balance(100000)
book2.Display_Balance()