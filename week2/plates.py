def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not valid_length(s):
        return False
    if not starts_with_two_letters(s):
        return False
    if not contains_only_alphanumeric(s):
        return False
    if not letter_after_number(s):
        return False
    if not first_number_not_zero(s):
        return False
    return True


def valid_length(s):  # checks if the password is between 2 and 6 characters
    return 2 <= len(s) <= 6


def starts_with_two_letters(s):  # checks if the first two characters are letters
    for c in s[0:2]:
        if c.isdigit():
            return False
    return True


def contains_only_alphanumeric(s):  # checks if there is no punctuation in the input
    return s.isalnum()


def letter_after_number(s):  # checks if there's a letter after a number, gives true when there isn't
    if s.isalpha():
        return True
    for index, c in enumerate(s):
        if c.isdigit():
            break
    for c in s[index:]:
        if c.isalpha():
            return False
    return True


def first_number_not_zero(s):  # checks if the first number that appears is zero, if not returns true
    if s.isalpha():
        return True
    for c in s:
        if c.isdigit():
            if c == "0":
                return False
            else:
                return True


main()
