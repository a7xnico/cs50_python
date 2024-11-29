def get_valid_coin(valid_coins):
    while True:
        try:
            coin_value = int(input("Insert Coin: "))
            if coin_value in valid_coins:
                return coin_value
        except ValueError:
            pass
        print("Invalid coin. Please insert a valid coin.")

def process_transaction(coke_cost, valid_coins):
    while coke_cost > 0:
        print(f"Amount Due: {coke_cost}")
        coin_value = get_valid_coin(valid_coins)
        coke_cost -= coin_value
    return abs(coke_cost)

def main():
    coke_cost = 50
    valid_coins = [5, 10, 25]
    change = process_transaction(coke_cost, valid_coins)
    print(f"Change owed: {change}")

main()

