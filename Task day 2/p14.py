percentage = float(input("Enter your percentage: "))
if percentage > 90:

    grade = "A"

elif percentage > 80 and percentage <= 90:

    grade = "B"

elif percentage >= 60 and percentage <= 80:

    grade = "C"

else:

    grade = "D"


print(f"Your Grade is: {grade}")
