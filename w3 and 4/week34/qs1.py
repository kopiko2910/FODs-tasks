#this program displays sum, diff, product and remainder
def calculate_operations(num1, num2):
    """Function to calculate and display sum, difference, product, and remainder."""
    print("Sum:", num1 + num2)
    print("Difference:", num1 - num2)
    print("Product:", num1 * num2)
    
    if num2 != 0:
        print("Remainder:", num1 % num2)
    else:
        print("Remainder: Cannot divide by zero")

try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    calculate_operations(number1, number2)
except ValueError:
    print("Please enter valid integers.")
