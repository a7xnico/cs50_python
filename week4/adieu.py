import inflect
p = inflect.engine()  # easier to add to the code
name_list = []  # creates a list
while True:  # create a loop to get input
    try:
        name = input("Name: ")  # asks user for name
        name_list.append(name)  # adds the name to the previously made list
    except EOFError:  # user presses ctrl d
        print()  # new line
        break  # stop loop
    # with p.join doesn't matter the number of input, it will always work
name_list = p.join(name_list)  # adds , & and to the list of names
print(f"Adieu, adieu, to {name_list}")  # prints to the user
