import calculator

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

addition = calculator.add(num1, num2)
print(f"Addition: {addition}")

subtraction = calculator.subtract(num1, num2)
print(f"Subtraction: {subtraction}")

multiplication = calculator.multiply(num1, num2)
print(f"Multiplication: {multiplication}")

division = calculator.divide(num1, num2)
print(f"Division: {division}")