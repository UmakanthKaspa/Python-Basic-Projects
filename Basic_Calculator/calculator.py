def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def square_root(x):
    if x < 0:
        return "Error: Invalid input for square root"
    return x ** 0.5

def power(x, y):
    return x ** y

while True:
    print("\nOptions:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'sqrt' for square root")
    print("Enter 'power' for exponentiation")
    print("Enter 'quit' to end the program")
    
    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ["add", "subtract", "multiply", "divide", "power"]:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if user_input == "add":
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif user_input == "subtract":
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif user_input == "multiply":
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif user_input == "divide":
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"Result: {num1} / {num2} = {result:.2f}")
        elif user_input == "power":
            print(f"Result: {num1} ^ {num2} = {power(num1, num2)}")
    elif user_input == "sqrt":
        num = float(input("Enter a number: "))
        result = square_root(num)
        if isinstance(result, str):
            print(result)
        else:
            print(f"Result: √{num} = {result:.2f}")
    else:
        print("Invalid input. Please try again.")
