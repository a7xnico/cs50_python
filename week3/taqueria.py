food_menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    total_price = 0  # counter to each item
    while True:  # while loop through every order
        try:
            item = input("Item: ").title()  # title to match with the menu uppercase
            price = get_item_price(item)  # gets the value from the dict
            if price == "Not in menu":  # unvalid input
                print(price)
            else:
                total_price += price  # adds to the total price of the order
                print(f"Total: ${total_price:.2f}")
        except EOFError:  # ctrl D input
            print()  # gets new line
            break  # ends the program, already did last problem set by chance
            # use break instead of exit(), seems too abrupt and ending the while loop is enough


def get_item_price(item):

    if item in food_menu:  # searches in the dict for the key
        return food_menu.get(item)  # gets the value from said key
    else:
        return "Not in menu"  # not in dict


main()
