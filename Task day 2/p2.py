qty=float(input("Enter quantity :"))
cost=100
price=qty*cost
if price>=1000:
 discount=price-price*(10/100)
 print("Price after discount :", discount)
else:
 print("Price :", price)

