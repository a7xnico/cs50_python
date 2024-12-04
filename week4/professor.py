import random


def main():
    level = get_level()  # asks user for level, must be 1, 2, 3 or it will ask again
    score = 0  # sets the score to 0
    for _ in range(10):  # the 10 questions
        x, y = generate_integer(level)  # sets value for x and y, outside of the loop to no repeat
        for rounds in range(3):  # the 3 chances
            try:
                answer = int(input(f"{x} + {y} = "))  # asks user for the answer
                if answer == (x + y):  # answer is correct
                    break
                else:
                    print("EEE")  # invalid answer
                    if rounds == 2:  # if in last chance
                        print(f"{x} + {y} =", x + y)  # gives the result
            except ValueError:  # not an int
                print("EEE")
                if rounds == 2:  # if last chance
                    print(f"{x} + {y} =", x + y)
                continue  # continue the loop
        if answer == (x + y):
            score += 1  # if the aswer is correct +1 score
    print(f"Score: {score}")  # gives the score to the user


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in (1, 2, 3):  # the 3 available levels
                raise ValueError
            else:
                return level
        except ValueError:  # not those 3 numbers or not an integer
            continue


def generate_integer(level):
    max_number, min_number = calculate_min_max(level)
    x = random.randint(min_number, max_number)  # assigns a random number between the min and max
    y = random.randint(min_number, max_number)
    return x, y


def calculate_min_max(level):
    max_number = (pow(10, level) - 1)  # to get the max number within 1, 2 or 3 digits
    min_number = 0  # level 1
    if level != 1:  # level 2 and 3
        min_number = pow(10, level - 1)  # lvl2 is 10 pow 1 lvl3 is 10 pow 2
    return max_number, min_number  # gives these values to generate_integer


if __name__ == "__main__":
    main()
