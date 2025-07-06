#this program is a card guessing game.
import random

def card_guessing_game():
    
    card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    card_suits = ['Heart', 'Diamond', 'Club', 'Spade']

    answer_value = random.choice(card_values)
    answer_suit = random.choice(card_suits)
    answer = [answer_value, answer_suit]
    
    print("Welcome to the Card Guessing Game!")
    print("Try to guess the hidden playing card!")
    print("-----------------------------------")
  
    print("\nCard Values:", ', '.join(card_values))
    print("Card Suits:", ', '.join(card_suits))
    
    try:
        guess_value = input("\nGuess the card value: ").capitalize()
        guess_suit = input("Guess the card suit: ").capitalize()
        
        print("\nResults:")
        print("--------")
        
        value_match = guess_value == answer_value
        suit_match = guess_suit == answer_suit
        
        if value_match and suit_match:
            print("❤️ 😊 Congratulations! You guessed it right!")
            print(f"The card was the {answer_value} of {answer_suit}s")
        elif value_match or suit_match:
            print("😊 Close! You got one part right!")
            print(f"The card was the {answer_value} of {answer_suit}s")
            if value_match:
                print("You guessed the value correctly!")
            else:
                print("You guessed the suit correctly!")
        else:
            print("💔 Game Over! Your guess was wrong.")
            print(f"The card was the {answer_value} of {answer_suit}s")
    
    except:
        print("Invalid input! Please try again.")

if __name__ == "__main__":
    card_guessing_game()
