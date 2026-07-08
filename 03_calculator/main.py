print("=" * 40)
print("      SIMPLE CALCULATOR")
print("=" * 40)

# Get two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Display menu
print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("\nEnter your choice (1-4): ")

# Perform calculation
if choice == "1":
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")

elif choice == "2":
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")

elif choice == "3":
    result = num1 * num2
    print(f"\nResult: {num1} * {num2} = {result}")

elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\nError! Division by zero is not allowed.")

else:
    print("\nInvalid choice! Please run the program again.")

print("\nThank you for using the Calculator!")