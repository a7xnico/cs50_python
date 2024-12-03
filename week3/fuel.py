def main():
    while True: # infinite loop to ask
        fraction = input("Fraction: ")
        result = verify_input(fraction) # gets the numbers to make the percentage of fuel
        if result:
            divisor, dividend = result # gives the input for the
            break
        print("To exit the program press: E") # no way to get out with only wrong inputs
    percentage = calculate_percentage(divisor, dividend)
    if percentage <= 1: # empty
        print("E")
    elif percentage >= 99: # full
        print("F")
    else:
        print(f"{percentage}%") # the percentage



def calculate_percentage(x, y):
    result = x / y
    percentage = round(result * 100) # easy way to get integer and porcentage
    return percentage

def verify_input(fraction):
    if "e" == fraction.lower():
        exit() # end the code
    if '/' in fraction: # checks if it's a fraction
        try:
            x, y = fraction.split('/') # gives the numbers to each variable
            x = int(x)
            y = int(y)
            if not_zero_divisor() and x <= y: # looks for a 0 in y and if the divisor is bigger than the dividend
                return x, y
        except ValueError:
            pass
    return None # looks cool

def not_zero_divisor(y):
    return y != 0 




main()
