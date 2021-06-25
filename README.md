### Roshambo Breakdown                  - written 6/24/2021 by brettandrews3
### Here's my step-by-step description of how this program works:

### First, we import the two Python libraries that we need: random and IntEnum. The former generates the computer's
### random answer, while the latter swaps out simple integer inputs for the rock, paper, scissors choices in class Action().
import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors =2

# Here's the scoring variables. Since the rest of the code is function definitions and calls, I figured that
# declaring numeric variables up here with the IntEnum data made sense. I could probably shift the scores into 
# IntEnum, too, but they work just fine as integers here.
user_score = 0
comp_score = 0
tie_score = 0

print("Welcome to Roshambo!\n") 

### Here, we define the get_user_choice function. 'The choices =' line links the key/value pairs
### from the class Action() description. It joins them together to create a string (choices_str),
### which feeds into the input question from the user_choice line. By approaching user_choice in this
### way, you can expand or contract class Action() to feature answers besides rock, paper, and scissors.
### The Big Bang Theory version 'Rock Paper Scissors Lizard Spock" applies this expansion option. 
def get_user_choice():
    choices = [f'{action.name}[{action.value}]' for action in Action]
    choices_str = ', '.join(choices)
    user_choice = int(input(f'Enter a choice ({choices_str}): '))
    action = Action(user_choice)
    return action

### Computer generates comp_choice using random.randint and scalable class Action(). The complex definition
### for comp_choice applies the randomizer of random.randint while accounting for the expandable nature of
### class Action(). By setting len() - 1, it keeps the counting of both Action and len() set to zero index.
def get_comp_choice():
    comp_choice = random.randint(0, len(Action) -1) ### Action counts from 0, len() counts from 1.
    action = Action(comp_choice)
    return action

### Here's where I defined the winning conditions for Roshambo. The decide_winner() takes in the user_choice and comp_choice
### arguments to determine the winner each round. Setting the tie conditions as the initial if statement allows for a simplified
### two-condition process for each rock/paper/scissors combination: if you account for ties, you can only win or lose in other
### combinations. This would expand if I apply the 'Rock Paper Scissors Lizard Spock' rules mentioned earlier. Nevertheless,
### the elif-if-else pockets for each entry keep the code clean.
### The '_score' variables must be declared global within the function to work. Why?  ¯\_(ツ)_/¯

def decide_winner(user_choice, comp_choice):
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

### With the rules established above, the while loop is responsible for executing the game.
### The setup is simple: while True (game is running), the program tries to get the user_choice as defined above.
### The except ValueError statement catches any input that falls outside the current range of class Action();
### in this initial case, the user must re-enter their choice if they give a number lower than 0 or higher than 2.
### This numerical approach simplifies my previous efforts, where the user had to enter the string 'rock'|'paper'|'scissors'
### exactly as shown in the input prompt. Changing to a simple int answer eliminates the need to account for spelling variations.

### Finally, the play_again input lets the user decide whether to play again or end the game. The "if play_again.lower() != 'y'"
### line allows for either 'Y' or 'y' input from the user without the complications of defining additional Regex responses.
### If the user decides not to continue, the program gives a 'Thanks for playing!' message and ends. 
### 6/25/2021: I added that scoring system mentioned in the previous version of this README. The print(f'Score...') displays
### the running tally after each round.

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