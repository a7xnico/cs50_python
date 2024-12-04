import sys
import requests

forced_exit = 1
bitcoin_api = "https://api.coindesk.com/v1/bpi/currentprice.json"

if len(sys.argv) == 2:  # if the program is run with the amount of bitcoin desired
    try:
        bitcoin_amount = float(sys.argv[1])  # makes it into a float
    except ValueError:  # cant convert to float
        print("Command-line argument is not a number")
        sys.exit(forced_exit)  # ends the program
else:  # user runs the program without any other input
    print("Missing command-line argument")
    sys.exit(forced_exit)

try:  # gets the data from the api
    r = requests.get(bitcoin_api)
    response = r.json()
    # searches for the dollar value of bitcoin
    dollar_conversion = (response["bpi"]["USD"]["rate_float"])
    total_amount = bitcoin_amount * dollar_conversion  # gets the total amount
    print(f"${total_amount:,.4f}")  # prints the amount with a , for the thousand
except requests.RequestException:  # in case of it being invalid
    print("RequestException")
    sys.exit(forced_exit)
