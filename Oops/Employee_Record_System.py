'''Employee Record System
Create a class Employee with private fields: id, name, and salary.
Use setter methods to assign values. Add a method to display employee details.'''

class Employee:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__salary = None

    def set_id(self, emp_id):
        self.__id=emp_id

    def set_name(self, emp_name):
        self.__name=emp_name

    def set_salary(self, emp_salary):
        self.__salary=emp_salary

    def Display(self):
        print("----Employee Details----")
        print(f"Employee Id : {self.__id}")
        print(f"Employee Name : {self.__name}")
        print(f"Employee Salary : {self.__salary}")

emp1= Employee()
emp1.set_id(101)
emp1.set_name("Ankit")
emp1.set_salary(100000)
emp1.Display()

emp2=Employee()
emp2.set_id(102)
emp2.set_name("Yashasvi")
emp2.set_salary(88000)
emp2.Display()
