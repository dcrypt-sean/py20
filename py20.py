import sys
import random as r

class color:
    MAIN = '\033[32m'
    RESULTS = '\033[93m'
    RESET = '\033[0m'

def dice():
    d_sides = input(color.MAIN + "What would you like to roll? " + color.RESET)
    die = input(color.MAIN + "How many? " + color.RESET)
    for _ in range(die):
        print(color.RESULTS + str(r.randint(1, d_sides)) + color.RESET)

while True:
    try:
        dice()
    except KeyboardInterrupt:
        print('\n'+'Thanks for playing!')
        sys.exit(0)
