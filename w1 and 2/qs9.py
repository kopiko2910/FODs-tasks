#this program prindts the factorial of a number
def calculate_factorial():
    user_input = input("Enter a positive integer to calculate its factorial: ")
    if user_input.isdigit():
        num = int(user_input)
        if num < 0:
            print("Error: Please enter a positive integer.")
        else:
            factorial = 1
            if num == 0 or num == 1:
                print("The factorial of " + str(num) + " is 1")
            else:
                for i in range(1, num + 1):
                    factorial *= i
                print("The factorial of " + str(num) + " is " + str(factorial))
    else:
        print("Error: Not a number.")
calculate_factorial()
