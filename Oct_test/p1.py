'''Write a program that accepts an integer and checks whether it is a Harshad number.
A number is a Harshad number if it is divisible by the sum of its digits.'''

num=int(input("Enter a number:"))
sum=0
temp=num
while num>0:
    last_digit=num%10
    sum+=last_digit
    num=num//10
print("sum is",sum)
if temp%sum==0:
    print("Yes! its harshad's number")
else:
    print("its not harshad's number")