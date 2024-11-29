def main():
    variable = input("camelCase: ")
    output = converter(variable)
    print(f"snake_case: {output}")


def converter(name):
    result = "" # Makes a new string for the snake_case
    for c in name:
        if c.isupper(): # checks the uppercase letter and adds _
            result += f"_{c.lower()}"
        else:
            result += c # returns all other normal letters
    return result # gives the new string

main()
