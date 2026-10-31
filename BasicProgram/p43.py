height = 4
slant_height = 5
rate = 10
pi = 22 / 7
radius = (slant_height**2 - height**2) ** 0.5
base_area = pi * radius * radius
cost = base_area * rate
print("cost:", cost)