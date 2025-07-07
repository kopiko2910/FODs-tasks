#this profram Returns a new list with duplicate values removed
def remove_duplicates(numbers):
    """Return a new list with duplicate values removed"""
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

def main():
    print("Duplicate Number Remover")
    print("Enter numbers separated by spaces (e.g., '1 2 2 3 4 4 5')")
    
    try:
        user_input = input("Enter your numbers: ")
        numbers = [float(num) for num in user_input.split()]
        unique_numbers = remove_duplicates(numbers)
        print("\nOriginal list:", numbers)
        print("List without duplicates:", unique_numbers)
    
    except ValueError:
        print("Error: Please enter valid numbers separated by spaces")

if __name__ == "__main__":
    main()
