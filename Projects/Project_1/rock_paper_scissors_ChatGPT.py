### write me rock paper scissors game in python

import random

# Define choices
choices = ["rock", "paper", "scissors"]

# Game logic
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Main game loop
while True:
    # Get player's choice
    player_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
    
    if player_choice == "quit":
        print("Thanks for playing!")
        break
    
    if player_choice not in choices:
        print("Invalid choice. Try again.")
        continue
    
    # Computer's choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    # Determine and display the winner
    result = determine_winner(player_choice, computer_choice)
    print(result)

#####################################################################################
### I want to print the computer and player choice so the user can see what they choice

# import random

# # Define choices
# choices = ["rock", "paper", "scissors"]

# # Game logic
# def determine_winner(player, computer):
#     if player == computer:
#         return "It's a tie!"
#     elif (player == "rock" and computer == "scissors") or \
#          (player == "scissors" and computer == "paper") or \
#          (player == "paper" and computer == "rock"):
#         return "You win!"
#     else:
#         return "Computer wins!"

# # Main game loop
# while True:
#     # Get player's choice
#     player_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
    
#     if player_choice == "quit":
#         print("Thanks for playing!")
#         break
    
#     if player_choice not in choices:
#         print("Invalid choice. Try again.")
#         continue
    
#     # Computer's choice
#     computer_choice = random.choice(choices)
    
#     # Display choices
#     print(f"\nYou chose: {player_choice}")
#     print(f"Computer chose: {computer_choice}")
    
#     # Determine and display the winner
#     result = determine_winner(player_choice, computer_choice)
#     print(result + "\n")

#################################################################################
### Can you make shorter as i can see you repeated the condition of winning 3 times

# import random

# # Define choices and winning conditions
# choices = ["rock", "paper", "scissors"]
# winning_combinations = {
#     "rock": "scissors",
#     "scissors": "paper",
#     "paper": "rock"
# }

# # Main game loop
# while True:
#     # Get player's choice
#     player_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
    
#     if player_choice == "quit":
#         print("Thanks for playing!")
#         break
    
#     if player_choice not in choices:
#         print("Invalid choice. Try again.")
#         continue
    
#     # Computer's choice
#     computer_choice = random.choice(choices)
    
#     # Display choices
#     print(f"\nYou chose: {player_choice}")
#     print(f"Computer chose: {computer_choice}")
    
#     # Determine and display the winner
#     if player_choice == computer_choice:
#         print("It's a tie!\n")
#     elif winning_combinations[player_choice] == computer_choice:
#         print("You win!\n")
#     else:
#         print("Computer wins!\n")
####################################

# Can you make shorter as i can see you repeated the condition of winning 3 times

import random

# Define choices and winning conditions
choices = ["rock", "paper", "scissors"]
winning_combinations = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

# Main game loop
while True:
    # Get player's choice
    player_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
    
    if player_choice == "quit":
        print("Thanks for playing!")
        break
    
    if player_choice not in choices:
        print("Invalid choice. Try again.")
        continue
    
    # Computer's choice
    computer_choice = random.choice(choices)
    
    # Display choices
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    # Determine and display the winner
    if player_choice == computer_choice:
        print("It's a tie!\n")
    elif winning_combinations[player_choice] == computer_choice:
        print("You win!\n")
    else:
        print("Computer wins!\n")
