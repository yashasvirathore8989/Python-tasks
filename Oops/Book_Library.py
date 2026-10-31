'''Book Library
Create a class Book with fields: title, author, and price.
Use setters to assign values and a method to print book details.'''

class Book:
    def __init__(self):
        self.__title = None
        self.__author = None
        self.__price = None

    def set_title(self, book_title):
        self.__title=book_title

    def set_author(self, book_author):
        self.__author=book_author

    def set_price(self, book_price):
        self.__price=book_price

    def Display(self):
        print("----Book Details----")
        print(f"Book Title : {self.__title}")
        print(f"Book Author : {self.__author}")
        print(f"Book Price : {self.__price}")

book1= Book()
book1.set_title("Just Like Heaven")
book1.set_author("Jephrey")
book1.set_price(1000)
book1.Display()

book2=Book()
book2.set_title("Atomic Habits")
book2.set_author("Steven frost")
book2.set_price(550)
book2.Display()