class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b


calculator = Calculator()

print("===== CALCULATOR =====")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice: ")

    if choice == "1":
        result = calculator.add(num1, num2)

    elif choice == "2":
        result = calculator.subtract(num1, num2)

    elif choice == "3":
        result = calculator.multiply(num1, num2)

    elif choice == "4":
        result = calculator.divide(num1, num2)

    else:
        print("Invalid choice.")
        result = None

    if result is not None:
        print(f"Result: {result}")

except ValueError:
    print("Invalid input. Please enter numbers only.")

except ZeroDivisionError as error:
    print(f"Error: {error}")

except Exception as error:
    print(f"Unexpected error: {error}")