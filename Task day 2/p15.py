cost_price = float(input("Enter the cost price of the bike (in Rs): "))


if cost_price > 100000:

    tax_percentage = 15
    
    road_tax = (15 / 100) * cost_price

elif cost_price > 50000 and cost_price <= 100000:

    tax_percentage = 10

    road_tax = (10 / 100) * cost_price

else:

    tax_percentage = 5

    road_tax = (5 / 100) * cost_price

print(f"Tax Rate: {tax_percentage}%")

print(f"Road Tax to be paid: Rs. {road_tax}")