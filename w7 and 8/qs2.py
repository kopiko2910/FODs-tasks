def get_user_array():
    while True:
        user_input = input("Enter at least 10 numbers separated by spaces: ")
        numbers = user_input.split()
        
        if len(numbers) < 10:
            print("Please enter at least 10 numbers!")
            continue
            
        try:
            num_list = [float(num) for num in numbers]
            return num_list
        except ValueError:
            print("Invalid input! Please enter numbers only.")

def main():
   
    numbers = get_user_array()
    
   
    sorted_numbers = sorted(numbers)
    print("\nSorted array:", sorted_numbers)
    
   
    print("\nSlicing operations:")
    print("Elements from index 2 to 5:", sorted_numbers[2:6]) 
    print("Elements from index 5 to 8:", sorted_numbers[5:9])
    print("Elements from index 2 to 9:", sorted_numbers[2:10])
    
  
    print("\nAdditional slicing examples:")
    print("First 5 elements:", sorted_numbers[:5])
    print("Elements from index 3 to end:", sorted_numbers[3:])
    print("Last 4 elements:", sorted_numbers[-4:])
    print("Every alternate element:", sorted_numbers[::2])

if __name__ == "__main__":
    main()