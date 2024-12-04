import random
# loops to get the level from user
while True:
    try:
        level = int(input("Level: "))
        if level > 0:  # positive integer breaks the loop
            break
    except ValueError:  # gets rid of incorrect inputs
        continue

random_number = random.randint(1, level)
# loops for the guessing game, asks the user for a number and then checks if it's correct
while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            continue  # gets rid of all negative inputs
        else:
            if guess < random_number:
                print("Too small!")
            elif guess > random_number:
                print("Too large!")
            else:
                print("Just right!")
                break  # ends the program
    except ValueError:
        continue
