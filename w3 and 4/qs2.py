def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2
#this program performs addition, subtraction, multiplication, division, modulo and floor division using separate functions
def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Cannot divide by zero"

def modulo(num1, num2):
    try:
        return num1 % num2
    except ZeroDivisionError:
        return "Cannot modulo by zero"

def floor_divide(num1, num2):
    try:
        return num1 // num2
    except ZeroDivisionError:
        return "Cannot floor divide by zero"

# Main program
def main():
    print("Mathematical Operations Calculator")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        print("\nResults:")
        print(f"Addition:        {num1} + {num2} = {add(num1, num2)}")
        print(f"Subtraction:     {num1} - {num2} = {subtract(num1, num2)}")
        print(f"Multiplication:  {num1} × {num2} = {multiply(num1, num2)}")
        print(f"Division:        {num1} ÷ {num2} = {divide(num1, num2)}")
        print(f"Modulo:          {num1} % {num2} = {modulo(num1, num2)}")
        print(f"Floor Division:  {num1} // {num2} = {floor_divide(num1, num2)}")
    
    except ValueError:
        print("Error: Please enter valid numbers!")

if __name__ == "__main__":
    main()
