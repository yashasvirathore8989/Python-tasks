class Time:
    def __init__(self, hrs, minutes, seconds):
        self.__hrs = hrs
        self.__minutes = minutes
        self.__seconds = seconds

    def add(self, t1, t2):
        self.__seconds = t1.__seconds + t2.__seconds
        self.__minutes = t1.__minutes + t2.__minutes
        self.__hrs = t1.__hrs + t2.__hrs
        if self.__seconds >= 60:
            self.__minutes += self.__seconds // 60
            self.__seconds = self.__seconds % 60
        if self.__minutes >= 60:
            self.__hrs += self.__minutes // 60
            self.__minutes = self.__minutes % 60
        return self  
    
    def display(self):
        print(f"Hrs: {self.__hrs}, Minutes: {self.__minutes}, Seconds: {self.__seconds}")

t1 = Time(10, 20, 50)
t2 = Time(20, 40, 30)

t3 = Time(0, 0, 0)  
t3.add(t1, t2)      
t3.display()
         