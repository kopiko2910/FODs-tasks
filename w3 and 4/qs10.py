#this program takes number form user untill they like and
#displays the list of even and odd after the input is finished
def segregate_numbers():
    even_numbers = []
    odd_numbers = []
    
    print("Number Segregation Program")
    print("Enter numbers one by one (type 'stop' to finish)")
    
    while True:
        user_input = input("Enter a number (or 'stop' to exit): ")
        
        if user_input.lower() == 'stop':
            break
            
        try:
            num = float(user_input)
            if num.is_integer():  
                num = int(num)
                if num % 2 == 0:
                    even_numbers.append(num)
                else:
                    odd_numbers.append(num)
            else:
                print("Please enter whole numbers only (decimals will be ignored)")
        except ValueError:
            print("Invalid input! Please enter a number or 'stop' to exit")
    
    # Display results
    print("\nResults:")
    print("Even numbers:", sorted(even_numbers))
    print("Odd numbers:", sorted(odd_numbers))
if __name__ == "__main__":
    segregate_numbers()
