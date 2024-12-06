def main():
    while True:
        try:
            print("To exit the program press: E")
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (TypeError, ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    if "e" == fraction.lower():
        exit()
    if '/' in fraction:
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError
        elif x > y:
            raise ValueError
        else:
            percentage = calculate_percentage(x, y)
            return percentage
    else:
        raise ValueError




def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f"{percentage}%"

def calculate_percentage(x, y):
    result = x / y
    percentage = round(result * 100)
    return percentage

if __name__ == "__main__":
    main()
