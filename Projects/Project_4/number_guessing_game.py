import random

attempts_list = []

def show_score():
    if not attempts_list:
        print("There's currently a high score, start playing!")
    else:
        print(f"The current high score is {min(attempts_list)} attempts")

attempts_list = 0
rand_number = random.randint(1, 10)

print("Hello player! Welcome to the guessing game!")
player_name = input("What's your name? ")
wanna_play = input(
    f"Hi, {player_name}, would you like to play the guessing game?"
    " (Enter Yes/No) "
).lower()

if wanna_play == "no":
    print("That's cool, Thanks!")
    exit()
else:
    show_score()

while wanna_play == "yes":
    try:
        guess = int(input("Pick a number between 1 and 10: "))
        if(guess < 1 or guess > 10):
            raise ValueError("Please guess a number within the given range")

        attempts += 1 

        if(guess == rand_number):
            print("Nice, you got it!")
            print(f"It took you {attempts} attempts!") 
            wanna_play = input("Would you like play again? (Enter Yes/No): ").lower()

            attempts_list.append(attempts) 

            if wanna_play == "no":
                print("That's cool, have a good day.")
            else:
                attempts = 0
                rand_number = random.randint(1, 10)
                show_score()
                continue
        elif (guess > rand_number):
            print("It's lower!")
        else:
            print("It's higher!")
    except ValueError as err:
        print("err")

####################

import random

# Initialize the list to track high scores
attempts_list = []

def show_score():
    """Displays the current high score based on attempts."""
    if not attempts_list:
        print("There's currently no high score, start playing!")
    else:
        print(f"The current high score is {min(attempts_list)} attempts.")

def play_game():
    """Main function to play the number guessing game."""
    rand_number = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            guess = int(input("Pick a number between 1 and 10: "))
            if guess < 1 or guess > 10:
                raise ValueError("Please guess a number within the given range.")

            attempts += 1

            if guess == rand_number:
                print(f"Nice, you got it in {attempts} attempts!")
                attempts_list.append(attempts)
                break
            elif guess > rand_number:
                print("It's lower!")
            else:
                print("It's higher!")
        except ValueError as err:
            print(f"Invalid input: {err}")

def main():
    print("Hello player! Welcome to the guessing game!")
    player_name = input("What's your name? ")
    print(f"Hi, {player_name}! Let's play!")

    while True:
        wanna_play = input("Would you like to play the guessing game? (Enter Yes/No): ").strip().lower()
        if wanna_play == "no":
            print("That's cool, thanks for stopping by!")
            break
        elif wanna_play == "yes":
            show_score()
            play_game()
            play_again = input("Would you like to play again? (Enter Yes/No): ").strip().lower()
            if play_again == "no":
                print("Thanks for playing! Have a great day!")
                break
        else:
            print("Please enter 'Yes' or 'No'.")

# Start the game
main()
