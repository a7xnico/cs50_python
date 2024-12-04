import sys
import requests


def main():
    # converts the link into a variable
    bitcoin_api = "https://api.coindesk.com/v1/bpi/currentprice.json"
    # gets the bitcoin value from the user
    bitcoin = get_bitcoin_amount()
    # gets the data from the api
    response = request_bitcoin(bitcoin_api)
    # calculates the amount of bitcoin converted to dollars
    amount = bitcoin_to_dollar(response, bitcoin)
    # prints that amount with a , in the thousand place
    print(f"${amount:,.4f}")


def get_bitcoin_amount():
    # continues if the command argument is of 2 exactly
    if len(sys.argv) == 2:
        try:
            # converts the second argument into a float
            bitcoin = float(sys.argv[1])
            # returns to main
            return bitcoin
        # not a float
        except ValueError:
            print("Command-line argument is not a number")
            sys.exit(1)
    # if no argument outside of the program
    else:
        print("Missing command-line argument")
        sys.exit(1)


def request_bitcoin(bitcoin_api):
    # requests from the api
    r = requests.get(bitcoin_api)
    # transform into json
    response = r.json()
    # return to main
    return response


def bitcoin_to_dollar(response, bitcoin):
    # looks for the dollar value of bitcoin
    dollar_conversion = (response["bpi"]["USD"]["rate_float"])
    # multiplies by the amount the user wants
    total_amount = bitcoin * dollar_conversion
    # returns that amount to main
    return total_amount


if __name__ == "__main__":
    main()
