perimeter=36
side1 = 10
side2= 9
side3= perimeter-side1-side2
semi_perimeter = (side1 + side2 + side3) / 2
area = (semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3)) ** 0.5
print("area:", area)

#output: area: 36.0