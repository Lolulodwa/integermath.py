# Ask the user to enter three different integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

sum_all = num1 + num2 + num3
difference = num1 - num2
product = num3 * num1
division = sum_all / num3 if num3 != 0 else "Undefined (division by zero)"

print("\nResults:")
print(f"Sum of all numbers: {sum_all}")
print(f"First number minus second number: {difference}")
print(f"Third number multiplied by first number: {product}")
print(f"Sum of all numbers divided by third number: {division}")