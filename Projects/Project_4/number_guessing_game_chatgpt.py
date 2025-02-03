# import random

# def guessing_game():
#     print("Welcome to the Number Guessing Game!")
#     number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
#     attempts = 0

#     while True:
#         try:
#             guess = int(input("Guess a number between 1 and 100: "))
#             attempts += 1

#             if guess < number_to_guess:
#                 print("Too low! Try again.")
#             elif guess > number_to_guess:
#                 print("Too high! Try again.")
#             else:
#                 print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
#                 break
#         except ValueError:
#             print("Please enter a valid number.")

# guessing_game()
# ###############
import random

def start_game():
    player_name = input("Enter your name: ")
    print(f"Welcome {player_name}! Try to guess the number between 1 and 100. You have 10 attempts.")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations, {player_name}! You've guessed the correct number in {attempts} attempts.")
            break
    else:
        print(f"Game over! The correct number was {number_to_guess}. Better luck next time, {player_name}!")
    
    # End the game
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        start_game()
    else:
        print("Thank you for playing. Goodbye!")

# Start the game
start_game()
############
# import random

# def guessing_game():
#     print("Welcome to the Number Guessing Game!")
#     player_name = input("Enter your name: ")
#     print(f"Hello, {player_name}! Let's start the game.")

#     while True:
#         number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
#         attempts = 0

#         while True:
#             try:
#                 guess = int(input("Guess a number between 1 and 100: "))
#                 attempts += 1

#                 if guess < number_to_guess:
#                     print("Too low! Try again.")
#                 elif guess > number_to_guess:
#                     print("Too high! Try again.")
#                 else:
#                     print(f"Congratulations, {player_name}! You've guessed the number {number_to_guess} in {attempts} attempts.")
#                     break
#             except ValueError:
#                 print("Please enter a valid number.")

#         # Ask if the player wants to play again
#         play_again = input("Do you want to play again? (yes/no): ").strip().lower()
#         if play_again != 'yes':
#             print("Thank you for playing! Goodbye.")
#             break

# guessing_game()
