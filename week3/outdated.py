months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:  # initial loop, aks for input and reprompts user if the format is incorrect
        date = input("Date: ").strip()  # gets rid of the spaces
        if "/" in date:  # when the date is in format of x/x/x
            if not numerical_format(date):  # checks if theres a string in the input
                continue
            else:
                month, day, year = numerical_format(date)  # assigns the values
        elif "," in date:  # if the format is month day, year with the month being a string
            if not string_month_format(date):  # searches both if the month is something else
                continue                      # and if the month is in the day input or in the year input
            else:
                # assigns the numerical value of month and gives day as an integer
                month, day, year = string_month_format(date)
        else:
            continue  # if its not those formats repromts
        try:
            if valid_day_and_month(day, month):  # if the days are between 1 and 31 and months between 1 and 12
                break
            else:
                continue
        except ValueError:  # if the input is invalid just reprompts
            continue

    # prints the date in year-month-day, if its a single digit gives a 0 in month and day
    print(f"{year}-{month:02}-{day:02}")


def numerical_format(date):  # splits without the /
    month, day, year = date.split("/")
    try:
        month = int(month)
        day = int(day)
        return month, day, year  # returns all 3 values
    except ValueError:  # gives false if month or day cant be an integer
        return False


def string_month_format(date):
    month, day, year = date.split()  # splits without the spaces
    if month in months:  # searches through the months
        month = months.index(month)  # gets the index of the list with the months
        month += 1  # index starts at 0 need to sum 1
        day = day.strip(",")  # erases the , in the day to make it an int
        day = int(day)
        month = int(month)
        return month, day, year  # pass each value individually
    else:
        return False


def valid_day_and_month(day, month):  # bool to see if it's valid or not
    if (1 <= day <= 31 and 1 <= month <= 12):
        return True
    else:
        return False


main()
