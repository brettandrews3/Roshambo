# Starting over to test out enumeration as a simplified way
# to generate responses. This should make for cleaner code than the main
# branch's version.

import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors =2

print("Welcome to Roshambo!")

"""# Player input, option 1 - verbose:
def get_user_choice():
    user_choice = input("Enter your choice of rock[0], paper[1], or scissors[2]: ")
    choice = int(user_choice)
    action = Action(choice)
    return action              # Take user input, convert to int, then convert int to class Action.
"""

# Player input, option 2 - list comprehension:
def get_user_choice():
    choices = [f'{action.name}[{action.value}]' for action in Action]
    choices_str = ', '.join(choices)
    user_choice = int(input(f'Enter a choice ({choices_str}): '))
    action = Action(user_choice)
    return action
#TODO: Comment through each step of this interpolation function.

# Computer generates comp_choice using random.randint and scalable class Action:
def get_comp_choice():
    comp_choice = random.randint(0, len(Action) -1) # Action counts from 0, len() counts from 1.
    action = Action(comp_choice)
    return action
#TODO: Comment through each step of this function.

def decide_winner(user_action, comp_action):
    if user_action == comp_action:
        print(f"You both chose {user_choice.name}. It's a tie!")
    elif user_action == Action.Rock:
        if comp_action == Action.Scissors:
            print("Rock smashes scissors. You win!")
        else:
            print("Paper covers rock! The computer wins.")
    elif user_action == Action.Paper:
        if comp_action == Action.Rock:
            print("Paper covers rock. You win the round!")
        else:
            print("Scissors cut paper! The computer wins.")
    elif user_action == Action.Scissors:
        if comp_action == Action.Paper:
            print("Scissors cut paper. You win the round!")
        else:
            print("Rock smashes scissors. The computer wins.")