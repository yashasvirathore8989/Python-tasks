def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    if b == 0:
        return "Error: Division by zero not allowed!"
    return a/b

def power(a,b):
    return a**b

def floor_division(a,b):
    return a//b

def modulus(a, b):
    if b == 0:
        return "Error: Division by zero not allowed!"
    return a % b

def get_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

while True:
    print("----Smart Calculator---- ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. floor_division")
    print("7. power")
    print("8. exit")

    choice=input("Enter your choice (1-8): ")
    if choice=='8':
        print("Thank you for using calculator....!!!")
        break

    if choice=='1':
        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            num1, num2 = get_numbers()
            if choice == '1':
                print(f"Result: {addition(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtraction(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiplication(num1, num2)}")
            elif choice == '4':
                print(f"Result: {division(num1, num2)}")
            elif choice == '5':
                print(f"Result: {modulus(num1, num2)}")
            elif choice == '6':
                print(f"Result: {power(num1, num2)}")
            elif choice == '7':
                print(f"Result: {floor_division(num1, num2)}")
            else:
                print("Invalid choice! Please select from 1-8")
