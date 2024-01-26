print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Remaider")
print("6. Floor Division")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

choice = input("Enter choice (+, -, *, /, %, //): ")

if choice in ('+', '-', '*', '/', '%', '//'):

    if choice == '+':
        result = num1 + num2
        print("Result: ",result)
    elif choice == '-':
        result = num1 - num2
        print("Result: ",result)
    elif choice == '*':
        result = num1 * num2
        print("Result: ",result)
    elif choice == '/':
        if num2 != 0:
            result = num1 / num2
            print("Result: ",result)
        else:
            print("Cannot divide by zero!")
    elif choice == '%':
        result = num1 % num2
        print("Result: ",result)
    elif choice == '//':
        result = num1 // num2
        print("Result: ",result)
else:
    print("Invalid input. Please enter a valid operation.")