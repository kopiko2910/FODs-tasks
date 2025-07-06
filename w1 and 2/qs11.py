#this program is about an numner guessing game
import random
def number_guessing_game():
    # Generating a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 5
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it.\n")
    
    for attempt in range(1, attempts + 1):
        print(f"Attempt {attempt} of {attempts}")
        try:
            guess = int(input("Enter your guess: "))
            
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Correct number! You guessed it in {attempt} attempts!")
                return
        except ValueError:
            print("Please enter a valid number!")
            continue
        if attempt < attempts:
            print("Try again!\n")
    print(f"\nGame Over! The number was {secret_number}.")
number_guessing_game()
