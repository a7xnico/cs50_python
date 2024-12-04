import random
# same code as game.py but in functions for practice


def main():
    level = level_check()
    random_number = random.randint(1, level)
    game_loop(random_number)


def level_check():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
            else:
                continue
        except ValueError:
            continue


def game_response(guess, random_number):
    if guess < random_number:
        print("Too small!")
        return False
    elif guess > random_number:
        print("Too large!")
        return False
    else:
        print("Just right!")
        return True


def game_loop(random_number):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                continue
            else:
                if game_response(guess, random_number) == True:
                    break
        except ValueError:
            continue


main()
