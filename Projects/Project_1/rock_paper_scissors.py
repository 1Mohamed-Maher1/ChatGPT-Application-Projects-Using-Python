# Start the game
# Ask the player to make a move (r,p,s)
# PC would select a move randomly
# PC == Player -> Tie
# (Player == P and PC == Rock) or (Player == R and PC == Scissors) or (player == S and PC == P)
## User won / You won
# Any other case
## PC won / You lose

import random

user = input ("What's your choice? 'r' for Rock, 'p' for paper, 's' for scissors\n")
pc = random.choice(['r','p','s'])

print("User played: " + user)
print("PC played: " + pc)

if user == pc:
    print("It's a tie")
elif ( (user == 'p' and pc == 'r') or (user == 'r' and pc == 's') or (user == 's' and pc == 'p')):
    print("You won")
else:
    print("You lose!")

# Refactor 

import random

# Winning conditions dictionary
winning_combinations = {
    'r': 's',  # Rock beats Scissors
    'p': 'r',  # Paper beats Rock
    's': 'p'   # Scissors beats Paper
}

# Start the game
user = input("What's your choice? 'r' for Rock, 'p' for Paper, 's' for Scissors\n").lower()
pc = random.choice(['r', 'p', 's'])

# Display choices
print(f"User played: {user}")
print(f"PC played: {pc}")

# Determine the outcome
if user == pc:
    print("It's a tie!")
elif winning_combinations.get(user) == pc:
    print("You won!")
else:
    print("You lose!")
