# Very Simple Calculator

# Ask the user to enter two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Convert the input to numbers (float)
num1 = float(num1)
num2 = float(num2)

# Ask the user to choose an operation
operation = input("Choose operation (+, -, *, /): ")

# Perform the calculation and show the result
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("Invalid operation")
