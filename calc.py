def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Undefined (division by zero)" 
    return x / y

while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break

    if user_input in ("add", "subtract", "multiply", "divide"):
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if user_input == "add":
            print(add(x, y))
        elif user_input == "subtract":
            print(subtract(x, y))
        elif user_input == "multiply":
            print(multiply(x, y))
        elif user_input == "divide":
            print(divide(x, y))
    else:
        print("Invalid Input")
