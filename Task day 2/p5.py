age1 = int(input("Enter age of person 1: "))
age2 = int(input("Enter age of person 2: "))
age3 = int(input("Enter age of person 3: "))
if age1 >= age2 and age1 >= age3:
    oldest = age1
elif age2 >= age1 and age2 >= age3:
    oldest = age2
else:
    oldest = age3
if age1 <= age2 and age1 <= age3:
    youngest = age1
elif age2 <= age1 and age2 <= age3:
    youngest = age2
else:
    youngest = age3
print("Oldest age:", oldest)
print("Youngest age:", youngest)
