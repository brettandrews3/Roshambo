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
user_action = input("Make your choice: Rock(0), Paper(1), or Scissors(2)?  ")