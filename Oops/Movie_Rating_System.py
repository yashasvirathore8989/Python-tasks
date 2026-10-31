'''Create a class Movie with fields: name, genre, and rating.
Use setters and create a method isHit() that returns true if rating ≥ 8.0.'''

class Movie:
    def __init__(self):
        self.__name = None
        self.__genre = None
        self.__rating = None

    def set_name(self, name):
        self.__name = name

    def set_genre(self, genre):
        self.__genre = genre

    def set_rating(self, rating):
            self.__rating = rating

    def isHit(self):
        return self.__rating >= 8.0

    def display(self):
        print("\n--- Movie Details ---")
        print(f"Name   : {self.__name}")
        print(f"Genre  : {self.__genre}")
        print(f"Rating : {self.__rating}")
        if self.isHit():
            print("Status : HIT Movie")
        else:
            print("Status : Average Movie")

m1 = Movie()
m1.set_name("Bahubali 2")
m1.set_genre("Action Drama")
m1.set_rating(8.4)
m1.display()

print(f"Movie Hit or Flop : {m1.isHit()}") 

m2 = Movie()
m2.set_name("KGF Chapter 2")
m2.set_genre("Action")
m2.set_rating(7.5)
m2.display()

print(f"Movie Hit or Flop : {m2.isHit()}") 