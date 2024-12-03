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
    total_price = 0
    while True:
        try:
            item = get_user_input()
            price = get_item_price(item)
            if price == "Not in menu":
                print(price)
            else:
                total_price = update_total_price(total_price, price)
                print(f"Total: ${total_price:.2f}")
        except EOFError:
            print()
            break


def get_user_input():
    return input("Item: ").title()


def get_item_price(item):
    if item in food_menu:
        return food_menu.get(item)
    else:
        return "Not in menu"


def update_total_price(total, price):
    return total + price


main()
