# I'm rewriting rockPaperScissors.py to see if I can get more killer
# and less filler in the code. More succinct comments, lean variable usage.

import random

while True:
    #winner = ''
    user_choice = ''

    computer_choice = random.randint(0, 2) # Computer has 3 game choices.
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    print('Welcome to Roshambo!\n')
    user_choice = input('Choose your weapon: rock, paper, or scissors? ')
    print(f"You chose {user_choice}. The computer chose {computer_choice}.\n")

    # The code runs through all potential outcomes and prints the result:
    if user_choice == computer_choice:
        print("You both made the same choice. It's a tie!\n")
    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            print('Rock smashes scissors. You win!\n')
        else:
            print('Paper covers rock. You lose the round.\n')
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print('Paper covers rock. You win!\n')
        else:
            print('Scissors cut paper. You lose the round.\n')
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            print('Scissors cut paper. You win!\n')
        else:
            print('Rock smashes scissors. You lose the round.\n')

    # User can choose to play again or end the program:
    play_again = input('Want to play again? (y/n): ')
    if play_again.lower() != 'y':
        break