def main():
    answer = input("What time is it? ")

    time = convert(answer)
    # checks the hours
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")  # splits the time into hours and minutes without the :
    # converst the hours and minutes to a floating point
    return float(hours) + (float(minutes) / 60)


if __name__ == "__main__":
    main()
