#this program prints the even or odd number untill the user wants it
sum_even = 0
sum_odd = 0

while True:
    print("\nMenu:")
    print("1. Enter a number")
    print("2. Display sums and exit")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        try:
            num = int(input("Enter a number: "))
            if num % 2 == 0:
                sum_even += num
            else:
                sum_odd += num
            print("Number added successfully!")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    elif choice == '2':
        print("\nFinal Results:")
        print("Sum of even numbers:", sum_even)
        print("Sum of odd numbers:", sum_odd)
        print("Thank you for using the program!")
        break
    
    else:
        print("Invalid choice! Please enter 1 or 2.")
