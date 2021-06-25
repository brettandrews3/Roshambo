# Starting over to test out enumeration as a simplified way to generate responses.
# See the README file in this program's repo for a detailed description of each code block.

import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

# Declare the score variables here:
user_score = 0
comp_score = 0
tie_score = 0

print("Welcome to Roshambo!\n")

# Player input, using list comprehension to select from expandable class Action():
def get_user_choice():
    choices = [f'{action.name}[{action.value}]' for action in Action]
    choices_str = ', '.join(choices)
    user_choice = int(input(f'Enter a choice ({choices_str}): '))
    action = Action(user_choice)
    return action

# Computer generates comp_choice using random.randint and scalable class Action:
def get_comp_choice():
    comp_choice = random.randint(0, len(Action) -1) # Action counts from 0, len() counts from 1.
    action = Action(comp_choice)
    return action

def decide_winner(user_choice, comp_choice):
    # The two _score vars must be declared global within the function. Why?  ¯\_(ツ)_/¯
    global user_score
    global comp_score
    global tie_score

    if user_choice == comp_choice:
        print(f"You both chose {user_choice.name}. It's a tie!\n")
        tie_score += 1
    elif user_choice == Action.Rock:
        if comp_choice == Action.Scissors:
            print("Rock smashes scissors. You win!\n")
            user_score += 1
        else:
            print("Paper covers rock! The computer wins.\n")
            comp_score += 1
    elif user_choice == Action.Paper:
        if comp_choice == Action.Rock:
            print("Paper covers rock. You win the round!\n")
            user_score += 1
        else:
            print("Scissors cut paper! The computer wins.\n")
            comp_score += 1
    elif user_choice == Action.Scissors:
        if comp_choice == Action.Paper:
            print("Scissors cut paper. You win the round!\n")
            user_score += 1
        else:
            print("Rock smashes scissors. The computer wins.\n")
            comp_score += 1

while True:
    try:
        user_action = get_user_choice()
    except ValueError as e:
        range_str = f"[0, {len(Action) -1}]"
        print(f"Invalid choice. Enter a value in range {range_str}.\n")
        continue

    comp_action = get_comp_choice()
    decide_winner(user_action, comp_action)

    print(f'Score: User {user_score}, Computer {comp_score}, Ties {tie_score}\n')

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != 'y':
        print("Thanks for playing Roshambo!")
        break