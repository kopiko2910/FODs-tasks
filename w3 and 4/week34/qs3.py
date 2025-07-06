#this program displays the factorial of the number using function
def calculate_factorial(n):
    """Function to calculate and return factorial of a number"""
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

def main():
    print("FACTORIAL CALCULATOR")
    print("-------------------")
    
    try:
        num = int(input("Enter a non-negative integer: "))
        result = calculate_factorial(num)
        
        if isinstance(result, str):  
            print(result)
        else:
            print("The factorial of", num, "is:", result)
    
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    main()
