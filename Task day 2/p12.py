n=int(input("Enter 4 digit number:"))
if n>=1000 and n<=9999:
 d1=n%10
 d2=(n//10)%10
 d3=(n//100)%10
 d4=n//1000
 reversed_num =d1*1000+d2*100+d3*10+d4
print("Reversed number:",reversed_num)