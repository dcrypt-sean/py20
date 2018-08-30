import random as r

def dice():

    print("Which Die Do You Want To Roll?")
    print("[1]d100, [2]d20, [3]d12, [4]d10, [5]d8, [6]d6, [7]d4")

    x = input(">> ")
    
    if x == 1: print("You rolled a d100 and got a " + str(r.randint(1, 100)))
    elif x == 2: print("You rolled a d20 and got a " + str(r.randint(1, 20)))
    elif x == 3: print ("You rolled a d12 and got a " + str(r.randint(1, 12)))
    elif x == 4: print ("You rolled a d10 and got a " + str(r.randint(1, 10)))
    elif x == 5: print ("You rolled a d8 and got a " + str(r.randint(1, 8)))
    elif x == 6: print ("You rolled a d6 and got a " + str(r.randint(1, 6)))
    elif x == 7: print ("You rolled a d4 and got a " + str(r.randint(1, 4)))
    elif x not in [1, 2, 3, 4, 5, 6, 7]: print("Sorry please choose a number between 0 and 6.")
    
while True:
	dice()
