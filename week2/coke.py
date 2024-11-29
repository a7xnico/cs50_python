coke_cost = 50
valid_coins = [5, 10, 25] # all valid inputs
while coke_cost > 0:
    while True: # loops asking for correct input until the user uses a valid coin
        print(f"Amount Due: {coke_cost}")
        coin_value = int(input("Insert Coin: "))
        if coin_value in valid_coins:
            break
    coke_cost -= coin_value # gives the new value to the cost of the coke
    if coke_cost <= 0: # checks when the coke has been fully paid
        change = abs(coke_cost) # gives change to the user, abs() makes the number positive
        print(f"Change Owed: {change}")

