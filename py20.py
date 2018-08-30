import random as r

def dice():
        d_sides = input("What would you like to roll? ")
        die = input("How many? ")
        for _ in range(die):
                print(r.randint(1, d_sides))
while True:
        dice()
