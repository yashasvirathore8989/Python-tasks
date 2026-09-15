print("                         D-MART")
name = input("Enter Customer Name : ")
gender = input("Enter Gender (Male/Female) : ")

print("\nEnter Product 1 Details")
item1 = input("Item Name : ")
qty1 = int(input("Quantity : "))
price1 = 10
total1 = qty1 * price1
if qty1 > 4:
    dis1 = total1 * 5 / 100
else:
    dis1 = 0
after1 = total1 - dis1

print("\nEnter Product 2 Details")
item2 = input("Item Name : ")
qty2 = int(input("Quantity : "))
price2 = 20

total2 = qty2 * price2
dis2 = 0
after2 = total2 - dis2


print("\nEnter Product 3 Details")
item3 = input("Item Name : ")
qty3 = int(input("Quantity : "))
price3 = 30
total3 = qty3 * price3
dis3 = 0
after3 = total3 - dis3


print("\nEnter Product 4 Details")
item4 = input("Item Name : ")
qty4 = int(input("Quantity : "))
price4 = 40

total4 = qty4 * price4
dis4 = 0
after4 = total4 - dis4


print("\nEnter Product 5 Details")
item5 = input("Item Name : ")
qty5 = int(input("Quantity : "))
price5 = 50

total5 = qty5 * price5

if qty5 >= 0:
    dis5 = total5 * 10 / 100
else:
    dis5 = 0

after5 = total5 - dis5


print("\nEnter Product 6 Details")
item6 = input("Item Name : ")
qty6 = int(input("Quantity : "))
price6 = 60

total6 = qty6 * price6
dis6 = 0
after6 = total6 - dis6


print("\nEnter Product 7 Details")
item7 = input("Item Name : ")
qty7 = int(input("Quantity : "))
price7 = 70

total7 = qty7 * price7
dis7 = 0
after7 = total7 - dis7


print("\nEnter Product 8 Details")
item8 = input("Item Name : ")
qty8 = int(input("Quantity : "))
price8 = 80

total8 = qty8 * price8
dis8 = 0
after8 = total8 - dis8


print("\nEnter Product 9 Details")
item9 = input("Item Name : ")
qty9 = int(input("Quantity : "))
price9 = 90

total9 = qty9 * price9
dis9 = 0
after9 = total9 - dis9


# ================= PRODUCT 10 =================
print("\nEnter Product 10 Details")
item10 = input("Item Name : ")
qty10 = int(input("Quantity : "))
price10 = 100
total10 = qty10 * price10
dis10 = total10 * 15 / 100
after10 = total10 - dis10


actual_price = (
    total1 + total2 + total3 + total4 + total5 +
    total6 + total7 + total8 + total9 + total10
)

product_discounted_price = (
    after1 + after2 + after3 + after4 + after5 +
    after6 + after7 + after8 + after9 + after10
)




if product_discounted_price > 10000:
    bill_discount = product_discounted_price * 15 / 100
else:
    if product_discounted_price >= 5000:
        bill_discount = product_discounted_price * 10 / 100
    else:
        bill_discount = 0


after_bill_discount = product_discounted_price - bill_discount

gst = after_bill_discount * 10 / 100
carry_bag = input("\nDo you want Carry Bag? (yes/no) : ")

if carry_bag == "yes":
    bag_amount = 10
    bag_text = "Yes"
else:
    bag_amount = 0
    bag_text = "No"

if gender == "female":
    gift = "Cadbury"
else:
    if gender == "male":
        gift = "Leather Wallet"
    else:
        gift = "No Gift"

final_amount = after_bill_discount + gst + bag_amount

print("\n\n")
print("==============================================================")
print("                         D-MART")
print("==============================================================")
print("Name :", name)
print("Gender :", gender)
print("--------------------------------------------------------------")

print("Item Name\tQuantity\tPrice\tTotal\tAfter-Discount")
print("--------------------------------------------------------------")

print(item1, "\t\t", qty1, "\t\t", price1, "\t",
      total1, "\t", after1)

print(item2, "\t\t", qty2, "\t\t", price2, "\t",
      total2, "\t", after2)

print(item3, "\t\t", qty3, "\t\t", price3, "\t",
      total3, "\t", after3)

print(item4, "\t\t", qty4, "\t\t", price4, "\t",
      total4, "\t", after4)

print(item5, "\t\t", qty5, "\t\t", price5, "\t",
      total5, "\t", after5)

print(item6, "\t\t", qty6, "\t\t", price6, "\t",
      total6, "\t", after6)

print(item7, "\t\t", qty7, "\t\t", price7, "\t",
      total7, "\t", after7)

print(item8, "\t\t", qty8, "\t\t", price8, "\t",
      total8, "\t", after8)

print(item9, "\t\t", qty9, "\t\t", price9, "\t",
      total9, "\t", after9)

print(item10, "\t\t", qty10, "\t\t", price10, "\t",
      total10, "\t", after10)

print("--------------------------------------------------------------")

print("Actual Price              :", actual_price)
print("Product Discounted Price  :", product_discounted_price)
print("Bill Discount             :", bill_discount)
print("After Bill Discount       :", after_bill_discount)

print("Gift :-", gift, "             : 0.00")

print("Carry Bag :", bag_text, "          :", bag_amount)

print("GST (10%)                 :", gst)

print("--------------------------------------------------------------")
print("FINAL BILL AMOUNT         :", final_amount, "RS")
print("--------------------------------------------------------------")

print("                     Thank You")
print("                      To Visit")
print("                       D-Mart")
print("--------------------------------------------------------------")
 
           