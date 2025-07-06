import datetime

def perform_calculations():
    history = []
    
    while True:
        print("\nCalculator Menu:")
        print("1. Perform calculations")
        print("2. Exit and view history")
        
        choice = input("Enter your choice (1/2): ")
        
        if choice == '1':
         
            numbers = input("Enter numbers separated by spaces: ").split()
            try:
                numbers = [float(num) for num in numbers]
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue
            
            if not numbers:
                print("No numbers entered. Please try again.")
                continue
                
         
            addition = sum(numbers)
            subtraction = numbers[0] - sum(numbers[1:])
            multiplication = 1
            for num in numbers:
                multiplication *= num
                
            try:
                division = numbers[0]
                for num in numbers[1:]:
                    division /= num
            except ZeroDivisionError:
                division = "Undefined (division by zero)"
            
          
            now = datetime.datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            
           
            result = {
                'timestamp': timestamp,
                'numbers': numbers,
                'addition': addition,
                'subtraction': subtraction,
                'multiplication': multiplication,
                'division': division
            }
            
           
            history.append(result)
            
         
            with open("calculations_history.txt", "a") as file:
                file.write(f"\n\nTimestamp: {timestamp}\n")
                file.write(f"Numbers: {numbers}\n")
                file.write(f"Addition: {addition}\n")
                file.write(f"Subtraction: {subtraction}\n")
                file.write(f"Multiplication: {multiplication}\n")
                file.write(f"Division: {division}\n")
                file.write("-" * 40)
            
            print("\nCalculations performed and saved successfully!")
            
        elif choice == '2':
           
            print("\nCalculation History:")
            try:
                with open("calculations_history.txt", "r") as file:
                    print(file.read())
            except FileNotFoundError:
                print("No history found.")
            break
            
        else:
            print("Invalid choice. Please enter 1 or 2.")

perform_calculations()