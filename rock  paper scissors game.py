import random

# define the options
options = ["rock", "paper", "scissors"]

# define colors
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
END = '\033[0m'

# print game title and instructions
print(f'{GREEN}{"="*35}\n{" "*10}Rock Paper Scissors\n{"="*35}{END}\n')
print(f'{YELLOW}Welcome to the game!{END}\n{YELLOW}To play, choose rock, paper, or scissors.{END}')

# get user input
user_choice = input(f'\n{YELLOW}Your choice: {END}').lower()

# generate computer choice
computer_choice = random.choice(options)

# print choices and design
print(f'\n{YELLOW}You chose:{END}     {user_choice}')
print(f'{YELLOW}Computer chose:{END} {computer_choice}\n')
print(f'{GREEN}{"-"*35}{END}')

# determine winner
if user_choice == computer_choice:
    print(f'{YELLOW}It\'s a tie!{END}')
elif user_choice == "rock":
    if computer_choice == "scissors":
        print(f'{YELLOW}You win!{END}')
    else:
        print(f'{RED}Computer wins!{END}')
elif user_choice == "paper":
    if computer_choice == "rock":
        print(f'{YELLOW}You win!{END}')
    else:
        print(f'{RED}Computer wins!{END}')
elif user_choice == "scissors":
    if computer_choice == "paper":
        print(f'{YELLOW}You win!{END}')
    else:
        print(f'{RED}Computer wins!{END}')
else:
    print(f'{RED}Invalid choice. Please choose rock, paper, or scissors.{END}')
