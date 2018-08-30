def dice():
    d100 = random.randint(1, 100)
    d20 = random.randint(1, 20)
    d12 = random.randint(1, 12)
    d10 = random.randint(1, 10)
    d8 = random.randint(1, 8)
    d6 = random.randint(1, 6)
    d4 = random.randint(1, 4)

    print("Which Die Do You Want To Roll?")
    print("[0]d100, [1]d20, [2]d12, [3]d10")
    print("[4]d8, [5]d6, [6]d4")

    x = input(">> ")
    
    if x == 0: print("You rolled a d100 and got a " + str(d100))
    elif x == 1: print("You rolled a d20 and got a " + str(d20))
    elif x == 2: print ("You rolled a d12 and got a " + str(d12))
    elif x == 3: print ("You rolled a d10 and got a " + str(d10))
    elif x == 4: print ("You rolled a d8 and got a " + str(d8))
    elif x == 5: print ("You rolled a d6 and got a " + str(d6))
    elif x == 6: print ("You rolled a d4 and got a " + str(d4))
    elif x not in [0, 1, 2, 3, 4, 5, 6]: print("Sorry please choose a number between 1 and 6.")
    
while True:
    dice()
