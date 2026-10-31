def Calculate_Total(marks):
    return sum(marks)

def Calculate_Percentage(total,max_marks=500):
    return(total/max_marks)*100

def Calculate_Grade(percentage):
    if percentage>=90:
        return "A+"
    elif percentage >=80:
        return "A"
    elif percentage>=70:
        return "B"
    elif percentage>=60:
        return "C"
    elif percentage>=40:
        return "D"
    else:
        return "F"

def check_result(percentage):
    if percentage>=40:
        return "Pass"
    else:
        return "Fail"
    
def input_marks():
    marks = []
    subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]
    
    for i in range(5):
        while True:
                mark = int(input(f"Enter marks for {subjects[i]} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Invalid! Marks should be between 0 and 100.")
    return marks

def main():
    all_percentage=[]

    while True:
        n = int(input("How many students :"))
        if n > 0:
            break
        else:
            print("Please enter valid number grerater than 0 !!!")

    for student_no in range(1, n+1):
        print(f"----------Student {student_no}----------")
        name=input("Enter name of student :")
        marks=input_marks()
        total=Calculate_Total(marks)
        percentage=Calculate_Percentage(total)
        grade=Calculate_Grade(percentage)
        result=check_result(percentage)
        all_percentage.append(percentage)
        print("\n---------- Result ----------")
        print(f"Name       : {name}")
        print(f"Marks      : {marks}")
        print(f"Total      : {total}/500")
        print(f"Percentage : {percentage:.2f}%")
        print(f"Grade      : {grade}")
        print(f"Result     : {result}")
main()



    
