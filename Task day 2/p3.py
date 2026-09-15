years=int(input("Enter years of service :"))
salary= float(input("Enter salary :"))
net_salary=years*salary
if years>5:
 bonus=net_salary+net_salary*(5/100)
 print("As you completed 5 years")
 print("Your net salary with bonus :",bonus)
else:
 print("Your net salary :",net_salary)