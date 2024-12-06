def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6:
        return False
    if not starts_with_two_letters(s):
        return False
    if not s.isalnum():
        return False
    if not letter_after_number(s):
        return False
    if not first_number_not_zero(s):
        return False
    return True


def starts_with_two_letters(s):
    for c in s[0:2]:
        if c.isdigit():
            return False
    return True

def letter_after_number(s):
    if s.isalpha():
        return True
    for index, c in enumerate(s):
        if c.isdigit():
            break
    for c in s[index:]:
        if c.isalpha():
            return False
    return True

def first_number_not_zero(s):
    if s.isalpha():
        return True
    for c in s:
        if c.isdigit():
            if c == "0":
                return False
            else:
                return True

if __name__ == "__main__":
    main()
